from setuptools import setup

APP = ['GUI_Template/GUI.py']  # Replace with the entry point to your GUI
DATA_FILES = []  # Add any non-Python files your app needs, such as images, config files, etc.
OPTIONS = {
    'argv_emulation': True,  # Allows for drag-and-drop in the dock
    'packages': [],  # List any Python dependencies
    'excludes': ['PyInstaller','PyInstaller.hooks.hook-PySide6.QtPositioning', 'PyInstaller.hooks.hook-scipy.sparse.csgraph', 'PyQt6.QtSerialPort'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=[
        'pandas',
        'yfinance',
        'customtkinter',
        'numpy',
        'matplotlib',
        'scipy',
        'requests',
        
    ]
)
