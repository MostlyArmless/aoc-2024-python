def new_day(day: int):
    text = """
from utils import timer

sample_input = '''stuff'''
real_input = '''things'''

@timer
def part1(input: str):
    pass

assert part1(sample_input) == 42
# assert part1(real_input) == 42
"""
    with open(f'{day}.py', 'w') as stream:
        stream.write(text)

if __name__ == '__main__':
    import sys
    new_day(int(sys.argv[1]))