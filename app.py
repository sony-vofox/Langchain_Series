from langchain_openai import ChatOpenAI           # for OpenAI connection
from langchain_core.prompts import ChatPromptTemplate       # For setting the Prompt template
from langchain_core.output_parsers import StrOutputParser   # Default output Parser for LLM response

import streamlit as st
import os
from dotenv import load_dotenv 

import os

# Get the value of LANGCHAIN_API_KEY from environment variables
api_key = os.getenv("LANGCHAIN_API_KEY")

# Check if api_key is not None before assigning it
if api_key is not None:
    os.environ["LANGCHAIN_API_KEY"] = api_key
else:
    # Handle the case when LANGCHAIN_API_KEY is not set
    print("Error: LANGCHAIN_API_KEY environment variable is not set.")



# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
# ## Langmith tracking
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system","You are a helpful assistant. Please response to the user queries"),    # system prompt
#         ("user","Question:{question}")             # user prompt                      
#     ]
# )

# ## streamlit framework

# st.title('Langchain Demo With OPENAI API')
# input_text=st.text_input("Search the topic u want")

# # openAI LLm 
# llm=ChatOpenAI(model="gpt-3.5-turbo")
# output_parser=StrOutputParser()
# chain=prompt|llm|output_parser

# if input_text:
#     st.write(chain.invoke({'question':input_text}))

