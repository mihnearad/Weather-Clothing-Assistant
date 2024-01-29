# Weather-Driven Outfit Assistant

## Overview

This Python project leverages the OpenWeatherMap API and OpenAI's GPT-3.5 model to provide personalized clothing recommendations based on the current weather conditions. The script fetches weather data, utilizes GPT-3.5 for outfit suggestions, and sends the consolidated advice via email.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- OpenAI Python library (`openai`)
- Requests library (`requests`)
- Python's built-in `subprocess`, `sys`, `ssl`, and `smtplib` libraries
- `dotenv` for handling environment variables

## Setup

1. **Clone the repository:**
   - Clone the repository: `git clone https://github.com/your-username/Weather-Outfit-Assistant.git`

2. **Navigate to the project directory:**
   - Navigate to the project directory: `cd Weather-Outfit-Assistant`

3. **Create a virtual environment (optional but recommended):**
   - Create a virtual environment: `python -m venv venv`

4. **Activate the virtual environment:**
   - For Windows: `venv\Scripts\activate`
   - For macOS/Linux: `source venv/bin/activate`

5. **Install additional dependencies:**
   - Install dependencies: `pip install -r requirements.txt`

6. **Create a `.env` file in the project root and add your API keys and email credentials:**
   - Add API keys and credentials to `.env`:
     ```
     OPENWEATHER_API_KEY=your_openweather_api_key
     OPENAI_API_KEY=your_openai_api_key
     GMAIL_USER=your_gmail_user
     GMAIL_PASS=your_gmail_password
     TO_EMAIL=recipient_email_address
     ```

## Usage

Run the main script:

- Run the main script: `python main.py`

The script will fetch current weather information, query GPT-3.5 for outfit suggestions, and send the consolidated advice to the specified email address.

## Contributing

Feel free to contribute to the project by opening issues or creating pull requests. We welcome suggestions, bug reports, and enhancements!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your needs.
