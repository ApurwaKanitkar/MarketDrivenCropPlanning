from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

app = Flask(__name__)
CORS(app)

def get_pdf_text(pdf_files):
    text = ""
    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore, llm=None, memory=None):
    if not llm:
        llm = ChatOpenAI()
    if not memory:
        memory = ConversationBufferMemory(
            memory_key='chat_history', return_messages=True
        )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memory
    )
    return conversation_chain

@app.route('/', methods=['POST'])
def ask():
    user_question = request.json['question']
    print(f"Received question: {user_question}")  # Log the received question
    conversation_chain = get_conversation_chain(vectorstore)
    response = conversation_chain.run({'question': user_question})
    return jsonify({'response': response})

if __name__ == '__main__':
    load_dotenv()
    embeddings = OpenAIEmbeddings(openai_api_key='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')
    with open('C:\\Users\\ajitk\\Documents\\Apurwa\\PICT\\ExtraCoCurricular\\Tech\\TechFiesta\\MarketDrivenCropPlanning\\chatbot\\Rice.pdf', 'rb') as f:
        raw_text = get_pdf_text([f])
    text_chunks = get_text_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks)
    app.run(port=5000, debug=True)