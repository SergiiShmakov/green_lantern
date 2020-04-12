class Obstacle:
    def __init__(self, x_obstacle, y_obstacle, asteroid):
        self.x_obstacle = x_obstacle
        self.y_obstacle = y_obstacle
        self.asteroid = asteroid
        if self.x_obstacle > self.asteroid.x or self.y_obstacle > self.asteroid.y \
                or self.x_obstacle < 0 or self.y_obstacle < 0:
            raise ObstacleError


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction, obstacle):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        self.direction = direction
        self.obstacle = obstacle
        if self.x > self.asteroid.x or self.y > self.asteroid.y or self.x < 0 or self.y < 0:
            raise MissAsteroidError
        elif self.x == self.obstacle.x_obstacle or self.obstacle.y_obstacle == self.asteroid.y:
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
        self.x, self.y = moving_forward.get(self.direction)

    def move_backward(self):
        moving_backward = {
             "N": (self.x, self.y - 1),
             "E": (self.x - 1, self.y),
             "S": (self.x, self.y + 1),
             "W": (self.x + 1, self.y),
         }
        self.x, self.y = moving_backward.get(self.direction)


class MissAsteroidError(Exception):
    def __str__(self):
        return 'Your robot missed the asteroid'


class RobotMovementError(Exception):
    def __str__(self):
        return 'There is the obstacle on your way'


class ObstacleError(Exception):
    def __str__(self):
        return 'The obstacle is out of the asteroid'
