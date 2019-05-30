def count_substring(string, sub_string):
    index = 0
    count = 0
    while index < len(string):
        index = string.find(sub_string, index)
        if index == -1:
            break
        count += 1
        index += 1
    return count

