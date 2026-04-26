# AI Career Guidance Chatbot

## Overview
AI-powered Career Guidance Chatbot built using Flask and OpenAI API that provides personalized career recommendations based on a student's education, goals, and future plans.

## Features
- Personalized career guidance
- Suggests career/education paths
- Recommends skills to build
- Suggests courses and certifications
- AI-generated long-term advice
- Simple and user-friendly web interface

## Tech Stack
- Python
- Flask
- OpenAI API
- HTML/CSS
- Jinja Templates

## Project Structure
```bash
career_chatbot_web/
│── app.py
│── config.py
│── templates/
│   ├── index.html
│   └── result.html
```

## Installation

### Clone Repository
```bash
git clone https://github.com/your-username/career-guidance-chatbot.git
cd career-guidance-chatbot
```

## Create Virtual Environment
```bash
python -m venv venv
```

Activate it:

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

## Install Dependencies
```bash
pip install flask openai
```

Or using requirements.txt:
```bash
pip install -r requirements.txt
```

## Set API Key
In `config.py` add your OpenAI API key:

```python
OPENAI_API_KEY="your_api_key_here"
```

## Run Project
```bash
python app.py
```

Open browser:
```bash
http://127.0.0.1:5000/
```

## How It Works
1. Enter:
- Name
- Education
- Career Goal
- Future Plans

2. AI analyzes input.

3. Chatbot provides:
- Career options
- Skills to develop
- Recommended certifications
- Long-term guidance

## Example Use Cases
- Students choosing higher studies
- Freshers looking for jobs
- Career switch guidance
- Skill roadmap suggestions

## Future Improvements
- Resume analyzer
- Interview preparation module
- Course recommendation engine
- Career roadmap visualization

## Requirements
Create `requirements.txt`

```txt
flask
openai
```

## Author
Nishant
