# Simple Chatbot

A simple Python-based chatbot using natural language processing with NLTK.

## Features

- Pattern matching responses
- Basic conversation capabilities
- Easy to extend with new patterns and responses

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mmoenterprise/simple-chatbot.git
   cd simple-chatbot
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the chatbot:
   ```bash
   python chatbot.py
   ```

## Usage

- Start a conversation with the chatbot
- Type 'quit' to exit

## Extending the Chatbot

To add new responses, edit the `pairs` list in `chatbot.py`. Each pair consists of:
1. A pattern to match (using regular expressions)
2. A list of possible responses

## License

This project is open source and available under the MIT License.