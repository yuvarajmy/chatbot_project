"""Terminal chat management command.

Run this command from the project root with:

    python manage.py chat_terminal

Optional:
    python manage.py chat_terminal --train
        Trains the chatbot on the default English corpus before starting
        the interactive session.
"""

from django.core.management.base import BaseCommand
from chatapp.bot import get_chatbot, train_chatbot


class Command(BaseCommand):
    """Django management command to start a terminal chat session."""

    help = "Start a terminal-based chat session with the ChatterBot bot."

    def add_arguments(self, parser):
        """Define optional CLI arguments for the command."""
        parser.add_argument(
            "--train",
            action="store_true",
            help="Train the chatbot using the default English corpus before starting the chat.",
        )

    def handle(self, *args, **options):
        """Entry point when the command is executed."""
        self.stdout.write(self.style.SUCCESS("Initializing chatbot..."))
        bot = get_chatbot()

        # Optionally train the bot if requested
        if options.get("train"):
            self.stdout.write(self.style.WARNING("Training chatbot. This may take a moment..."))
            train_chatbot(bot)
            self.stdout.write(self.style.SUCCESS("Training complete."))

        self.stdout.write(self.style.SUCCESS("Chatbot is ready!"))
        self.stdout.write(
            self.style.HTTP_INFO(
                "Type your message and press Enter. "
                "Type 'exit' or 'quit' to end the conversation.\n"
            )
        )

        # Main interactive loop
        while True:
            try:
                user_input = input("user: ").strip()

                # Exit conditions
                if user_input.lower() in {"exit", "quit"}:
                    self.stdout.write(self.style.WARNING("Ending chat session. Goodbye!"))
                    break

                if not user_input:
                    # Ignore empty input for a cleaner experience
                    continue

                # Get response from the chatbot
                response = bot.get_response(user_input)

                # Print bot's response
                self.stdout.write(f"bot: {response}")

            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                self.stdout.write(
                    "\n" + self.style.WARNING("Chat interrupted by user. Goodbye!")
                )
                break
            except Exception as exc:  # noqa: BLE001
                # Log error and continue loop
                self.stderr.write(self.style.ERROR(f"An error occurred: {exc}"))
