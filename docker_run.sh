
#Pull neo4j and ollama
sudo docker run --name neo4j -p 7474:7474 -p 7687:7687 -d -e NEO4J_AUTH=neo4j/password -e NEO4J_PLUGINS=\[\"apoc\"\] neo4j:latest
sudo docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

#Run the following command to pull llama3
container_id=$(docker ps | grep ollama | awk '{print $1}')
docker exec -it $container_id ollama pull llama3:8b

