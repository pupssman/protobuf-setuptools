import os
import sys
import subprocess

from os import path as op 
from distutils.spawn import find_executable
from setuptools.command.build_py import build_py


class ProtoBuild(build_py):
    """
    This command automatically compiles all .proto files with `protoc` compiler
    and places generated files near them -- i.e. in the same directory.

    TODO: this should be release to the big PyPI for the general public to enjoy.
    """
    def find_protoc(self):
        "Locates protoc executable"

        if 'PROTOC' in os.environ and os.path.exists(os.environ['PROTOC']):
            protoc = os.environ['PROTOC']
        else:
            protoc = find_executable('protoc')

        if protoc is None:
            sys.stderr.write('protoc not found. Is protobuf-compiler installed? \n'
                             'Alternatively, you can point the PROTOC environment variable at a local version.')
            sys.exit(1)

        return protoc

    def run(self):
        for package in self.packages:
            packagedir = self.get_package_dir(package)

            for protofile in filter(lambda x: x.endswith('.proto'), os.listdir(packagedir)):
                source = op.join(packagedir, protofile)
                output = source.replace('.proto', '_pb2.py')

                if (not op.exists(output) or (op.getmtime(source) > op.getmtime(output))):
                    sys.stderr.write('Protobuf-compiling ' + source + '\n')
                    subprocess.check_call([self.find_protoc(), '--python_out=.', source])


