# print the pattern
# a.
# r = 4
# c = 1
# for i in range(5):
#     for j in range(1, i+1):
#         print(c, end = "")
#         c = c+1
#     print()


# b.
# n = 6
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(i, end = " ")
#     print()


# c.
# n = 10
# c = 1
# for i in range(1, 10):
#     for j in range(i, i+1):
#         print(c, end = " ")
#         c = c+1
#     print()



# 2. Fibonacci series
# nterms = int(input("enter the num of terms"))
# n1, n2, = 0, 1
# count = 0
# if nterms == 1:
#     print(n1)
# else:
#     print("Fibonacci series:")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#
#         n1 = n2
#         n2 = nth
#         count += 1


# 3. Strong number
# def fac(n):
#     f = 1
#     for i in range(1, n+1):
#         f = f * i
#         return f
# n = int(input("enter the number\n"))
# m = str(n)
# l = len(m)
# sum = 0
# for i in m:
#     sum = sum + fac(int(i))
# if sum == n:
#     print("strong number")
# else:
#     print("it is not strong number")







# 4.Pascal traiangle
# n = 5
# for i in range(1, n+1):
#     for j in range(0, n-i+1):
#         print(' ', end = ' ')
#
#     C = 1
#     for j in range(1, i+1):
#         print(' ', C, sep = ' ', end = ' ')
#
#         C = C * (i - j) // j
#     print()



# 5. greedy problem

cntr = 0
j = 1
while cntr < 6:
    num = j
    flag = False
    lst = []
    for i in range(3):
        if (num - 1) % 3 == 0:
            res = (num - 1) // 3 + 1
            lst.append(res)
            if i == 2:
                flag = True
        else:
            break
    if flag and num and num % 3 == 0:
        print("Total {} --> remaining{} --> father distributes {} to each daughter".formate(j, num, num//3))
        print("\t\tDaughter #1 --> {}\n\t\tDaughter #2 -->")

        cntr += 1
    j += 1


