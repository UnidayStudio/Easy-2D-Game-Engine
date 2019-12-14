# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
	("game/data", "data")
]

import os
buildDir = os.getcwd() # 'E:\\Game Design v2\\Code\\Python\\Easy2D'
print("DIR:", buildDir)

a = Analysis(['game\\main.py'],
             pathex=[buildDir],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
