from MotionDetector import df

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_String"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_String"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)
p = figure(x_axis_type='datetime', height=800, width=1000, title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start ", "@Start_String"), ("End ", "@End_String")])
p.add_tools(hover)
q = p.quad(left="Start", right="End", bottom=0, top=1, color="red", source = cds)

output_file("Graph.html")
show(p)
