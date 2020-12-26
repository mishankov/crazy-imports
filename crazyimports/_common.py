import importlib.util
import importlib.abc
import os

ex_registry = []


class ExPathFinder(importlib.abc.MetaPathFinder):
    """Class that extends default python module finder to find files with certain extensions"""

    def find_spec(self, fullname, path, target=None):
        if not path:
            path = [os.getcwd()]
        if "." in fullname:
            fullname = fullname.split(".")[-1]
        for cat in path:
            for mod in ex_registry:
                for mod_ext in mod.extensions:
                    in_path = os.path.join(cat, fullname) + mod_ext
                    if os.path.exists(in_path):
                        return importlib.util.spec_from_file_location(
                            name=fullname + mod_ext, location=in_path, loader=mod()
                        )
        return None


class ExDataLoader(importlib.abc.Loader):
    """Base class for custom module loaders"""

    extensions = []

    def repack(self, mod, data):
        """Converts top level dict keys to attributes of module"""
        if isinstance(data, dict):
            for k, v in data.items():
                if k.startswith("__") and k.endswith("__") or hasattr(mod, k):
                    continue
                setattr(mod, k, v)
        mod.raw_data = data

    def exec_module(self, mod):
        """Define module "execution". Overrides exec_module() from importlib.abc.Loader"""
        data = self.load_data(open(mod.__spec__.origin, "r").read())
        self.repack(mod, data)

    def load_data(self, data):
        """Loads data from file. Needs to be overrided in subclasses"""
        return {}

    def __init_subclass__(self):
        """For every subclass adds it to ex_registry and set extensions attribute if it is not presented"""
        ex_registry.append(self)

        if not hasattr(self, "extensions") or len(getattr(self, "extensions")) == 0:
            setattr(self, "extensions", ["." + self.__name__.lower()])
