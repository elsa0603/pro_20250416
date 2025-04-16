import streamlit as st

ps = st.navigation(
    [st.Page("pages/p1.py", title="IRIS樣本資訊", icon="🌹"),
    st.Page("pages/p2.py", title="IRIS品種預測", icon="👏")]
    )

ps.run()
