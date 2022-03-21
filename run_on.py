import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

# 2 --- you can add some css to your Streamlit app to customize it
# TODO: Change values below and observer the changes in your app
st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )
#######################################

st.set_option('deprecation.showPyplotGlobalUse', False)


# here is how to create containers
header_container = st.container()
stats_container = st.container()	
#######################################

# You can place things (titles, images, text, plots, dataframes, columns etc.) inside a container
with header_container:

	# for example a logo or a image that looks like a website header
	# st.image('logo.png')

	# different levels of text you can include in your app
	st.title("Churn")
	st.header("Welcome!")
	st.subheader("We predict churn within banking")
	st.write("There yet needs to be some editing to improve the visualizations.")

# Another container
with stats_container:
    
    
    # 4 --- You import datasets like you always do with pandas
	# 		if you'd like to import data from a database, you need to set up a database connection
    df = pd.read_csv('data/Churn_Modelling.csv')
    
    st.write(df)
    
    labels = 'Exited', 'Retained'
    sizes = [df.Exited[df['Exited']==1].count(), df.Exited[df['Exited']==0].count()]
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%') #autopct= %
    ax1.axis('equal')
    plt.title("Proportion of customer churned and retained", size = 20)
    plt.show()
    
    fig, axarr = plt.subplots(2, 2, figsize=(20, 12))
    sns.countplot(x='Geography', hue = 'Exited',data = df, ax=axarr[0][0])
    sns.countplot(x='Gender', hue = 'Exited',data = df, ax=axarr[0][1])
    sns.countplot(x='HasCrCard', hue = 'Exited',data = df, ax=axarr[1][0])
    sns.countplot(x='IsActiveMember', hue = 'Exited',data = df, ax=axarr[1][1])

    
    
    st.pyplot(fig1)
    st.pyplot(fig)
    
    
    
    st.write(df)
    #Bar Chart
    st.bar_chart(df.Geography)
    
    st.line_chart(df.Geography)
    
    #df = pd.read_csv('data/Churn_Modelling.csv'), columns = [‘Geography’,’Gender’,’HasCrCard’])
    df.hist()
    plt.show()
    st.pyplot()
        
    
#st.line_chart(df)
    
#chart_data = df["Exited"], df[['Geography', 'Gender', 'HasCrCard']]

#st.(chart_data)


