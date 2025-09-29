
docker start intel-ollama

docker exec -it intel-ollama bash

/llm/scripts/start-ollama.sh

/llm/modelfiles/gemma3.modelfile

docker stop intel-ollama

--- 

ollama create <nome_tuo> -f /path/file.modelfile