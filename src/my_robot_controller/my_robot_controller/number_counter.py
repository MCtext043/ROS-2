#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
class NumberCounterNode(Node):
    def __init__(self):
        super().__init__('number_counter_node')
        self.numbers_queue = []
        self.subscriber_ = self.create_subscription(
            Int64, # тип сообщения
            '/number', # имя топика
            self.callback_sum_numbers,
            10 # размер очереди
            )
        
    def callback_sum_numbers(self, msg):
        if len(self.numbers_queue) < 5:
            self.numbers_queue.append(int(msg.data))
            self.get_logger().info(f"{sum(self.numbers_queue)}")
        else:
            self.get_logger().info(f"Сумма после 5 чисел: {sum(self.numbers_queue)}")
            self.numbers_queue = []
        
def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main_':
    main()