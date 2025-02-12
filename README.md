# NeoGPT-streamlit-chatbot
# LLM ChatBot 🤖

A streamlined chatbot application built with Streamlit and OpenAI's GPT-4, offering an intuitive interface for AI-powered conversations.

## Features ✨

- Real-time chat interface using Streamlit
- Integration with OpenAI's GPT-4 (configurable to use GPT-3.5-turbo)
- Stream-based response generation for smooth user experience
- Chat history management
- Environment-based configuration
- Error handling and recovery
- Responsive design with custom styling
- Clear chat functionality

## Prerequisites 📋

Before running the application, make sure you have:

- Python 3.8 or higher
- An OpenAI API key
- Git (for cloning the repository)

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/Aditya-Nagpure/LLM-ChatBot.git
cd LLM-ChatBot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage 🚀

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically `http://localhost:8501`)

3. Start chatting with the AI!

## Project Structure 📁

```
LLM-ChatBot/
├── main.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # Project documentation
```

## Configuration ⚙️

You can modify the following parameters in `app.py`:
- `model`: Change between "gpt-4" and "gpt-3.5-turbo"
- `temperature`: Adjust response creativity (0.0 - 1.0)
- `max_tokens`: Modify maximum response length

Streamlit Link: https://neogpt-chatbot.streamlit.app/
