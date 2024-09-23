from neo4j import GraphDatabase

if __name__=="__main__":

    URI = "bolt://neo4j-andrei:portnumber"

    driver = GraphDatabase.driver(URI, auth=("neo4j", "password"))

    while True:
        userinput = input("Enter your query: ")
        print(userinput)
        records, _, _ = driver.execute_query(userinput, database="neo4j")

        for record in records:
            print(records)
