from flask import Flask, render_template
import random

# Create a Flask app instance
app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def home():
    # Generate a random number
    random_number = random.randint(1, 100)
    return render_template('index.html', random_number=random_number)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
