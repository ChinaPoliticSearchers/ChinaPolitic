# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='politic_proto_python',
    version='0.0.1',
    description='politi proto',
    install_requires=['protobuf>=3.1.0', 'google'],
    author='trumpfans',
    author_email='DownloadTrumpFans@outlook.com',
    #packages=find_packages(exclude=["struct_test", "dist", "build"]),
    packages=find_packages(exclude=["dist", "build"]),
    platforms='any',
)
