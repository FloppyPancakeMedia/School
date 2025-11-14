class MyMath:
    def __init__(self):
        pass
    
    def absolute(self, num : int) -> int:
        if num < 0: return num * -1
        else: return num
    
    def average(self, nums : list[float]) -> float:
        return sum(nums) / len(nums)

    