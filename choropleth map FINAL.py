"""
INTRO TO COMPUTER SCIENCE MIDTERM PROJECT: CHOROPLETH MAP
due date: january 3, 2022

installed libraries:
pip install plotly
pip install pandas

**the files used are located on my personal github account.
"""

# imports
import plotly.express as px
import pandas as pd

# files
df = pd.read_csv(r'https://raw.githubusercontent.com/snowfall26/midterm-project-2021/main/energy-cons.csv')
dfFinal = pd.read_csv(r'https://raw.githubusercontent.com/snowfall26/midterm-project-2021/main/energy-cons-cleaned.csv')

# clean data
def energyCons_clean(df):

        # checks all cells in the 'iso_alpha' column and removes the rows that do not have an iso-3 code
        df.dropna(subset = ['iso_alpha'], inplace = True)
        
        # filters dataframe by year (1980-2015)
        df = df[(df.year >= 1980) & (df.year <= 2015)]  

        # checks if year is a mutiple of 5
        df = df[df.year % 5 == 0]

        # resets index
        df.reset_index(level=None, drop=True, inplace=True, col_level=0, col_fill='')

        # convert dataframe to new csv file
        #df.to_csv(r'C:\Programs\Midterm Project\energy-cons-cleaned.csv')
        
# create choropleth map
def energyCons_map(dfFinal):

    fig = px.choropleth(dfFinal,
                  locations = 'iso_alpha',
                  scope = 'world',
                  color = 'PEC(TWh)',
                  hover_name='country',
                  animation_frame = 'year',
                  color_continuous_scale = px.colors.sequential.amp,
                  range_color = (0, 35000),
                  title = 'Global Energy Consumption (1980-2015)',
    )

    fig.show()

# functions
energyCons_clean(df)
energyCons_map(dfFinal)