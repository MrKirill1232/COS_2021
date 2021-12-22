import math

r = 1
n_a = 3

A = []

B = []

b = []

for i in range(n_a):
    A_2 = [[0] * r for i in range(3)]
    for n in range(n_a):
        if n == 0 & i == 0:
            print("A[" + str(i) + "," + str(n) + "] = ")


        A_2[n] = input()
        print("A[" + str(i) + "," + str(n) + "] = " + str(A_2[n]))


        n = n + 1
    A.append(A_2)
    i = i + 1
print(A[0])
print(A[1])
print(A[2])
print("Знахождення модуля матриці")

A_task_2 = []
A_task_2.append(A)

for i in range(n_a):
    for n in range(n_a):
        j = A_task_2[i,n]
        A_task_2[i][n] = math.fabs(j)
        n = n + 1
    i = i + 1
print(A_task_2[0])
print(A_task_2[1])
print(A_task_2[2])
