from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt
import mpld3
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(f"Current working directory: {os.getcwd()}")
    if request.method == 'POST':
        # Get user input data from the form
        user_data = request.form['user_data']
        # Perform data analysis based on user input
        data = analyze_data(user_data)
        # Generate visualization
        fig, ax = plt.subplots()
        ax.plot(data)
        # Convert the visualization to HTML
        visualization_html = mpld3.fig_to_html(fig)
    else:
        visualization_html = None

    return render_template('index.html', visualization=visualization_html)

def analyze_data(user_data):
    # Perform data analysis based on user input
    # Example: Split the user input by commas and convert to integers
    data = [int(x) for x in user_data.split(',')]
    return data

if __name__ == '__main__':
    app.run(debug=True)