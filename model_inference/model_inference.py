import os
#os.environ["OLLAMA_HOST"] = "http://127.0.0.1:8080"
from langchain_community.llms.ollama import Ollama
from langchain_core.documents import Document



#graph = Neo4jGraph(url="http://localhost:7474")


#llm = Ollama(model='gemma:2b', base_url="http://127.0.0.1:8080")
#print(llm.invoke('Why is the sky blue?'))





# response = ollama.chat(model='gemma:2b', messages=[{'role':'user', 'content':'Why is the sky blue?'}])
# print(response['message']['content'])