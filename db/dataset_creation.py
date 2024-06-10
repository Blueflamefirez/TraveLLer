import os
from langchain_community.document_loaders import WikipediaLoader
from langchain_community.graphs import Neo4jGraph
from langchain.text_splitter import TokenTextSplitter
from langchain_community.llms.ollama import Ollama
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.documents import Document


graph = Neo4jGraph(url="bolt://localhost:7687", username="neo4j", password="password")

llm = Ollama(model="mistral:7b", base_url="http://localhost:8080")

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
split_docs = []
text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=24)

# text = """
# Marie Curie, born in 1867, was a Polish and naturalised-French physicist and chemist who conducted pioneering research on radioactivity.
# She was the first woman to win a Nobel Prize, the first person to win a Nobel Prize twice, and the only person to win a Nobel Prize in two scientific fields.
# Her husband, Pierre Curie, was a co-winner of her first Nobel Prize, making them the first-ever married couple to win the Nobel Prize and launching the Curie family legacy of five Nobel Prizes.
# She was, in 1906, the first woman to become a professor at the University of Paris.
# """
# documents = [Document(page_content=text)]

for country in countries[:1]:
    docs = WikipediaLoader(query=country, load_max_docs=1, doc_content_chars_max=-1).load()
    #print(docs)
    split_docs = text_splitter.split_documents(docs)
    #print(split_docs)
    with open(f"./country_documents/{country}.txt", "a") as f:
        for doc in docs:
            print(doc.page_content, file=f)
            

graph_docs = llm_graph_transformer.convert_to_graph_documents(split_docs)
graph.add_graph_documents(graph_docs, baseEntityLabel=True, include_source=True)
