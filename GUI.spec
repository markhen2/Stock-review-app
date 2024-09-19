# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/markhenry/Documents/Stock-review-app/GUI Template/GUI.py'],
    pathex=['/Users/markhenry/Documents/Stock-review-app/GUI Template'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'm_carlo',
        'customtkinter',
        'tkinter',
        'pandas',
        'numpy',
        'matplotlib',
        'fetch_basic_data',
        'plotly',
        
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='StockAnalyticsV1.0.1',
    icon=None,
    bundle_identifier=None,
)
