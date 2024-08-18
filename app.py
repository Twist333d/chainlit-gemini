from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig
from langchain.memory import ConversationBufferMemory
import chainlit as cl
import yaml
from langchain.chat_models import ChatOpenAI as GeminiPro15
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load the entire prompts.yaml file
with open('prompts.yaml', 'r') as file:
    prompts = yaml.safe_load(file)

# Access the system prompt
system_prompt = prompts.get('system_prompt')
if system_prompt is None:
    raise ValueError("System prompt not found in prompts.yaml")

# Initialize LLM (Gemini via OpenRouter)
def get_llm():
    return GeminiPro15(
        model="google/gemini-pro-1.5",
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        streaming=True
    )

# Initialize llm
llm = get_llm()

@cl.on_chat_start
async def on_chat_start():
    model = llm
    memory = ConversationBufferMemory(return_messages=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)
    cl.user_session.set("memory", memory)

@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")
    memory = cl.user_session.get("memory")
    msg = cl.Message(content="")
    async for chunk in runnable.astream(
        {"question": message.content, "history": memory.chat_memory.messages},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)
    await msg.send()
    memory.chat_memory.add_user_message(message.content)
    memory.chat_memory.add_ai_message(msg.content)