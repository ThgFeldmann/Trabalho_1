
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
    
    def Info(self): #* Método para informar *todos* os livros

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

#* main function
if __name__ == "__main__":

    lista_livros = []
    
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

    running = True
    escolha = 0
    
    print("-"*30)
    print("\tSistema Livraria")
    
    #* Condition to run the system
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
            print("Executar função de cadastro")
            Cadastro(lista_livros)

        elif escolha == 2: # Listagem geral dos livros
            print("-"*30)
            for livro in lista_livros:
                livro.Info()

        elif escolha == 3: # Buscar livro por nome
            print("-"*30)
            print("Executar função de busca de livro por nome")

        elif escolha == 4: # Buscar livro por categoria
            print("-"*30)
            print("Executar função de busca de livro por categoria")

        elif escolha == 5: # Buscar livro por preço
            print("-"*30)
            print("Executar função de busca de livro por preço")

        elif escolha == 6: # Buscar livro por estoque
            print("-"*30)
            print("Executar função de buscar livros por estoque")

        elif escolha == 7: # Valor total no estoque
            print("-"*30)
            print("Executar função de calculo do estoque")

        else: # Opção inválida
            print("-"*30)
            print("Opção não encontrada")
            
        input("\nContinuar...")