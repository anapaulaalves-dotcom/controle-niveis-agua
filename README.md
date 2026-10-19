# 🌊 Sistema de Controle de Níveis de Água

Este projeto consiste em um sistema simples de monitoramento de reservatório de água desenvolvido em Python. O sistema executa no terminal e exibe mensagens de alerta com cores dinâmicas e progressivas de acordo com o nível atual de água, permitindo uma visualização clara das situações de risco.

---

## 📌 Funcionalidades

- **Monitoramento por Níveis**: Representação de 5 níveis de capacidade do reservatório (do crítico ao alerta).
- **Alertas Coloridos**: Utilização da biblioteca `colorama` para associar cores específicas a cada nível de risco:
  - 🔴 **Nível 1 (Muito baixo - crítico)**: Vermelho
  - 🟡 **Nível 2 (Baixo)**: Amarelo
  - 🟢 **Nível 3 (Médio)**: Verde
  - 🔵 **Nível 4 (Alto)**: Ciano
  - 🔷 **Nível 5 (Muito alto - alerta)**: Azul
- **Simulação em Tempo Real**: Pausas graduais entre as leituras para simular a medição contínua de um reservatório real.
- **Restauração de Estilo**: Limpeza automática do estilo de cor no terminal ao finalizar a exibição.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **[Colorama](https://pypi.org/project/colorama/)**: Biblioteca para estilização de texto e cores ANSI no terminal.

---

## 📁 Estrutura do Projeto

```text
├── main.py            # Código-fonte principal do programa
├── requirements.txt    # Dependências do projeto (colorama)
└── README.md          # Documentação do projeto
