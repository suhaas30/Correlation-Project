import plotly.express as px
import csv
import numpy as np

def createGraph(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    marks = []
    days = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))

    return {"x" : days, "y": marks}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in Percentage vs Days Present :-  \n--->",correlation[0, 1])

def setup():
    data_path  = "student vs marks.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    createGraph(data_path)

setup()
