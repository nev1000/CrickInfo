# CricFix

CricFix is a web application for viewing cricket game information using the Ultimate Cricket Data API.

## Features
- View upcoming and past cricket games

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/nev1000/CricFix.git
   cd CricFix
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get an API Key**
   - Sign up for an account at [Ultimate Cricket Data API](https://ultimatecricketdata.com/) to obtain your API key.
   - After signing up, you will receive an API key. Add this key directly in your code as the value for 'API_KEY'.

4. **Run the application**
   ```bash
   flask run
   ```

## Configuration

- Make sure to set your API key in the application before making requests to the Ultimate Cricket Data API.
- Example (in `views.py`):
  ```python
  API_KEY = "your_api_key_here"
  ```

