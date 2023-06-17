# Ledger for Telegram groupchat

This repository contains a Telegram bot built with Python that can be run using Docker and utilizes Firestore as its database.
The purpose of this project is to provide ledger capabilites to Telegram making it easy to register and keep track of expenses within a groupchat.

- Split an expenses with another user
- Split an expenses with every other users
- Refund a single user
- Display the value owed to every other users

![Ledgerbot](/assets/ledgerbot.png?raw=true "Ledgerbot")

## Prerequisites

Before running the Telegram bot, make sure you have the following prerequisites set up:

- Docker installed on your machine
- A Firestore database set up on Google Cloud Platform
- Telegram Bot API token obtained from BotFather

## Getting Started

Follow these steps to get the Telegram bot up and running:

1. Clone the repository:

```shell
git clone https://github.com/your-username/telegram-bot-docker-firestore.git
```

2. Install the required dependencies:

```shell
pip install -r requirements.txt
```

3. Set up environment variables:
Copy `configuration-sample.yaml` into `configuration.yaml` in the project root directory and provide the following information:
You can define seperate credentials for production and development environment.

```yaml
BOT_TOKEN: 1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi
TELEGRAM_TOKEN: your-telegram-bot-token
FIRESTORE_PROJECT_ID: your-firestore-project-id
FIRESTORE_CREDENTIALS: /path/to/your/credentials.json
```
5. Build and run the Docker container:

```shell
docker-compose up --build
```
6. Register users
Once the bot is running, you need to configure the groupchat users to firebase.
This can be done by running the bot /register command.
More information can be found using the /help command.

## Usage

Once the Telegram bot is running, you can interact with it through your Telegram account. Start a conversation with the bot using its username and explore the available commands and features.

## Project structure
Commands are defined as handles and registered through the index
- `handlers` directory: as a placeholder for all command handlers  
- `index.py` file: to register all the function members

## Firestore Database

The Firestore database is used to store and manage ledger entries for the Telegram bot. To access and manage your Firestore database, refer to the official Firestore documentation.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

[python-telegram-bot][https://github.com/python-telegram-bot/python-telegram-bot] - A Python wrapper for the Telegram Bot API.
[firebase-admin][https://github.com/firebase/firebase-admin-python] - Firebase Admin SDK for Python.
[python-telegram-bot-template][https://github.com/jansenicus/python-telegram-bot-template] - Modular python-telegram-bot template.

Feel free to customize the structure according to your specific project needs. Make sure to include the necessary installation and setup instructions, as well as any relevant information for contributors or users of your Telegram bot.
