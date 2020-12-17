import crazyimports.json
import config


def test_number():
    assert config.number == 42


def test_string():
    assert config.string == "apple"


def test_number_in_object():
    assert config.object["number"] == 43


def test_string_in_object():
    assert config.object["string"] == "orange"
