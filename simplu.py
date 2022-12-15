import pandas as pd
import plotly.express as px

data_mea = pd.read_csv('')

fig = px.pie(data_mea, values='Deaths', names='Bldg #', color='side')


fig.show()

