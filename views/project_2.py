import streamlit as st

# Project Title
st.title("🤖 Power BI Chatbot Integration :")

# Project Description
st.write(
    "This project integrates a **chatbot** that processes **Power BI report table data** using **Gemini API**. "
    "Users can ask questions about the data, and the chatbot provides insights based on the report tables."
)

st.header("🚀 Project Overview")
st.write(
    "- **Technology Stack:** Uses **Flask** to create a chatbot API, **Gemini API** for NLP, and **Power BI** for report data.")
st.write(
    "- **Chatbot Functionality:** Takes user queries, processes the report data, and returns insights.")
st.write(
    "- **Data Handling:** Power BI report tables are passed to the chatbot instead of direct report integration."
)

# BI Report Image
st.subheader("📊 Power BI Report Table Data Processing")
st.image("assets/bi_chatbot.png", caption="Chatbot Processing Power BI Report Data", use_container_width=True)

# Code Section
st.subheader("🛠️ Code Implementation")
st.markdown("#### Sample Code :")
st.code(
    '''
from flask import Flask, request, jsonify
import google.generativeai as genai
import pandas as pd

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="your_gemini_api_key")

# Load Power BI Report Table Data
df = pd.read_csv("data/powerbi_report_table.csv")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.json.get("query")

    # Convert DataFrame to text format for Gemini
    table_data = df.to_string(index=False)

    # Generate response using Gemini API
    prompt = f"Based on the following Power BI report data:\n{table_data}\n\nAnswer this question: {user_input}"
    response = genai.generate_text(model="gemini-pro", prompt=prompt)

    return jsonify({"query": user_input, "response": response.result})

if __name__ == "__main__":
    app.run(debug=True)
    ''',
    language="python",
)

st.write("This Flask API processes **Power BI report table data**, uses **Gemini API** for insights, and responds to user queries.")

st.success("🚀 This chatbot makes **Power BI data more accessible**, helping users extract insights effortlessly!")

