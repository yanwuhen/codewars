def solution(args):
    # print args
    for i in range(1, len(args)):
        if args[i] - args[0] != i:
            break
    # print args[0],args[i],i,len(args)
    if i == len(args)-1:
        rst = "%d-%d" % (args[0], args[-1])
    elif i == 1:
        rst = "%d," % args[0] + solution(args[1:])
    elif i == 2:
        rst = "%d,%d," % (args[0], args[i-1]) + solution(args[i:])
    else:
        rst = "%d-%d," % (args[0], args[i-1]) + solution(args[i:])
    # print args, rst
    return rst
            

if __name__ == '__main__':
    def test(a, b):
        if a == b:
            print("right")
        else:
            print(a, "is not equal", b)
    test(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
    test(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')