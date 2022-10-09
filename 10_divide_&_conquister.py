from operator import le


A = [-5,-23,5,0,23,-6,23,67]
C = []  

while A:
  minimum = A[0]
  for i in A:
    if i < minimum:
      minimum = i
      print(minimum)
      
  C.append(minimum)
  A.remove(minimum)
  
  print(C)
  

def merging(left, right):
  C = []
  while min(len(left), len(right)) > 0:
    if left[0] > right[0]:
      insert = right.pop(0)
      #print(min(len(left), len(right)))
      C.append(insert)
      
    elif left[0] <= right[0]:
      insert = left.pop(0)
      #print(min(len(left), len(right)))
      C.append(insert)
  
  print(f"before while {C}")
      
  if len(left) > 0:
    for i in left:
      C.append(i)
      print(f"left: {C}")
  
  if len(right) > 0:
    for i in right:
      C.append(i)
      print(f"right: {C}")
      
  return C


l = [2,5,6,10]
r = [3,4,12,20]
print(min(len(l), len(r)))
print(merging(l, r))

def sortArray(A):
  if len(A) <= 0:
    return A
  middle = len(A) // 2
  left = sorted(A[:middle])
  right = sorted(A[middle:])
  merged = []
  
  while left and right:
    if left[0] <= right[0]:
      merged.append(left.pop(0))
    else:
      merged.append(right.pop(0))
  
  merged.extend(right if right else left)
  return merged


arr = [100,-1000,25,54,8,74,98,64,-23,0,1,5,4,6,9,98,98,98,3485,156165]   
print(sortArray(arr))  

class Solution(object):
  def sortArray(self, nums):
    #iterative merge sort using sorted
    mid = len(nums) // 2
    left = sorted(nums[:mid])
    right = sorted(nums[mid:])
    C = []
    while min(len(left), len(right)) > 0:
      if left[0] > right[0]:
        insert = right.pop(0)
        #print(min(len(left), len(right)))
        C.append(insert)
      
      elif left[0] <= right[0]:
        insert = left.pop(0)
        #print(min(len(left), len(right)))
        C.append(insert)
  
    print(f"before while {C}")
      
    if len(left) > 0:
      for i in left:
        C.append(i)
        print(f"left: {C}")
    
    if len(right) > 0:
      for i in right:
        C.append(i)
        print(f"right: {C}")
      
    return C
 
 
ordenado = Solution()
sortArray(arr)
print(ordenado)