import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crazyimports", # Replace with your own username
    version="0.0.1",
    author="Denis Mishankov",
    author_email="mishankov@mail.com",
    description="Treat your data as your code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mishankov/crazy-imports",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)