import random 
import statistics
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
count = []
df = pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()

mean=sum(data)/len(data)
mode=statistics.mode(data)
median=statistics.median(data)
std_deviation=statistics.stdev(data) 

first_std_deviation_start,first_std_deviation_end = mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*std_deviation),mean+(3*std_deviation)
list_of_data_within_1_std_deviation =[result for result in data if result>first_std_deviation_start and result<first_std_deviation_end]
list_of_data_within_2_std_deviation =[result for result in data if result>first_std_deviation_start and result<first_std_deviation_end]
list_of_data_within_3_std_deviation =[result for result in data if result>first_std_deviation_start and result<first_std_deviation_end]

print("mean of the data is = ",mean)
print("mode of the data is = ",mode)
print("median of the data is = ",median)
print("standard deviation = ",std_deviation)
print("{}% of data lies within one standard deviation", format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within one standard deviation", format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within one standard deviation", format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))

fig=ff.create_distplot([data],[" Result"])
fig.show()

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="STD deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STD deviation 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="STD deviation 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STD deviation 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="STD deviation 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="STD deviation 3"))