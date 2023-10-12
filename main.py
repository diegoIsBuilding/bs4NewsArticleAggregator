from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    #Load processed JSON file data for the first source
    with open('data/processed/source_one.json') as file:
        source_one_articles = json.load(file)

    #Load processed JSON file data for the second source
    with open ('data/processed/source_two.json') as file:
        source_two_articles = json.load(file)
        
    #Load processed JSON file data for the third source
    with open ('data/processed/source_three.json') as file:
        source_three_articles = json.load(file)
        
    #Now this data is able to be passed into the html template
    return render_template('index.html', 
    source_one = source_one_articles, 
    source_two = source_two_articles, 
    source_three = source_three_articles)
    
if __name__ == '__main__':
    app.run(debug=True)