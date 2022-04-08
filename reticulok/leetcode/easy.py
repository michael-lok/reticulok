from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    Elements can only be used once.
    You can return the answer in any order.

    Args:
        nums (list): array of integers
        target (int): target number that two integers should sum up to

    Returns:
        list: indices from initial list that add up to target.
    """
    nums_range = range(len(nums))
    for i in nums_range:
        for j in [x for x in nums_range if x != i]:
            if nums[i] + nums[j] == target:
                return [i, j]
    raise ValueError("Impossible to obtain %s with %s", target, nums)
