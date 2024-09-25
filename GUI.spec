# StockAnalysisApp.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    [r'C:\Users\markh\OneDrive\Documents\Stock-review-app\GUI Template\GUI.py'],
    pathex=[r'C:\Users\markh\OneDrive\Documents\Stock-review-app\GUI Template'],
    binaries=[],
    datas=[
        (r'C:\Users\markh\OneDrive\Documents\Stock-review-app\GUI Template\version.py', '.'),  
        (r'C:\Users\markh\OneDrive\Documents\Stock-review-app\GUI Template\ARI.py', '.'),      
        (r'C:\Users\markh\OneDrive\Documents\Stock-review-app\GUI Template\DCF.py', '.'),
        (r'C:\Users\markh\OneDrive\Documents\Stock-review-app\GUI Template\m_carlo.py', '.'),
        (r'C:\Users\markh\OneDrive\Documents\Stock-review-app\GUI Template\fetch_basic_data.py', '.'),
        (r'C:\Users\markh\OneDrive\Documents\Stock-review-app\GUI Template\update_available.py', '.')
    ],
    hiddenimports=[
        'customtkinter',
        'tkinter',
        'pandas',
        'numpy',
        'matplotlib',
        'fetch_basic_data',
        'plotly.graph_objects',
        'plotly.express',
        'm_carlo',
        'DCF',
        'ARI',
        'update_available',
        'version',
        'yfinance'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='StockAnalysisApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='StockAnalysisApp'
)