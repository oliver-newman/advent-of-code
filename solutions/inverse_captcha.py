"""
Day 1: Inverse Captcha
"""


def main():
    from utils import get_input_for_day

    sequence = get_input_for_day(1)

    print(f'Part1: {part1(sequence)}')
    print(f'Part2: {part2(sequence)}')


def part1(sequence):
    """
    Determine the sum of all the digits d in the sequence such that the digit
    immediately following d is equal to d. Note that the sequence is
    circular; i.e., the first digit is considered to follow the last digit.
    """
    total = 0

    for i, num in enumerate(sequence):
        next_num = sequence[(i + 1) % len(sequence)]
        if num == next_num:
            total += int(num)

    return total


def part2(sequence):
    """
    Determine the sum of all the digits d in the sequence such that the digit
    halfway around the circular list (always of even length) is equal to d.
    """
    total = 0

    halfway = len(sequence) // 2

    for i, num in enumerate(sequence):
        next_num = sequence[(i + halfway) % len(sequence)]
        if num == next_num:
            total += int(num)
    
    return total


if __name__ == '__main__':
    main()
