import os


from dotenv import load_dotenv


from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)


from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


from langchain_chroma import Chroma


from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings
)





# ================= LOAD ENV =================


load_dotenv()





# ================= PATHS =================


DB_PATH = "chroma_db"


KNOWLEDGE_FOLDER = "knowledge_base"









# ================= GEMINI EMBEDDINGS =================


def get_embedding():


    return GoogleGenerativeAIEmbeddings(

        model="gemini-embedding-001",

        google_api_key=os.getenv(
            "GEMINI_API_KEY"
        )

    )









# ================= BUILD VECTOR DATABASE =================


def build_vector_database():


    documents=[]





    # check folder exists

    if not os.path.exists(
        KNOWLEDGE_FOLDER
    ):


        print(
            "Knowledge folder missing ❌"
        )


        return False








    # load files

    for file in os.listdir(
        KNOWLEDGE_FOLDER
    ):



        file_path=os.path.join(

            KNOWLEDGE_FOLDER,

            file

        )







        if file.endswith(".pdf"):



            loader=PyPDFLoader(

                file_path

            )



            documents.extend(

                loader.load()

            )









        elif file.endswith(".txt"):



            loader=TextLoader(

                file_path,

                encoding="utf-8"

            )



            documents.extend(

                loader.load()

            )











    if len(documents)==0:



        print(

            "No medical files found ❌"

        )



        return False










    # split text

    splitter=RecursiveCharacterTextSplitter(

    chunk_size=5000,

    chunk_overlap=200

)




    chunks=splitter.split_documents(

        documents

    )

    print(
    "TOTAL CHUNKS:",
    len(chunks)
)







    # create chroma db


    Chroma.from_documents(

        documents=chunks,

        embedding=get_embedding(),

        persist_directory=DB_PATH

    )







    print(

        "Vector database created successfully ✅"

    )



    return True













# ================= RETRIEVE CONTEXT =================


def retrieve_context(

        question

):


    try:



        db=Chroma(

            persist_directory=DB_PATH,

            embedding_function=get_embedding()

        )








        results=db.similarity_search(

            question,

            k=3

        )








        context=""


        sources=[]







        for doc in results:



            context += (

                doc.page_content

                +

                "\n"

            )






            sources.append(

                doc.metadata.get(

                    "source",

                    "unknown"

                )

            )








        return (

            context,

            sources

        )









    except Exception as e:



        print(

            "RAG ERROR:",

            e

        )






        return (

            "",

            []

        )