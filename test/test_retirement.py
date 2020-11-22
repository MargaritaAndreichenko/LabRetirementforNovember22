import pytest
import retirement as retirement


def test_birth_year_earlier_1900():
    birth_year = 1825
    with pytest.raises(ValueError):
        year, month = retirement.calculate_retirement_age(birth_year)


def test_birth_year_under_1937():
    birth_year = 1901
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 65
    assert month == 0


def test_birth_year_is_1937():
    birth_year = 1937
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 65
    assert month == 0


def test_birth_year_is_1938():
    birth_year = 1938
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 65
    assert month == 2


def test_birth_year_is_1939():
    birth_year = 1939
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 65
    assert month == 4


def test_birth_year_is_1940():
    birth_year = 1940
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 65
    assert month == 6


def test_birth_year_is_1941():
    birth_year = 1941
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 65
    assert month == 8


def test_birth_year_is_1942():
    birth_year = 1942
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 65
    assert month == 10

def test_birth_year_is_1943():
    birth_year = 1943
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 66
    assert month == 0


def test_birth_year_is_1954():
    birth_year = 1954
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 66
    assert month == 0


def test_birth_year_between_1943_1954():
    birth_year = 1950
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 66
    assert month == 0


def test_birth_year_is_1955():
    birth_year = 1955
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 66
    assert month == 2


def test_birth_year_is_1956():
    birth_year = 1956
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 66
    assert month == 4


def test_birth_year_is_1957():
    birth_year = 1957
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 66
    assert month == 6


def test_birth_year_is_1958():
    birth_year = 1958
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 66
    assert month == 8


def test_birth_year_is_1959():
    birth_year = 1959
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 66
    assert month == 10


def test_birth_year_later_1959():
    birth_year = 1960
    year, month = retirement.calculate_retirement_age(birth_year)
    assert year == 67
    assert month == 0


def test_birth_year_is_3000():
    birth_year = 3000
    with pytest.raises(ValueError):
        year, month = retirement.calculate_retirement_age(birth_year)

def test_birth_year_after_3000():
    birth_year = 3001
    with pytest.raises(ValueError):
        year, month = retirement.calculate_retirement_age(birth_year)

def test_month_is_greater_12():
    year, month = retirement.calculate_retirement_date(1999, 6, 65, 7)
    assert year == 2065
    assert month == 1

def test_month_is_12():
    year, month = retirement.calculate_retirement_date(1999, 6, 65, 6)
    assert year == 2064
    assert month == 12

def test_month_is_less_12():
    year, month = retirement.calculate_retirement_date(1999, 6, 65, 2)
    assert year == 2064
    assert month == 8

def test_not_valid_year():
    with pytest.raises(ValueError):
        year, month = retirement.calculate_retirement_date('1999a', 6, 66, 2)

def test_not_valid_month():
    with pytest.raises(ValueError):
        year, month = retirement.calculate_retirement_date(1999, 'jan', 66, 2)

def test_not_valid_age_year():
    with pytest.raises(ValueError):
        year, month = retirement.calculate_retirement_date(1999, 6, 'b6', 2)

def test_not_valid_age_month():
    with pytest.raises(ValueError):
        year, month = retirement.calculate_retirement_date(1999, 6, 66, 'I1')


def test_valid_year():
    year, month = retirement.calculate_retirement_date('1999', 6, 66, 2)

def test_valid_month():
    year, month = retirement.calculate_retirement_date(1999, '11', 66, 2)

def test_valid_age_year():
    year, month = retirement.calculate_retirement_date(1999, 6, '66', 2)

def test_valid_age_month():
    year, month = retirement.calculate_retirement_date(1999, 6, 66, '11')



