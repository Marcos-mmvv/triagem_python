# Atendimento em uma emergência

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input(
    "Suspeita de doença infecto-contagiosa? ").upper()

while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
    print("Digite SIM ou NAO")
    doenca_infectocontagiosa = input(
        "Suspeita de doença infecto-contagiosa? ").upper()

if doenca_infectocontagiosa == "SIM":
    print(f"Encaminhe o paciente {nome} para sala AMARELA")
else:
    print(f"Encaminhe o paciente {nome} para sala BRANCA")

if idade >= 65:
    print(f"Paciente {nome} COM prioridade no atendimento")
else:
    genero = input("Digite o gênero do paciente: ").upper()
    if genero == "FEMININO" and idade > 10:
        gravidez = input("A paciente está grávida? ").upper()
        if gravidez == "SIM":
            print(f"Paciente {nome} COM prioridade no atendimento")
        else:
            print(f"Paciente {nome} SEM prioridade no atendimento")
    else:
        print(f"Paciente {nome} SEM prioridade no atendimento")
