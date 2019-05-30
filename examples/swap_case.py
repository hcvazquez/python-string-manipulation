def swap_case(s):

    name_list = []

    for i in s:
        if i.isupper():
            name_list.append(i.lower())
        elif i.islower():
            name_list.append(i.upper())
        else:
            name_list.append(i)

    return ''.join(name_list)
