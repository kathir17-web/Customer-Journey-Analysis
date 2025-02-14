from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Load the dataset
def load_data():
    csv_file = 'customer_journey_data.csv'
    return pd.read_csv(csv_file)

@app.route('/')
def index():
    # Load data
    data = load_data()

    # Visualization 1: Income vs Average Spending
    fig1 = px.scatter(
        data,
        x="Income",
        y="Avg_Spending",
        title="Income vs Average Spending",
        labels={"Income": "Income", "Avg_Spending": "Average Spending"}
    )
    chart1 = pio.to_html(fig1, full_html=False)

    # Visualization 2: Purchase Frequency by Location
    location_freq = data.groupby("Location")["Purchase_Frequency"].sum().reset_index()
    fig2 = px.bar(
        location_freq,
        x="Location",
        y="Purchase_Frequency",
        title="Purchase Frequency by Location",
        labels={"Location": "Location", "Purchase_Frequency": "Total Purchase Frequency"}
    )
    chart2 = pio.to_html(fig2, full_html=False)

    # Pass the charts to the template
    return render_template('index.html', chart1=chart1, chart2=chart2)

if __name__ == '__main__':
    app.run(debug=True)