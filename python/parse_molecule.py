import re
import string
from collections import Counter

def get_cnt(sub_formula, sumary):
    # print(sub_formula)
    m = re.match("([A-z]+[a-z]*)(\\d*)", sub_formula)
    if m:
        # print(sub_formula,m.groups())
        if m.groups()[1]:
            value = m.groups()[1]
            key = sub_formula[:-len(value)]
            value = string.atoi(value)
        else:
            key = sub_formula
            value = 1
        if sumary.get(key):
            sumary[key] += value
        else:
            sumary[key] = value

revert_dict = {'(':')', '[':']', '{':'}'}

def parse_molecule (formula):
    # print("input is",formula)
    rst = {}
    if formula is None or formula == "":
        return rst
        
    left_cnt = right_cnt = 0
    f_len = len(formula)
    m = re.match("^([A-Z][a-z]*\\d*)?\\S*?([A-Z][a-z]*\\d*)?$", formula)
    if m:
        left_str = m.groups()[0]
        right_str = m.groups()[1]
        if left_str:
            left_cnt = len(left_str)
            get_cnt(left_str, rst)
            # print("left:",rst)
        if right_str:
            right_cnt = len(right_str)
            get_cnt(right_str, rst)
            # print("right", rst)
    if left_cnt !=0 or right_cnt !=0:
        # print(left_str,right_str,formula[left_cnt:f_len-right_cnt])
        sub = parse_molecule(formula[left_cnt:f_len-right_cnt])
        rst = dict(Counter(rst)+Counter(sub))
    else:
        # print(formula)
        cnt=0
        for i in range(len(formula)):
            if formula[i] in ("(","[","{"):
                cnt += 1
            elif formula[i] in (")", "]", "}"):
                cnt -= 1
            if cnt == 0 and i !=0:
                break
        sub_rst = parse_molecule(formula[1:i])
        for j in range(i+1, len(formula)):
            # print("j",j,"f[j]:",formula[j],"len", len(formula))
            if not ('0' <= formula[j] <= '9'):
                break
        if j == len(formula)-1:
            cnt = string.atoi(formula[j])
        elif j == i+1:
            cnt = 1
        else:
            # print(i+1,j)
            cnt = string.atoi(formula[i+1:j])
        # print("cnt is ", cnt)
        for i in range(cnt):
            rst = dict(Counter(rst) + Counter(sub_rst))
        if j != len(formula) - 1:
            sub_rst = parse_molecule(formula[j:])
            rst = dict(Counter(rst) +Counter(sub_rst))
    # print(formula, rst)
    return rst

if __name__ == '__main__':
    def test(a, b):
        if a == b:
            print("right")
        else:
            print(a, "is not equal", b)
    test(parse_molecule("H2O"), {'H': 2, 'O' : 1})
    test(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O' : 2, 'H': 2})
    test(parse_molecule("K4[ON(SO3)2]2"), {'K': 4,  'O': 14,  'N': 2,  'S': 4})
    test(parse_molecule("C6H12O6"), {'C': 6, 'H':12, 'O' : 6})
    test(parse_molecule("Mo(CO)6"), {'Mo': 1, 'C':6, 'O' : 6})
    test(parse_molecule("(C5H5)Fe(CO)2CH3"), {'C': 8, 'H':8, 'Fe' : 1, 'O':2})
    test(parse_molecule("C2H2(COOH)2"), {'C': 4, 'H':4, 'O':4})
    