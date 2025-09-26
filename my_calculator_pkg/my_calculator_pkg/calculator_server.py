import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class CalculatorServerNode(Node):

    def __init__(self):
        super().__init__('calculator_server')
        self.server_ = self.create_service(
            AddTwoInts,
            'add_two_ints',
            self.add_two_ints_callback)
        self.get_logger().info('Servidor da Calculadora está pronto para somar!')

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Requisição recebida: {request.a} + {request.b}. Retornando soma: {response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)
    calculator_server_node = CalculatorServerNode()
    rclpy.spin(calculator_server_node)
    calculator_server_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
