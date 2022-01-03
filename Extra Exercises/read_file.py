
try:
    with open('read_file.txt', 'r') as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("File not found")


