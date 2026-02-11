def main():
    counter = 0
    with open("input.txt", "r") as f:
        for ch in f.read():
            if ch == "(":
                counter += 1
            else:
                counter -= 1

    print(counter)

if __name__ == "__main__":
    main()