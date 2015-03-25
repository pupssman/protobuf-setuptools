from setuptools import setup

setup(
    name='protobuf-setuptools',
    version='0.1',
    license='Apache License, Version 2.0',
    author="Ivan Kalinin",
    author_email="pupssman@yandex-team.ru",
    description='setuptools build_proto command',
    long_description=open('README.rst').read(),
    
    py_modules=['protobuf_setuptools'],
    entry_points = {
        "distutils.commands": [
            "build_proto = protobuf_setuptools:ProtoBuild",
        ],
    }
)
