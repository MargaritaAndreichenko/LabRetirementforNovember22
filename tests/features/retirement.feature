Feature: Retirement application

    Scenario Outline: birth_year_is_1937
        Given the birth year is 1937
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 65
        And retirement age months is 0

    Scenario Outline: birth_year_is_1938
        Given the birth year is 1938
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 65
        And retirement age months is 2


    Scenario Outline: birth_year_is_1939
        Given the birth year is 1939
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 65
        And retirement age months is 4


    Scenario Outline: birth_year_is_1940
        Given the birth year is 1940
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 65
        And retirement age months is 6


    Scenario Outline: birth_year_is_1941
        Given the birth year is 1941
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 65
        And retirement age months is 8


    Scenario Outline: birth_year_is_1942
        Given the birth year is 1942
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 65
        And retirement age months is 10

    Scenario Outline: birth_year_is_1943
        Given the birth year is 1943
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 66
        And retirement age months is 0


    Scenario Outline: birth_year_is_1954
        Given the birth year is 1954
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 66
        And retirement age months is 0

    Scenario Outline: birth_year_is_1955
        Given the birth year is 1955
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 66
        And retirement age months is 2


    Scenario Outline: birth_year_is_1956
        Given the birth year is 1956
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 66
        And retirement age months is 4

    Scenario: birth_year_is_1957
        Given the birth year is 1957
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 66
        And retirement age months is 6


    Scenario: birth_year_is_1958
        Given the birth year is 1958
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 66
        And retirement age months is 8


    Scenario: birth_year_is_1959
        Given the birth year is 1959
        When retirement calculator calculate_retirement_age function is invoked with the given birthdate
        Then retirement age years is 66
        And retirement age months is 10
