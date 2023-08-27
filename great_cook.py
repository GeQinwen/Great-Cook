import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

st.title("Great Cook")

# Initialize user inputs
ingredients = ""

# Get the list of ingredients from the user
ingredients = st.text_area("Enter the list of ingredients")

# Initialize cooking methods and recipes
cooking_methods = ""
recipes = ""

# Generate possible cooking methods based on the given ingredients
def cookingMethodGenerator(ingredients):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0.7
    )
    system_template = """You are a cooking assistant. Your task is to generate possible cooking methods based on the given ingredients: {ingredients}."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please suggest possible cooking methods using the following ingredients: {ingredients}."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(ingredients=ingredients)
    return result # returns string   

# Generate recipes based on the given ingredients
def recipeGenerator(ingredients):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0.7
    )
    system_template = """You are a recipe generator. Your task is to create recipes based on the given ingredients: {ingredients}."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please generate a recipe using the following ingredients: {ingredients}."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(ingredients=ingredients)
    return result # returns string   

# Check if ingredients are provided and call the respective functions
if ingredients:
    cooking_methods = cookingMethodGenerator(ingredients)
    recipes = recipeGenerator(ingredients)

# Display the generated cooking methods and recipes to the user
st.markdown(cooking_methods)
st.markdown(recipes)
