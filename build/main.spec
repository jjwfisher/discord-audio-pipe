# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

DATAPATH = os.path.abspath(os.path.join(SPECPATH, '..'))

a = Analysis(
    ['../main.pyw', '../spotiCmds.py', '../cli.py', '../gui.py', '../sound.py'],
    pathex=[],
    binaries=[],
    datas=[(os.path.join(DATAPATH, 'assets'), './assets')],
    hiddenimports=[],
    hookspath=['./build'],
    runtime_hooks=None,
    excludes=['numpy', 'tkinter', 'tcl'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

a.binaries = a.binaries - TOC([
    ('opengl32sw.dll', None, None),
    ('d3dcompiler_47.dll', None, None),
    ('libegl.dll', None, None),
    ('libglesv2.dll', None, None),
    ('qt5nfc.dll', None, None),
    ('qt5opengl.dll', None, None),
    ('qt5positioning.dll', None, None),
    ('qt5positioningquick.dll', None, None),
    ('qt5printsupport.dll', None, None),
    ('qt5qml.dll', None, None),
    ('qt5qmlmodels.dll', None, None),
    ('qt5qmlworkerscript.dll', None, None),
    ('qt5quick.dll', None, None),
    ('qt5quick3d.dll', None, None),
    ('qt5quick3dassetimport.dll', None, None),
    ('qt5quick3drender.dll', None, None),
    ('qt5quick3druntimerender.dll', None, None),
    ('qt5quick3dutils.dll', None, None),
    ('qt5quickcontrols2.dll', None, None),
    ('qt5quickparticles.dll', None, None),
    ('qt5quickshapes.dll', None, None),
    ('qt5quicktemplates2.dll', None, None),
    ('qt5quicktest.dll', None, None),
    ('qt5quickwidgets.dll', None, None),
    ('qt5remoteobjects.dll', None, None),
    ('qt5sensors.dll', None, None),
    ('qt5serialport.dll', None, None),
    ('qt5sql.dll', None, None),
    ('qt5test.dll', None, None),
    ('qt5texttospeech.dll', None, None),
    ('qt5webchannel.dll', None, None),
    ('qt5websockets.dll', None, None),
    ('qt5winextras.dll', None, None),
    ('qt5xml.dll', None, None),
    ('qt5xmlpatterns.dll', None, None),
    ('qt5bluetooth.dll', None, None),
    ('qt5dbus.dll', None, None),
    ('qt5designer.dll', None, None),
    ('qt5help.dll', None, None),
    ('qt5location.dll', None, None),
    ('qt5multimedia.dll', None, None),
    ('qt5multimediawidgets.dll', None, None),
    ('qt5network.dll', None, None),
    ('qt5networkauth.dll', None, None)
])

a.datas = [
    x for x in a.datas if not
    x[0].startswith("PyQt5\\Qt\\translations\\")
]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='DAPS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=False,
    icon=os.path.join(DATAPATH, 'assets/favicon.ico')
)
