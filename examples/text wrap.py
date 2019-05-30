import textwrap 

print (textwrap.fill(input(),int(input())))

'''Code Equivalent
def wrap(string, max_width):
    for i in range(0,len(string), max_width):
        #print(i,len(string),max_width)
        if i+max_width < len(string):
            print(string[i:i+max_width])
        else:
            print(string[len(string)-len(string)%max_width:])
    return ''
'''