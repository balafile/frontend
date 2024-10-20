from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
