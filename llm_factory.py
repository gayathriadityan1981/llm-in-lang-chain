import os
import json
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
with open("config.json","r") as file:
    config = json.load(file)    
    provider =  config["provider"]
print(config)

#Initialize the LLM
def get_llm():
    if provider == "gemini":
        print("Provider is gemini")
        llm = ChatGoogleGenerativeAI(
                model = config["gemini"]["model"],
                temperature = config["gemini"]["temperature"],
                max_tokens = config["gemini"]["max_token"],
                api_key = os.getenv("GOOGLE_API_KEY")
            )
        return llm
    elif provider == "openai":
        print("Provider is openai")
        llm = ChatOpenAI(
            model = config["openai"]["model"],
            temperature = config["openai"]["temperature"],
            max_tokens = config["openai"]["max_token"],
            api_key = os.getenv("open_api_key")
        )
        return llm
    else :
        raise ValueError("Invalid provider in config.json.It must be openai or gemini")
