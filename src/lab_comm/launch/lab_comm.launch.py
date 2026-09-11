from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
        threshold = LaunchConfiguration('threshold')

        return LaunchDescription([
            DeclareLaunchArgument('threshold', default_value='0.5'),

            Node(
                package='lab_comm',
                executable='main_sensor',        
                name='sensor_publisher',
                parameters=[{'rate_hz': 10.0, 'amplitude': 1.0}],
                output='screen'
            ),
            Node(
                package='lab_comm',
                executable='main_processing',    
                name='processing_node',
                parameters=[{'threshold': threshold}],
                output='screen'
            ),
            Node(
                package='lab_comm',
                executable='main_reset',
                name='reset_service',
                output='screen'
            ),
            Node(
                package='lab_comm',
                executable='main_motion',
                name='motion_action_server',
                output='screen'
            ),
        ])