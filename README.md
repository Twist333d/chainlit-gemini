# Gemini Chainlit Chat Application

This project implements a chat interface using Chainlit and LangChain, powered by Google's Gemini Pro 1.5 model via OpenRouter.

## Features

- Interactive chat interface using Chainlit
- Integration with Google's Gemini Pro 1.5 model
- Conversation memory to maintain context
- Streaming responses for real-time interaction
- Custom system prompts loaded from YAML file
- Environment variable management for secure API key storage

## Supported Functionalities

- Supports Gemini 1.5 Pro model only
- Uses langchain openai library to connect to open router

## Setup

1. Clone the repository
2. Setup poetry environment
2. Install dependencies: `poetry install`
3. Set up your `.env` file with your OpenRouter API key
4. Customize `prompts.yaml` with your desired system prompt
5. Run the application: `poetry run chainlit run app.py` or `chainlit run app.py`

## Requirements

- Python 3.8+
- Poetry for dependency management
- OpenRouter API key for accessing Gemini Pro 1.5

## Usage
After starting the application, navigate to the provided local URL in your web browser to begin chatting with the AI assistant.