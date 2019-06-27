from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.io as pio

import os
import numpy as np

pio.orca.config.executable = '/home/ubuntu/visionai/secret-brushlands-95547/orca'

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N)*30

fig = go.Figure()
fig.add_scatter(x=x,
                y=y,
                mode='markers',
                marker={'size': sz,
                        'color': colors,
                        'opacity': 0.6,
                        'colorscale': 'Viridis'
                       });
#iplot(fig)
img_bytes = pio.to_image(fig, format='png')
pio.write_image(fig, 'fig1.png')