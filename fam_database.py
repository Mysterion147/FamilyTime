class FamilyDatabase:
    def __init__(self, database):
        self.db = database

    def create_person(self, id, name, sex, age):
        query = "CREATE (:Person {name: $name, id: $id, sex: $sex, age: $age})"
        parameters = {"id": id, "name": name, "sex": sex, "age": age}
        self.db.execute_query(query, parameters)

    def define_occupation(self, aimed_id, occupation):
        query = f"MATCH (n:Person{{id: $aimed_id}}) SET n:{occupation}"
        parameters = {"aimed_id": aimed_id}
        self.db.execute_query(query, parameters)

    # match por id porque arvores maiores podem ter duas entidades com o mesmo nome
    def create_parenthood(self, ancestor_id, descendant_id, quality):
        query = "MATCH (d:Person {id: $descendant_id}), (a:Person {id: $ancestor_id}) CREATE (d) -[:PAI_DE]-> (a)"
        parameters = {"ancestor_id": ancestor_id, "descendant_id": descendant_id, "quality":quality}
        self.db.execute_query(query, parameters)

    def create_brotherhood(self, ancestor_id, descendant_id, quality):
        query = "MATCH (d:Person {id: $descendant_id}), (a:Person {id: $ancestor_id}) CREATE (d) -[:IRMAO_DE]-> (a)"
        parameters = {"ancestor_id": ancestor_id, "descendant_id": descendant_id, "quality":quality}
        self.db.execute_query(query, parameters)

    def create_marriage(self, ancestor_id, descendant_id, quality):
        query = "MATCH (d:Person {id: $descendant_id}), (a:Person {id: $ancestor_id}) CREATE (d) -[:CASADO_COM{quality: $quality}]-> (a)"
        parameters = {"ancestor_id": ancestor_id, "descendant_id": descendant_id, "quality":quality}
        self.db.execute_query(query, parameters)

    def create_pet(self, id, name, age, sex):
        query = "CREATE (:Pet {name: $name, id: $id, sex: $sex, age: $age})"
        parameters = {"id": id, "name": name, "age": age, "sex": sex}
        self.db.execute_query(query, parameters)

    def define_specie(self, aimed_id, specie):
        query = f"MATCH (n:Pet{{id: $aimed_id}}) SET n:{specie}"
        parameters = {"aimed_id": aimed_id, "specie": specie}
        self.db.execute_query(query, parameters)

    # match por id porque arvores maiores podem ter duas entidades com o mesmo nome
    def create_ownership(self, pet_id, owner_id):
        query = "MATCH (p:Person {id: $owner_id}), (a:Pet {id: $pet_id}) CREATE (p) -[:DONO_DE]-> (a)"
        parameters = {"pet_id": pet_id, "owner_id": owner_id}
        self.db.execute_query(query, parameters)

    def get_military(self):
        query = "MATCH (p:Militar) RETURN p.name AS nome"
        results = self.db.execute_query(query)
        return results

    def get_owned_pets(self, id):
        query = "MATCH (p:Person {id: $id})--(a:Pet) RETURN a.name AS nome"
        parameters = {"id": id}
        results = self.db.execute_query(query, parameters)
        return [(result["nome"]) for result in results]

    def get_partner(self, id):
        query = "MATCH (p:Person {id: $id})<-[:CASADO_COM]-(q:Person) RETURN q.name AS nome"
        parameters = {"id": id}
        results = self.db.execute_query(query, parameters)
        return [(result["nome"]) for result in results]





