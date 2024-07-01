# Django Visitor Greeting API

This is a basic Django project that sets up a web server to expose an basic API endpoint which greets a visitor by name and also returns the client's IP address and a default location.

## Features

- **GET <domain_name>/api/hello/?visitor_name=themy**: Accepts a `visitor-name` query parameter and responds with a greeting, the client's IP address, and a default location.

## Requirements

- Python 3.x
- Django 3.x or later

## Installation

 **Clone the repository and setup:**
   ```sh
   git clone https://github.com/Popthemy/ApiGreet.git
   cd ApiGreet
   pipenv install : install dependencies
   pipenv shell  : activate virtual environment


Example of response
JSON
{
  "client_ip": "127.0.0.1",
  "location": "New York",
  "greeting": "Hello, themy!"
}

