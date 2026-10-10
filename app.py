

import streamlit as st

from add_updateUI import add_update_tab
from analytics_ui import analytics_tab
from analyticsbymonth_UI import analyticsbymonth_tab




st.title("Expense Tracking System")
tab1,tab2,tab3=st.tabs(["Add/Update","Analytics By Category","Analytics By Month"])
with tab1:
    add_update_tab()
with tab2:
    analytics_tab()
with tab3:
    analyticsbymonth_tab()





