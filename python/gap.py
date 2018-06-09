import math

def is_prime(x):
    if x % 2 == 0: return False
    if x <= 3 : return True
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

def gap(g, m, n):
    begin = end = 0
    for i in range(m,n+1):
        if is_prime(i):
            begin = end
            end = i
            # print([begin, end])
            if begin != 0 and end - begin == g:
                return [begin, end]
    return



if __name__ == '__main__':
    def test(a, b):
        if a == b:
            print("right")
        else:
            print(a, "is not equal", b)
    test(gap(2,100,110), [101, 103])
    test(gap(4,100,110), [103, 107])
    test(gap(6,100,110), None)
    test(gap(8,300,400), [359, 367])
    test(gap(10,300,400), [337, 347])