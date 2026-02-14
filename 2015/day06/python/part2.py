# Advent of Code
# Year: 2015
# Day: 6

def main():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith("turn on"):
                operation = "on"
            elif line.startswith("turn off"):
                operation = "off"
            elif line.startswith("toggle"):
                operation = "toggle"

            parts = line.split()

            if operation == "toggle":
                start = parts[1]
                end = parts[3]
            else:
                start = parts[2]
                end = parts[4]
            
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if operation == "on":
                        grid[x][y] += 1
                    elif operation == "off":
                        if grid[x][y] > 0:
                            grid[x][y] -= 1
                    elif operation == "toggle":
                        grid[x][y] += 2

        print(sum(sum(row) for row in grid))
        
if __name__ == "__main__":
    main()