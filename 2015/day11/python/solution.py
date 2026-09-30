# Advent of Code
# Year: 2015
# Day: 11

from pathlib import Path

def read_input():
    return Path("input.txt").read_text().splitlines()

def increment_password(password):
    password_chars = list(password)
    for i in range(len(password_chars) - 1,-1,-1):
        if password_chars[i] != 'z':
            password_chars[i] = chr(ord(password_chars[i]) + 1)
            break
        else:
            password_chars[i] = 'a'

    return "".join(password_chars)

def has_straight(password):
    for i in range(len(password) - 2):
        if (ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2):
            return True

    return False

def has_forbidden_letters(password):
    if ('i' in password or 'o' in password or 'l' in password):
        return True

    return False

def has_two_pairs(password):
    pairs_found = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs_found.add(password[i])
            i += 1
        if len(pairs_found) >= 2:
            return True
        i += 1

    return False

def is_valid(password):
    return has_straight(password) and not has_forbidden_letters(password) and has_two_pairs(password)

def part1(password):
    while not is_valid(password):
        password = increment_password(password)

    return password

def part2(password):
    password = increment_password(password)
    while not is_valid(password):
        password = increment_password(password)
    
    return password
    

def main():
    data = read_input()
    data = data[0].strip()

    part_one_answer = part1(data)
    print("Part 1:", part_one_answer)
    print("Part 2:", part2(part_one_answer))

if __name__ == "__main__":
    main()