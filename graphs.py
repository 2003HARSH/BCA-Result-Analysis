import matplotlib.pylab as plt
import plotly.graph_objs as go

from df import df

def line_graph(credentials):
    data=[]
    for i in credentials:
        trace=go.Scatter(x=df.columns[2:7],y=df[df['credentials']==i].values[0][2:7],
                 mode='lines+markers',
                 text=str(df[df['credentials']==i][['roll_no']].values[0][0]),
                 name=df[df['credentials']==i][['name']].values[0][0]
                 )
        data.append(trace)
    return data

def bar_graph(credentials):
    data=[]
    for i in credentials:
        trace=go.Bar(x=df.columns[2:7],y=df[df['credentials']==i].values[0][2:7],
                text=str(df[df['credentials']==i][['name']].values[0][0]),
                name=str(df[df['credentials']==i][['roll_no']].values[0][0])
                 )
        data.append(trace)
    return data

def mean_line():
    trace=go.Scatter(x=df.columns[2:7],y=[df['first_sem'].mean(),df['second_sem'].mean(),df['third_sem'].mean(),df['fourth_sem'].mean(),df['fifth_sem'].mean()],
             mode='lines+markers',
             text='Class Average',
             name='Class Average'
             )
    return [trace]

def median_line():
    trace=go.Scatter(x=df.columns[2:7],y=[df['first_sem'].median(),df['second_sem'].median(),df['third_sem'].median(),df['fourth_sem'].median(),df['fifth_sem'].median()],
             mode='lines+markers',
             text='Class Median',
             name='Class Median'
             )   
    return [trace] 

def max_line():
    trace=go.Scatter(x=df.columns[2:7],y=[df['first_sem'].max(),df['second_sem'].max(),df['third_sem'].max(),df['fourth_sem'].max(),df['fifth_sem'].max()],
        mode='lines+markers',
        name='Topper',
        text=[df[df['first_sem']==df['first_sem'].max()][['name']].values[0][0],df[df['second_sem']==df['second_sem'].max()][['name']].values[0][0],df[df['third_sem']==df['third_sem'].max()][['name']].values[0][0],df[df['fourth_sem']==df['fourth_sem'].max()][['name']].values[0][0],df[df['fifth_sem']==df['fifth_sem'].max()][['name']].values[0][0]]
        )
    return [trace]

def rank_line_graph(credentials):
    data=[]
    for i in credentials:
        trace=go.Scatter(x=df.columns[9:15],y=df[df['credentials']==i].values[0][9:15],
                 mode='lines+markers',
                 text=str(df[df['credentials']==i][['roll_no']].values[0][0]),
                 name=df[df['credentials']==i][['name']].values[0][0]
                 )
        data.append(trace)
    return data

def rank_plotter(data,title):
    layout=go.Layout(title=title,
        xaxis={'title':'Semester'},
        yaxis={'title':'SGPA'})
    fig=go.Figure(data,layout)
    fig.update_yaxes(autorange="reversed")
    return fig

def plotter(data,title):
    layout=go.Layout(title=title,
        xaxis={'title':'Semester'},
        yaxis={'title':'SGPA'})
    fig=go.Figure(data,layout)
    return fig

def bar_plot(sem,sem1):
    plt.title(f'BCA {sem1} Semester')
    plt.xlabel('SGPA')
    plt.ylabel('No. of Students')
    df[sem].value_counts().plot(kind='bar')    
    return plt