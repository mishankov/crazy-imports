import pickle
from ._common import ExDataLoader


class Pickle(ExDataLoader):
    def exec_module(self, mod):
        data = self.load_data(open(mod.__spec__.origin, "rb"))
        self.repack(mod, data)

    def load_data(self, data):
        return {"data": pickle.load(data)}  # nosec
