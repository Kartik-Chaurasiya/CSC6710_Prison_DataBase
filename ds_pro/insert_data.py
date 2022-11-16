import streamlit as st
import pandas as pd
import connection
import datetime
import psycopg2

conn = connection.conn
cursor = conn.cursor()

def insert_date(table):
    if table == "prisoners":
        query = "SELECT prison_id, prison_name FROM prisons;"
        cursor.execute(query)
        prison_idlst = cursor.fetchall()
        query = "SELECT section_id, section_desc FROM federal_sections;"
        cursor.execute(query)
        section_idlst = cursor.fetchall()
        pris =  st.form("pris", clear_on_submit=True)
        prisoner_name = pris.text_input('Prisoner name')
        age = pris.slider('Age', 1, 150)
        gender = pris.selectbox('Gender', ["Male", "Female"]) 
        sentence_date = pris.date_input("Sentence Date", datetime.date(2022, 1, 1))
        sentence_period_years = pris.slider('Sentence Period Years', 1, 50)
        total_worked_hours = pris.number_input('Total Worked Hours', 0, 100000)
        wage_per_hour = pris.number_input('Wage Per Hour', 0, 100)
        education = pris.selectbox('Education', ["Middle School", "High School"])
        prison_id = pris.selectbox('prison', prison_idlst)
        convict_reason = pris.text_area('Convict Reason')
        section_id = pris.selectbox('Section', section_idlst)

        submit = pris.form_submit_button("submit this form")

        if submit:
            if prisoner_name == "" or convict_reason == "":
                st.error("Fill empty columns")
            else:
                try:
                    query = "SELECT max(prisoner_id) FROM prisoners;"
                    cursor.execute(query)
                    last_id = cursor.fetchall()
                    data = (last_id[0][0] + 1, prisoner_name, age, gender, sentence_date, sentence_period_years, total_worked_hours, wage_per_hour, total_worked_hours*wage_per_hour, education, prison_id[0], convict_reason, section_id[0])
                    cursor.execute("INSERT into prisoners VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
                    conn.commit()
                    st.success("Success")
                except (Exception, psycopg2.DatabaseError) as error:
                    st.error(error)
    elif table == "prisoner_released":
        query = "SELECT prisoner_id, prisoner_name FROM prisoners;"
        cursor.execute(query)
        prisoner_idlst = cursor.fetchall()
        query = "SELECT prison_id, prison_name FROM prisons;"
        cursor.execute(query)
        prison_idlst = cursor.fetchall()
        pris_r =  st.form("pris_rel", clear_on_submit=True)
        prisoner_id = pris_r.selectbox('prisoner', prisoner_idlst) 
        rel_date = pris_r.date_input("Release Date", datetime.date(2019, 7, 6))
        prison_id = pris_r.selectbox('prison', prison_idlst) 
        is_parole = pris_r.selectbox('Is on Parole', [1,0])

        submit = pris_r.form_submit_button("submit this form")

        if submit:
            try:
                data = (prisoner_id[0], rel_date, prison_id[0], is_parole)
                cursor.execute("INSERT into prisoner_released VALUES (%s, %s, %s, %s)", data)
                conn.commit()
                st.success("Success")
            except (Exception, psycopg2.DatabaseError) as error:
                st.error(error)
    elif table == "prisons":
        query = "SELECT DISTINCT p_type FROM prisons;"
        cursor.execute(query)
        p_typelst = cursor.fetchall()
        query = "SELECT DISTINCT state FROM prisons;"
        cursor.execute(query)
        statelst = cursor.fetchall()
        statelst1=[]
        for x in range(len(statelst)):
            statelst1.append(statelst[x][0])
        p_typelst1=[]
        for x in range(len(p_typelst)):
            p_typelst1.append(p_typelst[x][0])
        prison =  st.form("prison", clear_on_submit=False)
        prison_name = prison.text_input('Prison name')
        p_type = prison.selectbox('Prison Type', p_typelst1) 
        state = prison.selectbox('State', statelst1) 
        p_email = prison.text_input('Prison Email')
        num_of_prisoners = prison.number_input('Number of Prisoners', 0, 10000)
        num_of_staff = prison.number_input('Number of Staff', 0, 1000)
        num_of_vehicles = prison.number_input('Number of Vehicles', 0, 500)
        contact_num = prison.number_input('Contact Number')

        submit = prison.form_submit_button("submit this form")

        if submit:
            if prison_name == "" or len(str(contact_num)) < 10:
                st.error("Fill empty columns or data Error")
            else:
                try:
                    query = "SELECT max(prison_id) FROM prisons;"
                    cursor.execute(query)
                    last_id = cursor.fetchall()
                    data = (last_id[0][0] + 1, prison_name,  p_type, state, p_email, num_of_prisoners, num_of_staff, num_of_prisoners+num_of_staff, num_of_vehicles, int(contact_num))
                    # print(data)
                    cursor.execute("INSERT into prisons VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
                    conn.commit()
                    st.success("Success")
                except (Exception, psycopg2.DatabaseError) as error:
                    st.error(error)
    elif table == "budget_flow":
        query = "SELECT state_year_id, state_name FROM state_year;"
        cursor.execute(query)
        state_year_idlst = cursor.fetchall()
        query = "SELECT prison_id, prison_name FROM prisons;"
        cursor.execute(query)
        prison_idlst = cursor.fetchall()
        budget =  st.form("budget", clear_on_submit=True)
        prison_id = budget.selectbox('prison', prison_idlst) 
        state_year_id = budget.selectbox('State Year', state_year_idlst) 
        planned_budget = budget.number_input('Planned Budget')
        expenditure = budget.number_input('Expenditure')
        gross_income = budget.number_input('Gross Income')

        submit = budget.form_submit_button("submit this form")

        if submit:
            try:
                data = (prison_id[0], state_year_id[0], planned_budget, expenditure, gross_income)
                cursor.execute("INSERT into budget_flow VALUES (%s, %s, %s, %s, %s)", data)
                conn.commit()
                st.success("Success")
            except (Exception, psycopg2.DatabaseError) as error:
                st.error(error)
    elif table == "crime_gender_numbers":
        query = "SELECT Distinct crime_head FROM crime_gender_numbers;"
        cursor.execute(query)
        crime_headlst = cursor.fetchall()
        query = "SELECT state_year_id, state_name FROM state_year;"
        cursor.execute(query)
        state_year_idlst = cursor.fetchall()
        crime_headlst1=[]
        for x in range(len(crime_headlst)):
            crime_headlst1.append(crime_headlst[x][0])
        crime_gender =  st.form("crime_gender", clear_on_submit=True)
        crime_head = crime_gender.selectbox('Crime Head', crime_headlst1) 
        state_year_id = crime_gender.selectbox('State Year', state_year_idlst) 
        male_16_18_years = crime_gender.number_input('Male 16-18 Years', 0, 10000)
        female_16_18_years = crime_gender.number_input('Female 16-18 Years', 0, 10000)
        male_19_30_years = crime_gender.number_input('Male 19-30 Years', 0, 10000)
        female_19_30_years = crime_gender.number_input('Female 19-30 Years', 0, 10000)
        male_31_50_years = crime_gender.number_input('Male 31-50 Years', 0, 10000)
        female_31_50_years = crime_gender.number_input('Female 31-50 Years', 0, 10000)
        male_above_50_years = crime_gender.number_input('Male above 50 Years', 0, 10000)
        female_above_50_years = crime_gender.number_input('Female above 50 Years', 0, 10000)

        submit = crime_gender.form_submit_button("submit this form")

        if submit:
            try:
                total_male = male_16_18_years + male_19_30_years + male_31_50_years + male_above_50_years
                total_female = female_16_18_years + female_19_30_years + female_31_50_years + female_above_50_years
                grand_total = total_male + total_female
                data = (crime_head, state_year_id[0], male_16_18_years, female_16_18_years, male_19_30_years, female_19_30_years, male_31_50_years, female_31_50_years, male_above_50_years, female_above_50_years, total_male, total_female, grand_total)
                cursor.execute("INSERT into crime_gender_numbers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
                conn.commit()
                st.success("Success")
            except (Exception, psycopg2.DatabaseError) as error:
                st.error(error)
    elif table == "deaths_in_prison":
        query = "SELECT prison_id, prison_name FROM prisons;"
        cursor.execute(query)
        prison_idlst = cursor.fetchall()
        query = "SELECT prisoner_id, prisoner_name FROM prisoners;"
        cursor.execute(query)
        prisoner_idlst = cursor.fetchall()
        query = "SELECT staff_id, staff_name FROM staff;"
        cursor.execute(query)
        staff_idlst = cursor.fetchall()
        prisoner_or_staff_idlst = prisoner_idlst + staff_idlst
        death =  st.form("death", clear_on_submit=True)
        death_reason = death.text_input('Death Reason')
        death_year = death.number_input('Death Year', 1500, 2022)
        is_natural_death = death.selectbox('Is Natural Death', [1,0])
        is_prisoner = death.selectbox('Is Prisoner', [1,0])
        prisoner_or_staff_id = death.selectbox('Prisoner or Staff Name', prisoner_or_staff_idlst) 
        prison_id = death.selectbox('Prison', prison_idlst) 

        submit = death.form_submit_button("submit this form")

        if submit:
            if death_reason == "":
                st.error("Fill empty columns or data Error")
            else:
                try:
                    query = "SELECT max(death_id) FROM deaths_in_prison;"
                    cursor.execute(query)
                    last_id = cursor.fetchall()
                    data = (last_id[0][0] + 1, death_reason,  death_year, is_natural_death, is_prisoner, prisoner_or_staff_id[0], prison_id[0])
                    # print(data)
                    cursor.execute("INSERT into deaths_in_prison VALUES (%s, %s, %s, %s, %s, %s, %s)", data)
                    conn.commit()
                    st.success("Success")
                except (Exception, psycopg2.DatabaseError) as error:
                    st.error(error)
    elif table == "federal_sections":
        federal_sections =  st.form("federal_sections", clear_on_submit=False)
        section_desc = federal_sections.text_input('Section Desc')
        section_number = federal_sections.text_input('Section Number')

        submit = federal_sections.form_submit_button("submit this form")

        if submit:
            if section_desc == "" or section_number == "":
                st.error("Fill empty columns")
            else:
                try:
                    query = "SELECT max(section_id) FROM federal_sections;"
                    cursor.execute(query)
                    last_section_id = cursor.fetchall()
                    data = (last_section_id[0][0] + 1, section_number, section_desc)
                    cursor.execute("INSERT into federal_sections VALUES (%s, %s, %s)", data)
                    conn.commit()
                    st.success("Success")
                except (Exception, psycopg2.DatabaseError) as error:
                    st.error(error)
    elif table == "illness":
        query = "SELECT prisoner_id, prisoner_name FROM prisoners;"
        cursor.execute(query)
        prisoner_idlst = cursor.fetchall()
        query = "SELECT DISTINCT ill_type FROM illness;"
        cursor.execute(query)
        ill_typelst = cursor.fetchall()
        ill_typelst1=[]
        for x in range(len(ill_typelst)):
            ill_typelst1.append(ill_typelst[x][0])
        illness =  st.form("illness", clear_on_submit=False)
        prisoner_id = illness.selectbox('prisoner', prisoner_idlst) 
        ill_type = illness.selectbox('Ill Type', ill_typelst1) 
        treatment_cost = illness.number_input('Treatment Cost')
        diagnosed_date = illness.date_input("Diagnosed Date", datetime.date(2022, 11, 16))

        submit = illness.form_submit_button("submit this form")

        if submit:
            try:
                data = (prisoner_id[0], ill_type, treatment_cost, diagnosed_date)
                cursor.execute("INSERT into illness VALUES (%s, %s, %s, %s)", data)
                conn.commit()
                st.success("Success")
            except (Exception, psycopg2.DatabaseError) as error:
                st.error(error)
    elif table == "staff":
        query = "SELECT prison_id, prison_name FROM prisons;"
        cursor.execute(query)
        prison_idlst = cursor.fetchall()
        staff =  st.form("staff", clear_on_submit=True)
        prison = staff.selectbox('Prison', prison_idlst) 
        staff_name = staff.text_input('Staff name')
        age = staff.slider('Age', 1, 150)
        gender = staff.selectbox('Gender', ["Male", "Female"]) 
        s_email = staff.text_input('Staff Email')
        in_service = staff.selectbox('In Service', [1, 0]) 

        submit = staff.form_submit_button("submit this form")

        if submit:
            if staff_name == "" or s_email == "":
                st.error("Fill empty columns")
            else:
                try:
                    query = "SELECT max(staff_id) FROM staff;"
                    cursor.execute(query)
                    last_id = cursor.fetchall()
                    data = (last_id[0][0] + 1, prison[0], staff_name, gender, age, s_email, int(in_service))
                    cursor.execute("INSERT into staff VALUES (%s, %s, %s, %s, %s, %s, %s)", data)
                    conn.commit()
                    st.success("Success")
                except (Exception, psycopg2.DatabaseError) as error:
                    st.error(error)
    elif table == "state_year":
        state_year =  st.form("state_year", clear_on_submit=False)
        state_name = state_year.text_input('State Name')
        year = state_year.number_input('Year', 1500, 2022)

        submit = state_year.form_submit_button("submit this form")

        if submit:
            if state_name == "":
                st.error("Fill empty columns")
            else:
                try:
                    query = "SELECT max(state_year_id) FROM state_year;"
                    cursor.execute(query)
                    last_section_id = cursor.fetchall()
                    data = (last_section_id[0][0] + 1, state_name, year)
                    cursor.execute("INSERT into state_year VALUES (%s, %s, %s)", data)
                    conn.commit()
                    st.success("Success")
                except (Exception, psycopg2.DatabaseError) as error:
                    st.error(error)
    elif table == "prisoner_statistics_year_wise":
        query = "SELECT state_year_id, state_name FROM state_year;"
        cursor.execute(query)
        state_year_idlst = cursor.fetchall()
        year_wise =  st.form("year_wise", clear_on_submit=True)
        state_year_id = year_wise.selectbox('State Year', state_year_idlst) 
        convicts_admitted = year_wise.number_input('Convicts Admitted')
        habitual_offenders = year_wise.number_input('Habitual Offenders')
        financial_assistance_received_num = year_wise.number_input('Financial Assistance Received Number')
        rehabilitated = year_wise.number_input('Rehabilitated')
        legal_aid_received_num = year_wise.number_input('Legal Aid Received Number')
        women_prisoners_with_children = year_wise.number_input('Women Prisoners With Children')
        children_of_women_prisoner_num = year_wise.number_input('Children Of Women Prisoner Num')

        submit = year_wise.form_submit_button("submit this form")

        if submit:
            try:
                data = (state_year_id[0], convicts_admitted, habitual_offenders, financial_assistance_received_num, rehabilitated, legal_aid_received_num, women_prisoners_with_children, children_of_women_prisoner_num)
                cursor.execute("INSERT into prisoner_statistics_year_wise VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", data)
                conn.commit()
                st.success("Success")
            except (Exception, psycopg2.DatabaseError) as error:
                st.error(error)

