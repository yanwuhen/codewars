def comp(array1, array2):
    if not array1:
        return array1 == array2
    for a in array1:
        t = a*a
        if t in array2:
            array2.remove(t)
        else:
            return False
    return True

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)
