# Index

- [About](#telegram-bot-manager)
- [Installation](#installation)
- [Installation via Docker](#installation-via-docker)
- [Contributing](#contributing)
- [License](#license)


## Telegram Bot Manager

Telegram Bot Manager is a Python project designed to simplify the management of multiple Telegram bots.
This project allows you to run, monitor, and control several Telegram bots from a centralized platform,
making it easier to manage various tasks and interactions across multiple chat groups or channels.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Jaldsky/TelegramBotManager.git

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv

3. Activate the virtual environment (recommended):
   ```bash
   venv\Scripts\activate

4. Install the project dependencies from the requirements.txt file:
    ```bash
    pip install -r requirements.txt

5. Fill sensitive data at *app/config.ini*
6. Start the Telegram Bot Manager:
    ```bash
    python main.py

## Installation via Docker
1. docker pull jaldsky/tbm
2. mkdir tbm && cd tbm
3. vim config.ini *(Add sensitive data like tokens, trusted users etc., filling template you can find here app/config.ini)*
4. docker run -d jaldsky/tbm bash -c "python3 main.py"

## Contributing
We welcome contributions to this project. Feel free to fork the repository,
make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.
