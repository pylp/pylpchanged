"""

Setup PylpChanged.

Copyright (C) 2017 The Pylp Authors.
This file is under the MIT License.

"""

from setuptools import setup, find_packages
from pylpchanged import __version__ as version


setup(
	name = "pylpchanged",
	version = version,
	author = "Guillaume Gonnet",
	author_email = "gonnet.guillaume97@gmail.com",
	description = "A Pylp plugin for filtering unchanged files",
	long_description = open("README.rst").read(),
	license = "MIT",
	keywords = "pylp gulp changed",
	url = "https://github.com/pylp/pylpchanged",
	packages = find_packages(),
	install_requires = ["pylp"],
	python_requires = ">=3.5",
	classifiers = [
		"Development Status :: 4 - Beta",
		"Topic :: Utilities",
		"Topic :: Software Development :: Build Tools",
		"Framework :: AsyncIO",
		"Programming Language :: Python :: 3 :: Only",
		"Programming Language :: Python :: 3.5",
		"Intended Audience :: Developers",
		"Natural Language :: English",
		"License :: OSI Approved :: MIT License",
	],
)
