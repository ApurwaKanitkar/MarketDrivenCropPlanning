from flask import Flask, send_file
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import plot 

app = Flask(__name__)

@app.route('/plot/<int:year>')
def serve_plot():
    # Replace with your actual data
    data1 = {"Year": [2010, 2011, 2012], "RICE AREA (1000 ha)": [10, 12, 15]}
    fig1 = plot.create_plot1(data1)

    data2 = {"Year": [2010, 2011, 2012], "RICE PRODUCTION (1000 tons)": [600, 100, 1200], "WHEAT PRODUCTION (1000 tons)": [100, 1000, 1200],"MAIZE PRODUCTION (1000 tons)": [500, 1000, 1200]}
    fig2 = plot.create_plot2(data2)

    img = BytesIO()
    # fig1.savefig(img, format='png')
    fig2.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)