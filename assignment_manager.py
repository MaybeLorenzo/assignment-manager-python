import random

# Criando uma classe Tarefa que vai ser responsável por criar objetos que representam a tarefa de um aluno.
class Tarefa:
    
    def __init__(self, nome : str, desc: str, prioridade : int, situacao="Ativa"):
# A criação do identificador é feita utilizando a função choices() da biblioteca random, que pega itens aleátorios de um iterável e retorna uma lista
# que então é transformada em uma string usando o método .join(), criando um código aleátorio para cada tarefa.
        self.padrao = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]
        self.id = "".join(random.choices(self.padrao[0], k=5))
        self.nome = nome
        self.desc = desc
        self.situacao = situacao
        self.prioridade = prioridade

# Aqui temos uma verificação de que todos os atributos nome, descrição e situação são do tipo string e o atributo prioridade é um número inteiro maior igual a 1 e menor igual a 4..
# Caso qualquer um destes seja de um tipo diferente do esperado, o programa retornará um TypeError seguido de uma mensagem para o usuário.
        if any(not isinstance(atributo, str) for atributo in [self.nome, self.desc, self.situacao]) or not isinstance(self.prioridade, int) or (self.prioridade < 1 or self.prioridade > 4):
            raise TypeError(f"O nome, descrição e a situação da sua tarefa devem ser do tipo string/texto.\nA prioridade deve ser um número inteiro.")
        
# Quando o programa precisar imprimir a tarefa, será feito da maneira a seguir
    def __str__(self):
            return f"Tarefa : '{self.nome}'\nDescrição: '{self.desc}'\nIdentificador : '{self.id}'\nPrioridade : '{self.prioridade}'\nSituação : '{self.situacao}'\n"

# Decidi criar essas duas separadas da função atualizar para meu código ficar mais simples de ler, elas simplesmente modificam o valor do atributo situação.
    def concluir(self):
        self.situacao = "Concluída"
        return self
    
    def abertura(self):
        self.situacao = "Ativa"
        return self

# Um método que criei pra atualizar os atributos de descrição e prioridade de uma Tarefa, tem por padrão os seus parâmetros como None para que o usuário possa
# editar um deles sem necessariamente editar o outro
    def atualizar(self, nova_desc=None, nova_prio=None):

# Se o valor de qualquer um desses parâmetros for None, a função retorna a própria tarefa sem modificar ela.
# Porém se passar por essa primeira verificação, eu verifico se o valor é do tipo esperado, senão eu retorno um TypeError.
# Se o valor inserido passar por todas as verificações, o atributo respectivo é atualizado e a função retorna uma Tarefa modificada.
        if nova_desc is not None:
            if not isinstance(nova_desc, str):
                raise TypeError("A descrição deve ser um atributo do tipo string.")
            self.desc = nova_desc

        if nova_prio is not None:
            if not isinstance(nova_prio, int) or nova_prio < 1 or nova_prio > 4:
                raise TypeError("A prioridade deve ser um número inteiro de 1 a 4 (inclusivo).")
            self.prioridade = nova_prio
        
        return self

# Criando uma classe que vai me permitir criar um objeto que armazena todas as tarefas do usuário.
class ConjuntoTarefas: 
    def __init__(self):
# Com o inicializador eu posso criar um dict que vai ter a chave como o identificador de uma tarefa e o seu respectivo valor como um objeto da classe tarefa
# Como eu já criei um método de str() pro objeto tarefa, ele vai imprimir cada tarefa em uma estrutura padronizada.
        self.tarefas = {}

# Pra que eu pudesse criar um dict com a estrutura que comentei ali em cima, eu poderia talvez usar um append() mas preferi criar um método especial de adição 
# que vai usar a propriedade de poder inserir um valor em um objeto se a gente der um valor padrão pra ele
    def __add__(self, other : Tarefa):

