# rcj_soccer_player controller - ROBOT Y2

# Feel free to import built-in libraries
import math  # noqa: F401

# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP


class MyRobot3(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                utils.hello()
                ball_data = self.get_new_ball_data()
                self.left_motor.setVelocity(0)
                self.right_motor.setVelocity(0)
