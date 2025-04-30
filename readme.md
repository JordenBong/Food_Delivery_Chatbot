# Mira - The ChatBot for Food Delivery System

## 📌 Overview
Mira is an AI-powered chatbot designed for a Food Delivery System, built using Google DialogFlow. It assists users in placing food orders and tracking deliveries through natural language interactions. 

## ✨ Features
- Order Placement: Users can order food via conversational commands.

- Order Tracking: Real-time updates on delivery status.

## 🛠️ Technologies Used
- DialogFlow: For NLP, Intent and Context Recognition
- Python: Backend fulfillment
- MySQL: Database
- Webhook Integration: FastAPI
- HTML / CSS: Simple Web Design
- NGROK: For https tunneling

## 📂 Project Structure
  Food-Delivery-Chatbot/
  mira-chatbot/  
  ├── backend/              # FastAPI Python backend  
  │   ├── main.py           # API routes 
  │   ├── db_helper.py      * Connection to MySQL DB
  │   ├── generic_helper.py * Some common generic functions
  │   └── requirements.txt  # Dependencies  
  ├── db/                   # Database(.sql)  
  ├── dialogflow_assets/    # DialogFlow config & guidelines  
  ├── frontend/             # Static web files (HTML/CSS/Images)  
  └── README.md             
  

## 📚 Attribution & Credits
This project was developed as part of the Codebasics learning program. Special thanks to the Codebasics team for their guidance and resources. 

**Refer:** 
[End-to-End NLP Project | Build a Chatbot in Dialogflow | NLP Tutorial | S3 E2](https://www.youtube.com/watch?v=2e5pQqBvGco&list=PLeo1K3hjS3uuvuAXhYjV2lMEShq2UYSwX&index=27)



