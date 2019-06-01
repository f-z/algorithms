def find_number_three_person_families(N, S):
    seats = [[0 for j in range(10)] for i in range(N)]
    reserved_seats = S.split(' ')
    for reserved in reserved_seats:
        if len(reserved) > 0:
            row = int(reserved[0]) - 1
            col = ord(reserved[1]) - ord('A')
            seats[row][col] = 1

    num_families = 0

    for i in range(len(seats)):
        can_fit_ac = True
        for j in range(0, 3):
            if seats[i][j] == 1:
                can_fit_ac = False
        if can_fit_ac:
            num_families += 1

        can_fit_dg = False
        if (seats[i][3] == 0 and seats[i][4] == 0 and seats[i][5] == 0) or (
                seats[i][4] == 0 and seats[i][5] == 0 and seats[i][6] == 0):
            can_fit_dg = True
        if can_fit_dg:
            num_families += 1

        can_fit_hk = True
        for j in range(7, 10):
            if seats[i][j] == 1:
                can_fit_hk = False
        if can_fit_hk:
            num_families += 1

    return num_families


print(find_number_three_person_families(1, ''))

print(find_number_three_person_families(2, '1A 2F 1C'))
