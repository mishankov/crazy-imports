import csv
from ._common import ExDataLoader


class CSV(ExDataLoader):
    def exec_module(self, mod):
        mod.data = []
        with open(mod.__spec__.origin, newline="") as f:
            reader = csv.reader(f)
            mod.raw_data = reader
            for row in reader:
                mod.data.append(row)
