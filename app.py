import streamlit as st

st.set_page_config(page_title="Smart Waste Classifier", page_icon="♻️")

st.title("♻️ Smart Waste Classifier")
st.write("Classify waste and get a disposal suggestion.")

waste_type = st.selectbox(
    "Select the waste type",
    [
        "Plastic Bottle",
        "Paper",
        "Banana Peel",
        "Glass Bottle",
        "Battery",
        "Food Waste"
    ]
)

if st.button("Classify Waste"):

    if waste_type == "Plastic Bottle":
        category = "Recyclable Waste ♻️"
        suggestion = "Place it in the recyclable waste bin."

    elif waste_type == "Paper":
        category = "Paper Waste 📄"
        suggestion = "Place it in the paper/recyclable waste bin."

    elif waste_type == "Banana Peel":
        category = "Organic Waste 🍌"
        suggestion = "Use it for composting or organic waste collection."

    elif waste_type == "Glass Bottle":
        category = "Glass Waste 🫙"
        suggestion = "Place it in the glass recycling collection."

    elif waste_type == "Battery":
        category = "E-Waste 🔋"
        suggestion = "Give it to an authorized e-waste collection center."

    else:
        category = "Organic Waste 🍎"
        suggestion = "Place it in the organic/compost waste bin."

    st.success(f"Category: {category}")
    st.info(f"Suggestion: {suggestion}")
