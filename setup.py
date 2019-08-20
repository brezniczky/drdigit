import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drdigit-brezniczky",
    version="0.0.1",
    author="Janos Brezniczky",
    author_email="brezniczky@gmail.com",
    description="A digit doctoring detection package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brezniczky/drdigit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: "
        "GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning ",
        "Topic :: Scientific/Engineering"
    ],
)
