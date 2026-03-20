#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
class BatteryNode(Node):
    def __init__(self):
        super().__init__('battery_node')
        self.battery_level = 100.0 # процент заряда
        self.is_robot_moving = False # движется ли робот

        # Publisher для уровня батареи
        self.battery_publisher = self.create_publisher(
        Float32,
        '/battery_level',
        10
        )

        # Таймер для разрядки батареи (каждые 2 секунды)
        self.timer = self.create_timer(1.0, self.update_battery)


    def update_battery(self):
        if self.battery_level > 0:
            self.battery_level -= 1
        if self.battery_level % 10 == 0:
            msg = Float32()
            msg.data = f'Battery: {self.battery_level}%'
            self.battery_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
