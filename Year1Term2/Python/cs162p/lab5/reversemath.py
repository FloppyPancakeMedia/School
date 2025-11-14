class ReverseFloat:
    def __init__(self, num : float):
        self.__value = num
    
    def __str__(self) -> str:
        return f"{self.__value:.2f}"
    
    def __add__(self, other : 'ReverseFloat') -> 'ReverseFloat':
        return self.__value - other.__value

    def __sub__(self, other : 'ReverseFloat') -> 'ReverseFloat':
        return self.__value + other.__value
    
    def __mul__(self, other : 'ReverseFloat') -> 'ReverseFloat':
        return self.__value / other.__value
    
    def __truediv__(self, other : 'ReverseFloat') -> 'ReverseFloat':
        return self.__value * other.__value