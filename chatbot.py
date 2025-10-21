import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# 🔑 OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_SECRET_KEY")

# 🏷️ App header
st.header("My first chatbot")

# 📂 Sidebar – PDF uploader
with st.sidebar:
    st.title("Your Document")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

# 🧩 Extract text from uploaded PDF
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # 🪓 Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # 🔠 Generate embeddings
    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

    # 🧠 Create vector store (FAISS)
    vector_store = FAISS.from_texts(chunks, embeddings)

    # 💬 Get user's question
    user_question = st.text_input("Type your question:")

    if user_question:
        # 🔍 Perform similarity search
        matched_docs = vector_store.similarity_search(user_question, k=3)

        # 🤖 Initialize LLM
        llm = ChatOpenAI(
            api_key=OPENAI_API_KEY,
            model="gpt-3.5-turbo",
            temperature=0
        )

        # ⚙️ Load QA chain
        chain = load_qa_chain(llm, chain_type="stuff")

        # 🧠 Run the chain
        response = chain.run(input_documents=matched_docs, question=user_question)

        # 🖊️ Display result
        st.subheader("Answer:")
        st.write(response)
else:
    st.info("👈 Please upload a PDF file to start chatting.")
