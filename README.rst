protobuf-setuptools
===================

.. image:: https://pypip.in/v/protobuf-setuptools/badge.png
        :alt: Release Status
        :target: https://pypi.python.org/pypi/protobuf-setuptools
.. image:: https://pypip.in/d/protobuf-setuptools/badge.png
        :alt: Downloads
        :target: https://pypi.python.org/pypi/protobuf-setuptools


Setuptools protobuf plugin.

Adds command to generate python probobuf stubs from .proto files.


Usage
=====

Install from PyPI and run ::

  python setup.py build_proto


That will find all the ``.proto`` files in the provided packages, compile them with ``protoc`` and put resulting ``_pb2.py`` files near them.
