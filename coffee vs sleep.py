import plotly.express as px
import csv
import numpy as np

def createGraph(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()

def getData(data_path):
    coffee = []
    sleep = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
        
        return {"x": coffee, "y":sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml drank vs amount of sleep in hours :-  \n--->",correlation[0, 1])

def setup():
    data_path  = "coffee vs sleep.csv"

    datasource = getData(data_path)
    findCorrelation(datasource)
    createGraph(data_path)

setup()


