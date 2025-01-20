from flask import Flask, render_template
import random

# Create a Flask app instance
app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def home():
    # Generate a list of 10 random numbers (or any other count you prefer)
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    return render_template('index2.html', random_numbers=random_numbers)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
