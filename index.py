import streamlit as st
import pandas as pd
import numpy as np
import plost

st.set_page_config(page_title = "MSMT",layout='wide', initial_sidebar_state='expanded', page_icon=':bar_chart:')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
#st.sidebar.header('Dashboard')
#st.sidebar.header('Dashboard')
#time_hist_color = st.sidebar.selectbox('Color by', ('sample analyzed', 'number od positives')) 

#st.sidebar.subheader('Donut chart parameter')
#donut_theta = st.sidebar.selectbox('Select data', ('sample analyzed', 'number of positives'))

#st.sidebar.subheader('Line chart parameters')
#plot_data = st.sidebar.multiselect('Select data', ['sample analyzed', 'number of positives'], ['sample analyzed', 'number of positives'])
#plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)


set1 = pd.read_csv('dataset.csv')
set2 = pd.read_csv('data.csv')  

region = pd.DataFrame(set1['Region'].value_counts())
district = pd.DataFrame(set1['District'].value_counts())
status = pd.DataFrame(set1['Status'].value_counts())
type = pd.DataFrame(set1['Study_type'].value_counts())









#THE IFS
with st.sidebar: 
    st.image("https://i0.wp.com/kusamchaina.com/wp-content/uploads/2022/05/cropped-cropped-MSMT-logo-1.png?w=512&ssl=1", width= 100)
    
    st.info("Select one of the following below.")
    choice = st.radio("", ["Overall", "Region", "District", "Status","Study Type"])
    
if choice == "Overall":
    # Row A
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('This is a laboratory report of MRDT Negative Samples Analysis Summary')
    col2.metric("", "", "")
    col3.metric("", "","")

    c1, c2 = st.columns((7,3))
    with c1:
        st.markdown('### Prevelance Per Region')
        plost.line_chart(
        data=set2,
        x='Region',
        y='Prevalence',
        width=500,)
    with c2:
        st.markdown('### Number of Samples Analyzed Per Region')
        plost.pie_chart(
            data=set2,
            theta='samples analyzed',
            color='Region',
            legend='bottom')
if choice == "Region":
    st.header("Number of Samples per Region")
    st.bar_chart(region)

if choice == "District":
    st.header("Number of Samples per District")
    st.bar_chart(district)
if choice == "Status":
    st.header("Total Number of Samples")
    st.bar_chart(status)


if choice == "Study Type":
    st.header("Total Number of Samples")
    st.bar_chart(type)



st.sidebar.markdown('''
---
Created with ❤️ by [Kusa Mchaina](https://kusamchaina.com/).
''')