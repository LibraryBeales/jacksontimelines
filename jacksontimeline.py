import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

df = pd.DataFrame([
    dict(Name="Ann D. Godfrey", Loc="Godfrey's Ferry, SC", Start='1829', Finish='1832', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Ann H. Richards", Loc="Joanne Furnace, PA", Start='1833', Finish='1844', Admin='Jackson Administration,Harrison / Tyler Administration'),
    dict(Name="Betsy S. Wilson", Loc="Ten Mile Stand, TN", Start='1829', Finish='1832', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Catharine M. Browner", Loc="New Windsor, MD", Start='1833', Finish='1844', Admin='Jackson Administration,Harrison / Tyler Administration'),
    dict(Name="Catherine Ann Canfield", Loc="New Philadelphia, OH", Start='1829', Finish='1848', Admin='Jackson Administration,Polk Administration'),
    dict(Name="Catherine Graham", Loc="Port Republic, VA", Start='1833', Finish='1840', Admin='Jackson Administration,Van Buren Administration'),
    dict(Name="Elizabeth Coffin Hoggatt", Loc="Paoli, IN", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Elizabeth Meyers Lauman", Loc="Middletown, PA", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Freeborn Rider", Loc="Rice City, RI", Start='1833', Finish='1840', Admin='Jackson Administration,Van Buren Administration'),
    dict(Name="Jane Compton", Loc="Manchester, SC", Start='1833', Finish='1840', Admin='Jackson Administration,Van Buren Administration'),
    dict(Name="Jane Dick", Loc="Dicks Mills, OH", Start='1829', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Margaret J. Walters", Loc="Lewistown, PA", Start='1829', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Margaret Johnston", Loc="Michigantown, IN", Start='1833', Finish='1840', Admin='Jackson Administration,Van Buren Administration'),
    dict(Name="Margaret M. Reid", Loc="Cotocton, MD", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Mary Odenheimer Deshong", Loc="Chester, PA", Start='1829', Finish='1840', Admin='Jackson Administration,Van Buren Administration'),
    #dict(Name="Mary Dickson", Loc="Lancaster, PA", Start='1829', Finish='1852', Admin='Jackson Administration,Taylor / Fillmore Administration'),
    dict(Name="Mary Dickson", Loc="Lancaster, PA", Start='1829', Finish='1837', Admin='Jackson Administration'),
    dict(Name="Mary Dickson", Loc="Lancaster, PA", Start='1837', Finish='1841', Admin='Van Buren Administration'),
    dict(Name="Mary Dickson", Loc="Lancaster, PA", Start='1841', Finish='1845', Admin='Harrison/Tyler Administration'),
    dict(Name="Mary Dickson", Loc="Lancaster, PA", Start='1845', Finish='1849', Admin='Polk Administration'),
    dict(Name="Mary Dickson", Loc="Lancaster, PA", Start='1849', Finish='1853', Admin='Taylor/Fillmore Administration'),
    dict(Name="Mary M. Hayes", Loc="Hayesville, NC", Start='1833', Finish='1844', Admin='Jackson Administration,Harrison / Tyler Administration'),
    dict(Name="Mary McKain", Loc="High Rock, NC", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Rebecca Jewett Gay", Loc="Washington Hollow, NY", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Rebecca Sanders", Loc="Leesburg, OH", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Sarah A. Cunningham", Loc="New London Crossroads, PA", Start='1833', Finish='1844', Admin='Jackson Administration,Harrison / Tyler Administration'),
    dict(Name="Sarah Davis", Loc="Paoli, PA", Start='1833', Finish='1848', Admin='Jackson Administration,Polk Administration'),
    dict(Name="Sarah Pryor", Loc="Pryors Vale, VA", Start='1833', Finish='1840', Admin='Jackson Administration,Van Buren Administration')
])

df2 = pd.DataFrame([
    dict(Name="Jackson Administration", Start='1829', Finish='1837'),
    dict(Name="Van Buren Administration", Start='1838', Finish='1841'),
    dict(Name="Harrison/Tyler Administration", Start='1842', Finish='1845'),
    dict(Name="Polk Administration", Start='1845', Finish='1848'),
    dict(Name="Taylor Administration", Start='1849', Finish='1850'),
    dict(Name="Fillmore Administration", Start='1851', Finish='1852')
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Name", color="Admin")

'''
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    px.timeline(df, x_start="Start", x_end="Finish", y="Name", color="Admin")
)
      
fig.add_trace(
    px.timeline(df2, x_start="Start", x_end="Finish", y="Name", color="Name"))
'''

fig.update_yaxes(autorange="reversed")
fig.show()

#https://stackoverflow.com/questions/64204353/plotly-how-to-highlight-certain-periods-in-a-pandas-time-series-with-rectangle
#https://stackoverflow.com/questions/63559119/how-to-specify-color-for-elements-in-plotly-gannt-chart
#https://stackoverflow.com/questions/65910725/plotly-bar-chart-opacity-changes-with-longer-time-range
#https://stackoverflow.com/questions/67964550/add-custom-markers-to-gantt-chart-in-plotly
