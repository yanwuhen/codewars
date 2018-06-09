# import sys
# sys.setrecursionlimit(100000)
# def whoIsNext(names, r):
#     if r == 1:
#         return names[0]
#     names.append(names[0])
#     names.append(names[0])
#     return whoIsNext(names[1:], r-1)

def whoIsNext(names, r):
    # print(names,r)
    l = len(names)
    i = 1
    while True:
        if r < l*(i):
            # print(r,i)
            return names[(r-1)/i]
        r -= l * i
        i *= 2
    
    

if __name__ == '__main__':
    def test(a, b):
        if a == b:
            print("right")
        else:
            print(a, "is not equal", b)
    # test(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1), "Sheldon")
    # test(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 6), "Sheldon")
    # test(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7), "Sheldon")
    # test(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 8), "Leonard")
    test(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1802), "Penny")

# def whoIsNext(names, r):
#     while r > 5:
#         r = (r - 4) / 2
#     return names[r-1]

# import math

# def whoIsNext(names, r):
#     n = len(names)
#     k = 2 ** int(math.log(1 + (r - 1) // n, 2))
#     s = 1 + (k - 1) * n
#     return names[(r - s) // k]