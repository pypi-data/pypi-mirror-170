"""
setup file for pagemeta package

- Publish version
$ python setup.py publish

- Alternative (for building wheel)
pip install build
python -m build
"""


import os
import sys
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()


if sys.argv[-1] == 'publish':
	if os.system("pip3 freeze | grep twine"):
		print("twine not installed.\nUse `pip install twine`.\nExiting.")
		sys.exit()
	os.system("rm -rf dist")
	os.system("python3 setup.py sdist bdist_wheel")
	os.system("twine upload dist/*")
	sys.exit()


setuptools.setup(
	name="django-pagemeta",
	version="1.2.1",
	author="Ajesh Sen Thapa",
	author_email="aj3sshh@gmail.com",
	description="A simple django package for managing meta tags, og tags, images, and descriptions dynamically.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	keywords=['django meta', 'django page meta', 'meta tags', 'og tags', 'open tags', 'twitter card', 'seo', 'seo tags', 'keywords', 'keywords management'],
	url="https://github.com/aj3sh/pagemeta",
	packages=setuptools.find_packages(),
	package_data={
		'pagemeta': ['templates/pagemeta/*.html'],
	},
	install_requires=[
	],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
)
