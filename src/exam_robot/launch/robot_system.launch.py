import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('exam_robot')
    
    # Пути к файлам
    urdf_path = os.path.join(pkg_share, 'urdf', 'exam_robot.urdf')
    rviz_config_path = os.path.join(pkg_share, 'rviz', 'exam_robot.rviz')

    return LaunchDescription([
        # Состояние робота (URDF)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open(urdf_path).read()}]
        ),

        # Узлы системы с параметрами (Бонус 2)
        Node(
            package='exam_robot',
            executable='battery_node',
            name='battery_node',
            parameters=[{'discharge_rate': 1.0}] # 1% в сек
        ),
        Node(
            package='exam_robot',
            executable='robot_controller',
            name='robot_controller',
            parameters=[{'max_speed': 0.3}] # 0.3 м/с
        ),
        Node(package='exam_robot', executable='distance_sensor', name='distance_sensor'),
        Node(package='exam_robot', executable='status_display', name='status_display'),

        # Запуск RViz (Бонус 1)
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_path],
            condition=None
        )
    ])
