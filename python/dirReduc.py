def dirReduc(arr):
    rst =[]
    i = 0
    change = False
    while i < len(arr)-1:
        if sorted([arr[i],arr[i+1]]) in (["NORTH", "SOUTH"], ["EAST", "WEST"]):
            i+=2
            change = True
            continue
        rst.append(arr[i])
        i+=1
    if i == len(arr)-1:
        rst.append(arr[i])
    if change:
        rst = dirReduc(rst)
    return rst



opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)

    return new_plan

def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]

    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)

    return arr
