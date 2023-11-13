import streamlit as st
import pandas as pd
import plotly.express as px


#reading the file, dropping unneded column
df=pd.read_csv('vehicles_us.csv')




#creating header with checkbox
st.header('Cars in the United States')
st.write("""
##### Filter the data below to see the ads by manufacturer
""")

fuel=df['fuel'].unique()
fuel_selected = st.selectbox('Select manufacturer:', fuel)

filtered_type=df[(df.fuel== fuel_selected)]
filtered_type

list_for_hist=['transmission','condition','model_year']
choice_for_hist = st.selectbox('Split for price distribution', list_for_hist)
fig1 = px.histogram(df, x="price", color=choice_for_hist)
fig1.update_xaxes(range=[0, 150000])
fig1.update_layout(
title="<b> Split of price by {}</b>".format(choice_for_hist))
st.plotly_chart(fig1)


#defining price category of car

def price_category(x):
    if x>50000: return 'Expensive'
    elif x>=30000 and x<50000: return 'Cheap'
    elif x<30000 :return 'Dirt Cheap'
    
df['price_category']=  df['price'].apply(price_category)    




st.write("""
###### Now let's check how price is affected by odometer, transmission, color or condition
""")


#Distribution of price depending on odometer,transmission,paint_color,condition
list_for_scatter=['odometer','transmission','paint_color','condition']
choice_for_scatter = st.selectbox('Price dependency on ', list_for_scatter)
fig2 = px.scatter(df, x="price", y=choice_for_scatter, color="price_category",
                  hover_data=['model_year'])




fig2.update_layout(
title="<b> Price vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)


