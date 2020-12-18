import crazyimports.csv
import tests.test_data.table as table


def test_csv_types():
    for row in table.data:
        for number in row:
            assert type(int(number)) == int
