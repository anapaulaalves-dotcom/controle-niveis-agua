import time
from colorama import Fore, Style, init

# Inicializa o colorama (autoreset garante a restauração automática do estilo)
init(autoreset=True)

# 1. Lista contendo as informações dos níveis do reservatório
# Estrutura: (Nível, Descrição da Situação, Cor correspondente)
NIVEIS_RESERVATORIO = [
    (1, "Muito baixo (crítico)", Fore.RED),
    (2, "Baixo", Fore.YELLOW),
    (3, "Médio", Fore.GREEN),
    (4, "Alto", Fore.CYAN),
    (5, "Muito alto (alerta)", Fore.BLUE),
]


def formatar_mensagem_alerta(nivel_info: tuple) -> str:
    """Função responsável por formatar a mensagem de alerta

    com a cor correspondente ao nível do reservatório.
    """
    numero_nivel, situacao, cor = nivel_info

    # Aplica a cor, o texto em negrito (Style.BRIGHT) e formata a mensagem
    mensagem = (
        f"{cor}{Style.BRIGHT}[NÍVEL {numero_nivel}] Situação: {situacao}"
    )

    return mensagem


def simular_monitoramento():
    """Função principal que simula a leitura dos níveis do reservatório."""
    print("==================================================")
    print("   SISTEMA DE MONITORAMENTO DE NÍVEL DE ÁGUA      ")
    print("==================================================\n")

    # Percorre a lista exibindo o estado de cada nível
    for nivel in NIVEIS_RESERVATORIO:
        mensagem_colorida = formatar_mensagem_alerta(nivel)
        print(mensagem_colorida)

        # Pausa de 1 segundo entre as leituras para simular um ambiente real
        time.sleep(1)

    print("\n==================================================")
    print("      MONITORAMENTO CONCLUÍDO COM SUCESSO        ")
    print("==================================================")


if __name__ == "__main__":
    simular_monitoramento()
