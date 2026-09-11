import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class ResetService(Node):
    def __init__(self):
        super().__init__('reset_service')
        self.counter = 10  # Contoh nilai awal counter
        self.srv = self.create_service(
            Trigger, 'reset_system', self.on_reset
        )
        self.get_logger().info('Service /reset_system siap dilayani.')

    def on_reset(self, request, response):
        old = self.counter
        self.counter = 0
        response.success = True
        response.message = f'Counter reset from {old} to {self.counter}'
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ResetService()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()