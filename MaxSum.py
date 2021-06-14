# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

# test.describe("Tests")
# test.it('should work on an empty array')   
# test.assert_equals(max_sequence([]), 0)
# test.it('should work on the example')
# test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

def max_sequence(arr):
    
    sum = 0
    if all(x < 0 for x in arr): 
        return 0

    for index, x in enumerate(arr):
        temp = x
        for y in arr[index+1:]:
            temp += y
            if temp > sum:
                sum = temp

    return sum        
            
print(max_sequence([-2, -1, -3, 4, -1, 2, 1, -5, 4]))  