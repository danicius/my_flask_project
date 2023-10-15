# SALVE AI
Project: Multilingual Chatbot for Service Plans
Overview:

This project is a multilingual chatbot designed to assist users with information about service plans, specifically tailored for Verizon. The chatbot is built using Flask for the backend and integrates Google Cloud's Dialogflow and Vertex AI for natural language processing and understanding. The chatbot is capable of understanding and responding in both English and Spanish.

Features:

Speech-to-Text Integration: Users can communicate with the chatbot using voice inputs. The system transcribes the voice input into text using Google Cloud's Speech-to-Text API.
Language Detection: The chatbot automatically detects the language of the user's input, ensuring a seamless experience for both English and Spanish-speaking users.
Intuitive UI: An interactive chatbox UI with voice input capabilities.
Rich Responses: The chatbot can provide detailed answers, including cards and quick replies using Dialogflow's rich response capabilities.
Integration with Verizon Data: Through Vertex AI and Dialogflow, the chatbot provides accurate information about Verizon's service plans and billing options.
Future Improvements:

Extend support for more languages.
Improve the accuracy and richness of responses by integrating with more data sources and refining the training data.
Add features like account management, bill payments, and real-time support.

Setting Up a Virtual Environment

A virtual environment helps isolate your project's dependencies. To create a virtual environment, follow these steps:

    Open Terminal/Command Prompt:

    Open your terminal or command prompt.

    Navigate to Your Project Directory:

    Use the cd command to navigate to your project's directory.

    bash

cd /path/to/your/project

Create a Virtual Environment:

Run the following command to create a virtual environment.

bash

python -m venv venv

Replace venv with the name you prefer for your virtual environment.

Activate the Virtual Environment:

On Windows:

bash

venv\Scripts\activate

On macOS and Linux:

bash

source venv/bin/activate

You should see the virtual environment name in your terminal prompt, indicating that the virtual environment is active.

Install Dependencies:

Within your virtual environment, use pip to install the required packages from your requirements.txt file.

bash

    pip install -r requirements.txt

Running the Application

With your virtual environment set up, you're ready to run the Flask application. Follow these steps:

    Set Flask App Variable:

    Ensure that the FLASK_APP environment variable points to your main application file (usually app.py or a filename you've chosen).

    bash

export FLASK_APP=app.py

Set Flask Environment:

Set the Flask environment to development for debugging and automatic reloading.

bash

export FLASK_ENV=development

Run the Application:

Start the Flask application.

bash

flask run

You should see output indicating that the application is running locally. Visit the provided URL in your web browser to access the application.
