import functools

#part 1
def reduce(elf):
    amounts = map(lambda n: int(n), elf.split("\n"))
    return functools.reduce(lambda a, b: int(a) + int(b), amounts)

def max(elves):
    max = -1
    for elf in elves:
        sum = reduce(elf)
        if sum > max:
            max = sum

    return max


#part 2
def top_n(elves, n):
    sums = [reduce(elf) for elf in elves]
    sums.sort(reverse=True)
    return sums[0:n]



with open('./input.txt') as f:
    data = f.read().strip()
    elves = data.split("\n\n")
    largest_amount = max(elves)
    print('Part 1: ',largest_amount)
    largest_amount_updated = top_n(elves, 1)
    print('Part 1 revised:', largest_amount_updated)

    t3 = top_n(elves, 3)
    print('Part 2:', sum(t3))
