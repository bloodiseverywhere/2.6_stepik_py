# игра сапер
# 
# Программа принимает на вход количество строк, столбцов, мин, 
# и координаты мин. 
# 
# Она вывводит матрицу, где:
# -1 - мина
# 0 - пустота
# другое - количество мин вокруг

n, m, k = [int(i) for i in input().split()]
a = [[0 for j in range(m)] for i in range(n)]
for i in range(k):
    row, col = (int(i) for i in input().split())
    a[row - 1][col - 1] = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            # тут мы перебираем все соседние элементы
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    # ai, aj - координаты соседнего элемента
                    ai = i + di
                    aj = j + dj
                    # если соседний элемент существует, 
                    # лежит в пределах поля, 
                    # и там стоит мина
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end = '')
        elif a[i][j] == 0:
            print('.', end = '')
        else:
            print(a[i][j], end = '')
    print()