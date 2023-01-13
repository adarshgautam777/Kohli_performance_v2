import numpy as np
arr = np.array(
    [[1, 2, 3]
     ]
)
# print(arr)
# print("Type of array: ", type(arr))
# print("Shape of array: ", arr.shape)
# print(type(np))

arr2D = np.array(
    [
        [2, 3, 7],
        [5, 6, 9]
    ]
)
# arr2D[1][0] =90
# print(arr2D, arr2D.shape)
# print(arr[0])
# print(
#     arr2D[0, 0], arr2D[0, 1]
# )
# print(
#     arr2D[1, 0], arr2D[1, 1]
# )
# print(
#     arr2D[0, 2], arr2D[1, 2]
# )

# arr3D = np.array([
#     [
#         [1, 2, 3],
#         [2, 3, 4],
#         [3, 4, 5]
#     ],
#     [
#         [5, 6, 3],
#         [6, 4, 7],
#         [7, 8, 9]
#     ],
#     [
#         [2, 6, 9],
#         [6, 8, 9],
#         [8, 1, 9]
#     ]
# ]
# )
# print(arr3D)
# print(
#     arr3D[0, 0, 0], arr3D[0, 1, 0]
# )
# print(arr3D[0])
# print(arr3D[0][0])
# print(arr3D[0][0][0])
# print(arr3D[0][0][1])

arr2D = np.array(
    [
        [2, 3, 7],
        [5, 6, 9]
    ]
)

# arr2D[0] = [4,5]

# print(arr2D)

zeros = np.zeros((4,5))
print(zeros)

ones = np.ones((3,))
print(ones)

print(zeros.dtype)

const = np.full((3,3), 9)
print(const)

rand = np.random.random((4,4))
print(rand)