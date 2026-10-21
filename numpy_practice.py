import numpy as np

#------------------- Numpy Shape and Array Assigned ---------- #
# balance= np.array([
#     [
#         [100,200,300],
#         [400,500,600]
#     ],
#     [
#         [700,800,900],
#         [250,350,450]
#     ]
# ])


# print(balance[0,1,2])
# print(balance[1,1,1])

#------------------- Numpy Reshape and Indexing ---------- #
# Increement= np.array([1,2,3,4,5,6,7,8,9,10])
# print(Increement)
# Increement2= Increement.reshape(2,5)
# print(Increement2)

# print(f"The Dimention of the array is :{np.ndim(balance)}D")
# print(f"The Structure of the array is: {balance}")
# print(f"The Shape of the array is:{np.shape(balance)}")

balance= np.array([1,2,3,4,5,6,7,8,9,10])
copy= balance.copy()
print(np.mean(balance))
print(np.std(balance))
print(np.min(balance))
print(np.max(balance))
print(f"The Copied Array is :{copy}")
print(f"Sliced Array is :{copy[0:8]}")


