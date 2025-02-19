
def twoSum(nums: list[int], target: int) -> list[int]:

        num_sp={}
        results=[]
        
        for i, num in enumerate(nums):
              awe=target-num
              if awe in num_sp:
                results.append([num_sp[awe], i])
              num_sp[num] = i
        return results

nums = [2,7,1,1,1,5,9,2,8,3,7,4,5]
target = 10
result = twoSum(nums, target)

print(result)
