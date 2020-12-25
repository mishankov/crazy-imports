import json
from ._common import ExDataLoader


class JSON(ExDataLoader):
    def load_data(self, data):
        return json.loads(data)
