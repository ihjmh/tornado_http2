import sys

try:
    import setuptools
    from setuptools import setup
except ImportError:
    setuptools = None
    from distutils.core import setup

version = '0.0.1'

kwargs = {}

if setuptools is not None:
    kwargs['install_requires'] = ['tornado>=4.3']

    if sys.version_info < (3, 4):
        kwargs['install_requires'].append('enum34')

setup(
    name='tornado_http2',
    version=version,
    packages=['tornado_http2', 'tornado_http2.test'],
    package_data={
        'tornado_http2': [
            'hpack_static_table.txt',
            'hpack_huffman_data.txt',
        ],
        'tornado_http2.test': [
            'test.crt',
            'test.key',
        ],
    },
    **kwargs)
