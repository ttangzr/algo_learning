#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 8:30 下午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 665-Non-decreasing Array.py
# @Software: PyCharm

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # method-1: greedy
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                cnt += 1
                if i - 2 >= 0 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
                # else:
                #     nums[i - 1] = nums[i]
            if cnt > 1:
                return False
        return True


if __name__ == "__main__":
    obj = Solution()
    # nums = [3, 4, 2, 3]     # False
    # nums = [-1, 4, 2, 3]    # True
    nums = [5, 7, 1, 8]     # True
    print(obj.checkPossibility(nums))
