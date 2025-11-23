"""ChatterBot setup for the Django terminal chatbot.

This module exposes helper functions to create and train a ChatBot
instance. Keeping this logic separate makes it easy to reuse in
other parts of the project (e.g., views or APIs) later.
"""

from chatterbot import ChatBot, languages
from chatterbot.trainers import ChatterBotCorpusTrainer


def get_chatbot():
    """Create and return a configured ChatBot instance.

    The database_uri points to the same SQLite database used by Django
    so that knowledge can be persisted across sessions.
    """
    chatbot = ChatBot(
        'TerminalBot',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
            }
        ],
        tagger_language=languages.ENG,
        database_uri='sqlite:///db.sqlite3',
    )
    return chatbot


def train_chatbot(chatbot: ChatBot):
    """Train the ChatBot using the default English corpus.

    You can customize this to train on specific categories or add your
    own custom conversation datasets if needed.
    """
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english')
