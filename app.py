from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Define business vision and mission
@app.route('/define', methods=['POST'])
@app.route('/define', methods=['POST'])
def define():
    # Previous fields (Vision, Mission, SWOT)
    vision = request.form['vision']
    mission = request.form['mission']
    strengths = request.form['strengths']
    weaknesses = request.form['weaknesses']
    opportunities = request.form['opportunities']
    threats = request.form['threats']

    # SMART Goals
    specific = request.form['specific']
    measurable = request.form['measurable']
    achievable = request.form['achievable']
    relevant = request.form['relevant']
    timebound = request.form['timebound']

    return (f"<h2>Your Business Vision:</h2><p>{vision}</p>"
            f"<h2>Your Business Mission:</h2><p>{mission}</p>"
            f"<h2>SWOT Analysis</h2>"
            f"<h3>Strengths:</h3><p>{strengths}</p>"
            f"<h3>Weaknesses:</h3><p>{weaknesses}</p>"
            f"<h3>Opportunities:</h3><p>{opportunities}</p>"
            f"<h3>Threats:</h3><p>{threats}</p>"
            f"<h2>SMART Goals</h2>"
            f"<h3>Specific:</h3><p>{specific}</p>"
            f"<h3>Measurable:</h3><p>{measurable}</p>"
            f"<h3>Achievable:</h3><p>{achievable}</p>"
            f"<h3>Relevant:</h3><p>{relevant}</p>"
            f"<h3>Time-bound:</h3><p>{timebound}</p>")

if __name__ == '__main__':
    app.run(debug=True)
