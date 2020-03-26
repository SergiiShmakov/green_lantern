class Obstacle:
    def __init__(self, x_obstacle: int, y_obstacle: int, asteroid):
        self.x = x_obstacle
        self.y = y_obstacle
        self.asteroid = asteroid


class Asteroid:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x: int, y: int, direction: str, asteroid, obstacle):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        self.obstacle = obstacle
        self.position = x, y
        if self.x > self.asteroid.x or self.y > self.asteroid.y or self.x < 0 or self.y < 0:
            raise MissAsteroidError
        if self.x == self.obstacle.x or self.y == self.obstacle.y:
            raise RobotMovementError

    def turn_left(self):
        turns_left = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}
        self.direction = turns_left.get(self.direction, 'N')

    def turn_right(self):
        turns_right = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}
        self.direction = turns_right.get(self.direction, 'N')

    def move_forward(self):
        moving_forward = {
             "N": (self.x, self.y + 1),
             "E": (self.x + 1, self.y),
             "S": (self.x, self.y - 1),
             "W": (self.x - 1, self.y),
         }
        self.position = moving_forward.get(self.direction, None)

    def move_backward(self):
        moving_backward = {self.position: self.x - 1 or self.y - 1}
        self.position = moving_backward.get(self.position, None)


class MissAsteroidError(Exception):
    def __str__(self):
        return 'Your robot missed the asteroid'


class RobotMovementError(Exception):
    def __str__(self):
        return 'There is the obstacle on your way'


