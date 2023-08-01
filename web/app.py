from flask import Flask, render_template, request
from scripts.ask_gpt import complete_table

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/project_table", methods=['GET',"POST"])
def create_table():
    if request.method =="POST":
        text = request.form.get('jobOfferText')
        table = complete_table(text)
        
        return render_template("table.html", text=table)

# python .\app.py
if __name__ == '__main__':
    app.run(debug=True, port=8000)