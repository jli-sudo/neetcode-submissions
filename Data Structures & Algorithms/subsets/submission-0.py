class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current_bucket):
            result.append(list(current_bucket))

            for i in range(start, len(nums)):
                current_bucket.append(nums[i])

                backtrack(i + 1, current_bucket)

                current_bucket.pop()

        backtrack(0, [])
        return result
        

