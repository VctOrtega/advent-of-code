# Advent of Code
# Year: 2015
# Day: 10

from pathlib import Path

def read_input():
    return Path("input.txt").read_text().splitlines()

def look_and_say(number):
    new_number = ""
    digit_counter = 0
    last_digit = None
    for digit in number:
        if last_digit == None:
            last_digit = digit
            digit_counter = 1
        elif digit == last_digit:
            digit_counter += 1
        else:
            new_number += str(digit_counter) + str(last_digit)
            digit_counter = 1
        last_digit = digit

    new_number += str(digit_counter) + str(last_digit)
    return new_number

def part1(data):
    number = data
    for _ in range(40):
        number = look_and_say(number)
    
    return len(number)

def part2(data):
    number = data
    for _ in range(50):
        number = look_and_say(number)
    
    return len(number)
    
def main():
    data = read_input()
    data = data[0].strip()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

if __name__ == "__main__":
    main()