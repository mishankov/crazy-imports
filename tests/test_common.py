import re
import os
import crazyimports


def test_version():
    with open(
        os.path.split(os.path.dirname(__file__))[0] + "/crazyimports/__init__.py", "r"
    ) as file:
        regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
        version = re.search(regex_version, file.read(), re.MULTILINE).group(1)

    assert crazyimports.__version__ == version
