import streamlit as st

st.title("🩺 WiFi-Enabled Blood Pressure Monitoring System :")

st.write(
    "This project is an **IoT-based blood pressure monitoring system** that connects an analog BP apparatus "
    "to a **WiFi-enabled microcontroller**. Readings are transmitted in real-time to a Django-based web application, "
    "where healthcare professionals and caretakers can monitor patient data, analyze trends, and receive **AI-powered health insights.**"
)

st.header("🚀 Project Overview")
st.write(
    "- **Technology Stack:** STM32 microcontroller, WiFi module, Django REST Framework, MySQL database, AI model integration.")
st.write(
    "- **Device Functionality:** Converts systolic & diastolic values into JSON and sends them via HTTP requests.")
st.write(
    "- **Web App Features:** Provides authentication, real-time BP tracking, and AI-driven health insights.")
st.write(
    "- **User Roles:**")
st.markdown(
    ":material/star: **Admin (Hospital Management):** Can manage all patient records and delete entries if necessary.")
st.markdown(
    ":material/star: **Caretakers/Patients:** Can log in using the hospital name and patient ID to access personal records.")
st.write(
    "- **AI Integration:** Analyzes BP trends and provides recommendations for health monitoring."
)

# Web Application Screenshots
st.subheader("📊 Web App Dashboard & Features")
st.image("assets/dboard.png", caption="Blood Pressure Monitoring", use_container_width=True)
st.image("assets/login.png", caption="🔐 Secure Login Authentication",use_container_width=True)
st.image("assets/data.png", caption="📜 Patient BP History View", use_container_width=True)
st.image("assets/ai_analysis.png", caption="🤖 AI-Based BP Trend Analysis", use_container_width=True)

# Code Section
st.subheader("🛠️ Django Backend Code (BP Data API)")
st.markdown("#### Sample Code :")
st.code(
    '''
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import BloodPressureReading
from .serializers import BPReadingSerializer
import datetime

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_bp_reading(request):
    """ Receives BP data from IoT device and stores it in the database """
    user = request.user
    systolic = request.data.get("systolic")
    diastolic = request.data.get("diastolic")

    reading = BloodPressureReading.objects.create(
        user=user,
        systolic=systolic,
        diastolic=diastolic,
        timestamp=datetime.datetime.now()
    )
    return JsonResponse({"status": "success", "message": "BP data stored successfully"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def view_patient_bp(request):
    """ Fetch BP readings for the logged-in user """
    user = request.user
    readings = BloodPressureReading.objects.filter(user=user).order_by("-timestamp")
    serializer = BPReadingSerializer(readings, many=True)
    return JsonResponse(serializer.data, safe=False)
    ''',
    language="python",
)

st.subheader("📜 User Authentication")
st.write(
    "The system supports **role-based authentication**: "
    "- **Admins** log in using their credentials to manage hospital records."
    "- **Caretakers & Patients** use the **hospital name as the username** and their **patient ID as the password**."
)

st.subheader("🤖 AI Analysis for BP Trends")
st.write(
    "An integrated AI model analyzes historical BP trends, detects anomalies, and provides health recommendations "
    "to assist non-clinical users in understanding patient conditions."
)

st.success("🚀 This system enhances **remote healthcare monitoring** and provides **AI-driven health insights**!")

