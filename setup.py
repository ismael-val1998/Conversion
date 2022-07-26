from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as readme:

    LONG_DESCRIPTION = readme.read()

VERSION = '0.0.1'

DESCRIPTION = 'A conversion package'

setup(
    name="conversion",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Ismael KOUASSI",
    author_email="kofiismael80@gmail.com",
    url="https://github.com/ismael-val1998/Conversion",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
