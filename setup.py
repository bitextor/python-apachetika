import tarfile
from fnmatch import fnmatch
from os.path import basename, exists, dirname, abspath, join
from distutils.core import setup

try:
    from urllib import urlretrieve
except:
    from urllib.request import urlretrieve

__version__ = '1.0.0.0'
DATAPATH = join(abspath(dirname((__file__))), 'src/pdfextract/data')

def download_jars(datapath):
    jar_url = 'https://github.com/bitextor/pdf-extract/raw/master/runnable-jar/PDFExtract.jar'
    jar_name = basename(jar_url)
    if not exists(datapath+"/"+jar_name):
        urlretrieve(jar_url, datapath+"/"+jar_name)

download_jars(datapath=DATAPATH)

setup(
    name='pdfextract',
    version=__version__,
    packages=['pdfextract', 'pdfextract.extract'],
    package_dir={'': 'src'},
    package_data={
        'pdfextract': [
            'data/pdfextract/PDFExtract.jar'
        ],
    },
    install_requires=[
        'JPype1',
        'chardet',
    ],
    author='Misja Hoebe',
    author_email='misja.hoebe@gmail.com',
    maintainer='Matthew Russell',
    maintainer_email='ptwobrussell@gmail.com',
    url='https://github.com/ptwobrussell/python-pdfextract/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
    ],
    keywords='pdfextract',
    license='Apache 2.0',
    description='Python interface to pdf-extract, HTML Extraction from PDF pages'
)
