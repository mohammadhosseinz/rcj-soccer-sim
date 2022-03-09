# rcj_soccer_player controller - ROBOT Y2

# Feel free to import built-in libraries
import math
from turtle import heading  # noqa: F401

# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP


class MyRobot2(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                heading=math.degrees(self.get_compass_heading())
                left_speed=-heading/10
                right_speed=heading/10
                if(left_speed>10):
                    left_speed=10
                if(right_speed>10):
                    right_speed=10
                if(left_speed<-10):
                    left_speed=-10
                if(right_speed<-10):
                    right_speed=-10
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