# Aqui eu checo se o que estamos tentando adicionar ao objeto ConjuntoTarefas é do tipo Tarefa, se não for eu retorno um TypeError com uma explicação pro usuário
        if isinstance(other, Tarefa):
            self.tarefas[other.id] = other
            return self
        else:
            raise TypeError("A classe ConjuntoTarefas suportar operações de soma somente com um objeto da classe 'Tarefa'.")
# Usar o método special de str() para visualização de todas as tarefas
    def __str__(self):
# Se não houver nenhuma tarefa dentro do dict eu retorno isso pro usuário.
# Se houver alguma, eu crio uma variável res (resultado) que é uma string vazia, fiz isso porque não sabia como retornar vários valores sem ter que criar uma
# variável que armazene eles. Então eu crio uma lista chamada ordenadas que vai conter os valores dos itens dentro do dict/atributo 'tarefas', eu ordeno eles do menor
# para o maior usando uma função lambda que leva em consideração o valor do atributo 'prioridade' de cada Tarefa dentro da lista.
# Por fim eu concateno cada Tarefa dentro da lista em forma de string a variável res usando um loop for, ai no final é só retornar o res que eu vou ter uma maneira
# de visualizar todas as Tarefas só usando um print() !
        if not self.tarefas:
            return "Nenhuma tarefa cadastrada."
        res = ""
        ordenadas = sorted(self.tarefas.values(), key=lambda tar: tar.prioridade)
        for tarefa in ordenadas:
            res += f"{tarefa}\n"
        return res


# Essa função muda o valor do atributo situacao para "Concluída" e retorna o objeto com o valor atualizado
def concluir_tarefa(tarefa):

    tarefa.situacao = "Concluída"

    return tarefa

# Essa função serve pra criar um novo objeto da classe Tarefa, que pede somente o seu nome, descrição e prioridade já que os atributos identificador e situacao
# são definidos automaticamente quando a gente cria um objeto dessa classe
def add_tarefa(no, descri, prio):
        tarefa = Tarefa(no, descri, prio)
        print("Operação realizada com sucesso.")
        return tarefa
    
# Essa função funciona usando as duas classes que criei antes, primeiro nós acessamos o atributo tarefas dentro do grupo, como ele é um dict a gente pode 
# acessar um item específico dentro dele usando sua key, que é o identificador. Após acessarmos ele a gente pode modificar o atributo situacao para "Ativa"
def reabrir_tarefa(identificador): 
    grupo.tarefas[identificador].situacao = "Ativa"


print("Bem vindo(a) estudante !\n")

menu = """As suas opções são:

Adicionar nova tarefa - Para criar uma nova tarefa digite 'adicionar'.
Concluir tarefa - Para definir a situação de uma tarefa como concluída digite 'concluir'.
Reabrir uma tarefa -  Para mudar a situação de uma tarefa concluída para ativa digite 'reabrir'.
Editar uma tarefa - Para editar a descrição ou a prioridade de uma tarefa digite 'editar'.
Visualizar tarefas - Para visualizar uma lista das suas tarefas digite 'visualizar'.
Encerrar programa - Para encerrar o programa digite 'encerrar'."""

# Iniciando um objeto que vai guardar todas as tarefas 
grupo = ConjuntoTarefas()
print(menu)

# Sempre vou usar o .lower() pra padronizar os inputs do usuário
opcao = input("O que você deseja fazer? ").lower()


# Iniciando um while loop que garante que o programa continue rodando enquanto o usuário não digitar "encerrar"
while opcao != "encerrar":

