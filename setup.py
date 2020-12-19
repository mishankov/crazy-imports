import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crazyimports",
    version="0.0.3",
    author="Denis Mishankov",
    author_email="mishankov@mail.com",
    description="Treat your data as your code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mishankov/crazy-imports",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    extras_require={"yaml": ["PyYAML==5.3.1"]},
)
