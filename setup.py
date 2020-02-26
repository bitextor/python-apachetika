import tarfile
from fnmatch import fnmatch
import shutil
from os.path import basename, exists, dirname, abspath, join
import subprocess
from distutils.core import setup
#from setuptools import setup

try:
    from urllib import urlretrieve
except:
    from urllib.request import urlretrieve

__version__ = '2.0.0'
DATAPATH = join(abspath(dirname((__file__))), 'src/pdfextract/data')

def download_or_compile_jars(datapath):
    jar_url = 'https://github.com/bitextor/pdf-extract/raw/poppler-rewrite/runnable-jar/PDFExtract.jar'
    setup_url = 'https://github.com/bitextor/pdf-extract/raw/poppler-rewrite/setup.sh'
    jar_name = basename(jar_url)
    if not exists(datapath+"/"+jar_name):
        urlretrieve(setup_url, datapath+"/"+"setup.sh")
        try:
            subprocess.check_call(["bash",datapath+"/"+"setup.sh","compile"])
            shutil.move('PDFExtract-2.0.jar', datapath+"/"+jar_name)
        except:
            urlretrieve(jar_url, datapath+"/"+jar_name)

download_or_compile_jars(datapath=DATAPATH)

setup(
    name='python-pdfextract',
    version=__version__,
    packages=['pdfextract', 'pdfextract.extract'],
    package_dir={'': 'src'},
    package_data={
        'pdfextract': [
            'data/PDFExtract.jar'
        ],
    },
    install_requires=[
        'JPype1',
        'chardet',
    ],
    author='Misja Hoebe, Leopoldo Pla',
    author_email='misja.hoebe@gmail.com, lpla@dlsi.ua.es',
    maintainer='Matthew Russell, Leopoldo Pla',
    maintainer_email='ptwobrussell@gmail.com, lpla@dlsi.ua.es',
    url='https://github.com/bitextor/python-pdfextract/',
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
