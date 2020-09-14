import pandas as pd
from .models import Registration
from bokeh.io import show, output_file,save
from bokeh.plotting import figure
from math import pi
from bokeh.transform import cumsum
from bokeh.palettes import Category20c
from bokeh.layouts import gridplot
from bokeh.embed import json_item
import json

class Visualization:

    # returns a dict object for chart 
    def get_dist(self,col_name):
        df_state=pd.DataFrame(Registration.objects.all().values(), columns=[col_name])
        dt=df_state.groupby(col_name)[col_name].agg(len)
        return dt.to_dict()
    
    # get all pie charts to show 
    def get_charts(self, fields):
        plots=[]
        for field in fields:
            print(field)
            d=self.get_dist(col_name=field)
            print(d)
            p=figure(title="Distribution of {}".format(field), plot_width=750, plot_height=750, tools="hover",toolbar_location=None,x_range=(-0.5,1.0))
            data=pd.Series(d).reset_index(name='value').rename(columns={'index':'field'})
            data['angle']=data['value']/data['value'].sum()*2*pi
            data['color']=Category20c[len(d)]
            p.wedge(x=0, y=1, radius=0.4
                ,start_angle=cumsum('angle',include_zero=True)
                ,end_angle=cumsum('angle')
                ,line_color="white"
                ,fill_color='color'
                ,legend_field='field'
                ,source=data)
            p.axis.axis_label=None
            p.axis.visible=False
            p.grid.grid_line_color=None
            plots.append(p)
        return json.dumps(json_item(gridplot(plots, ncols=2)))




            
        
        
    