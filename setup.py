import re
import setuptools

with open("crazyimports/__init__.py", "r") as file:
    regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(regex_version, file.read(), re.MULTILINE).group(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crazyimports",
    version=version,
    author="Denis Mishankov",
    author_email="mishankov@mail.com",
    description="Treat your data as your code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mishankov/crazy-imports",
    packages=["crazyimports"],
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
