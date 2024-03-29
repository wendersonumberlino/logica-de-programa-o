
""" 6,0 ponto Em Python crie um programa que atenda o menu a seguir. Desenvolva uma função para cada opção do menu. Utilize a criação de estruturas. Cadastrar 5 (vetor) compras e 2 (vetor) clientes.
CLIENTES	-	COMPRAS
cod_cli	-	cod_comp
nome	-	cod_cli
saldo_cashback	-	valor
Menu de Opções

1 Cadastrar clientes

2 Mostrar todos os clientes

3 Cadastrar compras

4 Mostrar todas as compras

5 Mostrar o total de todas as compras realizadas por um cliente

6 Armazenar todas as compras em arquivo

7 Apresentar o conteúdo do arquivo

8 Gerar um gráfico

9 Sair

Observaçôes:

Na opção 3, o valor da compra, deve ser descontado no saldo do cashback do cliente que a realizou. Por exemplo, cliente 1, tem 500 de saldo, se ele realizar uma compra de 100 reais, o saldo do cashback passará para 400.
Na opção 5, o usuário do sistema informará/digitará o código do cliente que quer e o sistema/programa fará uma pesquisa e calculará o total de compras do determinado cliente.
Na opção 6 use a função write antes da estrutura de repetição para armazenar o cabeçalho das colunas, depois dentro do laço grave todos os campos do tipo Compras como foi visto em aula, no arquivo de nome compras.csv. Use como sepador entre colunas/campos a , vírgula
Na opção 7 apresente todos os dados armazenados no arquivo compras.csv
Na opção 8 use a coluna valor no gráfico e adote a cor orange da biblioteca Matplotlib
 """
import csv
import matplotlib.pyplt as plt
class Cliente:
    def _init_(self, cod_cli,nome):
        self.cod_cli = cod_cli
        self.nome = nome
        self.saldo_cashback = 0
class Compra:
    def _init_(self, cod_comp, cod_cli, valor):
        self.cod_comp = cod_comp
        self.cod_cli = cod_cli
        self.valor = valor
clientes = []
compras= []
def cadastrar_clientes():
    for i in range(2):
        cod_cli = int(input("Digite o código do cliente: "))
        nome = input("Digite o nome do cliente: ")
        cliente = Cliente(cod_cli, nome)
        clientes.append(cliente)
    return clientes

def mostrar_clientes():
    return clientes
    
def cadastrar_compra():
    for i in range(5):
        cod_comp = int(input("Digite o código da compra: "))
        cod_cli = int(input("Digite o código do cliente que realizou a compra: "))
        valor = float(input("Digite o valor da compra: "))

        for cliente in clientes:
            if cliente.cod_cli == cod_cli:
                cliente.saldo_cashback -= valor
                break

        compra = Compra(cod_comp, cod_cli, valor)
        compras.append(compra)
    return compras

def mostrar_compras():
    return compras

def calcular_total_compras():
    cod_cli = int(input("Digite o código do cliente: "))
    total = 0
    for compra in compras:
        if compra.cod_cli == cod_cli:
            total += compra.valor
    return total

def armazenar_compras_arquivo():
    with open("compras.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["cod_comp", "cod_cli", "valor"])  # Cabeçalho
        for compra in compras:
            writer.writerow([compra.cod_comp, compra.cod_cli, compra.valor])

def apresentar_cont_arq():
    conteudo= []
    with open("compras.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            conteudo.append(row)
    return conteudo

def gerar_grafico():
    valores = [compra.valor for compra in compras]
    plt.plot(valores, color="orange")
    plt.xlabel("Compras")
    plt.ylabel("Valor")
    plt.title("Valores das Compras")
    plt.show()


def main():
    while True:
        print("\nMenu de Opções")
        print(" 1 cadastrar clientes")
        print("2 Mostrar todos os clientes ")
        print("3 cadastrar compras")
        print("4 Mostrar todas as compras")
        print("5 mostrar total de compras realizadas por cliente")
        print("6 Armazenar todas as compras em um arquivo")
        print("7 Apresentar o conteudo do arquivo")
        print("8 Gerar um grafico")
        print("9 sair")

        opc= int(input("digite a operação desejada: "))
        if opc ==1:
            clientes = cadastrar_clientes()
            print("clientes cadastrados",clientes)
        elif opc == 2:
            clientes = mostrar_clientes()
            print("clientes")
            for cliente in clientes:
                print("Codigo do cliente:",clientes.cod_cli)
                print("Nome do Cliente:", clientes.nome)
                print("Saldo cash back", clientes.saldo_cashback)
                print()
        elif opc == 3:
            compras = cadastrar_compra()
            print("compras cadastradas",compras)

        elif opc == 4:
            compras = mostrar_compras()
            print("compras")
            for compra in compras:
                print("Codedo da compra: ",compra.cod_comp)
                print("Codigo do cliente: ", compra.cod_cli)
                print("valor da compra: ", compra.valor)
                print("")

        elif opc == 5:
            total=calcular_total_compras()
            print("Tota de compras do cliente: ", total)

        elif opc == 6:
            armazenar_compras_arquivo()
            print("Compras armazenados no arquivo 'compras.csv'")

        elif opc == 7:
            conteudo = apresentar_cont_arq()
            print("conteudo do arquivo 'compras,csv'")
            for row in conteudo:
                print(row)
        elif opc == 8:
            gerar_grafico()
        elif opc == 9:
            break

        else:
            print("opção invalida")

main()