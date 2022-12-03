def split_half(val):
    l = len(val)
    half = round(l / 2)
    return val[0:half], val[half:]


def get_shared(sack_one, sack_two):
    d1 = build_char_dict(sack_one)

    for char in sack_two:
        if d1.get(char) is not None:
            return char

    return None


def get_shared_again(sacks):
    d1 = build_char_dict(sacks[0])
    d2 = build_char_dict(sacks[1])

    for char in sacks[2]:
        if d1.get(char) is not None and d2.get(char) is not None:
            return char

    return None


def split_input(ip):
    return [ip[i:i + 3] for i in range(0, len(ip), 3)]


def build_char_dict(sack):
    d = {}
    for char in sack:
        if d.get(char) is not None:
            d[char] += 1
        else:
            d[char] = 1

    return d


def get_points(char):
    c = char.lower()
    if c != char:
        #upper
        return ord(char) - 38 #ord('A') = 65
    else:
        # lower
        return ord(c) - 96


def test_build_char_dict():
    h = "abca"
    d = build_char_dict(h)
    print(d)


def test_half():
    h = "testtest"
    a, b = split_half(h)
    print(a)
    print(b)


def test_get_shared():
    h = "ccparkhicq"
    a, b = split_half(h)
    res = get_shared(a, b)
    print(res)


def test_get_points():
    p1 = get_points('p')
    p2 = get_points('L')
    print(p1)
    print(p2)


def test_get_shared_again():
    a = 'vJrwpWtwJgWrhcsFMMfFFhFp'
    b = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
    c = 'PmmdzqPrVvPwwTWBwg'

    print(get_shared_again([a, b, c]))


def test_split_input():
    input = ['a', 'b', 'c', 'd', 'e', 'f']
    print(split_input(input))


with open('./input.txt') as f:
    d = f.read()
    lines = d.splitlines()
    #part 1
    total = 0
    for line in lines:
        a, b = split_half(line)
        shared = get_shared(a, b)
        total += get_points(shared)

    print(total)

    #part 2
    total = 0
    buckets = split_input(lines)
    for bucket in buckets:
        shared = get_shared_again(bucket)
        total += get_points(shared)

    print(total)

