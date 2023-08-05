from random import randint
def caesar(string):
    yuanwen = string
    password = ""
    enc = ""
    randomnumber = 0
    final = []
    for c in yuanwen:
        randomnumber = randint(1,9)
        if "a" <= c <= "z":
            enc += chr(ord("a") + (ord(c) - ord("a") + randomnumber) % 26)
            password += str(randomnumber)
        elif "A" <= c <= "Z":
            enc += chr(ord("A") + (ord(c) - ord("A") + randomnumber) % 26)
            password += str(randomnumber)
        else:
            enc += c
            password += "-"
    final.append(enc)
    final.append(password)
    return final;
def uncaesar(str,pwd):
    yuanwen = str
    tru = ""
    for i in range(0,len(str)):
        if "a" <= yuanwen[i] <= "z":
            # ord返回字符对应的编码，chr返回编码对应的字符
            tru += chr(ord("a") + (ord(yuanwen[i]) - ord("a") - int(pwd[i])) % 26)
        elif "A" <= yuanwen[i] <= "Z":
            tru += chr(ord("A") + (ord(yuanwen[i]) - ord("A") - int(pwd[i])) % 26)
        else:
            tru += yuanwen[i]
    return tru;
def lowcaesar(string,n):
    yuanwen = string
    enc = ""
    for c in yuanwen:
        if "a" <= c <= "z":
            enc += chr(ord("a") + (ord(c) - ord("a") + n) % 26)
        elif "A" <= c <= "Z":
            enc += chr(ord("A") + (ord(c) - ord("A") + n) % 26)
        else:
            enc += c
    return enc;
def lowuncaesar(string,n):
    enc = ""
    for c in string:
        if "a" <= c <= "z":
            enc += chr(ord("a") + (ord(c) - ord("a") - n) % 26)
        elif "A" <= c <= "Z":
            enc += chr(ord("A") + (ord(c) - ord("A") - n) % 26)
        else:
            enc += c
    return enc;
def freopen(file,mode,function):
    import sys
    if(function == "in"):
        sys.stdin = open(file,mode)
    if(function == "out"):
        sys.stdout = open(file,mode)
def ptextout(text,tim,end = ""):
    import time
    for i in range(len(text)):
        print(text[i],end=end)
        time.sleep(tim)
    print()
##python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

