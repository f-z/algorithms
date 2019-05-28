#!/bin/python3


def is_balanced(string_to_check):
    """Function to check if brackets are balanced with substitution"""
    brackets = ["()", "{}", "[]"]

    while any(bracket_pair in string_to_check for bracket_pair in brackets):
        for matched_bracket_pair in brackets:
            string_to_check = string_to_check.replace(matched_bracket_pair, "")
    if not string_to_check:
        return True

    return False
