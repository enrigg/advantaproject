from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
import json

from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import load_prompt
import pandas as pd
from flask import jsonify

def complete_table(text):
    # Insert your OpenAI txt path with your personal key
    f = open('C:\\Users\\Desktop\\openai.txt')
    
    api_key = f.read()
    from langchain.llms import OpenAI
    output_parser = CommaSeparatedListOutputParser()
    format_instructions = output_parser.get_format_instructions()

    chat = ChatOpenAI(openai_api_key=api_key)
    system_template = "Give me 5 project names, 5 descriptions, 5 programming languages to be written in and a ranking of utility(over 10) so that the chances of being hired grow. I want the format to be json"
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

    human_template="{linkedin_text}\n{format_instructions}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    request = chat_prompt.format_prompt(linkedin_text=text, format_instructions = output_parser.get_format_instructions()).to_messages()

    result = chat(request)

    text = result.content
    json_data = json.loads(text)

    return json_data