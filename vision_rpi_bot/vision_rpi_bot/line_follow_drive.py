import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16
from gpiozero import Robot

class drive_rpi(Node):

    def __init__(self):
        super().__init__('Visionbot_Drive')
        self.error_value_subscription = self.create_subscription(
            Int16,
            '/line_following_error',
            self.car_drive_callback,
            10)
        self.Robot1 = Robot(left=(4, 14), right=(17, 18))
        self.get_logger().info("line follow drive node has started")

    def car_drive_callback(self, error_value):
        
        if error_value.data < 0:
            self.Robot1.value = (0.5, -0.5)  # left forward, right backward
        elif error_value.data > 0:
            self.Robot1.value = (-0.5, 0.5)  # left backward, right forward
        else:
            self.Robot1.value = (0.75, 0.75)


def main(args=None):
    rclpy.init(args=args)
    node = drive_rpi()
    rclpy.spin(node)
    rclpy.shutdown() 


if __name__ == '__main__':
    main()
