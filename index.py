import numpy as np

# arr = np.array(
#     [
#         [5, 4, 3, 8],
#         [3, 3, 9, 1],
#         [1, 6, 8, 9]
#     ]
# )
# print(arr[:2,1:3])

# Extract last row and col 0, col1
# Extract second row
# Extract third column
# Extract col1 and col2
# slicing part
# print(arr[-1:,:2])
# print(arr[-2,:])
# print(arr[:,2:3])
# print(arr[:,1:3])

arr = np.array(
    [
        [5, 4, 3, 8],
        [3, 3, 9, 1],
        [1, 6, 8, 9]
    ]
)

# print(arr)
# bool_idx = [arr >3]
# print(bool_idx)

# print(arr[arr>3])

# x = np.array([
#     [2,4],
#     [5,3]
# ]
#     )
# # print(x)

# y = np.array([
#     [4,6],
#     [3,5]
# ]
#     )
# print(y)
# print(x,y)
# print(x + y)
# print(np.add(x,y))
# print(np.subtract(x,y))
# print(np.multiply(x,y))
# print(np.divide(x,y))
# print(np.sqrt(x))

# print(x)
# print(x.dtype)

# #set of operators in numpy search on internet
# y = np.array([3,4],[5,6])
# print(y)
# print(y.dtype)

# x = np.array([
#     [2,4],
#     [5,3]
# ]
#     )
# # print(x)

# y = np.array([
#     [4,6],
#     [3,5]
# ]
#     )
# print(y)

# v =np.array([4,5])
# w =np.array([3,6])

# print(v.dot(w))
# print(np.dot(v,w))

# print(x.dot(w))
# print(np.dot(x,w))

# print(x.dot(y))
# print(np.dot(x,y))

# print(x)
# print(x.T)

# u = np.array([
#     [3, 7, 8],
#     [6, 8, 9],
#     [7, 1, 2]
# ])
# # print(u)
# # print(u.T)

# print("Sum of all elements of u: ", np.sum(u))
# # sum of all columns = (axis =0)
# print("Sum of all columns of u: ", np.sum(u, axis=0))
# print("Sum of all rows of u: ", np.sum(u, axis=1))  # sum of rows = (axis =1)


# Broadcasting in Numpy

# x = np.array([
#     [3, 7, 8],
#     [6, 8, 9],
#     [7, 1, 2]
# ])

# v = np.array([1,0,1])

# # for loop route
# # y = np.empty_like(x)
# # print(y)   # empty array of 3*3

# # for i in range(len(x)):
# #     y[i,:] = x[i,:] + v

# # print(x)    
# # print(y)

# # mathematical approach
# stacked_v = np.tile(v,[3,1])

# print(stacked_v)
# print(x + stacked_v)


# print(x + v)    # This is broadcasting in python

# Reshaping in python

# x = np.array([2,3,4])

# print(np.reshape(x,[3,1]))

# y = np.array([
#     [4,5,6],
#     [6,7,9]
# ])

# print(np.reshape(y,[3,2]))

# matsploit


