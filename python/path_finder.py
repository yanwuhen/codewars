def gen_id(x,y,d):
    return str(x) + ',' + str(y) + ',' + d
def path_finder(maze):
    if len(maze)==1:
        return False
    maze = maze.split('\n')
    map_maze = [list(m) for m in maze]
    max_y = len(maze) - 1
    max_x = len(maze[0]) - 1
    cur_y = cur_x = 0
    already = {}
    last_move = []
    while True:
        map_maze[cur_y][cur_x] = 'A'
        #move
        need_revert = False
        for direct in ('→', '↑', '←', '↓'):
            uid = gen_id(cur_x,cur_y,direct)
            if already.get(uid):
                continue
            else:
                already[uid] = True
                if direct == '→':
                    cur_x += 1
                if direct == '↑':
                    cur_y -= 1
                if direct == '←':
                    cur_x -= 1
                if direct == '↓':
                    cur_y += 1
                if cur_y == max_y and cur_x == max_x:
                    return True
                # print(direct)
                last_move.append(direct)
                break
        else:
            need_revert = True
        #judge
        if cur_x < 0 or cur_y < 0 or cur_x > max_x or cur_y > max_y or map_maze[cur_y][cur_x] in ('W','A'):
            need_revert = True
        # print(cur_x, cur_y, need_revert)
        #revert
        if need_revert:
            if last_move:
                # print("revert")
                # already[gen_id(cur_x,cur_y,direct)] = False
                direct = last_move.pop()
                if direct == '→':
                    cur_x -= 1
                if direct == '↑':
                    cur_y += 1
                if direct == '←':
                    cur_x += 1
                if direct == '↓':
                    cur_y -= 1
            elif cur_x == 0 and cur_y == 0:
                return False
            else:
                raise Exception("this is a exception")

    return True

if __name__ == '__main__':
    a = "\n".join([
    ".W.",
    ".W.",
    "..."
    ])

    b = "\n".join([
    ".W.",
    ".W.",
    "W.."
    ])

    c = "\n".join([
    "......",
    "......",
    "......",
    "......",
    "......",
    "......"
    ])

    d = "\n".join([
    "......",
    "......",
    "......",
    "......",
    ".....W",
    "....W."
    ])
    print(path_finder(a))#True
    print(path_finder(b))#False
    print(path_finder(c))#True
    print(path_finder(d))#False

# def path_finder(maze):
#     g = maze.splitlines()
#     end, bag = len(g[0]) -1 + len(g) * 1j - 1j, {0}
#     grid = {x + y * 1j for y,l in enumerate(g) for x,c in enumerate(l) if '.' == c}
#     while bag:
#         if end in bag: return True
#         grid -= bag
#         bag = grid & set.union(*({z + 1j ** k for k in range(4)} for z in bag))
#     return False



# sys.setrecursionlimit(5000)

# def can_solve(maze, x, y):
#     if x == len(maze)-1 and y == len(maze)-1:
#         return True
#     if (x == len(maze) or x < 0) or (y == len(maze) or y < 0) or (maze[y][x] == 'W' or maze[y][x] == 'X'):
#         return False
#     maze[y][x] = 'X'
#     if can_solve(maze, x+1, y):
#         return True
#     if can_solve(maze, x, y+1):
#         return True
#     if can_solve(maze, x-1, y):
#         return True
#     if can_solve(maze, x, y-1):
#         return True
#     return False
    
# def path_finder(maze):
#     return can_solve([list(y) for y in maze.split('\n')], 0, 0)