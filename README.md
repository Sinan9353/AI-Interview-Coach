# AI Interview Coach

AI Interview Coach is a Django-based web application that uses Large Language Models (LLMs) to generate personalized interview questions from uploaded resumes. The system analyzes resume content and creates role-specific interview questions using AI.


## Features

- Upload Resume PDF
- Extract text from resumes
- Generate AI-based interview questions
- Role-specific question generation
- Modern responsive UI
- Simple and user-friendly interface


## Technologies Used

### Frontend
- HTML
- CSS
- Bootstrap

### Backend
- Django

### AI Integration
- OpenAI API / Google Gemini API

### Libraries
- PyPDF2


## Project Workflow

1. User uploads a resume PDF
2. Resume text is extracted using PyPDF2
3. Resume content is sent to the LLM API
4. AI analyzes the resume
5. Personalized interview questions are generated
6. Questions are displayed on the frontend

---

## System Architecture
text
User Uploads Resume
        ↓
PDF Text Extraction
        ↓
Django Backend
        ↓
LLM API (OpenAI/Gemini)
        ↓
AI Generates Questions
        ↓
Display Results
