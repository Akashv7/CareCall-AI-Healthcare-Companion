from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_text_splitters import CharacterTextSplitter 



def create_rag():


    with open(
        "knowledge_base/medical.txt",
        "r",
        encoding="utf-8"
    ) as file:


        data=file.read()



    splitter=CharacterTextSplitter(

        chunk_size=300,

        chunk_overlap=50

    )



    chunks=splitter.split_text(
        data
    )



    embeddings=HuggingFaceEmbeddings(

        model_name="all-MiniLM-L6-v2"

    )



    db=Chroma.from_texts(

        chunks,

        embeddings

    )



    return db





def retrieve_context(question):


    db=create_rag()



    docs=db.similarity_search(

        question,

        k=2

    )



    context=""


    for doc in docs:


        context += doc.page_content + "\n"



    return context