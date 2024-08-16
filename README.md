# Online Shop

## Description

Online Shop is an object-oriented program that represents a core for an online store. Though it does not provide 
payment services, it can still be used as a basic for a website to a Telegram bot.

## Installation

1. Clone the repository:
```
git clone https://github.com/obladishka/online_shop.git
```
2. Install project dependencies:
```commandline
poetry intall
```

## Testing

The code is 97% covered by Pytest unit tests. To run it write the following commands in your terminal:
```
poetry add --group dev pytest # install pytest in the application's virtual environment
pytest # run the tests
```
A detailed coverage report can be found in the *index.html* file in the *htmlcov* folder after running the command:
```commandline
pytest --cov=src --cov-report=html
```
in the terminal.