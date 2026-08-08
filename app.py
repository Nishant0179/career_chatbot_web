from flask import Flask, render_template, request
from google import genai
import os

app = Flask(__name__)

# Fetch Gemini API Key from environment variable or config.py
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    try:
        import config
        GEMINI_API_KEY = getattr(config, 'GEMINI_API_KEY', getattr(config, 'OPENAI_API_KEY', ''))
    except ImportError:
        GEMINI_API_KEY = ''

def generate_career_guidance(name, education, path_choice, plans):
    api_key = os.environ.get("GEMINI_API_KEY", GEMINI_API_KEY)
    if not api_key:
        return "⚠️ Error: GEMINI_API_KEY is not set. Please set the GEMINI_API_KEY environment variable in Render."

    prompt = f"""
You are a friendly career counselor AI. A student named {name} has the following background:

- Highest Education: {education}
- Next Step: {path_choice}
- Future Plans: {plans}

Provide:
1. Three personalized career or education options
2. Skills they should build
3. Recommended courses or certifications
4. Long-term advice to help them grow

Tailor the suggestions based on whether they want to get a job or continue education. Use a friendly and helpful tone.
"""

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Error generating guidance: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form.get('phone', '')
        education = request.form['education']
        path_choice = request.form['path_choice']
        plans = request.form.get('plans', '')

        result = generate_career_guidance(name, education, path_choice, plans)
        return render_template('result.html', result=result, name=name)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)