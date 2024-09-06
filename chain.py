import os
import dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain.chains import create_retrieval_chain
from langchain.chains import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import AIMessage, HumanMessage


dotenv.load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

#Create a llm
llm = ChatOpenAI(
    model_name = "gpt-4o-mini",
    api_key = api_key,
    temperature = 0.4
)

#Load the data
file_path = "static/bio.txt"

loader = TextLoader(file_path)

docs = loader.load()


#Split the documents

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

splits = text_splitter.split_documents(docs)


#Store the splits in a vector database

vector_db = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(api_key=api_key))


#Create a retriever
retriever = vector_db.as_retriever()

# Creating history-aware retriever

context_aware_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

context_aware_q_prompt = ChatPromptTemplate(
    [
        ('system', context_aware_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ('human', "{input}")
    ]
)

history_aware_retriever = create_history_aware_retriever(llm, retriever, context_aware_q_prompt)

# System prompt
system_prompt = (
    "You are Buddy, an AI assistant dedicated to assisting Tanishq in his job search by providing recruiters with relevant information about his qualifications and achievements." 
    "Your goal is to support Tanishq in presenting himself effectively to potential employers and promoting his candidacy for job opportunities."
    "Use the following pieces of retrieved context to answer the question,"
    "If you do not know the answer, politely admit it and let recruiters know how to contact Tanishq to get more information directly from him." 
    "Don't put 'Buddy' or a breakline in the front of your answer."
    "Only answer the question if you are sure about the answer."
    "Keep your answer concise and to the point."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate(
    [
        ('system', system_prompt),
        MessagesPlaceholder("chat_history"),
        ('human', "{input}")
    ]
)

# Create retrieval chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)


def chat(prompt):
    history = []

    while True:
        question = prompt

        response = rag_chain.invoke({"input": question, "chat_history": history})


        history.extend(
            [
                HumanMessage(content=question),
                AIMessage(content=response['answer'])
            ]
        )
        return response['answer']