# Para adicionar uma tarefa, eu coleto o input do usuário para cada atributo obrigatório e crio uma nova Tarefa usando a função add_tarefa
# depois é só adicionar ela à minha variável grupo. Se houver um ValueError o programa alerta o usuário e volta para a seleção de opção.
    if opcao == "adicionar":
        try:
            nome = input("Digite o nome da sua tarefa: ")
            descricao = input("Digite a descrição da sua tarefa: ")
            prioridade = int(input("Digite a prioridade da sua tarefa (número inteiro de 1 a 4): "))
            nova = add_tarefa(nome, descricao, prioridade)
            grupo += nova
            print("Tarefa adicionada com sucesso!")
        except ValueError: 
            print("A prioridade deve ser um número inteiro maior igual a 1 e menor igual a 4, tente novamente.")
            print()

# Para concluir uma tarefa simplesmente usamos a função concluir(), se o identificador não existir o programa alerta e volta para seleção de opção.
    elif opcao == "concluir":
        identificador = input("Digite o identificador da sua tarefa (para saber o identificador de uma tarefa visualize a sua lista de tarefas): ")
        if identificador in grupo.tarefas:
            grupo.tarefas[identificador].concluir()
            print("Tarefa concluída com sucesso!")
        else:
            print(f"Identificador '{identificador}' não foi encontrado, tente novamente.\n")

# Para reabrir uma tarefa é o mesmo processo de conclusão porém dessa vez com a função abertura().

    elif opcao == "reabrir":
        identificador = input("Digite o identificador da sua tarefa (para saber o identificador de uma tarefa visualize a sua lista de tarefas): ")
        if identificador in grupo.tarefas:
            grupo.tarefas[identificador].abertura()
            print("Tarefa reaberta com sucesso!")
        else:
            print(f"Identificador '{identificador}' não foi encontrado, tente novamente.\n")

# A parte mais complexa é a de edição, pedimos primeiro o identificador da tarefa, se ele não for encontrado o programa alerta e volta para as opções.
    elif opcao == "editar":
        identificador = input("Digite o identificador da sua tarefa (para saber o identificador de uma tarefa visualize a sua lista de tarefas): ")

# Se o modificador existe nós criamos uma variável chamada modificar que corresponde a o que usuário quer editar, se ela existe nós pedimos ao usuário 
# uma nova descrição ou prioridade, dependendo do que ele quer mudar. Se ele inserir um comando inválido o programa alerta e volta para as opções.
        if identificador in grupo.tarefas:
            modificar = input("Digite 'desc' para mudar a descrição, 'prio' para prioridade ou 'ambas' para mudar as duas: ").lower()

            try:
                if modificar == "desc":
                    descricao = input("Digite a nova descrição da sua tarefa: ")
                    grupo.tarefas[identificador].atualizar(nova_desc=descricao, nova_prio=None)
                    print("Tarefa editada com sucesso!")

                elif modificar == "prio":
                    prio = int(input("Digite a nova prioridade da sua tarefa (um número inteiro de 1 a 4): "))
                    grupo.tarefas[identificador].atualizar(nova_desc=None, nova_prio=prio)
                    print("Tarefa editada com sucesso!")

                elif modificar == "ambas":
                    descricao = input("Digite a nova descrição da sua tarefa: ")
                    prioridade = int(input("Digite a nova prioridade da sua tarefa (um número inteiro de 1 a 4): "))
                    grupo.tarefas[identificador].atualizar(nova_desc=descricao, nova_prio=prioridade)
                    print("Tarefa editada com sucesso!")

# Temos esse bloco de exceção pra caso o usuário insira um valor incompatível na prioridade a gente possa alertar ele e voltar para o menu de opções.
            except (ValueError, TypeError):
                print("A prioridade deve ser um número inteiro maior igual a 1 e menor igual a 4, tente novamente")

            else:
                print("Comando inserido é inexistente.")
        else:
            print(f"Identificado '{identificador}' não foi encontrado, tente novamente.\n")

    elif opcao == "visualizar":
        print(grupo)
    else:
        print("A opção desejada não existe no programa, por favor tente novamente.")
        print()

    print(menu)
    opcao = input("O que você deseja fazer? ").lower()
    print()
print("O programa foi encerrado.")