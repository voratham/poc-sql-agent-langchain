# This repo poc about sql agent with lang-chain by using gemini model


## how to run project
```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

#  set to database your name on database_connector.py
# "mysql+pymysql://user:password@localhost:3306/db_name")

# set model and api-key on sql_agent.py

python3 main.py
```


reference: https://h3manth.com/notes/SQLDatabaseChain/
