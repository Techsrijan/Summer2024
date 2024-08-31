import sys
from cx_Freeze import setup, Executable

import os

PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)


include_files = [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86t.dll')),
                 (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll'))]

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [Executable('Calculator.py', base=base,icon=r"C:\Users\Ashwani\Desktop\newinstaller\calci.ico",
                   shortcutName="Techsrijan Calci",
                   shortcutDir="DesktopFolder")]

setup(name='Techsrijan Calulator Test Installer',
      version='0.1',
      author="Techsrijan",
      description='My First Installer',
      options={'build_exe': {'include_files': include_files}},
      executables=executables)

