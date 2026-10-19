
# Atividade: Controle de Níveis de Água
# Instalação da biblioteca

from colorama import Fore, Style, init

init(autoreset=True)

# Lista dos níveis do reservatório
niveis_agua = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função para definir a cor de cada nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibição das mensagens
print(Fore.WHITE + Style.BRIGHT +
      "=== CONTROLE DE NÍVEIS DE ÁGUA ===\n")

for nivel in range(1, len(niveis_agua) + 1):
    mensagem = niveis_agua[nivel - 1]
    cor = definir_cor(nivel)
    print(cor + mensagem + Style.RESET_ALL)

print("\nMonitoramento finalizado.")
