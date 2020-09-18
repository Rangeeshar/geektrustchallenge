import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geektrust",
    version="0.0.1",
    author="Rangeesh",
    author_email="rangees28@gmail.com",
    description="A simple python geekstrust code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rangeeshar/geektrustchallenge",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
