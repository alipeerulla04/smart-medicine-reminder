import streamlit as st
import pandas as pd
import os

# --------------------
# Page Config
# --------------------
st.set_page_config(
    page_title="Smart Medicine Reminder",
    page_icon="💊",
    layout="wide"
)

# --------------------
# Language Selection
# --------------------
language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "తెలుగు", "हिन्दी"]
)

translations = {
    "English": {
        "title": "💊 Smart Medicine Reminder",
        "subtitle": "Never miss your medicines again!",
        "add_medicine": "➕ Add Medicine",
        "medicine": "Medicine Name",
        "dosage": "Dosage",
        "time": "Medicine Time",
        "button": "Add Medicine",
        "saved": "📋 Saved Medicines",
        "success": "Medicine Added Successfully!",
        "delete": "🗑 Clear All Medicines",
        "deleted": "All medicines deleted!",
        "empty": "No medicines added yet.",
        "total": "Total Medicines"
    },

    "తెలుగు": {
        "title": "💊 స్మార్ట్ మెడిసిన్ రిమైండర్",
        "subtitle": "మీ మందులను మర్చిపోవద్దు!",
        "add_medicine": "➕ మందు జోడించండి",
        "medicine": "మందు పేరు",
        "dosage": "మోతాదు",
        "time": "మందు సమయం",
        "button": "మందు జోడించండి",
        "saved": "📋 సేవ్ చేసిన మందులు",
        "success": "మందు విజయవంతంగా జోడించబడింది!",
        "delete": "🗑 అన్ని మందులు తొలగించండి",
        "deleted": "అన్ని మందులు తొలగించబడ్డాయి!",
        "empty": "మందులు లేవు.",
        "total": "మొత్తం మందులు"
    },

    "हिन्दी": {
        "title": "💊 स्मार्ट मेडिसिन रिमाइंडर",
        "subtitle": "अपनी दवाइयाँ लेना न भूलें!",
        "add_medicine": "➕ दवा जोड़ें",
        "medicine": "दवा का नाम",
        "dosage": "खुराक",
        "time": "दवा का समय",
        "button": "दवा जोड़ें",
        "saved": "📋 सहेजी गई दवाएँ",
        "success": "दवा सफलतापूर्वक जोड़ी गई!",
        "delete": "🗑 सभी दवाएँ हटाएँ",
        "deleted": "सभी दवाएँ हटा दी गईं!",
        "empty": "कोई दवा नहीं मिली।",
        "total": "कुल दवाएँ"
    }
}

t = translations[language]

# --------------------
# Title
# --------------------
st.title(t["title"])
st.write(t["subtitle"])

# --------------------
# Add Medicine
# --------------------
st.subheader(t["add_medicine"])

medicine = st.text_input(t["medicine"])
dosage = st.text_input(t["dosage"])
time = st.time_input(t["time"])

if st.button(t["button"]):

    if medicine and dosage:

        new_data = pd.DataFrame({
            "Medicine": [medicine],
            "Dosage": [dosage],
            "Time": [str(time)]
        })

        if os.path.exists("medicines.csv"):
            new_data.to_csv(
                "medicines.csv",
                mode="a",
                header=False,
                index=False
            )
        else:
            new_data.to_csv(
                "medicines.csv",
                index=False
            )

        st.success(t["success"])

# --------------------
# Show Medicines
# --------------------
st.divider()

st.subheader(t["saved"])

if os.path.exists("medicines.csv"):

    df = pd.read_csv("medicines.csv")

    st.dataframe(df, width="stretch")

    st.metric(
        t["total"],
        len(df)
    )

else:
    st.info(t["empty"])

# --------------------
# Clear Medicines
# --------------------
if st.button(t["delete"]):

    pd.DataFrame(
        columns=["Medicine", "Dosage", "Time"]
    ).to_csv(
        "medicines.csv",
        index=False
    )

    st.success(t["deleted"])
    st.rerun()
