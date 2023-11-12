import streamlit as st
import pandas as pd


#reading the file, dropping unneded column
df=pd.read_csv('cars_workshop.csv')
df = df.drop(df.columns[0], axis=1)
#---------------------------------------------


#creating header with checkbox
st.header('Market of used cars.Original data')
st.write("""
##### Filter the data below to see the ads by manufacturer
""")
show_new_cars = st.checkbox('Include new cars from dealers')
if not show_new_cars:
    df = df[df.state!='new']
#---------------------------------------------

#creating filtered data by manufacturer and year
manufacturer_choice=df['manufacturer_name'].unique()
make_choice_man = st.selectbox('Select manufacturer:', manufacturer_choice)

min_year,max_year=int(df['year_produced'].min()),int(df['year_produced'].max())
year_range = st.slider(
     "Choose years",
     value=(min_year,max_year),min_value=min_year,max_value=max_year )

actual_range=list(range(year_range[0],year_range[1]+1))


filtered_type=df[(df.manufacturer_name==make_choice_man)&(df.year_produced.isin(list(actual_range)))]

st.table(filtered_type)

#---------------------------------------------
st.header('Price analysis')
st.write("""
###### Let's analyze what influences price the most. We will check how distibution of price varies depending on  transmission, engine or body type and state
""")

#histogram of price by different parameters
import plotly.express as px
#Distribution of price depending on color, transmission,engine_type,body_type, state
list_for_hist=['transmission','engine_type','body_type','state']
choice_for_hist = st.selectbox('Split for price distribution', list_for_hist)
fig1 = px.histogram(df, x="price_usd", color=choice_for_hist)

fig1.update_layout(
title="<b> Split of price by {}</b>".format(choice_for_hist))
st.plotly_chart(fig1)

#---------------------------------------------


#defining age category of car
df['age']=2022-df['year_produced']
def age_category(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'
df['age_category']=  df['age'].apply(age_category)    

#---------------------------------------------

st.write("""
###### Now let's check how price is affected by odometer, engine capacity or number of photos in the adds
""")

#Distribution of price depending on odometer_value,engine_capacity,number_of_photos
list_for_scatter=['odometer_value','engine_capacity','number_of_photos']
choice_for_scatter = st.selectbox('Price dependency on ', list_for_scatter)
fig2 = px.scatter(df, x="price_usd", y=choice_for_scatter, color="age_category",
                  hover_data=['year_produced'])

fig2.update_layout(
title="<b> Price vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)