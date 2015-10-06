try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Testing Python Project',
    'author': 'Balint Tamasi',
    'url': 'No URL',
    'download_url': 'Local',
    'author_email': 'balint.tamasi@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['testproj'],
    'scripts': ['bin/script1.py'],
    'name': 'testproj'
}

setup(**config)
