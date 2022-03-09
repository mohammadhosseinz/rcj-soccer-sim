# rcj_soccer_player controller - ROBOT Y1

# Feel free to import built-in libraries
import math
from turtle import heading  # noqa: F401

# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP


class MyRobot1(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                heading=math.degrees(self.get_compass_heading())
                if(-1<heading and heading<1):
                    self.left_motor.setVelocity(0)
                    self.right_motor.setVelocity(0)
                elif(heading>0):
                    self.left_motor.setVelocity(-5)
                    self.right_motor.setVelocity(5)
                elif(heading<0):
                    self.left_motor.setVelocity(5)
                    self.right_motor.setVelocity(-5)