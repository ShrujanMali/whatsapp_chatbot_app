# AI Chatbot on WhatsApp with Python, Twilio, and Gemini API


## Description

• Developed a WhatsApp chatbot that answers real-time queries using Google Gemini 2.0 Flash. Integrated Twilio API to enable two-way communication over WhatsApp. Built a FastAPI backend to handle requests efficiently and return AI-generated responses.Ensured scalability and performance optimization for handling multiple queries.

## Technologies used
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,fastapi,postgresql,gcp,git" />
  </a>
</p>

## Installation and Setup

1. Clone the repository:

        git clone https://github.com/ShrujanMali/whatsapp_chatbot_app

2. Navigate to the project directory:

        cd whatsapp_chatbot_app

3. Create and activate virtual environment

       >>> python -m venv <virtual_env_name>
       >>> env/Scripts/activate

4. Install the required libraries:

       >>> pip install -r requirements.txt

## How to get Gemini API
1. Go to Google cloud >> https://console.cloud.google.com/cloud-resource-manager?invt=Abtaog
2. And create new project
3. Then visit https://aistudio.google.com/prompts/new_chat
4. Click on "Get API click" and then select "create API key"
5. Select your project from the drop down after clicking on "create API key"
6. Copy and store into .env file.

You can use ChatGPT API also.

## How to Get Twilio API key for What'sAPP use
1. Visit to https://console.twilio.com/
2. Then left hand side select "Develop" option and then select "messaging" >> "Send a Whatsapp Message"
3. Then Scan the QR code using your What'sApp application and type "join bow-brain" and send
4. Then copy this following deatils from twilio and store into .env file
   i) TWILIO_ACCOUNT_SID = "<account_sid>"
   ii) TWILIO_AUTH_TOKEN = "<auth_token>"
   iii) TWILIO_NUMBER = "<Twilio_phone_number>"
