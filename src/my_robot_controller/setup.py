from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='kirillgame912@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_first_node = my_robot_controller.my_first_node:main',
            'battery_simulator = my_robot_controller.battery_simulator:main',
            'battery_monitor = my_robot_controller.battery_monitor:main',
            'number_publisher = my_robot_controller.number_publisher:main',
            'number_counter = my_robot_controller.number_counter:main'
        ],
    },
)
