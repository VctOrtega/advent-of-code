def main():
    counter = 0
    position = 0
    with open("input.txt", "r") as f:
        for ch in f.read():
            position += 1
            if ch == "(":
                counter += 1
            else:
                counter -= 1
            
            if counter < 0:
                print(f"The position of the character that causes Santa to first enter the basement is: {position}")
                break

    print(counter)

if __name__ == "__main__":
    main()