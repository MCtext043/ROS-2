import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        
        self.current_status = "ALL OK"
        self.last_logged_status = ""

        # Подписка на статус
        self.subscription = self.create_subscription(
            String, '/robot_status', self.status_callback, 10)
        
        # Публикация команд (10 Hz)
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_loop)

    def status_callback(self, msg):
        self.current_status = msg.data

    def control_loop(self):
        msg = Twist()
        
        # Логика выбора команды
        if self.current_status == "ALL OK":
            msg.linear.x = 0.3
            msg.angular.z = 0.0
        elif self.current_status == "WARNING: Low battery":
            msg.linear.x = 0.1
            msg.angular.z = 0.0
        elif self.current_status == "WARNING: Obstacle close":
            msg.linear.x = 0.0
            msg.angular.z = 0.5
        elif self.current_status == "CRITICAL":
            msg.linear.x = 0.0
            msg.angular.z = 0.0
        
        self.cmd_pub.publish(msg)

        # Логирование изменения режима
        if self.current_status != self.last_logged_status:
            self.get_logger().info(f'Mode changed: {self.current_status}. Commands: v={msg.linear.x}, w={msg.angular.z}')
            self.last_logged_status = self.current_status

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
