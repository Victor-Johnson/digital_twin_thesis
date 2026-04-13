from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument , IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration , PathJoinSubstitution
from  launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    use_hardware = LaunchConfiguration('use_hardware')
    use_rvis = LaunchConfiguration('use_rviz')

    declare_use_hardware = DeclareLaunchArgument(
        'use_hardware',
        default_value='false',
        description='Launches with real robot if set to True or Gazebo simulation (false)'
    )

    declare_use_rviz = DeclareLaunchArgument(
        'use_rviz',
        default_value='true',
        description='Launches Rviz for Visualization'
    )

    # Defining the simulation Path 
    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('twin_simulation'),
                'launch',
                'gazebo.launch.py'
            ])
        ]),
        condition=UnlessCondition(use_hardware)
    )

    hardware_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('twin_description'),
                'launch',
                'robot_state_publisher.launch.py'
            ])
        ]),
        condition=IfCondition(use_hardware)
    )

  

    return LaunchDescription([
        declare_use_hardware,
        declare_use_rviz,
        sim_launch,
        hardware_launch,
    ])