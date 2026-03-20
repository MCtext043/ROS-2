#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
class BatterySimulatorNode(Node):
    def __init__(self):
        super().__init__('battery_simulator_node')
        self.create_timer(1.0, self.battery_level)
        self.current_battery_level = 100
        self.publisher_ = self.create_publisher(
            Float32, # тип сообщения
            '/battery_level', # имя топика
            10 # размер очереди
            )
        
    def battery_level(self):
        msg = Float32()
        msg.data = float(self.current_battery_level)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Публикую: "{msg.data}"')
        self.current_battery_level -= 1
        
def main(args=None):
    rclpy.init(args=args)
    node = BatterySimulatorNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main_':
    main()