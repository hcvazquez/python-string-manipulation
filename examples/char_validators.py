if __name__ == '__main__':
    s = input()
    print(True) if len([[x] for x in list(s) if x.isalnum()]) > 0 else print(False)
    print(True) if len([[x] for x in list(s) if x.isalpha()]) > 0 else print(False)
    print(True) if len([[x] for x in list(s) if x.isdigit()]) > 0 else print(False)
    print(True) if len([[x] for x in list(s) if x.islower()]) > 0 else print(False)
    print(True) if len([[x] for x in list(s) if x.isupper()]) > 0 else print(False)