right_list = [1,2,3,4,5,6,7,8,9]

def done_or_not(board):
    for line in board:
        if sorted(line) != right_list:
            print 'lint Try again!'
            return 'Try again!'
    for i in range(0,9):
        if sorted([board[j][i] for j in range(0,9)]) != right_list:
            print 'colume Try again!'
            return 'Try again!'
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            l = [board[i][j+y] for y in range(3)]
            l += [board[i+1][j+y] for y in range(3)]
            l += [board[i+2][j+y] for y in range(3)]
            if sorted(l) != right_list:
                print i,j,'Try again!'
                return 'Try again!'
    return 'Finished!'
  # your solution here
  # ..
  # return 'Finished!'
  # ..
  # or return 'Try again!'

if __name__ == '__main__':
    def test(a, b):
        if a == b:
            print("right")
        else:
            print(a, "is not equal", b)

    test(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!')
                        
    test(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!')
    