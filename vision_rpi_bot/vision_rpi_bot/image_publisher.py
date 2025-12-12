import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy


class VideoPublisher(Node):

    def __init__(self):
        super().__init__('rpi_video_publisher')
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1
        )
        self.publisher_ = self.create_publisher(Image, '/rpi_video_feed', qos_profile)
        timer_period = 0.1  # ~30 FPS instead of 0.1s
        self.timer = self.create_timer(timer_period, self.camera_callback)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        self.bridge = CvBridge()
        self.get_logger().info('RPI Video Publisher has been started')

    def camera_callback(self):
        if self.cap is None:
            return  # No camera available
        
        ret, frame = self.cap.read()
        if ret and frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = self.bridge.cv2_to_imgmsg(frame, "mono8")
            self.publisher_.publish(frame)



def main(args=None):
    rclpy.init(args=args)
    node = VideoPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

# self.cap = None
#         for camera_index in [0, 1, 2, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 23, 31]:
#             cap = cv2.VideoCapture(camera_index, cv2.COLOR_BGR2GRAY)
#             if cap.isOpened():
#                 self.cap = cap
#                 self.get_logger().info(f'Camera found at index {camera_index}')
#                 break
#             cap.release()
        
#         if self.cap is None:
#             self.get_logger().error('No camera found!')
#         else:
#             self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
#             self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)