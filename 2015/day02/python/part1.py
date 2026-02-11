# Advent of Code
# Year: 2015
# Day: 2

def main():
    total_area = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip("\n")
            l, w, h = map(int, line.split("x"))
            total_area += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

    print(total_area)

if __name__ == "__main__":
    main()