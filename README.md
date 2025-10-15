# innovation-lab

File Adress: er/ros_ws/src/mycobot_client/mycobot_client_2/mycobot_client_2/get_data.py
terminal 1
mycobot-up
source install/setup.bash
source /opt/ros/humble/setup.bash
ource install/setup.bash
export ROS_DOMAIN_ID=10
ros2 launch mycobot_interface_2 mycobot_comms_launch.py use_realsense:=False

terminal 2
mycobot-client-up
export ROS_DOMAIN_ID=10
colcon build
source install/setup.bash
ros2 topic echo /mycobot/angles_real
ros2 topic echo /mycobot/angles_goal
ros2 topic echo /mycobot/gripper_status
ros2 topic echo /mycobot/pump_status
