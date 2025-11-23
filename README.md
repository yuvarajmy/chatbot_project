# Terminal Chatbot (Django + ChatterBot)

Terminal client that lets you chat with a ChatterBot from a Django management command.

## Requirements
- Python 3.11+
- Django 5.x
- chatterbot 1.0.8, chatterbot_corpus 1.2.0
- spaCy English model (`en_core_web_sm`)
- PyYAML (for corpus training)

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m pip install pyyaml
```

## Usage
- Quick chat:
  ```bash
  python manage.py chat_terminal
  ```
- Train on the default English corpus then chat:
  ```bash
  python manage.py chat_terminal --train
  ```
- Exit with `exit` or `quit`.

## Example session
```
Initializing chatbot...
Chatbot is ready!
Type your message and press Enter. Type 'exit' or 'quit' to end the conversation.
user: Hello
bot: Hi
user: exit
Ending chat session. Goodbye!
```

## Notes for submission
- Include this code and a screenshot of a terminal chat session in your Word document.
- Add your GitHub repository URL to the submission as required by the assignment.
