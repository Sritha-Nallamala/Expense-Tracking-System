import streamlit as st
import requests
import pandas as pd

API_URL="http://localhost:8000"
def analyticsbymonth_tab():
    st.header("Expense Breakdown By Months")
    response=requests.get(f"{API_URL}/analytics/monthly")
    df = pd.DataFrame(response.json())
    st.bar_chart(df.set_index("month_name")["total_expenses"])
    st.dataframe(df.set_index("month_number"))