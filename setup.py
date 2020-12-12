import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='simplecsv',
    version = '0.2',
    author = 'Chris Piech',
    author_email = 'piech@cs.stanford.edu',
    description = 'A tool for students working with CSVs',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="http://stanford.edu/~cpiech/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)