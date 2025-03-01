import streamlit as st
# Project Title
st.title("📊 OKR Performance Analysis :")

# Project Description
st.write(
    "This project is a **Proof of Concept (POC)** for analyzing **OKR (Objectives and Key Results)** performance "
    "using **PySpark & Pandas**, for ETL, **MySQL as DataWarehouse** for storage and **Power BI** for visualization."
)

st.header("🚀 Project Overview")
st.write(
    "- **Data Pipeline:** Ingests data from multiple sources into a **SQL Table** in **Local Server**.")
st.write(
    "- **Processing:** Uses **PySpark** transformations to clean, filter, and aggregate OKR performance data.")
st.write(
    "- **Data Load:** Uses **Pandas** to load the distributed output into the single data into the database.")
st.write(
    "- **Visualization:** Generates an **interactive Power BI report** to track OKR progress across departments."
)

# BI Report Image
st.subheader("📊 Power BI Report Screenshot")
st.image("assets/poc_bi_report.png", caption="OKR Performance Dashboard",  use_container_width=True)

# Code Section
st.subheader("🛠️ Code Implementation")
st.markdown("#### Sample Code :")
st.code(
    '''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Initialize Spark Session
spark = SparkSession.builder.appName("OKR_POC").getOrCreate()

# Load Data
df = spark.read.format("csv").option("header", "true").load("data/okr_data.csv")

# Data Processing
df_clean = df.select("Employee", "Objective", "Key Result", "Score") \
.withColumn("Score", col("Score").cast("float")) \
.groupBy("Employee", "Objective") \
.agg(avg("Score").alias("Average_Score"))

# Save Processed Data
df_clean.write.format("delta").mode("overwrite").save("data/okr_performance.delta")

print("OKR Processing Completed.")
    ''',
    language="python",
)

st.write("This script processes **OKR data** using **PySpark**, calculates average scores, and saves the results to a **Delta Table**.")

st.success("🎯 This project provides **actionable insights** into OKR performance, helping organizations improve goal tracking!")

