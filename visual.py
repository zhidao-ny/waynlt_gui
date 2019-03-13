import matplotlib.pyplot as plt
import pandas as pd



def create_bar_chart(var, data, varnames):

        plt.bar(var, data, color='b')
        # randomize color?

        plt.xlabel(varnames[0])
        plt.ylabel(varnames[1])
        plt.title('Popularity Ranking')
        # how to make the label as the title of the first variable? company name/skill set

        #plt.legend()
        plt.show()

#Tester
#import barchart
import pandas as pd
import matplotlib.pyplot as plt

column_names = [company, popularity]
#df = pd.DataFrame('', names = column_names)

var = ['a', 'b', 'c', 'd' ]
data = [1, 2, 3, 4]
varnames = column_names
create_bar_chart(var, data, varnames)
#plt.show()
