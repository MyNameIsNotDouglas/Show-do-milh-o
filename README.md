# Show do Milhão 🎮

Um jogo de perguntas e respostas em Python, inspirado no clássico programa de TV *Show do Milhão*, com múltiplas escolhas, progressão de dificuldade e interface gráfica intuitiva.

## 📘 Sobre o Projeto

Este jogo simula o formato de quiz com até 17 níveis, premiações progressivas e diferentes categorias. Conta com:

- Interface gráfica via Tkinter
- Banco de perguntas externo (JSON)
- Sistema de pontuação e ranking
- Opções de ajuda (cartas, universitários, plateia)
- Perguntas categorizadas por dificuldade (fácil a muito difícil)

## 🖼 Interface Gráfica

A interface apresenta:

- ✅ Janela principal com a pergunta e alternativas (A, B, C e D)
- ✅ Botões interativos para selecionar a resposta
- ✅ Aviso imediato sobre acerto ou erro
- ✅ Atualização automática do nível e premiação
- ✅ Botões de ajuda e pulo de pergunta
- ✅ Timer com barra de progresso

## 🎮 Como Jogar

1. Execute o arquivo principal

no caso aqui é interface.py, mas pode mudar ou renomear do jeito que quiser. 

2. Depois do jogo iniciado. Digite seu nome

3. Escolha 5 categorias entre as disponíveis

4. Responda as perguntas

-Use as ajudas se necessário

-Pule até 3 perguntas se quiser

-Cuidado com o tempo!

5. O jogo termina:

-Se acertar todas : Ganha R$1.000.000

-Se errar ou acabar o tempo : Perde metade da pontuação atual

-Se desistir : Leva a pontuação acumulada

a estrutura do jogo vai estar numa pasta ou em módulos no repositório :

show_do_milhao/
├── main.py                # Executa o jogo
├── interface.py           # Código principal da interface e lógica do jogo
├── perguntas.py           # Lógica para carregar perguntas e dificuldade
├── ranking.py             # Sistema de ranking (salvar, mostrar, deletar)
├── cores.py               # Paleta de cores da interface
├── perguntas.json         # Banco de perguntas por categoria e dificuldade
├── ranking.txt            # Ranking salvo (nome:pontuação) - é gerado automaticamente no jogo depois iniciado/jogado
└── README.md              # Instruções e informações do projeto

Requisitos
Python 3.8 ou superior

Tkinter (nativo no Windows/macOS; no Linux use sudo apt install python3-tk)
