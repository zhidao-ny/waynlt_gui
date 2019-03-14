import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import pandas as pd


#input: dataframe
def drawbarchart(df):
    column_names = list(df.columns.values)

#    column_names = ['Company', 'Frequency']
#    data = [['A', 2],['B',3],['C',1],['D',7],['E',6]]
#    df = pd.DataFrame(data,columns=['Company', 'Frequency'])



    #print(df)


    #input the data into lists
    var = []
    freq = []

    i = 0
    while i < 5:
        var.append(df.iloc[i,0])
        freq.append(df.iloc[i][1])
        i += 1
    #print(var)
    #print(freq)


    #create a bar chart
    plt.figure(1)
    plt.bar(var, freq, color='b')
    plt.xlabel(column_names[0])
    plt.ylabel(column_names[1])
    plt.title('Frequency Ranking')
    plt.show()


    #descendent bars??

    #assign different colors
    my_colors = 'rgbkymc'
    pd.Series.plot(
        df,
        kind='bar',
        color=my_colors,
    )


    # save as .jpg
    plt.savefig('barchart.png')
    #Image.open('barchart.png').save('barchart.jpg','JPEG')


