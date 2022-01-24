# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.building.build_main import *
import sys
import os

path = os.path.abspath(".")
kivymd_repo_path = path.split("demos")[0]
sys.path.insert(0, kivymd_repo_path)

from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path

a = Analysis(
    ["main.py"],
    pathex=[path],
    binaries=[],
    datas=[("assets\\", "assets\\"), ("libs\\kv\\", "libs\\kv\\")],
    hiddenimports=[
        "libs.baseclass.clp_connection",
        "libs.baseclass.connection_db",
        "libs.baseclass.email",
        "libs.baseclass.fonts",
        "libs.baseclass.form_layout",
        "libs.baseclass.navigation_bar",
        "libs.baseclass.tabela",
        "libs.baseclass.pdf",
        "libs.baseclass.periodo",
        "kivymd.effects.stiffscroll",
    ],
    hookspath=[kivymd_hooks_path],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    debug=False,
    strip=False,
    upx=True,
    name="Engesep",
    icon="C://Engesep//02- APPs//APPDB//executavel//v1.2.1//assets/logo.ico",
    console=False,
)
