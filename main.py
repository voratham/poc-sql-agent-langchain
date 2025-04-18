import os
from database_connector import DatabaseConnector
from sql_agent import SQLAgent
import time
from dotenv import load_dotenv


def main():
    load_dotenv()  # loading env
    gemini_api_key = os.getenv("GEMINI_API_KEY")  # setting up OpenAI 
    database_url = os.getenv("DATABASE_URL")

    if gemini_api_key.__len__() == 0:
        print("🔴 Error: Please set the GEMINI_API_KEY environment variable.")
        return
    if database_url.__len__() == 0:
        print("🔴 Error: Please set the DATABASE_URL environment variable.")
        return

    print("Connecting to database...")
    try:
        db_connector = DatabaseConnector(database_url)
        print("✅ Connected to database successfully!")

        agent = SQLAgent(db_connector, gemini_api_key=gemini_api_key)
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
        print(f"🔴 Error: {e}")


if __name__ == "__main__":
    main()
