from decimal import DecimalException
import statistics 
import random
import math
import plotly.figure_factory as ff
import plotly.graph_objects as go
diceResult = []
for i in range (0,1000):
    dice1= random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1+dice2)
mean=sum(diceResult)/len(diceResult)
print(mean)
sd = statistics.stdev(diceResult)
print(sd)
median = statistics.median(diceResult)
print(median)
mode = statistics.mode(diceResult)
print(mode)
figure = ff.create_distplot([diceResult],['result'],show_hist=False)
fsdstart,fsdend = mean-sd,mean+sd
ssdstart,ssdend= mean-(2*sd), mean+(2*sd)
tsdstart,tsdend = mean-(3*sd), mean+(3*sd)
listofdatawithinfsd = [result for result in diceResult if result > fsdstart and result < fsdend]
print('{}% of datalies with in sd'.format(len(listofdatawithinfsd)*100/len(diceResult)))
listofdatawithinssd = [result for result in diceResult if result > ssdstart and result < ssdend]
print('{}% of datalies with in sd'.format(len(listofdatawithinssd)*100/len(diceResult)))
listofdatawithintsd = [result for result in diceResult if result > tsdstart and result < tsdend]
print('{}% of datalies with in sd'.format(len(listofdatawithintsd)*100/len(diceResult)))
figure.add_trace(go.Scatter(x = [mean,mean],y= [0,0.17],mode = 'lines', name = 'mean'))
figure.add_trace(go.Scatter(x = [fsdstart,fsdstart], y = [ 0,0.17], mode = 'lines', name = 'sd1'))
figure.add_trace(go.Scatter(x = [fsdend,fsdend], y = [ 0,0.17], mode = 'lines', name = 'sd1'))
figure.add_trace(go.Scatter(x = [ssdstart,ssdstart], y = [ 0,0.17], mode = 'lines', name = 'sd2'))
figure.add_trace(go.Scatter(x = [ssdend,ssdend], y = [ 0,0.17], mode = 'lines', name = 'sd2'))
figure.add_trace(go.Scatter(x = [tsdstart,tsdstart], y = [ 0,0.17], mode = 'lines', name = 'sd3'))
figure.add_trace(go.Scatter(x = [tsdend,tsdend], y = [ 0,0.17], mode = 'lines', name = 'sd3'))












figure.show()