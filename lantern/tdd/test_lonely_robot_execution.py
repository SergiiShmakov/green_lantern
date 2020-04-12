import pytest
from lonely_robot import Robot, Asteroid, Obstacle, MissAsteroidError, RobotMovementError, ObstacleError



class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        asteroid = Asteroid(x, y)
        x_obstacle, y_obstacle = 5, 6
        obstacle = Obstacle(x_obstacle, y_obstacle, asteroid)
        direction = 'N'
        robot = Robot(x, y, asteroid, direction, obstacle)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid
        assert robot.obstacle == obstacle

    @pytest.mark.parametrize(
        'asteroid_size,robot_coordinates, obstacle_coordinates',
        (
            ((15, 25), (26, 20), (5, 6)),
            ((15, 25), (26, 24), (5, 6)),
            ((15, 25), (16, 27), (5, 6)),
            ((15, 25), (-5, 0), (5, 6)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates, obstacle_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            obstacle = Obstacle(*obstacle_coordinates, asteroid)
            Robot(*robot_coordinates, asteroid, 'W', obstacle)

    @pytest.mark.parametrize(
        'asteroid_size,obstacle_coordinates',
        (
            ((15, 25), (26, 27)),
            ((15, 25), (15, 26)),
            ((15, 25), (17, 10)),
            ((15, 25), (-10, 0)),
        )
    )
    def test_check_if_obstacle_on_asteroid(self, asteroid_size, obstacle_coordinates):
        with pytest.raises(ObstacleError):
            asteroid = Asteroid(*asteroid_size)
            Obstacle(*obstacle_coordinates, asteroid)


class RobotMovement:
    def setup(self):
        self.x, self.y = 10, 15
        self.asteroid = Asteroid(self.x, self.y)
        self.obstacle = Obstacle(self.x_obstacle, self.y_obstacle, self.asteroid)
        self.direction = 'N'
        self.robot.x, self.robot.y = 3, 4
        self.robot = Robot(self.x, self.y, self.direction, self.asteroid)

    @pytest.mark.parametrize(
        'current_direction,expected_direction',
        (
            ('N', 'W'),
            ('W', 'S'),
            ('S', 'E'),
            ('E', 'N'),
        )
    )
    def test_turn_left(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.direction, self.asteroid, self.obstacle)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        'current_direction,expected_direction',
        (
            ('N', 'E'),
            ('E', 'S'),
            ('S', 'W'),
            ('W', 'N'),
        )
    )
    def test_turn_right(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.direction, self.asteroid, self.obstacle)
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
         "direction,current_position,expected_position",
         (
                ("N", (10, 15), (10, 16)),
                ("E", (10, 15), (11, 15)),
                ("S", (10, 15), (10, 14)),
                ("W", (10, 15), (9, 15)),
         )
    )
    def test_move_forward(self, direction, current_position, expected_position):
        robot = Robot(self.x, self.y, self.direction, self.asteroid)
        robot.move_forward()
        assert robot.x, robot.y == expected_position

    @pytest.mark.parametrize(
         "direction,current_position,expected_position",
         (
                ("N", (10, 15), (10, 14)),
                ("E", (10, 15), (9, 15)),
                ("S", (10, 15), (10, 16)),
                ("W", (10, 15), (11, 15)),
         )
    )
    def test_move_backward(self, direction, current_position, expected_position):
        robot = Robot(self.x, self.y, self.direction, self.asteroid)
        robot.move_backward()
        assert robot.x, robot.y == expected_position

    @pytest.mark.parametrize(
        "current_position,expected_position,obstacle_position",
        (
            ((10, 15), (11, 15), (11, 15)),
            ((10, 15), (10, 16), (10, 16)),
        )
    )
    def test_robot_movement_problems(self, current_position, expected_position, obstacle_position):
        with pytest.raises(RobotMovementError):
            obstacle = Obstacle(*obstacle_position)
            Robot(*expected_position, obstacle, 'N')

