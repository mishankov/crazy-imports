import importlib.util
import importlib.abc
import os

ex_registry = []


class ExPathFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if not path:
            path = [os.getcwd()]
        if "." in fullname:
            fullname = fullname.split(".")[-1]
        for cat in path:
            for mod in ex_registry:
                in_path = os.path.join(cat, fullname) + mod.ext
                if os.path.exists(in_path):
                    return importlib.util.spec_from_file_location(
                        name=fullname + mod.ext, location=in_path, loader=mod()
                    )
        return None


class ExDataLoader(importlib.abc.Loader):
    def repack(self, mod, data):
        if type(data) == dict:
            for k, v in data.items():
                if k.startswith("__") and k.endswith("__") or hasattr(mod, k):
                    continue
                setattr(mod, k, v)
        mod.raw_data = data

    def exec_module(self, mod):
        data = self.load_data(open(mod.__spec__.origin, "r").read())
        self.repack(mod, data)

    def load_data(self, data):
        return {}

    def __init_subclass__(self):
        ex_registry.append(self)
        if not hasattr(self, "ext"):
            setattr(self, "ext", "." + self.__name__.lower())
