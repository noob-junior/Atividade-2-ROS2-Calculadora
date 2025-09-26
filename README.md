


Atividade 2: sistema de comunicação síncrono (requisição/resposta) usando Serviços




- `calculator_server`: Um nó que oferece um serviço chamado `/add_two_ints`. Ele fica aguardando por uma requisição que contenha dois números inteiros. Ao receber, ele os soma e retorna o resultado

- `calculator_client`: Um nó interativo que pede ao usuário para digitar uma soma no terminal (ex: "5 + 12"). Ele envia esses números para o servidor, aguarda a resposta e a imprime no console. O cliente continua pedindo por novas contas até que o usuário digite "sair"




Para rodar (abrir 2 terminais e escrever em cada um deles, comandos especificos, seguindo a ordem)

terminal 1:

cd ~/ros2_ws
source install/setup.bash
ros2 run my_calculator_pkg calculator_server



terminal 2:

cd ~/ros2_ws
source install/setup.bash
ros2 run my_calculator_pkg calculator_client
