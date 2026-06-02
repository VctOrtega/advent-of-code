# Advent of Code
# Year: 2015
# Day: 8

from pathlib import Path

def read_input():
    return Path("input.txt").read_text().splitlines()

def part1(data):
    total_characters = 0

    for line in data:
        char_count = 0
        i = 1
        while i < len(line) - 1:
            if (line[i] == "\\"):
                i += 1
                if (line[i] == "x"):
                    i += 2    
            char_count += 1
            i += 1

        total_characters += (len(line) - char_count)

    return total_characters

def part2(data):
    total_characters = 0

    for line in data:
        chars_encoded = 0
        i = 0
        while i < len(line):
            if (line[i] == "\\"):
                i += 1
                if (line[i] == "\\" or line[i] == "\""):
                    chars_encoded += 2
                if (line[i] == "x"):
                    i += 2
                    chars_encoded += 1

            i += 1

        chars_encoded += len(line) + 4
        total_characters += (chars_encoded - len(line))

    return total_characters

def main():
    data = read_input()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

if __name__ == "__main__":
    main()