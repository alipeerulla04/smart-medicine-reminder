import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(
    page_title="Smart Medicine Reminder",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Smart Medicine Reminder")
st.write("Never miss your medicines again!")

# ---------------------------
# Add Medicine
# ---------------------------

st.subheader("➕ Add Medicine")

medicine = st.text_input("Medicine Name")
dosage = st.text_input("Dosage")
time = st.time_input("Medicine Time")

if st.button("Add Medicine"):

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

        st.success("✅ Medicine Added Successfully!")

# ---------------------------
# Show Medicines
# ---------------------------

st.divider()

st.subheader("📋 Saved Medicines")

if os.path.exists("medicines.csv"):

    df = pd.read_csv("medicines.csv")

    st.dataframe(df, use_container_width=True)

    st.metric("Total Medicines", len(df))

else:
    st.info("No medicines added yet.")

# ---------------------------
# Reminder Alert
# ---------------------------

st.divider()

st.subheader("⏰ Reminder Check")

current_time = datetime.now().strftime("%H:%M")

if os.path.exists("medicines.csv"):

    df = pd.read_csv("medicines.csv")

    for _, row in df.iterrows():

        medicine_time = str(row["Time"])[:5]

        if medicine_time == current_time:

            st.warning(
                f"⚠️ Time to take {row['Medicine']} ({row['Dosage']})"
            )

# ---------------------------
# Delete Medicines
# ---------------------------

st.divider()

if st.button("🗑 Clear All Medicines"):

    pd.DataFrame(
        columns=["Medicine", "Dosage", "Time"]
    ).to_csv(
        "medicines.csv",
        index=False
    )

    st.success("All medicines deleted!")
    st.rerun()

# ---------------------------
# AI Medicine Assistant
# ---------------------------

st.divider()

st.subheader("🤖 AI Medicine Assistant")

question = st.text_input(
    "Ask about any medicine",
    placeholder="What is Crocin used for?"
)

if st.button("Get AI Answer"):

    medicine_info = {

        "crocin": """
### Crocin

**Uses**
- Reduces fever
- Relieves headache
- Reduces body pain

**Side Effects**
- Nausea
- Stomach discomfort

**Precautions**
- Do not exceed recommended dosage
""",

        "paracetamol": """
### Paracetamol

**Uses**
- Fever reduction
- Pain relief

**Side Effects**
- Rare allergic reactions

**Precautions**
- Avoid overdose
""",

        "dolo 650": """
### Dolo 650

**Uses**
- Fever
- Cold symptoms
- Body pain

**Side Effects**
- Nausea
- Dizziness

**Precautions**
- Use as directed by a doctor
"""
    }

    query = question.lower()

    found = False

    for med in medicine_info:

        if med in query:

            st.success("Answer Generated")

            st.markdown(medicine_info[med])

            found = True

            break

    if not found:

        st.info(
            "Medicine information not available in local database."
        )