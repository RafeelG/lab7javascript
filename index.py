

def index(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i



print(index([3,5,2,1,5], 6))
print(index([3,5,2,1,5], 10))
print(index([1, 3, 5, 6, 7, 2], 3))


# [3,5,2,1,5]

    # for i, num in enumerate(nums):
    # this looks like this:
    # 0: 3
    # 1: 5
    # 2: 2
    # 3: 1
    # 4: 5

def add_linked_lists(l1, l2):
    l1 = l1[::-1]
    l2 = l2[::-1]
    l1 = int("".join(map(str, l1)))
    l2 = int("".join(map(str, l2)))
    sum = l1 + l2
    sum = str(sum)
    sum = sum[::-1]
    return list(map(int, sum))

print(add_linked_lists([2,4,3], [5,6,4]))
    













            
