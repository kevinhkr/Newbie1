import random
import time

print('Hi! Welcome to Battleship 1.0 made by Kairan Huang.')
time.sleep(0.5)
print('In this game you\'ve got to find out the location of the whole Battleship.')
time.sleep(0.5)
print('You have 20 moves, good luck!')
time.sleep(0.5)
i = int(input('The size of the game: '))
time.sleep(0.5)
matrix = []

for k in range(i):
    matrix.append([0]*i)

# 随机决定中心点位置
xx = random.randint(0, i-1)
yy = random.randint(0, i-1)
matrix[xx][yy] = 1
zz = random.randint(1, 2)  # zz决定船是横着放的还是竖着放的，1代表横着放（y轴），2代表竖着放（x轴）

# print(matrix) # 调试


# 放置一个1*3的战船
if zz == 1:  # 如果是横着放的
    if yy == 0:  # 确保中心不能靠左边
        yy = 1
    elif yy == i-1:  # 确保中心不能靠右边
        yy = i-2
    matrix[xx][yy] = 1
    matrix[xx][yy+1] = 1
    matrix[xx][yy-1] = 1
else:  # 如果是竖着放的
    if xx == 0:  # 确保中心不能靠上边
        xx = 1
    elif xx == i-1:  # 确保中心不能靠下边
        xx = i-2
    matrix[xx][yy] = 1
    matrix[xx+1][yy] = 1
    matrix[xx-1][yy] = 1

# print(matrix) # 调试

# 猜战船位置
for round1 in range(31):

    if round1 == 20:  # 猜的次数到20次了
        time.sleep(0.5)
        print('Game over! You took too many moves!')
        break

    gsrow = int(input('The row you guess the ship is in: '))
    gscol = int(input('The column you guess the ship is in: '))

    if gsrow > i or gscol > i:  # 猜的坐标超出范围
        time.sleep(0.5)
        print('Man that is not even in the ocean!')
    else:
        if matrix[gsrow - 1][gscol - 1] == 1:  # 猜中船
            time.sleep(0.5)
            print('Oh! You hit the ship!')
            matrix[gsrow - 1][gscol - 1] = 3  # 1是没猜过的船，3是猜过的船
            if zz == 1:  # 横着放，如果这一行没有没猜过的船，游戏结束
                if 1 not in matrix[xx]:
                    time.sleep(0.5)
                    print('Well done! Game over!')
                    break
            elif zz == 2:  # 竖着放，如果这一列没有没猜过的船，游戏结束
                if 1 not in matrix[xx] and 1 not in matrix[xx + 1] and 1 not in matrix[xx - 1]:
                    time.sleep(0.5)
                    print('Well done! Game over!')
                    break
        elif matrix[gsrow - 1][gscol - 1] == 0:  # 没猜中
            time.sleep(0.5)
            print('Nah,nothing there.')
            matrix[gsrow - 1][gscol - 1] = 2
        elif matrix[gsrow - 1][gscol - 1] == 2:  # 同一个地点猜过一次了
            time.sleep(0.5)
            print('You hit there once, try again!')
