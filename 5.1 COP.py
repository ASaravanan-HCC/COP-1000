# Scenario a
a = 1
b = 2
c = 5
while a < c:
    a += 1
    b += c
print(a, b, c)


# Scenario b
d = 4
e = 6
f = 7
while d > f:
    d += 1
    e -= 1
print(d, e, f)


# Scenario c
g = 4
h = 6
while g < h:
    g += 1
print(g, h)


# Scenario d
j = 2
k = 5
n = 9
while j < k:
    m = 6
    while m < n:
        print("Goodbye")
        m += 1
    j += 1
print(j, k, n)

# Scenario e
j = 2
k = 5
m = 6
n = 9
while j < k:
    while m < n:
        print("Hello")
        m += 1
    j += 1
print(j, k, m, n)


# Scenario f
p = 2
q = 4
while p < q:
    print("Adios")
    r = 1
    while r < q:
        print("Adios")
        r += 1
    p += 1
print(p, q)
