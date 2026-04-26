from flask import Flask, render_template, request
from openai import OpenAI
import config 

app = Flask(__name__)
client = OpenAI(api_key=config.OPENAI_API_KEY)

def generate_career_guidance(name, education, path_choice, plans):
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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=600
    )

    return response.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        education = request.form['education']
        path_choice = request.form['path_choice']
        plans = request.form.get('plans', '')

        result = generate_career_guidance(name, education, path_choice, plans)
        return render_template('result.html', result=result, name=name)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)