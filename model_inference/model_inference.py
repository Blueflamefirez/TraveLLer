import os
#os.environ["OLLAMA_HOST"] = "http://127.0.0.1:8080"
import ollama
from langchain_community.graphs import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_community.llms.ollama import Ollama
from langchain_core.documents import Document
from langchain_community.document_loaders import WikipediaLoader


#graph = Neo4jGraph(url="http://localhost:7474")


#llm = Ollama(model='gemma:2b', base_url="http://127.0.0.1:8080")
#print(llm.invoke('Why is the sky blue?'))

countries = [
"Ukraine",
"France",
"Spain",
"Sweden",
"Germany",
"Finland",
"Norway",
"Poland",
"Italy",
"United Kingdom",
"Romania",
"Belarus",
"Greece",
"Bulgaria",
"Iceland",
"Portugal",
"Czech Republic",
"Denmark",
"Hungary",
"Serbia",
"Austria",
"Ireland",
"Lithuania",
"Latvia",
"Croatia",
"Bosnia",
"Herzegovina",
"Slovakia",
"Estonia",
"Netherlands",
"Switzerland",
"Moldova",
"Belgium",
"Albania",
"Macedonia",
"Slovenia",
"Montenegro",
"Cyprus",
"Luxembourg",
"Faroe Is.",
"Andorra",
"Malta",
"Liechtenstein",
"Guernsey",
"San Marino",
"Gibraltar",
"Monaco",
"Vatican City"]

for country in countries:
    docs = WikipediaLoader(query=country, load_max_docs=1, doc_content_chars_max=-1).load()
    with open("./country_documents/{country}.txt", "a") as f:
        for doc in docs:
            print(doc.page_content, file=f)




# response = ollama.chat(model='gemma:2b', messages=[{'role':'user', 'content':'Why is the sky blue?'}])
# print(response['message']['content'])