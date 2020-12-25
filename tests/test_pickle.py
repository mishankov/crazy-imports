import crazyimports
import tests.test_data.generated.pickle_file as pickle_file


def test_pickle_file_type():
    assert pickle_file.__file__.split(".")[-1] == "pickle"


def test_pickle_list_type():
    assert type(pickle_file.test_list) == list
