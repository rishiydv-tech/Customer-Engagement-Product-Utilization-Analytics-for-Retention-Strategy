# import numpy as np

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

# balance= np.array([1,2,3,4,5,6,7,8,9,10])
# copy= balance.copy()
# print(np.mean(balance))
# print(np.std(balance))
# print(np.min(balance))
# print(np.max(balance))
# print(f"The Copied Array is :{copy}")
# print(f"Sliced Array is :{copy[0:8]}")

#------------------- Numpy Assigment ---------- #
import numpy as np
# ndarrray= np.array([1,2,3,4])
# a= np.array(10)
# b= np.array([1,2,3])
# c= np.array([[1,2,3],
#              [4,5,6]])
# d= np.array(
#     [[[1,2,3],
#     [4,5,6]],

#     [[1,2,3],
#     [4,5,6]]]
# )
# print(
#     f"""The Dimention of array a is: {np.ndim(a)}
# The Dimension of array b is: {np.ndim(b)}
# The Dimension of array c is: {np.ndim(c)}
# The Dimension of array c is: {np.ndim(d)}"""
# )

# print(
#     f"""The shape of array a is: {np.shape(a)}
# The shape of array a is: {np.shape(b)}
# The shape of array a is: {np.shape(c)}
# The shape of array a is: {np.shape(d)}"""
# )

# print(
#     f"""The DataType of array a is: {a.dtype}
# The DataType of array b elements is: {b.dtype}
# The DataType of array c elements is: {c.dtype}
# The DataType of array d elements is: {d.dtype}"""
# )

# print(f"""The DataType of the Variable a is : {type(a)}
# The DataType of the Variable b is : {type(b)}
# The DataType of the Variable c is : {type(c)}
# The DataType of the Variable d is : {type(d)}""")

# print(
#     f"""
#     The length of the array b is : {len(b)}
# """
# )

# l1=[10,20,30]
# l2= [40,50,60]
# l3= np.array([10,20,30])
# l4= np.array([40,50,60])
# for x, y in zip(l3,l4):
#     print(x*y)

l5= np.arange(1,11) # List creation using Numpy
print(l5) 

l6= np.arange(1,11,2) #2-2 Gap Between the list
print(l6)

l7=np.eye(3) #Used to create a identity Matrix
print(l7)

x=np.arange(1,17)
# y=x.reshape(2,4,4)
x= x.reshape(4,-1) # -1 Stands for known dimension(Numpy Calculate itself ....Means just give the row and -1)
print(f"""The Reshaped 2D Array is:
{x}
""")
z= x.reshape(2,4,-1)
print(f"""The Reshaped 3D Array is:
{z}
""")
flatten_z= z.flatten()
print(f""" The flattened z is : 
{flatten_z}
""")

comp_array= np.arange(1,17)
array_list=[]
for x in comp_array:
    if x%2==0:
        array_list.append(x)
even_array=np.array(array_list)
print(
    f"""
The Even Array is :
{even_array}
    """
)
print(even_array[2], even_array[4], even_array[6], even_array[7])

array= np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
print(array[2,2])

b