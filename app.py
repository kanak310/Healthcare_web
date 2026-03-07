from flask import Flask , render_template , request , redirect , url_for, jsonify , session
from dotenv import load_dotenv
import os 
from google import genai
load_dotenv()

app = Flask(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
#print("API KEY:",GOOGLE_API_KEY)
client = genai.Client(api_key=GOOGLE_API_KEY)


app.secret_key = "your_secret_key"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tips', methods=['GET', 'POST'])
def tips():
    if request.method == 'POST':
        return redirect(url_for('result'))
    return render_template('tips.html')


@app.route('/chatbot', methods=['GET','POST'])
def chatbot():
    if request.method == 'POST':
        pass
    return render_template('chatbot.html')

@app.route('/about',methods=['GET','POST'])
def about():
    if request.method=='POST':
        pass
    return render_template('about.html')
@app.route('/ask',methods=['POST'])
def ask():
    try:
        data = request.get_json()
        user_input = data.get("question")
        prompt = f"""
        You are a health assistant.

        Rules:
        - Do NOT use markdown
        - Do NOT use ** or headings
        - Keep the answer short and clear
        - Use simple bullet points with hyphens (-)
        - Max 15-20 lines
        - Do NOT give medical diagnosis
        - End with a short disclaimer

        User symptoms:
       {user_input}
       """


        if not user_input:
            return jsonify({"error": "Question is required"}), 400

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        answer = response.text or "No response generated."

        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
  
     
 

    
if __name__ == "__main__":
    app.run(debug=True)

    