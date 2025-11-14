class Dingus:
    def __init__(self, name : str, age : int, is_khan : bool):
        self._name = name
        self._age = age
        self._is_khan = is_khan
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old. {self.is_khan}"
    
    def get_name(self) -> str: return self._name
    def get_age(self) -> int: return self._age
    def get_is_khan(self) -> str: 
        if self._is_khan == True: return "Dingus Khan, indeed"
        else: return "Just plain Dingus."

    def set_name(self, name : str): self._name = name
    def set_age(self, age : int): self._age = age
    def set_khan_status(self, is_khan : bool): self._is_khan = is_khan

    name : str = property(get_name, set_name)
    age : int = property(get_age, set_age)
    is_khan : bool = property(get_is_khan, set_khan_status)