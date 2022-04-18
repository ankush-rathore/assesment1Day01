
# problem 1 day02(identity matrix)

# n = int(input("enter the number"))
# matrix = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
# print("the matrix of {} * {}: ".format(n, n))
# for m in matrix:
#     print(m)


# problem 2 day02(ArmStrong Number)

# first = 1
# last = 500
# while first <= last:
#     res = 0
#     temp = first
#     noOfDigit = 0
#
#     while temp > 0:
#         temp = int(temp/10)
#         noOfDigit = noOfDigit + 1
#     num = first
#     while num > 0:
#         rem = num % 10
#         pow = 1
#         i = 0
#         while i <noOfDigit:
#             pow = pow * rem
#             i = i + 1
#         res = res + pow
#         num = int(num/10)
#     if res == first:
#         print(res)
#     first = first + 1


# 3. mazic matrix

# def generateSquare(n):
# # 2-D array with all
# # slots set to 0
#     magicSquare = [[0 for x in range(n)]
#                     for y in range(n)]
# # initialize position of 1
#     i = n / 2
#     j = n - 1
# # Fill the square by placing values
#     num = 1
#     while num <= (n * n):
#         if i == -1 and j == n: # 3rd condition
#             j = n - 2
#             i = 0
#         else:
# # next number goes out of
# # right side of square
#             if j == n:
#                 j = 0
# # next number goes
# # out of upper side
#             if i < 0:
#                 i = n - 1
#         if magicSquare[int(i)][int(j)]: # 2nd condition
#             j = j - 2
#             i = i + 1
#             continue
#         else:
#             magicSquare[int(i)][int(j)] = num
#             num = num + 1
#         j = j + 1
#         i = i - 1   # 1st condition
# # Printing the square
#     print ("Magic Square for n =", n)
#     print ("Sum of each row or column", n * (n * n + 1) / 2, "\n")
#     for i in range(0, n):
#         for j in range(0, n):
#             print('%2d ' % (magicSquare[i][j]), end = '')
# # To display output
# # in matrix form
#             if j == n - 1:
#                 print()
# # Driver Code
# # Works only when n is odd
# n=int(input("Number of rows of the Magic Square:"))
# generateSquare(n)




