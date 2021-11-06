import random
import sys
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        row = cast["brick"]
        
        #left
        if (ball.get_position().get_x() in range(paddle.get_position().get_x(), paddle.get_position().get_x() + 4)) and (ball.get_position().get_y() + 1 == paddle.get_position().get_y()):
            point = Point(-1, -1)
            ball.set_velocity(point)
        
        #middle
        elif (ball.get_position().get_x() in range(paddle.get_position().get_x() + 4, paddle.get_position().get_x() + 7)) and (ball.get_position().get_y() + 1 == paddle.get_position().get_y()):
            point = Point(0, -1)
            ball.set_velocity(point)
        
        #right
        elif (ball.get_position().get_x() in range(paddle.get_position().get_x() + 7, paddle.get_position().get_x() + 11)) and (ball.get_position().get_y() + 1 == paddle.get_position().get_y()):
            point = Point(1, -1)
            ball.set_velocity(point)

        #walls
        elif (ball.get_position().get_x() + ball.get_velocity().get_x() == 0) or (ball.get_position().get_x() + ball.get_velocity().get_x() == constants.MAX_X - 1):
            ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        
        elif (ball.get_position().get_y() == constants.MAX_Y - 1):
            sys.exit()
        
        for brick in row:
            if brick.get_position().equals(ball.get_position()):
                row.remove(brick)
                point = Point(random.choice(constants.DIRECTION), 1)
                ball.set_velocity(point)
                