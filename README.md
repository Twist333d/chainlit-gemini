# 🚀 Gemini Chainlit Chat Application

This project implements a chat interface using **Chainlit** and **LangChain**, powered by Google's **Gemini Pro 1.5** model via Google AI Studio.

## 🌟 Features

- 🎭 Interactive chat interface using Chainlit
- 🌐 Integration with Google's Gemini Pro 1.5 model
- 🧠 Conversation memory to maintain context
- ⚡ Streaming responses for real-time interaction
- 📝 Custom system prompts loaded from YAML file
- 🔐 Environment variable management for secure API key storage

## 🛠️ Supported Functionalities

- Supports Gemini 1.5 Pro model (or any other Google AI studio model)
- Uses langchain openai library to connect to Google AI Studio

## 🏗️ Setup

1. 🔄 Clone the repository
2. 🛠️ Setup poetry environment
3. 📦 Install dependencies: `poetry install`
4. 🔑 Set up your `.env` file with your Google AI Studio API key
5. ✏️ Customize `prompts.yaml` with your desired system prompt
6. 🏃 Run the application: `poetry run chainlit run app.py` or `chainlit run app.py`

## 📋 Requirements

- Python 3.8+
- Poetry for dependency management
- Google AI Studio API Key for accessing Gemini Pro 1.5

## 🌍 Usage

After starting the application, navigate to the provided local URL in your web browser to begin chatting with the AI assistant. Enjoy your journey into conversational AI! 🌟

## 📄 Code Structure

The code provided integrates various components to ensure a smooth chat experience with real-time updates and memory of past interactions. 