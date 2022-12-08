class Stack:
    def __init__(self):
        self.items = []

    def push(self, letter):
        self.items = [letter] + self.items

    def enqueue(self, letter):
        self.items = self.items + [letter]

    def pop(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def __str__(self):
        return ''.join(str(i) for i in self.items)


def build_stack_map(count):
    res = {}
    i = 1
    while i <= count:
        res[i] = Stack()
        i += 1
        

    return res


def move(stackMap, startIdx, endIdx):
    item = stackMap[startIdx].pop()
    stackMap[endIdx].push(item)


def superMove(stackMap, startIdx, endIdx, amount):
    toMove = []
    count = 0
    while count < amount:
        toMove.append(stackMap[startIdx].pop())
        count +=1

    toMove.reverse()
    for itm in toMove:
        stackMap[endIdx].push(itm)


def convert_input_to_map(ipt):
    m = build_stack_map(9)
    sp = ipt.split("\n")
    print(len(sp))
    for idx, line in enumerate(sp):
        if idx == len(sp) - 1:
            break
        # start num is 1
        i = 1
        it = 1
        while i < len(line):
            char = line[i]
            if char != ' ' and char != ' ':
                m[it].enqueue(char)
            i+= 4
            it +=1
    
    return m


def process_instructions(instructions, stackMap):
    for instr in instructions.split("\n"):
        count = get_count(instr)
        fr = get_from(instr)
        to = get_to(instr)

        superMove(stackMap, fr, to, count)


def get_count(instr):
    chunks = instr.split(' from')
    print(chunks)
    return int(chunks[0].split('move ')[1])

def get_from(instr):
    chunks = instr.split(' from ')
    return int(chunks[1].split(' to ')[0])

def get_to(instr):
    chunks = instr.split(' from ')
    return int(chunks[1].split(' to ')[1])


def split_input(ipt):
    chunks = ipt.split('\n\n')
    board = chunks[0]
    instructions = chunks[1]

    return board, instructions



# c = build_stack_map(5)
# c[1].push('a')
# c[1].push('z')

# move(c, 1, 3)
# print(c[1].pop()) # should be A
# print(c[3].pop()) # should be Z

# ip = '[D]                     [N] [F]    '
# res = convert_input_to_map(ip.split('\n'))

# print(res[1].pop()) # should be D
# print(res[7].pop()) # should be N
# print(res[8].pop()) # should be F



# print(get_count('move 11 from 3 to 9'))
# print(get_from('move 2 from 42 to 8'))
# print(get_to('move 69 from 11 to 99'))

with open('./input.txt') as f:
    board, instructions = split_input(f.read())
    mp = convert_input_to_map(board)
    process_instructions(instructions, mp)
    
    res = ''.join([mp[k].pop() for k in mp.keys()])
    print(res)