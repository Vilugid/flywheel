import streamlit as st
import plotly.express as px
import pandas as pd

# Page config
st.set_page_config(
    page_title="Client Journey Flywheel",
    layout="wide"
)

st.title("Q2 Client Journey Flywheel")

# -------------------------
# Data
# -------------------------
data = {
    'Stage': [
        'Attract','Attract','Attract','Attract','Attract','Attract','Attract','Attract','Attract','Attract',
        'Engage','Engage','Engage','Engage','Engage','Engage','Engage','Engage','Engage','Engage','Engage',
        'Delight','Delight','Delight','Delight','Delight'
    ],
    'Journey': [
        'Connect','Connect','Connect','Connect','Connect','Connect','Connect','Connect','Connect','Connect',
        'Relationship','Relationship','Relationship','Relationship','Relationship',
        'Honour','Honour','Honour','Honour','Honour','Honour',
        'Empower','Empower','Empower','Empower','Empower'
    ],
    'Platform': [
        'Website','Social Media','Email','Virtual Events','Outbound','In-Person',
        'Associations','Partnerships','Trade Partners','Trad. Media',
        'Website','Social Media','Email','Sales Call','Pitch',
        'Website','Social Media','Client Email','Kick-off','Acct Mgmt','Billing',
        'Website','Email','Hubspot','Engagement','Digital Mileage'
    ],
    'Activity': [
        'Content & News','Posts & Ads','Drip Campaigns','Fairs & Events','Cold Outreach',
        'Networking','Memberships','Org Partners','Gov Relations','PR & Awards',
        'Whitepapers/Chat','Content (CTA)','Inbound Inquiry','Calibration','Design/Negotiate',
        'Support/Sched','Msg Support','VOC/Newsletter','Kick-off Mtg','Biz Reviews','Invoicing',
        'Exclusive Insights','Newsletter','CSAT & NPS','Case Studies','Ad Slots'
    ],
    'Who': [
        'Marketing','Marketing','Marketing','Mktg/Source','Sales/Search',
        'Sales/Ops','Sales/Ops','Sales/Ops','Sales/Ops','Marketing',
        'Marketing','Mktg/Search','Marketing','Sales','Sales/Ops',
        'Marketing','Marketing','Marketing','Sales/Ops','Ops/CRM','Finance',
        'Marketing','Marketing','Mktg/Sales','Mktg/CRM','Mktg/Sales'
    ]
}

df = pd.DataFrame(data)

# -------------------------
# Plotly Sunburst
# -------------------------
fig = px.sunburst(
    df,
    path=['Stage','Journey','Platform','Activity','Who'],
    height=850
)

fig.update_traces(
    insidetextorientation='radial',
    textfont=dict(size=11)
)

fig.update_layout(
    margin=dict(t=40, l=0, r=0, b=0)
)

st.plotly_chart(fig, use_container_width=True)
