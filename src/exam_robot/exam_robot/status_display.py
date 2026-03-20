import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class StatusDisplay(Node):
    def __init__(self):
        super().__init__('status_display')
        
        # Данные от датчиков
        self.battery = 100.0
        self.distance = 3.0
        self.last_status = ""

        # Подписки
        self.create_subscription(Float32, '/battery_level', self.battery_cb, 10)
        self.create_subscription(Float32, '/distance', self.distance_cb, 10)
        
        # Публикация (2 Hz)
        self.status_pub = self.create_publisher(String, '/robot_status', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def battery_cb(self, msg):
        self.battery = msg.data

    def distance_cb(self, msg):
        self.distance = msg.data

    def timer_callback(self):
        # Логика определения статуса (от критических к нормальным)
        if self.battery < 10.0 or self.distance < 0.7:
            status = "CRITICAL"
        elif self.battery < 20.0:
            status = "WARNING: Low battery"
        elif self.distance < 1.0:
            status = "WARNING: Obstacle close"
        else:
            status = "ALL OK"

        # Публикация
        msg = String()
        msg.data = status
        self.status_pub.publish(msg)

        # Логирование только при изменении
        if status != self.last_status:
            self.get_logger().info(f'Status changed to: {status}')
            self.last_status = status

def main(args=None):
    rclpy.init(args=args)
    node = StatusDisplay()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()