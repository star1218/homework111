# import random #задание 1,1
# NUM_SIZE=10
# numbers=[]
# for i in range(NUM_SIZE):
#     numbers.append(random.randint(-10,10))
# print(numbers)
# negative_sum=0
# for num in numbers:
#     if num<0:
#         negative_sum +=num
# print(negative_sum)

# import random #1 задание 2
# NUM_SIZE=10
# numbers=[]
# for i in range(NUM_SIZE):
#     numbers.append(random.randint(1,10))
# print(numbers)
# sum=0
# for num in numbers:
#     if num % 2==0:
#         sum+=num
# print(sum)

# import random #1 задание 3
# NUM_SIZE=10
# numbers=[]
# for i in range(NUM_SIZE):
#     numbers.append(random.randint(1,10))
# print(numbers)
# sum=0
# for num in numbers:
#     if num %2!=0:
#         sum+=num
# print(sum)

# import random #1 задание 4
# NUM_SIZE=10
# numbers=[]
# for i in range(NUM_SIZE):
#     numbers.append(random.randint(1,10))
# print(numbers)
# sum=0
# for num in numbers:
#     if num % 3== 0:
#         sum+=num
# print(sum)


# import random #задание 1,5
#
# NUM_SIZE = 10
# numbers = []
# for i in range(NUM_SIZE):
#     numbers.append(random.randint(1, 10))
# print(numbers)
# min_index = numbers.index(min(numbers))
# max_index = numbers.index(max(numbers))
# start_index = min(min_index, max_index) + 1
# end_index = max(min_index, max_index)
# product = 1
# for num in numbers[start_index:end_index]:
#     product *= num
# print(product)

# numbers = [-2, -1, 3, -4, -5, 6, -7] # 1,6
# positive_numbers = [num for num in numbers if num > 0]
# if positive_numbers:
#     product = 1
#     for num in positive_numbers:
#         product += num
#     print(product)

# nums_1=[1,2,3,4,5,6,7,8,9]  #2,1
# nums_copy=nums_1.copy()
# numbers=[]
# for num in nums_1:
#     if num % 2==0:
#         numbers.append(num)
# print(nums_copy)
# print(numbers)

# nums_1=[1,2,3,4,5,6,7,8,9]  #2,2
# nums_copy=nums_1.copy()
# numbers=[]
# for num in nums_1:
#     if num % 2!=0:
#         numbers.append(num)
# print(nums_copy)
# print(numbers)

# nums_1=[1,2,3,4,5,-1,-2,-3,-4,-5] #2,3
# nums_copy=nums_1.copy()
# negetive_numbers=[]
# for num in nums_1:
#     if num <0:
#         negetive_numbers.append(num)
# print(nums_copy)
# print(negetive_numbers)

# nums_1=[1,2,3,4,5,-1,-2,-3,-4,-5] #2,4
# nums_copy=nums_1.copy()
# negetive_numbers=[]
# for num in nums_1:
#     if num >0:
#         negetive_numbers.append(num)
# print(nums_copy)
# print(negetive_numbers)
# --------------------------