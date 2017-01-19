try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'digExtractionClassification',
    'description': 'digExtractionClassification',
    'author': 'Rahul Kapoor',
    'url': 'https://github.com/r-kapoor/extractions-classification',
    'download_url': 'https://github.com/r-kapoor/extractions-classification',
    'author_email': 'rahulkap@isi.edu',
    'version': '0.3.0',
    'install_requires': ['digExtractor>=0.3.0'],
    # these are the subdirs of the current directory that we care about
    'packages': ['digExtractionsClasssifier'],
    'scripts': [],
}

setup(**config)
