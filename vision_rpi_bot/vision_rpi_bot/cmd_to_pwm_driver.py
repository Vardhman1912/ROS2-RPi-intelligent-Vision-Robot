import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from gpiozero import *

class CmdToPwmDriverNode(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_to_pwm_callback,
            10)
        self.robot = Robot(left=(4, 14), right=(17, 18))
        self.get_logger().info("Cmd_to_pwm_driver node has been started")

    def cmd_to_pwm_callback(self, msg):
        right_wheel_vel = (msg.linear.x + msg.angular.z)/2 
        left_wheel_vel = (msg.linear.x - msg.angular.z)/2

        print(right_wheel_vel,"/",left_wheel_vel)

        self.robot.value=(left_wheel_vel, right_wheel_vel)

        

def main(args=None): 
    rclpy.init(args=args)
    node = CmdToPwmDriverNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
