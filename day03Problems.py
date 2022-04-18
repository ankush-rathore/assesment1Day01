# 1.Write a Python script to concatenate following dictionaries to create a new one.

# Sample Dictionary :
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# resDic4 = {**dic1, **dic2, **dic3}
# print(resDic4)


# 2.Write a Python script to check whether a given key already exists in a dictionary
# dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# newKey = int(input("enter the key\n"))
# if newKey in dic1:
#     print("yes it is in the dictionary")
# else:
#     print("it is not")


# 3. Write a Python program to iterate over dictionaries using for loops

# dic1 = {1: 10, 'ankush': 20, 3: 30, 'jay': 40, 5: 50, 'vijay': 60}
# for key, value in dic1.items():
#     print(key, value)


# 4. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# d = {}
# print(type(d))
# n = 5
# for i in range(1, n+1):
#     d[i] = i * i
# print(d)


# 5. Write a Python program to remove duplicates (values) from Dictionary

# dic1 = {1: 10, 'ankush': 'rathore', 78 : 30, 'yaro': 'rathore', 'jay': 'rathore', 'jay': 'kushwah'}
# zen = []
# print(type(zen))
# res1 = {}
#
# for key, value in dic1.items():
#     if value not in zen:
#         zen.append(value)
#         res1[key] = value
# print(res1)



# 6.  Write a code to get the key of a minimum value from a dictionary

# myDic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(min(myDic, key = myDic.get))


# 7. Reverse a list in Python
# myList = ['ankush', 'jay', 'virat', 'sachin', 'dhoni']
# print(type(myList))
# myList.reverse()
# print(myList)


# 8 . Remove all occurrences of a specific item from a list.
# myFavList = [1, 4, 7, 4, 9, 1, 6, 5]
# value = 1
# try:
#     while True:
#         myFavList.remove(value)
# except ValueError:
#     pass
# print(myFavList)


# 9. Write a Python program to sum all the items in a list
# myFavList = [1, 4, 7, 4, 9, 1, 6, 5]
# print(sum(myFavList))
# sum = 0
# for i in myFavList:
#     sum += i
# print(sum)


# 10. Write a Python program to get the second largest number from a list
# myFavList = [1, 4, 7, 4, 9, 1, 6, 5]
# myFavList.sort()
# print(myFavList[-2])


#11. Write a Python program to find the second smallest number in a list

# myFavList = [1, 4, 7, 3, 9, 2, 6, 5]
# myFavList.sort()
# print(myFavList[1])



# 12. Write a Python program to get unique values from a list.

# myFavList = [2, 45, 74, 89, 74, 45, 89]
# print(myFavList)
# myFavSet = set(myFavList)
# newList = list(myFavSet)
# print(newList)



# 13. Write a Python program to get count of repetition of each value from a list.

# myBigList = ['ankush', 'jay', 'viru','ankush']
# i = input("enter the value\n")
# repeValue = myBigList.count(i)
# print(repeValue)


# 14. Write a Python program to find common items from two lists.

# a = [2, 4, 6, 8, 10]
# b = [1, 2, 3, 4, 5]
# sameElement = set(b).intersection(set(a))
# print(sameElement)


# 15. Write a Python program to count number of lists in a list of lists.
# def myBigList_count(myList):
#     return len(myList)
# myList = [1, 3, 6, 54, 67, [1, 2]]
# print(myBigList_count(myList))