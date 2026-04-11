# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('auth', 'auth'), ('data', 'data'), ('ui', 'ui'), ('LICENSE', '.'), ('lang.py', '.')],
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name='MisTareas2.1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    argv_emulation=False,
    icon='icon.icns',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MisTareas2.1',
)

app = BUNDLE(
    coll,
    name='MisTareas2.1.app',
    icon='icon.icns',
    bundle_identifier='com.fabianviera.mistareas',
    info_plist={
        'CFBundleName': 'MisTareas',
        'CFBundleDisplayName': 'MisTareas 2.1',
        'CFBundleVersion': '2.1.0',
        'CFBundleShortVersionString': '2.1',
        'NSHighResolutionCapable': True,
    },
)
