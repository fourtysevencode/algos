from typing import List
class Solution:
    def search(self, arr: List[int], target: int):
        l,r = 0, len(arr)-1 #len(arr) -1 == index of last
        while l<=r: #while they dont cross (while havent checked all)
            mid = (l+r)//2
            if target == arr[mid]:
                return f"present at {mid}"
            elif target <= arr[mid]:
                r = mid - 1
            elif target >= arr[mid]:
                l = mid + 1
        return "not present"

solution = Solution()

print(solution.search([1,2,3,4,5], 6))
