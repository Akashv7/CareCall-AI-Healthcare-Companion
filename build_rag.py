from src.rag_engine import build_vector_database





print(

    "Building CareCall Medical Knowledge Base..."

)






status=build_vector_database()






if status:


    print(

        "RAG Database Created Successfully ✅"

    )



else:


    print(

        "No PDF files found ❌"

    )


    print(

        "Add PDFs inside knowledge_base folder"

    )