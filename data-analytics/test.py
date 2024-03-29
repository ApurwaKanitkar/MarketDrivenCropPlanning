from flask import Flask, send_file
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import plot 

app = Flask(__name__)

@app.route('/plot')
def serve_plot():
    # Replace with your actual data
    data1 = {"Year": [2008, 2011, 2012], "RICE AREA (1000 ha)": [10, 12, 15]}

    fig = plot.create_plot(data1)
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)