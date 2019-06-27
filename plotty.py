import plotly.plotly as py
import plotly.graph_objs as go
import plotly.io as pio

pio.orca.config.executable = '/home/ubuntu/visionai/secret-brushlands-95547/orca'

def plot_results(emotions_stats,title):

    fig = {
            "data": [
                          {
                            "values": [
                                        emotions_stats['Joy_likelihood'],
                                        emotions_stats['Sorrow_likelihood'],
                                        emotions_stats['Anger_likelihood'],
                                        emotions_stats['Surprise_likelihood'],
                                        emotions_stats['Under_exposed_likelihood'],
                                        emotions_stats['Blurred_likelihood'],
                                        emotions_stats['Headwear_likelihood']
                                      ],
                            "labels": [
                                        "Joy likelihood",
                                        "Sorrow likelihood",
                                        "Anger likelihood",
                                        "Surprise likelihood",
                                        "Under exposed likelihood",
                                        "Blurred likelihood",
                                        "Headwear likelihood"
                                      ],
                            "domain": {"x": [0, 1]},
                            "name": "twitter stats",
                            "hoverinfo":"label+percent+name",
                            "hole": .4,
                            "type": "pie"
                          }
                    ],
            "layout": {
                        "title":title,
                        "annotations": [
                                            {
                                                "font": {
                                                          "size": 20
                                                        },
                                                "showarrow": False,
                                                "text": "",
                                                "x": 0.20,
                                                "y": 0.5
                                            }
                                        ]
                        }
          }

    #py.iplot(fig, filename='donut')
    pio.write_image(fig, 'fig2.png')

    return 'fig2.png'