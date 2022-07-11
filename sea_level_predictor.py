import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    


    # Create scatter plot
    fig = plt.figure(figsize = (12,6))
    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"])
    #plt.show()



    # Create first line of best fit
    res = linregress(x,y)
    xpr = pd.Series([i for i in range(1880,2051)])
    ypr = res.slope *xpr + res.intercept
    plt.plot(xpr,ypr,"r")


    # Create second line of best fit
    df_1 =df.loc[df["Year"]>=2000]
    df_1x=df_1["Year"]
    df_1y =df_1["CSIRO Adjusted Sea Level"]
    res = linregress(df_1x,df_1y)
    xpr1 = pd.Series([i for i in range(2000,2051)])
    ypr1 = res.slope *xpr1 + res.intercept
    plt.plot(xpr1,ypr1,"r")

    


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()