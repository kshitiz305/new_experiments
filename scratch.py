# To build a house, the construction team levels a squared plot of land. You are given an array ground where ground[i] is a square i  height in meters.
#
# Per one operation constructors lower or raise the square i by one meter. Determine the minimum number of operations to completely level the entire land plot.
#
# Input:
#
# ground  - integer array, 0<length(ground)<20, 0<ground[i]<200
# Output:
#
# integer - number of operations to completely level the entire land plot, that is to make an entire array consist of the same values.
# Example1:
#
# ground = [1, 3, 2, 2]
# get_result(ground) = 2 //In two operations it is possible to make the array completely equal.
# [1, 3, 2, 2]
# [*2*, 3, 2, 2]
# [2, *2*, 2, 2]
# Example2:
#
# ground = [6, 2, 8, 1]
# get_result(ground) = 11
# ! Important It is necessary to have only 60% tests passed to complete the challenge
#

# def get_result(ground):
#     n = len(ground)
#     avg_height = sum(ground) // n
#     total_ops = 0
#     for i in range(n):
#         total_ops += abs(ground[i] - avg_height)
#     return total_ops

def get_result(ground):
    # Find the minimum and maximum values in the array
    min_val = min(ground)
    max_val = max(ground)

    # Initialize the minimum number of operations to a large value
    min_ops = float('inf')

    # Try all possible levels between the minimum and maximum
    for level in range(min_val, max_val + 1):
        # Calculate the number of operations required to level the entire array to this level
        ops = sum(abs(level - x) for x in ground)

        # If the number of operations is smaller than the current minimum, update the minimum
        if ops < min_ops:
            min_ops = ops

    return min_ops

#
# An array of Latin characters is given. Each character in the array can be replaced by any natural number. After replacing, all identical characters will also be replaced by the same number.
#
# Determine if it is possible to make the sum of the array values equal to k.
#
# Input:
#
# sub_array - Latin characters array, 0<length(sub_array)<20, sub_array[i]="x" | "y" | "z"
# k - the value of the array sum to get, 0<k<150
# Output:
#
# boolean - it is possible to make the sum of the array values  sub_array equal to k
# Example1:
#
# sub_array = ["x", "x", "x", "y", "y"]
# k = 12
# get_result(sub_array, k) = True // You can replace x by 2, y by 3, then you get [2, 2, 2, 3, 3]
# Example2:
#
# sub_array = ["x","x","y","y"]
# k = 20
# get_result(sub_array, k) = True


def countSol(values, start, end, k):
    # Base case
    if (k == 0):
        return 1
    result = 0
    for i in range(start, end + 1):
        if (values[i] <= k):
            result += countSol(values, i, end,
                               k - values[i])

    return True if result>0 else False


def get_result(sub_array, k):
    # count the frequency of each character
    freq = {}
    for char in sub_array:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # get the unique values from the frequency dictionary
    values = list(set(freq.values()))
    n = len(values)
    return countSol(values, 0, n - 1, k)




sub_array = ["x","x","y","y"]
k = 20
# sub_array = ["x", "x", "x", "y", "y"]
# k = 12
print(get_result(sub_array, k))




def StringChallenge(strParam):
    stack = []
    elements = set(['b', 'i', 'em', 'div', 'p'])
    i = 0
    while i < len(strParam):
        if strParam[i] == '<':
            if strParam[i+1] == '/':
                if len(stack) == 0:
                    return strParam[i+2:strParam.index('>', i+2)]
                elif stack[-1] == strParam[i+2:strParam.index('>', i+2)]:
                    stack.pop()
                else:
                    return stack[-1]
            else:
                j = i + 1
                while strParam[j] != '>':
                    j += 1
                tag = strParam[i+1:j]
                if tag not in elements:
                    return tag
                stack.append(tag)
            i = j
        else:
            i += 1
    if len(stack) == 0:
        return "true"
    else:
        return stack[-1]
