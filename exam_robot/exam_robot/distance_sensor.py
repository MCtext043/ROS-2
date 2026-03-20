#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geographic_msgs.msg import Twist

class DistanceSimulator(Node):
    def __init__(self):
        super().__init__('distance_node')
        
        self.current_distance = 3.0
        self.current_linear_x = 0.0
        
        self.publisher_ = self.create_publisher(Float32, '/distance', 10)
        self.subscription = self.create_subscription(
            Twist, '/cmd_vel', self.cmd_vel_callback, 10)
            
        self.timer = self.create_timer(0.2, self.update_distance)


    def cmd_vel_callback(self, msg):
        self.current_linear_x = msg.linear.x
        
    def update_distance(self):
        # Логика изменения дистанции
        if self.current_linear_x == 0:
            self.current_distance = 3.0
        elif self.current_linear_x > 0:
            self.current_distance = max(0.5, self.current_distance - 0.2)
        elif self.current_linear_x < 0:
            self.current_distance = min(3.0, self.current_distance + 0.2)
        
        # Публикация
        msg = Float32()
        msg.data = float(self.current_distance)
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DistanceSimulator()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
