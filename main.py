from database import Database
from fam_database import FamilyDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.211.89.144:7687", "neo4j", "eighties-reinforcement-starboard")
db.drop_all()

# Criando uma instância da classe FamilyDatabase para interagir com o banco de dados
family_db = FamilyDatabase(db)

# criando as entidades
family_db.create_person("147a", "Johnny Murray II", "M", 65)
family_db.create_person("12e", "Kath Hunter", "F", 65)
family_db.create_person("232d", "Cynthia Hunter Murray", "F", 45)
family_db.create_person("890m", "Josef Parker", "M", 45)
family_db.create_person("5464k", "Raphael Hunter Parker", "M", 25)
family_db.create_person("0098c", "Leo Hunter Parker", "F", 25)
family_db.create_pet("4242", "Bob", 14, "M")
family_db.create_pet("1936v", "Cayde", 10, "M")
family_db.create_pet("754l", "Elsie", 7, "F")
family_db.create_pet("529y", "Ze", 9, "M")

# atribuindo segunda label as pessoas
family_db.define_occupation("147a", "Engenheiro")
family_db.define_occupation("12e", "Militar")
family_db.define_occupation("232d", "Arquiteto")
family_db.define_occupation("890m", "Atleta")
family_db.define_occupation("5464k", "Militar")
family_db.define_occupation("0098c", "Presidente")
# atribuindo segunda label aos pets
family_db.define_specie("4242", "Cachorro")
family_db.define_specie("1936v", "Cachorro")
family_db.define_specie("754l", "Gato")
family_db.define_specie("529y", "Papagaio")

# criando as relacoes familiares
family_db.create_marriage("147a", "12e", "medium")
family_db.create_marriage("12e", "147a", "medium")
family_db.create_parenthood("147a", "232d", "medium")
family_db.create_parenthood("12e", "232d", "good")
family_db.create_marriage("232d", "890m", "good")
family_db.create_marriage("890m", "232d", "good")
family_db.create_parenthood("232d", "5464k", "good")
family_db.create_parenthood("890m", "5464k", "bad")
family_db.create_parenthood("232d", "0098c", "medium")
family_db.create_parenthood("890m", "0098c", "medium")
family_db.create_brotherhood("5464k", "0098c", "good")
family_db.create_brotherhood("0098c", "5464k", "good")
# relacionando os pets e seus donos
family_db.create_ownership("4242", "12e")
family_db.create_ownership("1936v", "0098c")
family_db.create_ownership("754l", "5464k")
family_db.create_ownership("529y", "5464k")

while True:
    print("1) Busca todos militares da familia | 2) Busca todos os pets que um determinado id possui | 3) Busca o parceiro de um determinado id ")
    num = int(input("Digite um número entre 0 e 3 (0 para sair): "))

    if num == 0:
        break
    elif num == 1:
        print("As seguintes pessoas sao militares: ")
        print(family_db.get_military())
    elif num == 2:
        wanted_id = input("Qual o id da pessoa desejada?")
        print("A pessoa buscada possui pets de nome: ")
        print(family_db.get_owned_pets(wanted_id))
    elif num == 3:
        wanted_id = input("Qual o id da pessoa desejada?")
        print("A pessoa buscada é casada com: ")
        print(family_db.get_partner(wanted_id))
    else:
        print("Nao existe funcao para o numero digitado. Tente novamente!")

# Fechando a conexão
db.close()