import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify
import io
import base64

app = Flask(__name__)

df = pd.read_csv('C:\\Users\\ajitk\\Documents\\Apurwa\\PICT\\ExtraCoCurricular\\Tech\\TechFiesta\\MarketDrivenCropPlanning\\data-analytics\\dataset\\Cleaned_dataset.csv')
access_df = pd.read_csv('C:\\Users\\ajitk\\Documents\\Apurwa\\PICT\\ExtraCoCurricular\\Tech\\TechFiesta\\MarketDrivenCropPlanning\\data-analytics\\dataset\\render1.csv')

def give_final(dist):
    global combo1crop1, combo1crop2, combo2crop1, combo2crop2
    combo1crop1 = access_df.loc[access_df["District"] == dist, "Combination_1_Crop_1"].values[0]
    combo1crop2 = access_df.loc[access_df["District"] == dist, "Combination_1_Crop_2"].values[0]
    combo2crop1 = access_df.loc[access_df["District"] == dist, "Combination_2_Crop_1"].values[0]
    combo2crop2 = access_df.loc[access_df["District"] == dist, "Combination_2_Crop_2"].values[0]
    print("The top 2 crop combinations for",dist,"are:")
    print("Combination 1:",combo1crop1,"&",combo1crop2)
    print("Combination 2:",combo2crop1,"&",combo2crop2)
    return combo1crop1, combo1crop2, combo2crop1, combo2crop2


def yield_kg(combo1crop1, combo1crop2, combo2crop1, combo2crop2):
    dist_df = df[df['Dist Name'] == dist]
    yield1 = combo1crop1 + ' YIELD (Kg per ha)'
    yield2 = combo1crop2 + ' YIELD (Kg per ha)'
    yield3 = combo2crop1 + ' YIELD (Kg per ha)'
    yield4 = combo2crop2 + ' YIELD (Kg per ha)'

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 2))

    ax1.plot(dist_df['Year'], dist_df[yield1], marker='o', linestyle='-', color='g', label=yield1)
    ax1.plot(dist_df['Year'], dist_df[yield2], marker='o', linestyle='-', color='y', label=yield2)
    ax1.set_title('Yield over time for Crop Combination 1')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Yield (Kg per ha)')
    ax1.grid(True)
    ax1.legend()

    ax2.plot(dist_df['Year'], dist_df[yield3], marker='o', linestyle='-', color='b', label=yield3)
    ax2.plot(dist_df['Year'], dist_df[yield4], marker='o', linestyle='-', color='xkcd:sky blue', label=yield4)
    ax2.set_title('Yield over time for Crop Combination 2')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Yield (Kg per ha)')
    ax2.grid(True)
    ax2.legend()

    plt.subplots_adjust(left=0.12, right=0.9, top=0.9, bottom=0.1)
    plt.show()
yield_kg(combo1crop1, combo1crop2, combo2crop1, combo2crop2)

def price(combo1crop1, combo1crop2, combo2crop1, combo2crop2):
    dist_df = df[df['Dist Name'] == dist]
    price1 = combo1crop1 + ' HARVEST PRICE (Rs per Quintal)'
    price2 = combo1crop2 + ' HARVEST PRICE (Rs per Quintal)'
    price3 = combo2crop1 + ' HARVEST PRICE (Rs per Quintal)'
    price4 = combo2crop2 + ' HARVEST PRICE (Rs per Quintal)'

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 3))

    ax1.plot(dist_df['Year'], dist_df[price1], marker='o', linestyle='-', color='g', label=price1)
    ax1.plot(dist_df['Year'], dist_df[price2], marker='o', linestyle='-', color='y', label=price2)
    ax1.set_title('Price over time for Crop Combination 1')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Price (Rs per Quintal)')
    ax1.grid(True)
    ax1.legend()

    ax2.plot(dist_df['Year'], dist_df[price3], marker='o', linestyle='-', color='b', label=price3)
    ax2.plot(dist_df['Year'], dist_df[price4], marker='o', linestyle='-', color='xkcd:sky blue', label=price4)
    ax2.set_title('Price over time for Crop Combination 2')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Price (Rs per Quintal)')
    ax2.grid(True)
    ax2.legend()

    plt.subplots_adjust(left=0.12, right=0.9, top=0.9, bottom=0.1)
    plt.show()
price(combo1crop1, combo1crop2, combo2crop1, combo2crop2)


@app.route('/api/crop-analysis', methods=['POST'])
def crop_analysis():
    district = request.json.get('district')
    if not district:
        return jsonify({'error': 'Distric is required'}), 400
    combo1crop1, combo1crop2, combo2crop1, combo2crop2 = give_final(district)

    # Generate yield plot
    img_data = io.BytesIO()
    yield_img = yield_kg(combo1crop1, combo1crop2, combo2crop1, combo2crop2)
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    yield_img_base64 = base64.b64encode(img_data.getvalue()).decode('utf-8')

    # Generate price plot
    img_data = io.BytesIO()
    price_img = price(combo1crop1, combo1crop2, combo2crop1, combo2crop2)
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    price_img_base64 = base64.b64encode(img_data.getvalue()).decode('utf-8')

    return jsonify({'yield_img': yield_img_base64, 'price_img': price_img_base64})

if __name__ == '__main__':
    app.run(debug=True)