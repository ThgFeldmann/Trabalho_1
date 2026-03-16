
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
        
        print("-"*30)
        print(f">>>>>>Cod#{self.codigo}")
        print(f"Titulo/Editora: {self.titulo}/{self.editora}")
        print(f"Categoria: {self.categoria}")
        print(f"Ano: {self.ano}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Estoque: {self.estoque} unidade(s)")
        print(f"Valor total em estoque: R$ {valor_estoque:.2f}")

#* main function
if __name__ == "__main__":
    lista_livros = []
    running = True
    escolha = 0
    
    print("-"*30)
    print("\tSistema Livraria")
    
    # Condition to run the system
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
        
        try:
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

            elif escolha == 2: # Listagem geral dos livros
                print("-"*30)
                print("Executar função de listagem")
                Livro.Info()

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

        except Exception as error:
            print("-"*30)
            print("Ocorreu um erro, certifique-se de" +
                " digitar um número dentre as opções disponíveis")