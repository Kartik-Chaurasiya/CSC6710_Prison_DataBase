import streamlit as st
import pandas as pd
import connection

conn = connection.conn
cursor = conn.cursor()

df = pd.DataFrame()

cols = {
  'prisoners': ['prisoner_id', 'prisoner_name', 'age', 'gender', 'sentence_date', 'sentence_period_years', 'total_worked_hours', 'wage_per_hour', 'total_wage', 'education', 'prison_id', 'convict_reason', 'section_id'],
  'prisoner_released': ['prisoner_id', 'release_date', 'prison_id', 'is_on_parole'],
  'prisons': ['prison_id', 'prison_name', 'p_type', 'state', 'p_email', 'num_of_prisoners', 'num_of_staff', 'total_population', 'num_of_vehicles', 'contact_num'],
  'budget_flow': ['prison_id', 'state_year_id', 'planned_budget', 'expenditure', 'gross_income'],
  'crime_gender_numbers': ['crime_head', 'state_year_id', 'male_16_18_years', 'female_16_18_years', 'male_19_30_years', 'female_19_30_years', 'male_31_50_years', 'female_31_50_years', 'male_above_50_years', 'female_above_50_years', 'total_male', 'total_female', 'grand_total'],
  'deaths_in_prison': ['death_id', 'death_reason', 'death_year', 'is_natural_death', 'is_prisoner', 'prisoner_or_staff_id', 'prison_id'],
  'federal_sections': ['section_id', 'section_number', 'section_desc'],
  'illness': ['prisoner_id', 'ill_type', 'treatment_cost', 'diagnosed_date'],
  'staff': ['staff_id', 'prison_id', 'staff_name', 'gender', 'age', 's_email', 'in_service'],
  'state_year': ['state_year_id', 'state_name', 'year'],
  'prisoner_statistics_year_wise': ['state_year_id', 'convicts_admitted', 'habitual_offenders', 'financial_assistance_received_num', 'rehabilitated', 'legal_aid_received_num', 'women_prisoners_with_children', 'children_of_women_prisoner_num'],
  'Query 1': ['prison_name', 'total_treatment_cost', 'average_planned_budget'],
  'Query 2': ['prison_name', 'death']
}


def datapoint(n, N, df):
    start = ((n-1)*N)+1
    end = n*N
    if end >= df.shape[0]//10 & end < df.shape[0]:
        end = df.shape[0]
    if start == 1:
        start = 0
    return start, end

def show_data(table, submit):
    if 'count' not in st.session_state:
        st.session_state.count = 1
    if 'order' not in st.session_state:
        st.session_state.order = 1
    if 'order_by' not in st.session_state or submit:
        st.session_state.order_by = cols[table][0]
    if 'order_d' not in st.session_state or submit:
        st.session_state.order_d = 'ASC'
    if table != 'Query 1' and table != 'Query 2':
        st.text(f"Data: {table}")
        query = "SELECT * FROM {} ORDER BY {} {};".format(table, st.session_state.order_by, st.session_state.order_d)
        cursor.execute(query)
        df = cursor.fetchall()
    else:
        if table == 'Query 1':
            st.text("Display prison_name, total cost in prisoners treatment, average of their yearly ")
            st.text("planned budget and sort them by thier total treatment cost in desc.")
            query = """select pr.prison_name, sum(i.treatment_cost) as total_treatment_cost, avg(bf.planned_budget) as average_planned_budget
                        from prisons pr, prisoners p, illness i, budget_flow bf
                        where pr.prison_id = p.prison_id and
                            p.prisoner_id = i.prisoner_id and
                            pr.prison_id = bf.prison_id 
                        group by pr.prison_id
                        order by total_treatment_cost DESC;"""
            cursor.execute(query)
            df = cursor.fetchall()
        elif table == 'Query 2':
            st.text("display prison name for illtype Physical count number of death caused by it for ")
            st.text("prisoners sort by death count desc.")
            query = """select pr.prison_name, count(d.prisoner_or_staff_id) as death
                        from prisoners p, prisons pr, deaths_in_prison d, illness l
                        where pr.prison_id = p.prison_id and
                            p.prisoner_id = d.prisoner_or_staff_id and
                            l.prisoner_id = p.prisoner_id and
                            l.ill_type = 'Physical'
                        group by pr.prison_name
                        order by death DESC;"""
            cursor.execute(query)
            df = cursor.fetchall()
    order_by = st.selectbox('Order By Column', cols[table]) 
    cola, colb, _ = st.columns([0.1, 0.17, 0.1])
    with cola:
        if st.button('Order By'):
                st.session_state.order_by = order_by
    with colb:
        if st.button('Order ASC | DESC'):
                if st.session_state.order_d == "ASC":
                    st.session_state.order_d = "DESC"
                else:
                    st.session_state.order_d = "ASC"
    df = pd.DataFrame(df,columns=cols[table])

    if "page" not in st.session_state:
        st.session_state.page = 0

    def next_page():
        st.session_state.page += 1

    def prev_page():
        st.session_state.page -= 1

    col1, col2, col3, col4, _ = st.columns([0.1, 0.17, 0.1, 0.63, 0.1])

    if st.session_state.page < (df.shape[0]//10 + 1):
        col3.button(">", on_click=next_page)
    else:
        col3.write("")  # this makes the empty column show up on mobile

    if st.session_state.page > 0:
        col1.button("<", on_click=prev_page)
    else:
        col1.write("")
    with col4:
        if st.button('Order Rows'):
                st.session_state.order = -1*st.session_state.order
    col2.write(f"Page {1+st.session_state.page} of {df.shape[0]//10 + 1}")
    start = 10 * st.session_state.page
    end = start + 10
    st.write("")
    df1 = df.iloc[start:end]
    if st.session_state.order == -1:
        df1 = df1.loc[::-1, :]
    st.write(df1)


