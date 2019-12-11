## Importing Flask as fl
from flask import Flask as fl
from flask import render_template

# This section runs the Main application 
app = fl(__name__)

## Gives working directory for webpage
@app.route('/')
def hello():
    return render_template('app/frontend/Home.html')

    if __name__ == '__main__': 
        app.run()