import crazyimports
import tests.test_data.config_yaml as config


def test_yaml_file_type():
    assert config.__file__.split(".")[-1] == "yaml"


def test_yaml_integer_type():
    assert isinstance(config.number, int)


def test_yaml_integer_value():
    assert config.number == 42


def test_yaml_string_type():
    assert isinstance(config.string, str)


def test_yaml_string_value():
    assert config.string == "apple"


def test_yaml_number_in_object():
    assert config.object["number"] == 43


def test_yaml_string_in_object():
    assert config.object["string"] == "orange"
