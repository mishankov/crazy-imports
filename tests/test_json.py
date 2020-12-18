import crazyimports.json
import tests.test_data.config as config


def test_json_integer_type():
    assert type(config.number) == int


def test_json_integer_value():
    assert config.number == 42


def test_json_string_type():
    assert type(config.string) == str


def test_json_string_value():
    assert config.string == "apple"


def test_json_number_in_object():
    assert config.object["number"] == 43


def test_json_string_in_object():
    assert config.object["string"] == "orange"
