class Pascal:
    def __init__(self, depth):
        self._depth = depth
        self._data = dict()

    def get_value(self, x, y):
        # if self._data[x,y]:
        #     return self.data[x,y]

        if x == 0 or y == 0 or y == x:
            return 1
        return self.get_value(x - 1, y - 1) + self.get_value(x - 1, y)

    def populate_data(self):
        for x in range(self._depth):
            # Base case for first row
            if x == 0:
                self._data[x,0] = 1
                continue
            for y in range(x + 1):
                
                self._data[x,y] = self.get_value(x,y)

                

    def draw(self):
        for x in range(self._depth):
            for i in range(self._depth - x - 1):
                print(" ", end='')
            for y in range(x + 1):
                if self._data[x,y] < 10:
                    print(self._data[x,y], end='  ')
                else:
                    print(self._data[x,y], end=' ')
            print()

