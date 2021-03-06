'''
Question:
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
'''
def intersectionofThreeArray(arr1, arr2, arr3):
    finalList = []
    for i in arr1:
        if i in arr2:
            if i in arr3:
                finalList.append(i)
    return finalList

def intersectionofThreeArray(arr1, arr2, arr3):
    return list(set(arr1)&set(arr2)&set(arr3))