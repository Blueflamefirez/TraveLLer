import os
from langchain_community.document_loaders import WikipediaLoader
from langchain_community.graphs import Neo4jGraph
from langchain.text_splitter import TokenTextSplitter
from langchain_community.llms.ollama import Ollama
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.documents import Document
import wikivoyage
import re


graph = Neo4jGraph(url="bolt://localhost:7687", username="neo4j", password="password")

llm = Ollama(model="llama3:8b", base_url="http://localhost:8080")

llm_graph_transformer = LLMGraphTransformer(llm=llm)
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
"United_Kingdom",
"Romania",
"Belarus",
"Greece",
"Bulgaria",
"Iceland",
"Portugal",
"Czech_Republic",
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
"San_Marino",
"Gibraltar",
"Monaco",
"Vatican_City"]
split_docs = []
text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=24)

def remove_URL(text):
    """
    Remove URLs from a text string
    """
    text = re.sub(r"https\S+", "", text)
    text = re.sub(r"\[.*?\]\S", "", text)
    return text

for country in countries:
    doc = ""
    # docs = WikipediaLoader(query=country, load_max_docs=1, doc_content_chars_max=-1).load()
    sections = wikivoyage.get(f"https://en.wikivoyage.org/wiki/{country}").sections
    for i in sections:
        doc += i.title + "\n" + remove_URL(i.content)
    docs = [Document(page_content=doc, metadata={"title": country})]
    split_docs = text_splitter.split_documents(docs)
    #print(split_docs)
    with open(f"./country_documents/{country}.txt", "a") as f:
        for doc in docs:
            print(doc.page_content, file=f)
            

graph_docs = llm_graph_transformer.convert_to_graph_documents(split_docs)
graph.add_graph_documents(graph_docs, baseEntityLabel=True, include_source=True)
try:
    graph.query("MATCH (n:None) DETACH DELETE n")
except:
    print("No None nodes to delete")

