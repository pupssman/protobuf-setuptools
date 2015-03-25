import os
import sys
import subprocess

from distutils.spawn import find_executable
from setuptools.command.build_py import build_py


class ProtoBuild(build_py):
    """
    This command automatically compiles all .proto files with `protoc` compiler
    and places generated files near them -- i.e. in the same directory.

    TODO: this should be release to the big PyPI for the general public to enjoy.
    """
    def run(self):
        ""
        if 'PROTOC' in os.environ and os.path.exists(os.environ['PROTOC']):
            protoc = os.environ['PROTOC']
        else:
            protoc = find_executable('protoc')

        if protoc is None:
            sys.stderr.write('protoc not found. Is protobuf-compiler installed? \n'
                             'Alternatively, you can point the PROTOC environment variable at a local version.')
            sys.exit(1)

        for package in self.packages:
            packagedir = self.get_package_dir(package)

            for protofile in filter(lambda x: x.endswith('.proto'), os.listdir(packagedir)):
                sys.stderr.write('Protobuf-compiling ' + protofile + '\n')
                subprocess.check_call([protoc, '--python_out=.', os.path.join(packagedir, protofile)])


