# Python Telegram Ledgerbot

This bot has been developped to allow users to keep track of expenses in a telegram groupchat.
Forked from jansenicus [python-telegram-bot-template](https://github.com/jansenicus/python-telegram-bot-template)

![Ledgerbot](/assets/ledgerbot.png?raw=true "Ledgerbot")

## Features

- ### Split an expenses with another user

- ### Split an expenses with every other users

- ### Refund a single user

- ### Display the value owed to every other users


## _Easy configuration_ with a yaml file
`configuration.yaml`
```yaml
prod:
  - botname: My Production Bot
    username: my_production_bot
    token: 
      1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi
    about:
      "this is some short text about my bot"
    description:
      "This is a description of what my bot can do which customer will use"
```

## _Clear separation between Development Bot vs Production Bot_ 
`configuration.yaml`
```yaml
dev:
  - botname: Development Bot
    username: my_development_bot
    token: 
      1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi
    about:
      "this is some short text about development bot  "
    description:
      "This is a description of what my development bot can do with testing"
```
choose the mode
```yaml
mode: dev
```
or 
```yaml
mode: prod
```
## _Simplicity and sophistication met in one place_

  - `handlers` directory: as a placeholder for all command handlers  
  - `index.py` file: to register all the function members

## _Ready to deploy_ as a docker container
Just run
```bash

docker-compose up --build

```

# Steps 
  ## 1. Preparation
  - prepare two bot accounts from [@botfather](https:///t.me/botfather)
  - one bot will be used for development 
  - another bot for production
  
  ## 2. Clone This Repository
  ```bash

    git clone https://github.com/felixatschool/telegram-ledgerbot


  ```
  ## 3. Edit configuration file
  - edit `configuration-sample.yaml` and save it as `configuration.yaml`
   ```yaml
mode: prod
prod:
  - botname: My Production Bot
    username: my_production_bot
    token: 
      1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi
    about:
      "this is some short text about my bot"
    description:
      "This is a description of what my bot can do which customer will use"

```

  ## 4. Run Directly in local machine

  Make sure you are in the `bot` directory to install all the requirements and then run the telegram bot
  ```bash

    cd bot
    pipenv install -r requirements.txt
    pipenv run python main.py

  ```

  ## 5. Build and Run Docker container as a Service
  ### Build Docker container
  ```bash

      docker build -t telegram-ledgerbot -f Dockerfile .

  ```

  ### Run Docker container as a Service
  ```bash

      docker run -it --workdir /home telegram-ledgerbot pipenv run python main.py

  ```
  ### Build and run in one go
  You could also build and run in one go for the first time
  ```bash

      docker-compose up -d

  ```
  or you could also force build every you want to apply change into the image
  ```bash

      docker-compose up -d --build

  ```
