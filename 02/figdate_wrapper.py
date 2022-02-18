import shutil
import venv
import shutil
import subprocess

venv.create('venv', with_pip=True)
subprocess.run(['./venv/bin/pip', 'install', 'pyfiglet'], capture_output=True)
subprocess.run(['./venv/bin/python3', '-m', 'figdate', '%Y %d %b, %A', 'graceful'])
shutil.rmtree('venv')