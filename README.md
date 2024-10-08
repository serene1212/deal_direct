# DealDirect

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)

![Django](https://img.shields.io/badge/Django-5%2B-brightgreen)

![Django REST Framework](https://img.shields.io/badge/DRF-API_Framework-green)

![Django Channels](https://img.shields.io/badge/Django_Channels-WebSockets-brightgreen)

![Redis](https://img.shields.io/badge/Redis-Caching-red)

![RabbitMQ](https://img.shields.io/badge/RabbitMQ-Broker-orange)

![Celery](https://img.shields.io/badge/Celery-Queue-green)

![Docker](https://img.shields.io/badge/Docker-Ready-blue)

![SQLite](https://img.shields.io/badge/SQLite-Development-lightgrey)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Production-blue)

![HTML](https://img.shields.io/badge/HTML-Email_Templates-orange)

![Pytest](https://img.shields.io/badge/Pytest-Testing-yellow)

![Swagger UI](https://img.shields.io/badge/Swagger-Interactive_API_Docs-brightgreen)

![Redoc](https://img.shields.io/badge/Redoc-API_Docs-red)

![Black](https://img.shields.io/badge/Black-Code_Formatting-black)

![License](https://img.shields.io/badge/License-MIT-yellow)

***------------------------------------------------***

## Table of Contents

- [Endpoints](#endpoints)
- [ERD](#erd)
- [API Documentation](#api-documentation)
- [Code Formatting](#code-formatting)
    - [Pre-commit Hooks](#pre-commit-hooks)
- [Usage](#usage)
    - [Using Docker](#using-docker)
- [Chat Feature](#chat-feature)

- [Testing](#testing)

***------------------------------------------------***

## Endpoints

To see the current endpoints, run the following command:

```bash
python manage.py stdout_endpoints > ENDPOINTS.md
```

***------------------------------------------------***

## API Documentation

The API documentation is available in two formats:

- **Swagger UI**: Provides an interactive API documentation interface.
    - URL: `http://127.0.0.1:8000/api/schema/swagger-ui/`

- **Redoc**: Provides a more detailed and customizable API documentation interface.
    - URL: `http://127.0.0.1:8000/api/schema/redoc/`

***------------------------------------------------***

## ERD

checkout the diagram at:

- [ERD](documents/Entity%20Relationship%20Diagram.jpg)

***------------------------------------------------***

## Code Formatting

This project uses `black` for code formatting. Black is a code formatter for Python that ensures consistent code style.

### Pre-commit Hooks

Pre-commit hooks are used to ensure code quality before committing changes. This project uses the following pre-commit
hooks:

- check-yaml: Checks YAML files for syntax errors.


- end-of-file-fixer: Ensures files end with a newline.


- trailing-whitespace: Removes trailing whitespace.


- black: Formats Python code using black.

To install the pre-commit hooks, run:

```bash
pre-commit install
```

to run the pre-commit hooks manually, use:

```bash
pre-commit run --all-files
```

***------------------------------------------------***

## Usage

1. Clone the repository:

```bash
git clone git@github.com:serene1212/porsojo.git
```

2. Navigate to the project directory:

```bash
cd deal_direct
```

3. Install the required packages:

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

4. Copy sample.env and change variables:

```bash
cp sample.env .env
```

5. Run the server:

```bash
python manage.py runserver
```

### Using Docker

To build and run the Docker containers, use the following commands:

```bash
docker-compose up --build
```

This will start all the necessary services defined in the `docker-compose.yml` file.

For more details, refer to the [Dockerfile](Dockerfile) in the project repository.
***------------------------------------------------***

## Chat Feature

You can start real time chat for a product with the seller of the product.

### How to Use the Chat

1. **Run the Django Development Server**:
   ```sh
   python manage.py runserver
2. Access the Chat Room:
    - Open a web browser and navigate to http://localhost:8000/chat/<room_name>/, replacing <room_name> with the desired
      chat room name.


3. Start Chatting:
    - Type a message in the input box and press "Send" or hit the Enter key to send the message.
      Messages will appear in the chat log.


4. Permissions:
    - The IsParticipant permission class ensures that only authenticated users who are participants of the chat room can
      access the chat.

## Testing

This project aims to achieve over 95% test coverage.

All tests are written using **`pytest`**.

To run the tests and see the coverage report, use the following command:

```bash
pytest --cov --cov-config=.coveragerc
```

**this command will exclude **`custom_commands`** directory from testing**
