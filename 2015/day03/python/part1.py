# Advent of Code
# Year: 2015
# Day: 3

# ><^v

def main():
    x, y = 0, 0
    visited = set()
    visited.add((0,0))
    with open("input.txt", "r") as f:
        for ch in f.read():
            if ch == ">": 
                x += 1
            elif ch == "<":
                x -= 1
            elif ch == "^":
                y += 1
            elif ch == "v":
                y -= 1
            visited.add((x, y))

    print(len(visited))


if __name__ == "__main__":
    main()