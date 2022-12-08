def split_line(line):
    chunks = line.split(',')
    first_chunk = chunks[0].split('-')
    second_chunk = chunks[1].split('-')

    return [(int(first_chunk[0]), int(first_chunk[1])), (int(second_chunk[0]), int(second_chunk[1]))]


def fully_contains(chunk_one, chunk_two):
    if chunk_one[0] == chunk_two[0]:
        return True

    if chunk_one[0] < chunk_two[0]:
        return chunk_one[1] >= chunk_two[1]
    else:
        return chunk_two[1] >= chunk_one[1]


def overlap(chunk_one, chunk_two):
    a, b = chunk_one
    c, d = chunk_two

    if a == c or b == d or a == d or c == b:
        return True

    if a < c:
        return b > c
    else:
        return d > a



def test_overlap():
    a = (6, 11)
    b = (7, 9)

    print(overlap(a, b))

def test_split_line():
    test = '2-7,7-9'
    res = split_line(test)
    print(res[0][0], res[0][1])


def test_fully_contains():
    first = (2, 9)
    second = (3, 8)
    print(fully_contains(first, second))
    print(fully_contains(second, first))

    third = (3, 5)
    fourth = (4, 9)
    print(fully_contains(third, fourth))


with open('./input.txt') as f:
    data = f.readlines()
    lines = [split_line(line) for line in data]
    total = 0
    total_two = 0
    for line in lines:
        if fully_contains(line[0], line[1]):
            total += 1

        if overlap(line[0], line[1]):
            total_two += 1
            print(line[0], line[1], 'Success')
        else:
            print(line[0], line[1], 'Failure')

    print(total)
    print(total_two)
