def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        i = string.find(sub_string)
        string = string[:i]+string[i+1:]
        count += 1
    return count
print(count_substring(input(),input()))