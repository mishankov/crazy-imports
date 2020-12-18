import csv
from crazyimports.common import ExDataLoader


class CSV(ExDataLoader):
    def exec_module(self, mod):
        data = self.load_data(open(mod.__spec__.origin, newline="").read())
        self.repack(mod, data)

    def load_data(self, data):
        data = csv.reader(data, delimiter=",")
        return {"data": data}
