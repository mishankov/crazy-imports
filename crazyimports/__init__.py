"""crazyimports module allows you to use your data files as if it was python modules"""
import sys

from ._common import ExPathFinder
from ._csv import CSV
from ._json import JSON
from ._pickle import Pickle
from ._sqlite import SQLite3
from ._yaml import YAML

__version__ = "0.1.2"

__all__ = []

sys.meta_path.append(ExPathFinder())
