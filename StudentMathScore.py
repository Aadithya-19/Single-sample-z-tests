import random
import plotly.figure_factory as ff
import plotly.express as ps
import plotly.graph_objects as go
import pandas as spb
import statistics

df = spb.read_csv("StudentMathScore.csv")
data = (df["Math_score"].tolist())

mean = statistics.mean(data)
stnd = statistics.stdev(data)

def random_data(datapoint):
    dataset = []
    for i in range(0, datapoint):
        random_number = random.randint(0, (len(data)-1))
        value = data[random_number]
        dataset.append(value)
    samp_mean = statistics.mean(dataset)
    return (samp_mean)

print("Mean of Population = ", mean)
print("Standard Deviation of Population = ", stnd)

def show_fig(data):
    df = data
    mean = statistics.mean(df)

population_mean = statistics.mean(data)
print("Population Mean:- ", population_mean)

mean_list = []
for i in range(0, 1000):
    a = random_data(100)
    mean_list.append(a)
show_fig(mean_list)
Sam_mean = statistics.mean(mean_list)

stnd_mean = statistics.stdev(mean_list)

print("Mean of sampling distribution :-",Sam_mean )
print("Standard Deviation of sampling distribution :-",stnd_mean )

first_stnd_start, first_stnd_end = mean - stnd, mean + stnd
second_stnd_start, second_stnd_end = mean - (2*stnd), mean + (2*stnd)
third_stnd_start, third_stnd_end = mean - (3*stnd), mean + (3*stnd)

#Finding the mean of the first data and plotting it in the graph

df_i_1 = spb.read_csv("StudentMathIntervention1.csv")
data_i_1 = (df["Math_score"].tolist())

mean_i_1 = statistics.mean(data_i_1)
stnd_i_1 = statistics.stdev(data_i_1)
print("Mean of the first intervention - ",mean_i_1)



fig = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_i_1,mean_i_1], y = [0, 0.17], mode = "lines", name = "Mean of Sample 1"))
fig.add_trace(go.Scatter(x = [first_stnd_end,first_stnd_end], y = [0, 0.17], mode = "lines", name = "First Standard Deviation End"))
fig.add_trace(go.Scatter(x = [second_stnd_end,second_stnd_end], y = [0, 0.17], mode = "lines", name = "Second Standard Deviation End"))
fig.add_trace(go.Scatter(x = [third_stnd_end,third_stnd_end], y = [0, 0.17], mode = "lines", name = "Third Standard Deviation End"))

fig.show()

#Finding the mean of the second data and plotting it in the graph

df_i_2 = spb.read_csv("StudentMathIntervention2.csv")
data_i_2 = (df["Math_score"].tolist())

mean_i_2 = statistics.mean(data_i_2)
stnd_i_2 = statistics.stdev(data_i_2)
print("Mean of the second intervention - ",mean_i_2)



fig = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_i_2,mean_i_2], y = [0, 0.17], mode = "lines", name = "Mean of Sample 2"))
fig.add_trace(go.Scatter(x = [first_stnd_end,first_stnd_end], y = [0, 0.17], mode = "lines", name = "First Standard Deviation End"))
fig.add_trace(go.Scatter(x = [second_stnd_end,second_stnd_end], y = [0, 0.17], mode = "lines", name = "Second Standard Deviation End"))
fig.add_trace(go.Scatter(x = [third_stnd_end,third_stnd_end], y = [0, 0.17], mode = "lines", name = "Third Standard Deviation End"))

fig.show()

#Finding the mean of the third data and plotting it in the graph

df_i_3 = spb.read_csv("StudentMathIntervention3.csv")
data_i_3 = (df["Math_score"].tolist())

mean_i_3 = statistics.mean(data_i_3)
stnd_i_3 = statistics.stdev(data_i_3)
print("Mean of the third intervention - ",mean_i_3)



fig = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_i_3,mean_i_3], y = [0, 0.17], mode = "lines", name = "Mean of Sample 3"))
fig.add_trace(go.Scatter(x = [first_stnd_end,first_stnd_end], y = [0, 0.17], mode = "lines", name = "First Standard Deviation End"))
fig.add_trace(go.Scatter(x = [second_stnd_end,second_stnd_end], y = [0, 0.17], mode = "lines", name = "Second Standard Deviation End"))
fig.add_trace(go.Scatter(x = [third_stnd_end,third_stnd_end], y = [0, 0.17], mode = "lines", name = "Third Standard Deviation End"))

fig.show()