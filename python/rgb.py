def rgb(r, g, b):
    def valid(x):
        if x < 0: return 0
        if x > 255: return 255
        return x
    return "%02X%02X%02X" % (valid(r), valid(g), valid(b))

if __name__ == '__main__':
    def test(eq):
        if eq:
            print("right")
        else:
            print("wrong")
    test(rgb(0,0,0) == "000000")
    test(rgb(1,2,3) == "010203")
    test(rgb(255,255,255) == "FFFFFF")
    test(rgb(254,253,252) == "FEFDFC")
    test(rgb(-20,275,125) == "00FF7D")
    # print(rgb(0,0,0)) # "000000"
    # print(rgb(1,2,3)) # "010203"
    # print(rgb(255,255,255)) # "FFFFFF"
    # print(rgb(254,253,252)) # "FEFDFC"
    # print(rgb(-20,275,125)) # "00FF7D"

# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))