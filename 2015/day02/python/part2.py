# Advent of Code
# Year: 2015
# Day: 2

def main():
    total_ribbon = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip("\n")
            l, w, h = map(int, line.split("x"))
            smallest, middle, largest = sorted([l, w, h])
            total_ribbon += smallest * 2 + middle * 2 + l * w * h

    print(total_ribbon)

if __name__ == "__main__":
    main()