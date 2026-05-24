# ⭕ Jogo da Velha (Tic Tac Toe) em Python

Uma implementação robusta e interativa do clássico Jogo da Velha, desenvolvida em Python para rodar diretamente no terminal. O projeto foca em Experiência do Utilizador (UX) no terminal e Tratamento de Erros.

## 🎮 Sobre o Projeto

Este não é apenas um script simples. O jogo foi refatorado para incluir uma interface colorida, validação de entradas robusta (para que o jogo não feche se o utilizador digitar uma letra) e uma IA simples para o computador.

## ✨ Funcionalidades

**Interface Visual Colorida**: Uso de códigos ANSI para colorir o X (Vermelho) e o O (Azul), facilitando a visualização. <br>
**Grid Numérico**: O tabuleiro exibe números de 1 a 9 nas casas vazias, servindo de guia para o jogador (estilo teclado numérico). <br>
**Tratamento de Exceções**: O jogo utiliza blocos try/except para impedir falhas caso o utilizador digite algo que não seja um número. <br>
**Correção de Bug de Turnos**: Lógica aprimorada para garantir que jogadas inválidas não consumam a vez do jogador.<br>
**Cross-Platform**: Comando de limpeza de tela compatível tanto com Windows (cls) quanto Linux/Mac (clear). <br>

## 🕹️ Como Jogar

Execute o script. <br>
O tabuleiro será exibido com números indicando as posições livres: <br>

 1 | 2 | 3  <br>
----------- <br>
 4 | 5 | 6  <br>
----------- <br>
 7 | 8 | 9  <br>


Digite o número correspondente à posição onde deseja jogar. <br>

Tente vencer o computador alinhando 3 símbolos na horizontal, vertical ou diagonal! <br>

## 🚀 Como Executar

Pré-requisitos <br>
Ter o Python 3 instalado na máquina. <br>

Passo a passo <br>
Clone este repositório: <br>

git clone https://github.com/EnioJr18/Jogo-da-Velha <br>


Aceda à pasta do projeto: <br>
    cd Jogo-da-Velha <br>


Execute o jogo: <br>
    python jogo_da_velha.py <br>


## 🧠 Lógica do Código

Um destaque deste código é a verificação de vitória dinâmica e a proteção contra entradas inválidas: <br>

**Exemplo da proteção de input** <br>
try: <br>
    escolha = int(input(f"Sua vez ({COR_X}X{RESET}). Escolha (1-9): ")) <br>
except ValueError: <br>
    print("❌ Digite apenas números!") <br>
    continue <br>


## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor
Desenvolvido por Enio Jr, para fins de estudo de lógica de programação e Python.

📧 Entre em contato: eniojr100@gmail.com <br>
🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ <br>
📷 Instagram: https://www.instagram.com/enio_juniorrr/ <br>