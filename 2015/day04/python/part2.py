# Advent of Code
# Year: 2015
# Day: 4
# https://adventofcode.com/2015/day/4

import hashlib


def main():
    secret_key = "ckczppom"
    answer = 1
    
    while True:
        text = secret_key + str(answer)
        hash_obj = hashlib.md5(text.encode())
        hex_hash = hash_obj.hexdigest()

        if hex_hash.startswith("000000"):
            print("[!] Found a valid hash!")
            print(f"[>] The correct answer is {answer}")
            break

        answer += 1

if __name__ == "__main__":
    main()