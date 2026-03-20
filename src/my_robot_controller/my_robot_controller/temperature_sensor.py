#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class TemperatureSensorNode(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        self.numbers_queue = []
        self.subscriber_ = self.create_subscription(
            String, # тип сообщения
            '/motor_state', # имя топика
            self.motor,
            10 # размер очереди
            )
        
    def motor(self, msg):
        self.get_logger().info(msg.data)
        
def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensorNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main_':
    main()