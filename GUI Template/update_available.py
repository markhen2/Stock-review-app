import requests
import os
import shutil
import subprocess
import time
from version import __version__  # Ensure your app version is stored here

def get_latest_release_info():
    api_url = "https://api.github.com/repos/markhen2/Stock-review-app/releases/latest"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for HTTP errors
        release_data = response.json()
        return release_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching release info: {e}")
        return None

def is_update_available():
    release_info = get_latest_release_info()
    if not release_info:
        return False  # If there's an error fetching release data, no update
    latest_version = release_info.get('tag_name')  # Get the latest version from the GitHub release
    if latest_version:
        return latest_version != __version__  # Compare with current app version
    return False

if is_update_available():
    print("New version available!")
else:
    print("No update available.")

def download_latest_release():
    release_info = get_latest_release_info()
    if not release_info:
        return None

    assets = release_info.get('assets', [])
    if not assets:
        print("No assets found in the latest release.")
        return None

    download_url = assets[0].get('browser_download_url')
    if not download_url:
        print("No download URL found for the asset.")
        return None

    output_dir = "downloads"
    output_path = os.path.join(output_dir, "new_version.exe")

    # Ensure the downloads directory exists
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Download the update
        response = requests.get(download_url, stream=True)
        response.raise_for_status()
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"Downloaded new version to {output_path}")
        return output_path
    except requests.exceptions.RequestException as e:
        print(f"Error downloading update: {e}")
        return None

def apply_update(new_exe_path, current_exe_path):
    try:
        time.sleep(2)  # Wait for the app to fully close (if necessary)
        
        # Replace the old exe with the new one
        shutil.move(new_exe_path, current_exe_path)
        print("Application updated successfully.")

        # Relaunch the application
        subprocess.Popen([current_exe_path])
    except Exception as e:
        print(f"Error applying update: {e}")

def start_update_process():
    if is_update_available():
        new_exe_path = download_latest_release()
        if new_exe_path:
            current_exe_path = __file__  # Path to the current executable
            apply_update(new_exe_path, current_exe_path)
        else:
            print("Failed to download the update.")
    else:
        print("No updates available.")

# Example usage
start_update_process()
