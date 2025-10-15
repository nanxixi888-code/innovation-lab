import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from mycobot_msgs_2.msg import MycobotAngles

class JointStatePublisher(Node):
    def __init__(self):
        super().__init__('joint_state_publisher')
        self.pub = self.create_publisher(JointState, '/joint_states', 10)
        self.sub = self.create_subscription(MycobotAngles, '/mycobot/get_joint_angles', self.cb, 10)

    def cb(self, msg):
        js = JointState()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = [f'joint_{i+1}' for i in range(6)]
        js.position = [msg.joint_1, msg.joint_2, msg.joint_3, msg.joint_4, msg.joint_5, msg.joint_6]
        self.pub.publish(js)

def main(args=None):
    rclpy.init(args=args)
    node = JointStatePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
