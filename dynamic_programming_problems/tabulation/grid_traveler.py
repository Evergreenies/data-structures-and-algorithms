def grid_traveler(source: int, destination: int) -> int:
    dp_table = [[0 for _ in range(source + 2)] for _ in range(destination + 2)]
    dp_table[1][1] = 1

    for i in range(source):
        for j in range(destination):
            current = dp_table[i][j]

            if (j + 1) <= destination:
                dp_table[i][j + 1] += current

            if (1 + 1) <= source:
                dp_table[i + 1][j] += current

    return dp_table[source][destination]


if __name__ == '__main__':
    print(grid_traveler(1, 1))
    print(grid_traveler(2, 3))
    print(grid_traveler(3, 2))
    print(grid_traveler(18, 18))
