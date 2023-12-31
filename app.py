from flask import Flask, request, render_template, jsonify
import os
from google.cloud import speech_v1 as speech
from google.cloud import dialogflow
from google.cloud.dialogflow_v2 import SessionsClient
from google.cloud.dialogflow_v2.types import TextInput, QueryInput
from langdetect import detect




app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS_DIALOGFLOW"] = "response_dialog.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS_SPEECH"] = "sa_speech.json"

DIALOGFLOW_CREDENTIALS = "response_dialog.json"
SPEECH_TO_TEXT_CREDENTIALS = "sa_speech.json"

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    
    # Set environment variable for Dialogflow
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = DIALOGFLOW_CREDENTIALS
    
    # Get response from Dialogflow
    bot_response = get_dialogflow_response(user_message)
    
    return jsonify({'message': bot_response})

# def get_dialogflow_response(text):
#     project_id = "multilangproject"
#     session_id = "test_session"  # This should be unique for each user or session
    
#     session_client = SessionsClient()
#     session = session_client.session_path(project_id, session_id)
    
#     #i want english and spanish
#     detected_language = detect(text)
#     if detected_language == "es":
#         text_input = TextInput(text=text, language_code="es")
#     else:
#         text_input = TextInput(text=text, language_code="en")
        
#     query_input = QueryInput(text=text_input)

#     response = session_client.detect_intent(session=session, query_input=query_input)

#     return response.query_result.fulfillment_text

def get_dialogflow_response(text):
    project_id = "multilangproject"
    session_id = "test_session"  # This should be unique for each user or session
    
    session_client = SessionsClient()
    session = session_client.session_path(project_id, session_id)

    # Detect the language of the text
    detected_language = detect(text)

    # Default to English
    language_code = 'en-US'
    
    # If detected Spanish, change the language_code
    if detected_language == 'es':
        language_code = 'es'

    text_input = TextInput(text=text, language_code=language_code)
    query_input = QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    print(f"Detected language: {detected_language}")
    print(f"Language code: {language_code}")

    return response.query_result.fulfillment_text
@app.route('/')
def home():
     return render_template("home.html")
@app.route('/i')
def index():
    return render_template("index.html")


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Set environment variable for Google Cloud Speech-to-Text
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SPEECH_TO_TEXT_CREDENTIALS

    client = speech.SpeechClient()
    
    audio_data = request.data
    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio)
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return jsonify({'transcript': transcript}
)

if __name__ == '__main__':
    app.run(debug=True)
