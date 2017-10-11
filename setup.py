#!/usr/bin/env python
"""setup"""
# pylint: disable=invalid-name

from setuptools import setup

from app import __version__

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    changelog = history_file.read()

setup(
    name='Cosmic Goat',
    version='.'.join([str(v) for v in __version__]),
    description="personal blogging app",
    long_description=readme + '\n\n' + changelog,
    author="Dustin Farley",
    author_email="fdustin45@gmail.com",
    maintainer="Dustin Farley",
    maintainer_email="fdustin45@gmail.com",
    url='https://github.com/thewhowhatwhere/flask-blog',
    license="GNU GPLv3",
    packages=[
        'cosmic',
    ],
    package_dir={'cosmic': 'app'},
    include_package_data=True,
    install_requires=[
        'click',
        'flask',
        'flask-admin',
        'flask-babelex',
        'flask-htmlmin',
        'flask-login',
        'flask-mail',
        'flask-principal',
        'flask-security',
        'flask-sqlalchemy',
        'flask-wtf',
        'markupsafe',
        'sqlalchemy',
        'sqlalchemy-utils',
        'translitcodec',
        'wtforms',
        'wtforms-alchemy',
        'wtforms-components',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-flask',

    ],
    zip_safe=False,
    keywords='flask',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='tests'
)
