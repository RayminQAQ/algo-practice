"""
Problem : Contains Duplicate
Platform: NeetCode
Link    : https://neetcode.io/problems/duplicate-integer/question
Topic   : Arrays & Hashing
Level   : Easy


- 思路：建立 hash table 在搜索的過程中進行儲存，如果有跟 hash table 重複就 return true。
  複雜度:
        Time : O(N)
        Space: O(N)
"""
from typing import List

class Solutionv1:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num not in numSet:
                numSet.add(num)
                continue
            return True
        return False

if __name__ == "__main__":
    # 簡單自測
    s = Solutionv1()
    assert s.hasDuplicate([1]) == False
    assert s.hasDuplicate([1, 2, 3]) == False
    assert s.hasDuplicate([1, 2, 3, 2]) == True
    
    print("ok")
