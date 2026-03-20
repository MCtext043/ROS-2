import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class DistanceSensor(Node):
    def __init__(self):
        super().__init__('distance_sensor')
        self.publisher_ = self.create_publisher(Float32, 'distance', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = float(random.uniform(0.1, 5.0))
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
