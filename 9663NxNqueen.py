"""

0 1 2 3 ///|x-y| 맵
1 0 1 2
2 1 0 1
3 2 1 0

1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

가로 세로 x, y값이 달라야 하고 추가로 왼쪽 대각선으로는 x+y값이 달라야 하고 오른쪽 대각선으로는 |x-y| 값이 달라야 함
"""
n = int(input())
all_of_coordinate = []
queen_lst = []
def coordinate_list():
    for i in range(n):
        for j in range(n):
            all_of_coordinate.append([i, j])
coordinate_list()

for coordinate in all_of_coordinate:
    queen = coordinate
    queen_lst.append(queen)










