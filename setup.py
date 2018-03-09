import os
from setuptools import setup

setup(
        name         = "agf_parser",
        version      = "0.0.3",
        author       = "Sergey Ivanov",
        author_email = "powah.serge@gmail.com",
        description  = "Parses .agf files and makes a game object",
        license      = "MIT",
        url          = "http://github.com/Nyarmith/agf-parser",
        classifiers  = [
            'Programming Language :: Python :: 3.6',
            'Development Status :: 2 - Pre-Alpha',
            'License :: OSI Approved :: MIT License',
            'Topic :: Games/Entertainment'
            ],
        packages     = ['agf_parser'],
        install_requires=['lxml'],
        scripts=['bin/play']
        #entry_points --> use this to add entry-point cli thing to end-user
     )
