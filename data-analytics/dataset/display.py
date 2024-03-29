from flask import Flask, send_file
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import plot 

app = Flask(__name__)

@app.route('/plot')
def serve_plot():
  data1 = pd.read_csv('Cleaned_dataset.csv')
  data2 = pd.read_csv('render1.csv')
  df = data1.to_dict()
  access_df = data2.to_dict()