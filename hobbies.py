def find_names_people_hobbies(hobbies, hobby_to_search_for):
    results = []
    for name, values in hobbies.items():
        if hobby_to_search_for in values:
            results.append(name)

    return results


hobbies = {
    "Jane": ['skiing', 'traveling', 'reading'],
    "Peter": ['surfing', 'reading']
}

print(" ".join(find_names_people_hobbies(hobbies, 'reading')))
