arr1=[45,55]
arr=[1,3,5,6,8]
from array import*

def traversal(array):
    for i in array:
        print(i)
#traversal(arr)
#arr.append(3)
#arr.insert(0,4)
#arr.extend(arr1)
#arr.remove(3)
#print(arr.index(3))
#arr.reverse()
#print(arr.count(1))
#templist=arr.tolist()%
#arr4=str(arr)
#arr5=list(arr)


#####TWO DIMENTIONAL ARRAY#####
from numpy import*
twodarray=array([[1,2,4,5],[3,46,8,9],[45,67,888,66]])
#twodarray=insert(twodarray,0,[33,4,45,66],axis=0)
#print(twodarray[2][3])


# def traversal2d(array):
#     for i in range(len(array)):
#         for j in range(len(array)):
#             print(array [i][j])
# print(traversal2d(twodarray))##


# def search2d(array,value):
#     for i in range(len(array)):
#         for j in range(len(array)):
#             if array[i][j]==value:
#                 return i,j
#     return 'elemnet not fouhnd'
# print(search2d(twodarray,888))

two=delete(twodarray,1,0)
print(two)












