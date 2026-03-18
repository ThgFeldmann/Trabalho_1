
#* Classe para Livros
class Livro:
    def __init__(
                self, 
                titulo = "Lorem Ipsum", 
                codigo = "0123", 
                editora = "Lorem Ipsum", 
                categoria = "Lorem Ipsum",
                ano = "2000", 
                valor = 10.00, 
                estoque = 0
            ):

        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.categoria = categoria
        self.ano = ano
        self.valor = valor
        self.estoque = estoque
    
    def Info(self): # Método para informar *todos* os livros

        # Calculo para o valor total em estoque
        valor_estoque = self.valor * self.estoque

        print(f"\n>>>>>>Cod#{self.codigo}")
        print(f"Titulo/Editora: {self.titulo}/{self.editora}")
        print(f"Categoria: {self.categoria}")
        print(f"Ano: {self.ano}")
        print(f"Valor: R$ {self.valor}")
        print(f"Estoque: {self.estoque:.2f} unidade(s)")
        print(f"Valor total em estoque: R$ {valor_estoque:.2f}")

#* Funções

# Função de cadastro de livros
def Cadastro(lista_livros):
    codigo = ""
    titulo = ""
    editora = ""
    categoria = ""
    ano = ""
    valor = 0.00
    estoque = 0
    valor_estoque = 0.00
    confirmação = ""
    
    print("Cadastro\n")
    codigo = input("Digite o código do livro: ")
    titulo = input("Digite o titulo do livro: ")
    editora = input("Digite a editora do livro: ")
    categoria = input("Digite a categoria do livro: ")
    ano = input("Digite o ano de publicação do livro: ")
    valor = float(input("Digite o valor da unidade deste livro: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    
    # Calculo para o valor total em estoque
    valor_estoque = valor * estoque
    
    print("-"*30)
    print("Confirmando os dados...")
    print(f"\n>>>>>>Cod#{codigo}")
    print(f"Titulo/Editora: {titulo}/{editora}")
    print(f"Categoria: {categoria}")
    print(f"Ano: {ano}")
    print(f"Valor: R$ {valor}")
    print(f"Estoque: {estoque:.2f} unidade(s)")
    print(f"Valor total em estoque: R$ {valor_estoque:.2f}\n")
    
    print("-"*30)
    
    print("Cadastrar?\n")
    print("S - Confirmar")
    print("N - Cancelar\n")
    confirmação = input("Escolha: ").upper()
    
    if confirmação == "S":
        print("-"*30)
        print("\nCadastrando o livro...")
        print(".")
        print(".")
        print(".")

        try:
            lista_livros.append(Livro(
                codigo=codigo,
                titulo=titulo,
                editora=editora,
                categoria=categoria,
                ano=ano,
                valor=valor,
                estoque=estoque
            ))
            
            print("Livro cadastrado com sucesso.")
        except Exception as error:
            print("Ocorreu um no cadastro, tente novamente mais tarde.")
            print("Erro: ", error)
    
    elif confirmação == "N":
        print("-"*30)
        print("Cancelando o cadastro...")
        print(".")
        print(".")
        print(".")
        print("Cadastro cancelado.")

# Função de busca de livros pelo titulo
def Info_Por_Nome(lista_livros):
    nome_alvo = ""
    encontrados = 0
    
    print("Busca pelo nome do livro\n")
    nome_alvo = input("Digite o titulo do livro desejado: ").upper()
    
    print("Buscando livros...")
    
    for livro in lista_livros:
        if (livro.titulo.upper() == nome_alvo):
            encontrados += 1
            livro.Info()
            print("")
    
    print("-"*30)
    
    if encontrados > 0:
        print(f"\n{encontrados} livro(s) foram encontrados.")
    else:
        print("\nNenhum livro com este titulo foi encontrado.")

# Função de busca de livros por categoria
def Info_Por_Categoria(lista_livros):
    categoria_alvo = ""
    encontrados = 0
    
    print("Busca pela categoria do livro\n")
    categoria_alvo = input("Digite a categoria desejada: ").upper()
    
    print("Buscando livros...")
    
    # filtragem livro por livro
    for livro in lista_livros:
        if (livro.categoria.upper() == categoria_alvo):
            encontrados += 1
            livro.Info()
            print("")
    
    print("-"*30)
    
    # verificação para caso livros foram encontrados, ou não
    if encontrados > 0:
        print(f"\n{encontrados} livro(s) foram encontrados.")
    else:
        print("\nNenhum livro com esta categoria foi encontrado.")

# Função de busca de livros pelo valor
def Info_Por_Valor(lista_livros):
    estoque_alvo = 0.00
    encontrados = 0
    
    print("Busca pelo preco do livro\n")
    valor_alvo = float(input("Digite o valor máximo desejado: ").upper())
    
    print(f"Buscando livros até o valor de R$ {valor_alvo:.2f}...")
    
    # filtragem livro por livro
    for livro in lista_livros:
        if (livro.valor <= valor_alvo):
            encontrados += 1
            livro.Info()
            print("")
    
    print("-"*30)
    
    # verificação para caso livros foram encontrados, ou não
    if encontrados > 0:
        print(f"\n{encontrados} livro(s) foram encontrados.")
    else:
        print("\nNenhum livro até este valor foi encontrado.")

# Função de busca de livros pelo estoque
def Info_Por_Estoque(lista_livros):
    estoque_alvo = 0
    encontrados = 0
    
    print("Busca de livros pela quantidade em estoque\n")
    estoque_alvo = float(input("Digite a quantidade mínima desejada: ").upper())
    
    print(f"Buscando livros com quantidade maior que: {estoque_alvo}...")
    
    # filtragem livro por livro
    for livro in lista_livros:
        if (livro.estoque >= estoque_alvo):
            encontrados += 1
            livro.Info()
            print("")
    
    print("-"*30)
    
    # verificação para caso livros foram encontrados, ou não
    if encontrados == 1:
        print(f"\n{encontrados} livro foi encontrado.")
    
    elif encontrados > 1:
        print(f"\n{encontrados} livros foram encontrados.")
    else:
        print("\nNenhum livro com quantidade maior que esta foi encontrado.")

# Função de calculo para o valor total em estoque (entre todos os livros)
def Valor_Total_Estoque(lista_livros):
    valores_totais_livros = 0.0
    estoque_total = 0
    valor_total_estoque = 0.0

    print("Calculando o valor total em estoque...\n")
    
    for livro in lista_livros:
        valores_totais_livros += livro.valor
        estoque_total += livro.estoque
    
    valor_total_estoque = valores_totais_livros * estoque_total
    
    if (valor_total_estoque > 0):
        print("Valor total em estoque: ")
        print(f"R$ {valor_total_estoque:.2f}")
    else: 
        print("Não foi possível calcular o valor total do estoque.")

#* Função Principal
if __name__ == "__main__":
    # lista de livros
    lista_livros = []
    # flag para a execução contínua do sistema
    running = True
    # escolha inserida pelo usuário
    escolha = 0
    
    # Livros de exemplos
    lista_livros.append(
                        Livro(
                            codigo="0301", 
                            titulo="Compiladores",
                            editora="Pearson",
                            categoria="Computação",
                            ano="2016",
                            valor=85.00,
                            estoque=125
                        ))
    lista_livros.append(
                        Livro(
                            codigo="1203", 
                            titulo="Engenharia de Software",
                            editora="Pressman",
                            categoria="Computação",
                            ano="2011",
                            valor=78.00,
                            estoque=100
                        ))
    
    print("-"*30)
    print("\tSistema Livraria")
    
    # Condição para executar o sistema
    while running:
        print("-"*30)
        print("Funcionalidades Disponíveis: \n")
        print("1 - Cadastrar novo livro")
        print("2 - Listar livros")
        print("3 - Buscar livros por nome")
        print("4 - Buscar livros por categoria")
        print("5 - Buscar livros por preço")
        print("6 - Busca por quantidade em estoque")
        print("7 - Valor total no estoque")
        print("0 - Encerrar atividades\n")
        
        escolha = int(input(
            "Digite o número da funcionalidade desejada: "))

        if escolha == 0: # Encerrar o sistema
            print("-"*30)
            print("Encerrando atividades...")
            print("-"*30)
            running = False

        elif escolha == 1: # Cadastro de livros
            print("-"*30)
            Cadastro(lista_livros)

        elif escolha == 2: # Listagem geral dos livros
            print("-"*30)
            for livro in lista_livros:
                livro.Info()

        elif escolha == 3: # Buscar livro por nome
            print("-"*30)
            Info_Por_Nome(lista_livros)

        elif escolha == 4: # Buscar livro por categoria
            print("-"*30)
            Info_Por_Categoria(lista_livros)

        elif escolha == 5: # Buscar livro por preço
            print("-"*30)
            Info_Por_Valor(lista_livros)

        elif escolha == 6: # Buscar livro por estoque
            print("-"*30)
            Info_Por_Estoque(lista_livros)

        elif escolha == 7: # Valor total no estoque
            print("-"*30)
            Valor_Total_Estoque(lista_livros)

        else: # Opção inválida
            print("-"*30)
            print("Opção não encontrada")
        
        # Este input serve apenas para o sistema não voltar
        # ao menu imediatamente após uma funcionalidade
        input("\nContinuar...")