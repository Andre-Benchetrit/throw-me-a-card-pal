import os
from core.client import bot
from dotenv import load_dotenv

def main() -> None:
	load_dotenv()
	bot.run(os.getenv("TOKEN"))


if __name__ == "__main__":
	main()
