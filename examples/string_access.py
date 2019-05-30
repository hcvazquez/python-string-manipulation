def mutate_string(string, position, character):
    slist = list(string)
    slist[position] = character
    return ''.join(slist)

