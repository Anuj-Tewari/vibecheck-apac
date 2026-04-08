import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- THE TOOLS ---
def calculate_vibe_score(text):
    score = 0
    text = text.lower()
    # Keywords
    pos = ["lit", "fire", "slay", "best", "mantap", "lodi", "jugaad"]
    neg = ["mid", "capped", "toxic", "worst", "fail", "boring"]
    
    for word in pos:
        if word in text: score += 5  # Increased weight so score jumps high!
    for word in neg:
        if word in text: score -= 5
        
    return f"Analytical Vibe Score: {score}/10"

def get_apac_context(country):
    data = {
        "India": "Use 'Jugaad' for clever hacks; 'Namaste' for respect.",
        "Indonesia": "'Mantap' means awesome; 'Santuy' means relax.",
        "Philippines": "'Lodi' means idol; 'Petmalu' means amazing."
    }
    return data.get(country, "General APAC etiquette: High respect for community.")

# --- THE AGENT ENDPOINT ---
@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify({"status": "VibeCheck Agent is Online", "track": "APAC Track 1"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("text", "")
    country = data.get("country", "General")
    
    # Simulate Agentic Reasoning
    score_result = calculate_vibe_score(user_input)
    context_result = get_apac_context(country)
    
    return jsonify({
        "agent_response": f"I've analyzed the vibe: {score_result}",
        "cultural_note": context_result,
        "model": "gemini-1.5-flash-integrated"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
