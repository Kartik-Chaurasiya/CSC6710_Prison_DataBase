import streamlit as st
import show_data
import insert_data

new_title = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">Tables</p>'

st.header('Prisoner DataBase')
st.sidebar.markdown(new_title, unsafe_allow_html=True)
table =  st.sidebar.form("table")
insert_into = table.selectbox(' ', ["prisoner_released", "prisoners", "prisons", "budget_flow", "crime_gender_numbers", "deaths_in_prison", "federal_sections", "illness", "staff", "state_year", "prisoner_statistics_year_wise", "Query 1", "Query 2"]) 
submit = table.form_submit_button("Select Table")
show_data.show_data(insert_into, submit)
insert_data.insert_date(insert_into)