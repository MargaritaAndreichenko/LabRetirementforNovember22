from pytest_bdd import scenario, given, when, then, parsers, scenarios
from retirement import calculate_retirement_age, calculate_retirement_date


scenarios('../features/retirement.feature')



@given(parsers.parse('the birth year is {year}'),  target_fixture="retirement_age")
def birth_year(year):
    return calculate_retirement_age(birth_year = int(year))


@when("retirement calculator calculate_retirement_age function is invoked with the given birthdate")
def invokeBirthYear():
    pass


@then(parsers.parse("retirement age years is {age_years}"))
def assert_years(retirement_age, age_years):
    assert retirement_age[0] == int(age_years)


@then(parsers.parse("retirement age months is {age_months}"))
def assert_months(retirement_age, age_months):
    assert retirement_age[1] == int(age_months)

