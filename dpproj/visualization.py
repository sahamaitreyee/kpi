import pandas as pd
from .models import Registration
from bokeh.models import Legend
from bokeh.io import show, output_file,save
from bokeh.plotting import figure
from math import pi
from bokeh.transform import cumsum
from bokeh.palettes import Category20
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
            data=pd.Series(d).reset_index(name='value').rename(columns={'index':'field'})
            data['angle']=data['value']/data['value'].sum()*2*pi
            data['color']=Category20[len(d)]
            p=figure(title="Distribution of {}".format(field), plot_width=500, plot_height=500, tools="hover",toolbar_location=None,x_range=(-0.5,1.0), tooltips="@field: @value")
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

    def get_bar_plots(self, fields):
        plots=[]
        for field in fields:
            d=self.get_dist(col_name=field)
            data=pd.Series(d).reset_index(name='value').rename(columns={'index':'field'})
            data['color']=Category20[len(d)]
            # convert any int value to str categorial type 
            data['str_field']=list(map(str,data['field']))
            p=figure(title="Distribution of {}".format(field), 
                plot_height=500, 
                tools="hover",
                toolbar_location=None,
                tooltips="@field:@value",
                x_range=data['str_field'])
            p.vbar(source=data, 
                 x='str_field', top='value', 
                 line_color="green"
                ,fill_color='color'
                #,legend_field='str_field'
                )
            p.xaxis.axis_label=field
            p.xaxis.major_label_orientation="vertical"
            p.yaxis.axis_label="Count"
            #p.legend.orientation = "horizontal"
            #p.legend.location = "top_left"
            plots.append(p)
        return json.dumps(json_item(gridplot(plots, ncols=2, sizing_mode="fixed")))


            
        
        
    