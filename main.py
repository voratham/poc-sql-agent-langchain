from database_connector import DatabaseConnector
from sql_agent import SQLAgent
import time


def main():
    print("Connecting to database...")
    try:
        db_connector = DatabaseConnector(
            "mysql+pymysql://user:password@localhost:3306/db_name")
        print("Connected to database successfully!")

        agent = SQLAgent(db_connector)
        print("✅ SQL Agent created successfully!")

        while True:
            user_query = input("\n 🔥Enter your question (or 'exit' to quit): ")
            if user_query.lower() == 'exit':
                break

            try:
                print("\n🚀 Processing your query...")
                result = agent.agent(user_query)
                print("\n🟢 Result:")
                print(result)
            except Exception as e:
                print(f"🔴 Error processing query: {e}")
                
            time.sleep(2)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
