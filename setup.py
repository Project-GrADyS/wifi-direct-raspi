from setuptools import setup
from setuptools.command.install import install
import subprocess


def run():
    #install_process = install()
    #install_process.run()
    subprocess.run(['sudo', 'python', 'run_conf.py'])

setup (
    name='wifi_direct_raspi',
    version='0.0.1',
    description = "Wi-Fi Direct Library for Raspberry Pi",
    author="Tatiana Reimer", 
    author_email="tatireimer99@gmail.com",
    url='https://www.python.org/sigs/distutils-sig/',
    cmdclass={
        'install': run(),
    },
)