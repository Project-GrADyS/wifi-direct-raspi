from setuptools import setup
from setuptools.command.install import install
import subprocess

class InstallConfig:
    def run(self):
        install.run(self)
        subprocess.run(['sudo', 'python', 'run_conf.py'])

setup (
    name='wifi_direct_raspi',
    version='0.1',
    cmdclass={
        'install': InstallConfig,
    },
)