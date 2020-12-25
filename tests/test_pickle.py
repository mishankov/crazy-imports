import crazyimports
import tests.test_data.generated.pickle_file as pickle_file


def test_pickle_file_type():
    assert pickle_file.__file__.split(".")[-1] == "pickle"


def test_pickle_data_type():
    assert isinstance(pickle_file.data, tuple)


def test_pickle_list_type():
    assert isinstance(pickle_file.data[0], list)


def test_pickle_dict_type():
    assert isinstance(pickle_file.data[1], dict)
