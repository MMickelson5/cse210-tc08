import random
import sys
from game import constants
from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    @staticmethod
    def execute(cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0]  # there's only one
        paddle = cast["paddle"][0]  # there's only one
        row = cast["brick"]
        ball_x_position = ball.get_position().get_x()
        ball_y_position = ball.get_position().get_y()
        paddle_position_x = paddle.get_position().get_x()
        paddle_position_y = paddle.get_position().get_y()
        # left
        if (
                ball_x_position in range(paddle_position_x, paddle_position_x + 4) and
                ball_y_position + 1 == paddle_position_y
        ):
            point = Point(-1, -1)
            ball.set_velocity(point)
        # middle
        elif (
                ball_x_position in range(paddle_position_x + 4, paddle_position_x + 7) and
                ball_y_position + 1 == paddle_position_y
        ):
            point = Point(0, -1)
            ball.set_velocity(point)
        # right
        elif (
                ball_x_position in range(paddle_position_x + 7,paddle_position_x + 11) and
                ball_y_position + 1 == paddle_position_y
        ):
            point = Point(1, -1)
            ball.set_velocity(point)
        # walls
        elif (
                ball_x_position + ball.get_velocity().get_x() == 1 or
                ball_x_position + ball.get_velocity().get_x() == constants.MAX_X - 2
        ):
            ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        # top
        elif (
                ball_y_position + ball.get_velocity().get_y() == 1
        ):
            ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))
        elif (
                ball_y_position == constants.MAX_Y - 1
        ):
            sys.exit()
        for brick in row:
            if brick.get_position().equals(ball.get_position()):
                row.remove(brick)
                point = Point(random.choice(constants.DIRECTION), 1)
                ball.set_velocity(point)
