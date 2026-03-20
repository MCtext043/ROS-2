# Exam Robot System

Система управления мобильным роботом с мониторингом состояния.

## Архитектура
Система состоит из 5 основных узлов:
1. **battery_node**: Эмулирует разряд АКБ (Параметр `discharge_rate`).
2. **distance_sensor**: Генерирует случайные расстояния до препятствий.
3. **robot_controller**: Принимает данные и управляет скоростью (Параметр `max_speed`).
4. **status_display**: Выводит текущий режим (LOW BATTERY, OBSTACLE, ALL OK).
5. **robot_state_publisher**: Визуализирует URDF.

### Топики
- `/battery_level` (std_msgs/Float32)
- `/distance` (std_msgs/Float32)
- `/cmd_vel` (geometry_msgs/Twist)

## Запуск
```bash
colcon build --packages-select exam_robot
source install/setup.bash
ros2 launch exam_robot robot_system.launch.py
