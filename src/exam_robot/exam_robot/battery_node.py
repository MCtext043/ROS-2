import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class BatteryNode(Node):
    def __init__(self):
        super().__init__('battery_node')
        # Бонус 2: Параметр разряда
        self.declare_parameter('discharge_rate', 1.0)
        self.rate = self.get_parameter('discharge_rate').value
        
        self.publisher_ = self.create_publisher(Float32, 'battery_level', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.current_battery = 100.0

    def timer_callback(self):
        msg = Float32()
        self.current_battery -= self.rate
        if self.current_battery < 0: self.current_battery = 0.0
        
        # Исправление ошибки: явное приведение к float
        msg.data = float(self.current_battery)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Battery: {msg.data}%')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
