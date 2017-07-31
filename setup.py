import codecs
from setuptools import setup, find_packages

setup(
    name="pyamap",
    version="0.0.2",
    packages=['pyamap'],
    package_data={
    },
    install_requires=[
        'argparse',
    ],
    author="xlvecle",
    author_email="xlvecle@xlvecle.com",
    description="Draw pic with amap js api",
    license='''            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

    ''',
    url='http://xlvecle.github.io/pyamap'
)
