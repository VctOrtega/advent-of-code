# Advent of Code
# Year: 
# Day: 

def main():
    x_santa, x_robo, y_santa, y_robo = 0, 0, 0, 0   
    visited = set()
    visited.add((0,0))
    with open("input.txt", "r") as f:
        directions = f.read()

    for i, ch in enumerate(directions):
        if i % 2 == 0:
            if ch == ">": 
                x_santa += 1
            elif ch == "<":
                x_santa -= 1
            elif ch == "^":
                y_santa += 1
            elif ch == "v":
                y_santa -= 1
            visited.add((x_santa, y_santa))
        else:
            if ch == ">": 
                x_robo += 1
            elif ch == "<":
                x_robo -= 1
            elif ch == "^":
                y_robo += 1
            elif ch == "v":
                y_robo -= 1
            visited.add((x_robo, y_robo))

    print(len(visited))

if __name__ == "__main__":
    main()