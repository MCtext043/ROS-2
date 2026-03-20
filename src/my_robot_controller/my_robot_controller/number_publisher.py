#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__('number_publisher_node')
        self.create_timer(1.0, self.current_number)
        self.number = 0
        self.publisher_ = self.create_publisher(
            Int64, # тип сообщения
            '/number', # имя топика
            10 # размер очереди
            )
        
    def current_number(self):
        msg = Int64()
        msg.data = self.number
        self.publisher_.publish(msg)
        self.get_logger().info(f'Публикую: "{msg.data}"')
        self.number += 1
        
def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main_':
    main()