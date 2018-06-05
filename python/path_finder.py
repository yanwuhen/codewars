import string

def path_finder(maze):
    maze = maze.split('\n')
    map_maze = [list(m) for m in maze]
    max_y = len(maze) - 1
    max_x = len(maze[0]) - 1
    cur_y = cur_x = 0
    already = {}
    last_move = []
    while True:
        map_maze[cur_x][cur_y] = 'A'
        #move
        need_revert = False
        for direct in ('→', '↑', '←', '↓'):
            if already.get(direct+str(cur_x)+str(cur_y)):
                continue
            else:
                already[direct+str(cur_x)+str(cur_y)] = True
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
            print(direct)
            last_move.append(direct)
        else:
            need_revert = True
        #judge
        if cur_x < 0 or cur_y < 0 or cur_x > max_x or cur_y > max_y or map_maze[cur_x][cur_y] in ('W','A'):
            need_revert = True
        #revert
        if need_revert:
            if last_move:
                print("revert")
                direct = last_move.pop()
                if direct == '→':
                    cur_x -= 1
                if direct == '↑':
                    cur_y += 1
                if direct == '←':
                    cur_x += 1
                if direct == '↓':
                    cur_y -= 1
            else:
                return False

    return False

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
