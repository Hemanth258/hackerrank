def split_and_join(line):
    a = line.split(" ")
    return "-".join(a)

print(split_and_join(input()))