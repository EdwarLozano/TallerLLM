import os
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstore.pinecone import Pinecone

def main():
    pinecone.init(api_key=os.getenv('API_KEY_PINECONE'), environment=os.getenv('ENV_NAME'))

    embeddings = OpenAIEmbeddings()
    file_paths = [
        "documentos/economia.txt",
        "documentos/ingenieria-civil.txt",
        "documentos/ingenieria-electrica.txt",
        "documentos/ingenieria-electronica.txt",
        "documentos/ingenieria-industrial.txt",
        "documentos/ingenieria-sistemas.txt"
    ]

    text_list = []

    for file_path in file_paths:
        with open(file_path, "r", encoding="utf8", errors="ignore") as file:
            text_list.append(file.read())

    text = " ".join(text_list)

    data = Pinecone.from_texts(text=[text], embedding=embeddings, index_name="carreras")

if __name__ == "__main__":
    main()