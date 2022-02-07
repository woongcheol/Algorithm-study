# 1. Bubble Sort
# import random

# def bubble_sort(data):
#     for idx in range(0, len(data)-1):
#         sorted = False
#         for idx2 in range(len(data)-idx-1):
#             if data[idx2] > data[idx2+1]:
#                 data[idx2], data[idx2+1] = data[idx2+1], data[idx2]
#                 sorted = True
#         if sorted == False:
#             break
#     return data

# data = random.sample(range(30), 10)
# print(data)
# print(bubble_sort(data))

# 2. Insert Sort
import random

def insert_sort(data):
    for idx in range(1, len(data)):
        for idx2 in range(idx, 0, -1):
            if data[idx2] < data[idx2-1]:
                data[idx2], data[idx2-1] = data[idx2-1], data[idx2]
            else:
                break
    return data


data = random.sample(range(30), 10)
print(data)
print(insert_sort(data))