import string

# def increment_string(strng):    
#     l = len(strng)
#     last_num = 0
#     i = 0
#     for i in range(l):
#         if not ('0' <= strng[l-i-1] <= '9'):
#             if i > 0:
#                 last_num = string.atoi(strng[-i:])
#             break
#     else:
#         if strng != "":
#             last_num = string.atoi(strng)
#             return ("%0"+str(i+1)+"d") % (last_num + 1)
#     return strng[:l-i] + ("%0"+str(i)+"d") % (last_num + 1)

def increment_string(s):
    if s and s[-1].isdigit():
        print('aa',"0" if s[-1] == "9" else s[:-1] + `int(s[-1]) + 1`)
        return increment_string(s[:-1]) + "0" if s[-1] == "9" else s[:-1] + `int(s[-1]) + 1`
    return s + "1"


if __name__ == '__main__':
    def test(a, b):
        if a == b:
            print("right")
        else:
            print(a, "is not equal", b)
    # test(increment_string("1"), "2")
    # test(increment_string("foo"), "foo1")
    test(increment_string("foobar001"), "foobar002")
    # test(increment_string("foobar1"), "foobar2")
    # test(increment_string("foobar00"), "foobar01")
    # test(increment_string("foobar99"), "foobar100")
    # test(increment_string("foobar099"), "foobar100")
    # test(increment_string(""), "1")
    # test(increment_string("7k 754364tW422304'.OO424147,*v@5599JOMh13427812+23761840000"), "7k 754364tW422304'.OO424147,*v@5599JOMh13427812+23761840001")

# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))

# import re
# def increment_string(input):
#     match = re.search("(\d*)$", input)
#     if match:
#         number = match.group(0)
#         if number is not "":
#             return input[:-len(number)] + str(int(number) + 1).zfill(len(number))
#     return input + "1"
