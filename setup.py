import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="laps_and_gaps",
    version="1.0.0",
    author="Aindrila Ghosh",
    author_email="aindrila@ualberta.ca",
    description="A package for interpreting structural preservation of dimensionality reduction algorithms",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)