try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'example 47',
	'author': 'Lars Veenendaal',
	'url': 'github sometimes',
	'download':'',
	'author_email':'madmilla@gmail.com',
	'version':'0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name':'Example 47'
}

setup(**config)
