import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
populationmean=statistics.mean(data)
print("population mean",populationmean)
populationstd=statistics.stdev(data)
print("populationstd",populationstd)
def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

def showfig(meanlist):
    df=meanlist
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    mean=statistics.mean(meanlist)
    samplestd=statistics.stdev(meanlist)
    print("sampling mean",mean)
    print("samplestd",samplestd)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmean(100)
        meanlist.append(setofmeans)

    showfig(meanlist)

setup()