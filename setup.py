#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""setup.py

    setuptoolsを使う.コードの通り.
"""
import os
import sys
from codecs import open

import setuptools
from setuptools.command.test import test as testCommand

here = os.path.abspath(os.path.dirname(__file__))


class PyTest(testCommand):
    """ PyTestを実行するコマンドの実装

    pytestのオプションを指定する際は--pytest-args='{options}'を使用する.
    """
    user_options = [
        ('pytest-args=', 'a', 'Arguments for pytest'),
    ]

    def __init__(self, dist, **kw):
        super().__init__(dist, **kw)
        self.test_suite = 'tests'
        self.test_args = []
        self.pytest_args = []
        self.pytest_target = []

    def initialize_options(self):
        testCommand.initialize_options(self)

    def finalize_options(self):
        testCommand.finalize_options(self)

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('rm -rf dist/*')
    os.system('python setup.py sdist')
    os.system('twine upload dist/*')
    sys.exit()

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish_test':
    os.system('rm -rf dist/*')
    os.system('python setup.py sdist')
    os.system('twine upload --repository pypitest dist/*')
    sys.exit()

requires = [
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'tox'
]

about = {}
with open(os.path.join(here, 'design_db_manager', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.md', 'r', 'utf-8') as f:
    history = f.read()

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    maintainer=about['__maintainer__'],
    maintainer_email=about['__maintainer_email__'],
    url=about['__url__'],
    packages=setuptools.find_packages(),
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'design_db_manager': 'design_db_manager'},
    include_package_data=True,
    python_requires=">=3.5",
    setup_requires=['setuptools >= 30.3'],
    install_requires=requires,
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: Japanese',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities'
    ],
    entry_points={
        # 'console_scripts': ['design_db_manager= design_db_manager.core:main']
    },
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    extras_require={
        'test': ['pytest', 'tox'],
    },
)
