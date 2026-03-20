from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'exam_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Установка папок с ресурсами
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf', '*.urdf'))),
        (os.path.join('share', package_name, 'rviz'), glob(os.path.join('rviz', '*.rviz'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='kirillgame912@gmail.com',
    description='ROS 2 Exam Robot Package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'battery_node = exam_robot.battery_node:main',
            'distance_sensor = exam_robot.distance_sensor:main',
            'robot_controller = exam_robot.robot_controller:main',
            'status_display = exam_robot.status_display:main'
        ],
    },
)
