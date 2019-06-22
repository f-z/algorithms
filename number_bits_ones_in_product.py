def number_bits(a, b):
    product = a * b
    set_bit_count_map = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

    if 0 == product:
        return set_bit_count_map[0]

    # Bitwise operation
    nibble = product & 0xf

    return set_bit_count_map[nibble] + number_bits(product >> 4, 1)
