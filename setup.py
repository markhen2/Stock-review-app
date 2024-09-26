from setuptools import setup

APP = ['GUI Template/GUI.py']  # Replace with the entry point to your GUI
DATA_FILES = []  # Add any non-Python files your app needs, such as images, config files, etc.
OPTIONS = {
    'argv_emulation': True,  # Allows for drag-and-drop in the dock
    'packages': ['GUI Template.ARI','GUI Template.DCF','GUI Template.fetch_basic_data','GUI Template.m_carlo','GUI Template.update_available','GUI Template.version'],  # List any Python dependencies
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
