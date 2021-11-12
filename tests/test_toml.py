import crazyimports
import tests.test_data.config_toml as config


def test_toml_file_type():
    assert config.__file__.split(".")[-1] == "toml"


def test_toml_integer_type():
    assert isinstance(config.number, int)


def test_toml_integer_value():
    assert config.number == 42


def test_toml_string_type():
    assert isinstance(config.string, str)


def test_toml_string_value():
    assert config.string == "apple"


def test_toml_number_in_object():
    assert config.object["number"] == 43


def test_toml_string_in_object():
    assert config.object["string"] == "orange"
