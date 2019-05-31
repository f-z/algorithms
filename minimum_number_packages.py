def get_minimum_number_packages(items, available_large_packages, available_small_packages):
    large_packages_used, small_packages_used = 0, 0

    while items > 0:
        if items >= 5 and available_large_packages > 0:
            large_packages_used += 1
            available_large_packages -= 1
            items -= 5
        elif items <= available_small_packages:
            small_packages_used = items
            items = 0
        else:
            return - 1

    return large_packages_used + small_packages_used


# Large packages can hold up to 5 items
# Small packages can hold up to 1 item
print(get_minimum_number_packages(16, 2, 10))
print(get_minimum_number_packages(16, 2, 5))
print(get_minimum_number_packages(4, 2, 5))
print(get_minimum_number_packages(4, 2, 3))
