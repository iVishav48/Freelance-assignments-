import os

s1 = int(input("shift1? "))
s2 = int(input("shift2? "))

here = os.path.dirname(os.path.abspath(__file__))

r = open(os.path.join(here, "raw_text.txt")).read()
e = []
m = []

for x in r:
    if x.islower():
        i = ord(x) - 97
        if x < 'n':
            e.append(chr(97 + (i + s1 + s2) % 26))
            m.append(1)
        else:
            e.append(chr(97 + (i - s1 - s2) % 26))
            m.append(2)

    elif x.isupper():
        i = ord(x) - 65
        if x < 'N':
            e.append(chr(65 + (i - s1) % 26))
            m.append(3)
        else:
            e.append(chr(65 + (i + s2 * s2) % 26))
            m.append(4)

    else:
        e.append(x)
        m.append(0)

open(os.path.join(here, "encrypted_text.txt"), "w").write("".join(e))
open(os.path.join(here, "rules.txt"), "w").write(" ".join(str(i) for i in m))

c = open(os.path.join(here, "encrypted_text.txt")).read()
k = open(os.path.join(here, "rules.txt")).read().split()

d = []

for x, t in zip(c, k):
    t = int(t)

    if t == 1:
        d.append(chr(97 + (ord(x) - 97 - s1 - s2) % 26))
    elif t == 2:
        d.append(chr(97 + (ord(x) - 97 + s1 + s2) % 26))
    elif t == 3:
        d.append(chr(65 + (ord(x) - 65 + s1) % 26))
    elif t == 4:
        d.append(chr(65 + (ord(x) - 65 - s2 * s2) % 26))
    else:
        d.append(x)

open(os.path.join(here, "decrypted_text.txt"), "w").write("".join(d))

if r == "".join(d):
    print("done")
else:
    print("something went wrong")
