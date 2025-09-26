import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class CalculatorClientNode(Node):

    def __init__(self):
       
        super().__init__('calculator_client')
        self.client_ = self.create_client(AddTwoInts, 'add_two_ints')
        
        while not self.client_.wait_for_service(timeout_sec=1.0):
        
            self.get_logger().info('Serviço não disponível, esperando novamente...')
        
        self.get_logger().info('Servidor encontrado, cliente pronto.')

    def send_request(self, a, b):
    
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        self.future_ = self.client_.call_async(request)
        rclpy.spin_until_future_complete(self, self.future_)
        return self.future_.result()

def main(args=None):

    rclpy.init(args=args)
    calculator_client = CalculatorClientNode()
    
    while rclpy.ok():
        user_input = input("Digite a soma (ex: 5 + 12) ou 'sair' para terminar: ")
        
        if user_input.lower() == 'sair':
            break
            
        try:

            parts = user_input.split('+')
            a = int(parts[0].strip())
            b = int(parts[1].strip())
            response = calculator_client.send_request(a, b)
            calculator_client.get_logger().info(
                f'O servidor respondeu: {a} + {b} = {response.sum}')
        except (ValueError, IndexError):
            calculator_client.get_logger().warn('Entrada inválida. Por favor, use o formato "numero inteiro + numero inteiro".')

    calculator_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
