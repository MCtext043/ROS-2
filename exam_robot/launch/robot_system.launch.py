def generate_launch_description():
    pkg_name = 'exam_robot'
    pkg_share = get_package_share_directory(pkg_name)
    urdf_file = os.path.join(pkg_share, 'urdf', 'exam_robot.urdf') # Путь к вашему URDF
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    # 1. robot_state_publisher (стандартный узел)
    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    )

    # 2. battery_node
    battery_node = Node(
        package=pkg_name,
        executable='battery_node', # Имя executable из setup.py
        name='battery_node',
        output='screen'
    )

    # 3. distance_sensor
    distance_sensor = Node(
        package=pkg_name,
        executable='distance_sensor',
        name='distance_sensor',
        output='screen'
    )

    # 4. status_display
    status_display = Node(
        package=pkg_name,
        executable='status_display',
        name='status_display',
        output='screen'
    )

    # 5. robot_controller
    robot_controller = Node(
        package=pkg_name,
        executable='robot_controller',
        name='robot_controller',
        output='screen'
    )

    return LaunchDescription([
        robot_state_pub,
        battery_node,
        distance_sensor,
        status_display,
        robot_controller
    ])