a = str(input("napishi stroky: "))


def verxniy():
    print(a.upper())
verxniy()


def nigniy():
    print(a.lower())
nigniy()

v = list(map(str.upper, a))
n = list(map(str.lower, a))
print(v)
print(n)
