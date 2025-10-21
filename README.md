# AI-ChatBot

Setup & Installation


1️⃣ Clone the repository
      git clone https://github.com/yourusername/pdf-chatbot.git
      cd pdf-chatbot

2️⃣ Create a virtual environment
      python -m venv venv


Activate it:
    Windows
      venv\Scripts\activate
    Mac/Linux
       source venv/bin/activate

3️⃣ Install dependencies
      pip install -r requirements.txt


Your requirements.txt should include:

streamlit
PyPDF2
langchain
langchain-openai
langchain-community
faiss-cpu
python-dotenv

4️⃣ Create a .env file
      Create a file named .env in your project root with the following content:
      OPENAI_SECRET_KEY=your_openai_api_key_here

      
▶️ Run the App
streamlit run app.py
      Once the app starts, open your browser at:
      http://localhost:8501
