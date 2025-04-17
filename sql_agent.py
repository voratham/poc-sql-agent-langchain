from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_sql_query_chain
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit


class SQLAgent:
    def __init__(self, db_connector):
        self.db = db_connector.db

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash", 
            google_api_key="xxxxx",
            temperature=0,
            max_output_tokens=300,

        )

        self.toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)

        self.agent = create_sql_agent(
            llm=self.llm,
            toolkit=self.toolkit,
            verbose=True

        )

        self.sql_chain = create_sql_query_chain(self.llm, self.db)

    def run_agent(self, query):
        """ใช้ agent เพื่อตอบคำถามที่ซับซ้อน"""
        return self.agent.run(query)

    def generate_sql(self, query):
        """สร้าง SQL query จากคำถามภาษาธรรมชาติ"""
        return self.sql_chain.run({"question": query})
