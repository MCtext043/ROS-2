#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
class BatteryMonitorNode(Node):
    def __init__(self):
        super().__init__('battery_monitor_node')
        self.current_battery_level = 100
        self.subscriber_ = self.create_subscription(
            Float32, # тип сообщения
            '/battery_level', # имя топика
            self.callback_battery,
            10 # размер очереди
            )
        
    def callback_battery(self, msg):
        if msg.data > 50:
            self.get_logger().info("Батарея ОК")
        elif 20 <= msg.data <= 50:
            self.get_logger().info("Батарея разряжается")
        else:
            self.get_logger().info("КРИТИЧЕЙСКИЙ УРОВЕНЬ!")
        
def main(args=None):
    rclpy.init(args=args)
    node = BatteryMonitorNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main_':
    main()