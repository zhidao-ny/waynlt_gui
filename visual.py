class barchart:

    import matplotlib.pyplot as plt
    import pandas as pd

    def __init__(self, object, data, varnames):
        self.object = object
        self.data = data
        self.varnames = varnames

    def create_bar_chart(self):

        plt.bar(object, data, color='b')
        # randomize color?

        plt.xlabel(varnames[0])
        plt.ylabel(varnames[1])
        plt.title('Popularity Ranking')
        # how to make the label as the title of the first variable? company name/skill set

        #plt.legend()
        plt.show()



#how to


#Tester
#import barchart
#import pandas as pd
#column_names = [country, IMR, GNI, lifexp, litrate, enrlrate]
#df = pd.DataFrame('', names = column_names)

#df = barchart()
#df.object = []
#df.data =df.varnames = column_names


