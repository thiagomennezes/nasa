class SpaceProbe:
    def __init__(self, x=0, y=0, direction='', instructions=""):
        self.x = x
        self.y = y
        self.direction = direction
        self.instructions = instructions

    def run(self, highland):
        for instruction in self.instructions:
            if instruction == 'L':
                self.__rotate_left()
            elif instruction == 'R':
                self.__rotate_right()
            elif instruction == 'M':
                self.__move(highland)
        print(f"{self.x} {self.y} {self.direction}")

    def __move(self, highland):
        if self.direction == 'N':
            y = self.y + 1
            self.y = min(highland[1][1], y)
        elif self.direction == 'E':
            x = self.x + 1
            self.x = min(highland[1][0], x)
        elif self.direction == 'S':
            y = self.y - 1
            self.y = max(highland[0][1], y)
        elif self.direction == 'W':
            x = self.x - 1
            self.x = max(highland[0][0], x)

    def __rotate_left(self):
        directions = ["N", "W", "S", "E", "N"]
        i = directions.index(self.direction)
        self.direction = directions[i+1]

    def __rotate_right(self):
        directions = ["N", "E", "S", "W", "N"]
        i = directions.index(self.direction)
        self.direction = directions[i+1]

