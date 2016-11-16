from setuptools import setup

setup(
    name='parsetools',
    version='0.1.0',
    description='Tools for text extraction from pdf and html documents based on textract and beautiful soup',
    author='LorenzoCestaro',
    author_email='lorenzo@igenius.com',
    license='MIT',
    url='https://github.com/LorenzoCestaro/parsetools',
    download_url='https://github.com/LorenzoCestaro/parsetools/tarball/0.1.2',
    packages=['parsetools'],
    install_requires=[
        'argparse',
        'beautifulsoup4',
        'pandas',
        'textract',
    ],
    scripts=[
        'bin/htmlparse',
        'bin/pdfparse',
        'bin/csvparse',
    ],
    zip_safe=False
)
