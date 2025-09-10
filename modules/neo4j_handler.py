from neo4j import GraphDatabase

class Neo4jHandler:
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

    def record_result(self, value):
        with self.driver.session() as session:
            session.run(
                "CREATE (r:Result {value: $value, timestamp: timestamp()})",
                value=value
            )
        print(f"Записано значение {value} в Neo4j")
