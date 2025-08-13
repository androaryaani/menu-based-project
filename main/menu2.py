# Import modules
import streamlit.components.v1 as components
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from twilio.rest import Client
import smtplib
import PyPDF2
from PIL import Image
from email.message import EmailMessage
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from googlesearch import search
from openai import OpenAI
import pandas as pd
import base64
import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import plotly.express as px
import subprocess
import shutil
import zipfile
import time
import qrcode
import io
import cv2
import mediapipe as mp
import pygame
from streamlit.components.v1 import html


# ---------------- Task Functions ----------------

st.set_page_config(
    page_title="Task Machine Pro",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== INJECT BEAUTIFUL CUSTOM CSS & HEADER ==========
st.markdown("""
<style>
body, .stApp {
    background: linear-gradient(135deg, #232526 0%, #414345 100%);
    color: #ECECEC !important;
}
.st-emotion-cache-0 {
    background-color: #191b1f !important;
    border-radius: 14px !important;
    box-shadow: 0 4px 24px rgba(0,0,0,0.7)!important;
    padding: 2.5rem !important;
    margin-bottom: 2rem;
}
h1, h2, h3, h4 { color: #39C1E8 !important; }
.stButton>button {
    background-color: #1abc9c;
    color: white;
    font-weight: 600;
    border-radius: 8px;
    transition: all 0.2s;
    margin: 8px 0;
    box-shadow: 0 2px 8px #19344133;
}
.stButton>button:hover {
    background-color: #18B398;
    color: #f2f2f2;
    transform: scale(1.04);
}
.st-emotion-cache-1r4qj8v {
    background: linear-gradient(180deg, #2c5364 0%, #0f2027 100%) !important;
    color: #F8F8FF !important;
}
hr {
    border-top: 1.5px solid #39C1E8;
    margin: 1.5rem 0;
}
.block-container {
    background: rgba(27, 38, 59, 0.95);
    border-radius: 18px;
    box-shadow: 0 2px 24px #223A5043;
    padding: 2.5rem 2rem 2rem 2rem;
}
.stAlert, .stNotification {
    border-radius: 10px;
    font-weight: 500;
}
.stAlert[data-baseweb="alert"] {
    background: linear-gradient(90deg, #232526 0%, #485563 100%);
    box-shadow: 0 1px 6px #24454755;
}
</style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
st.markdown("""
<div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 2.5rem;">
    <span style="font-size: 2.6rem; margin-right: 16px;">🛠️</span>
    <div>
        <h1 style="margin-bottom: 2px;">Task Machine Pro</h1>
        <p style="margin:0;color: #ACE0F9; font-size: 1.2rem;">
            All-in-one Linux, Python, ML, and Project Toolkit
        </p>
    </div>
</div>
---
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns([2, 2, 2])
with col1:
    st.metric("Server Uptime", "5 days")
with col2:
    st.metric("CPU Load", "0.67")
with col3:
    st.metric("RAM Usage", "3.2 GB / 8 GB")

# ========== SIDEBAR BRANDING ==========
st.sidebar.image("https://img.icons8.com/color/96/dashboard-layout.png", width=56)
st.sidebar.title("Task Machine Pro")
st.sidebar.markdown("""
**Explore categories:**
- Linux Tools
- Python Utilities
- Machine Learning
- DevOps & Project Tools
---
""")
def javascript_nodejs_demo():
   st.subheader("🟨 JavaScript Task: Custom HTML + JS Integration")

    # Paste your full HTML content as a triple-quote string here
   html_code = """
       <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TaskMaster Pro | All-in-One Utility App</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
        <style>
            :root {
                --primary: #4361ee;
                --secondary: #3f37c9;
                --accent: #4895ef;
                --success: #4cc9f0;
                --light: #f8f9fa;
                --dark: #212529;
                --danger: #f72585;
                --warning: #f8961e;
                --info: #2ec4b6;
                --gray: #6c757d;
                --radius: 12px;
                --shadow: 0 8px 20px rgba(0,0,0,0.1);
                --transition: all 0.3s ease;
            }
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: var(--light);
                min-height: 100vh;
                padding: 20px;
                overflow-x: hidden;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
            }
            
            header {
                text-align: center;
                padding: 30px 0;
                animation: fadeIn 1s ease;
            }
            
            header h1 {
                font-size: 3rem;
                margin-bottom: 10px;
                text-shadow: 0 2px 10px rgba(0,0,0,0.2);
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 15px;
            }
            
            header p {
                font-size: 1.2rem;
                max-width: 700px;
                margin: 0 auto;
                opacity: 0.9;
            }
            
            .app-container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 25px;
                margin-top: 30px;
            }
            
            .task-card {
                background: rgba(255, 255, 255, 0.12);
                backdrop-filter: blur(12px);
                border-radius: var(--radius);
                padding: 25px;
                box-shadow: var(--shadow);
                border: 1px solid rgba(255, 255, 255, 0.1);
                transition: var(--transition);
                display: flex;
                flex-direction: column;
                height: 100%;
            }
            
            .task-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(0,0,0,0.2);
                background: rgba(255, 255, 255, 0.18);
            }
            
            .task-header {
                display: flex;
                align-items: center;
                margin-bottom: 20px;
                gap: 15px;
            }
            
            .task-icon {
                width: 50px;
                height: 50px;
                background: var(--primary);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.5rem;
                box-shadow: 0 4px 10px rgba(67, 97, 238, 0.3);
                flex-shrink: 0;
            }
            
            .task-title {
                font-size: 1.5rem;
                font-weight: 600;
            }
            
            .task-description {
                margin-bottom: 20px;
                line-height: 1.6;
                flex-grow: 1;
            }
            
            .task-content {
                margin: 15px 0;
                flex-grow: 1;
            }
            
            .task-actions {
                display: flex;
                gap: 10px;
                margin-top: auto;
                flex-wrap: wrap;
            }
            
            .btn {
                padding: 12px 24px;
                border: none;
                border-radius: 50px;
                font-weight: 600;
                cursor: pointer;
                transition: var(--transition);
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                font-size: 0.95rem;
                flex-grow: 1;
            }
            .btn:disabled {
                background: var(--gray);
                cursor: not-allowed;
                opacity: 0.6;
            }
            
            .btn-primary { background: var(--primary); color: white; }
            .btn-secondary { background: var(--secondary); color: white; }
            .btn-success { background: var(--success); color: var(--dark); }
            .btn-danger { background: var(--danger); color: white; }
            .btn-warning { background: var(--warning); color: white; }
            .btn-info { background: var(--info); color: white; }
            
            .btn:not(:disabled):hover {
                opacity: 0.9;
                transform: translateY(-2px);
            }
            
            .camera-container {
                position: relative;
                width: 100%;
                background: rgba(0,0,0,0.2);
                border-radius: var(--radius);
                overflow: hidden;
                margin-bottom: 15px;
                aspect-ratio: 16/9;
            }
            
            #cameraPreview, #videoPreview {
                width: 100%;
                height: 100%;
                display: block;
                object-fit: cover;
            }
            
            .captured-media {
                width: 100%;
                border-radius: var(--radius);
                margin: 15px 0;
                display: none;
                max-height: 300px;
                object-fit: contain;
                background: rgba(0,0,0,0.2);
            }
            
            .map-container {
                height: 200px;
                background: var(--dark);
                border-radius: var(--radius);
                margin: 15px 0;
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
                position: relative;
            }
            
            #map {
                width: 100%;
                height: 100%;
            }
            
            .map-placeholder { text-align: center; padding: 20px; z-index: 1; }
            
            .store-list {
                list-style: none;
                margin-top: 15px;
                max-height: 200px;
                overflow-y: auto;
            }
            
            .store-list li {
                padding: 10px 15px;
                background: rgba(255,255,255,0.1);
                margin-bottom: 8px;
                border-radius: 8px;
                display: flex;
                align-items: center;
                gap: 10px;
                transition: var(--transition);
            }
            .store-list li:hover { background: rgba(255,255,255,0.2); }
            
            .email-list {
                list-style: none;
                margin-top: 15px;
                max-height: 200px;
                overflow-y: auto;
            }
            
            .email-list li {
                padding: 12px 15px;
                background: rgba(255,255,255,0.1);
                margin-bottom: 8px;
                border-radius: 8px;
                cursor: pointer;
                transition: var(--transition);
            }
            .email-list li:hover { background: rgba(255,255,255,0.2); }
            .email-list li.unread { border-left: 4px solid var(--accent); }
            .email-subject { font-weight: 600; margin-bottom: 5px; }
            .email-sender { font-size: 0.9rem; opacity: 0.8; }
            
            .social-buttons {
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
                margin-top: 15px;
            }
            
            .social-btn { flex: 1; min-width: 120px; }
            
            .input-group { margin: 15px 0; }
            .input-group label { display: block; margin-bottom: 8px; font-weight: 500; }
            .input-group input, .input-group textarea, .input-group select {
                width: 100%;
                padding: 12px 15px;
                border-radius: var(--radius);
                border: 1px solid rgba(255,255,255,0.2);
                background: rgba(0,0,0,0.2);
                color: white;
                font-size: 1rem;
                transition: var(--transition);
            }
            
            .input-group input:focus, .input-group textarea:focus, .input-group select:focus {
                outline: none;
                border-color: var(--accent);
                box-shadow: 0 0 0 3px rgba(72, 149, 239, 0.3);
            }
            
            .input-group input::placeholder, .input-group textarea::placeholder { color: rgba(255,255,255,0.5); }
            
            .status-message {
                padding: 10px 15px;
                border-radius: var(--radius);
                margin: 15px 0;
                text-align: center;
                display: none;
            }
            
            .status-success { background: rgba(76, 201, 240, 0.2); border: 1px solid var(--success); }
            .status-error { background: rgba(247, 37, 133, 0.2); border: 1px solid var(--danger); }
            
            .notification {
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 15px 25px;
                border-radius: var(--radius);
                background: var(--dark);
                color: var(--light);
                box-shadow: var(--shadow);
                display: flex;
                align-items: center;
                gap: 15px;
                z-index: 1000;
                transform: translateX(120%);
                transition: transform 0.4s ease-in-out;
            }
            
            .notification.show { transform: translateX(0); }
            .notification i { font-size: 1.5rem; }
            .notification-success { border-left: 5px solid var(--success); }
            .notification-error { border-left: 5px solid var(--danger); }
            .notification-warning { border-left: 5px solid var(--warning); }
            
            footer {
                text-align: center;
                padding: 30px 0;
                margin-top: 50px;
                font-size: 0.9rem;
                opacity: 0.8;
            }
            
            /* New styles for enhanced features */
            .scanner-container {
                position: relative;
                width: 100%;
                height: 250px;
                background: rgba(0,0,0,0.2);
                border-radius: var(--radius);
                margin: 15px 0;
                overflow: hidden;
            }
            
            #qr-reader, #barcode-reader {
                width: 100%;
                height: 100%;
            }

            .scanner-result {
                margin-top: 15px;
                padding: 10px;
                background: rgba(255,255,255,0.1);
                border-radius: var(--radius);
                word-break: break-all;
                display: none;
            }
            
            .document-preview {
                width: 100%;
                height: 200px;
                background: rgba(0,0,0,0.2);
                border-radius: var(--radius);
                margin: 15px 0;
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
                cursor: pointer;
                transition: var(--transition);
                border: 2px dashed rgba(255,255,255,0.3);
            }
            
            .document-preview:hover { background: rgba(0,0,0,0.3); border-color: var(--accent); }
            .document-preview i { font-size: 3rem; margin-bottom: 10px; }
            #documentPreview { width: 100%; height: 100%; object-fit: contain; display: none; background: white; border-radius: var(--radius); }
            
            .weather-display { display: flex; align-items: center; gap: 15px; margin: 15px 0; }
            .weather-icon { font-size: 3rem; }
            .weather-info { flex: 1; }
            .weather-temp { font-size: 2rem; font-weight: bold; }
            .weather-desc { opacity: 0.9; }
            .weather-details { display: flex; gap: 15px; margin-top: 10px; flex-wrap: wrap; }
            .weather-detail { display: flex; align-items: center; gap: 5px; font-size: 0.9rem; }
            
            .notes-container { height: 200px; overflow-y: auto; margin: 15px 0; padding-right: 5px; }
            .note-item { background: rgba(255,255,255,0.1); padding: 12px; border-radius: var(--radius); margin-bottom: 10px; transition: var(--transition); }
            .note-item:hover { background: rgba(255,255,255,0.2); }
            .note-title { font-weight: bold; margin-bottom: 5px; }
            .note-content { font-size: 0.9rem; line-height: 1.4; }
            .note-date { font-size: 0.8rem; opacity: 0.7; margin-top: 5px; text-align: right; }
            
            .tab-container { display: flex; border-bottom: 1px solid rgba(255,255,255,0.2); margin-bottom: 15px; }
            .tab { padding: 8px 16px; cursor: pointer; border-bottom: 2px solid transparent; transition: var(--transition); }
            .tab.active { border-bottom: 2px solid var(--accent); color: var(--accent); font-weight: bold; }
            .tab-content { display: none; }
            .tab-content.active { display: block; animation: fadeIn 0.5s; }
            
            .currency-converter { display: flex; flex-direction: column; gap: 10px; margin: 15px 0; }
            .currency-row { display: flex; align-items: center; gap: 10px; }
            .currency-row input { flex: 1; }
            .currency-row select { width: 100px; }
            .conversion-rate { text-align: center; margin: 10px 0; font-size: 0.9rem; opacity: 0.8; }
            
            .expense-list { list-style: none; margin-top: 15px; max-height: 200px; overflow-y: auto; }
            .expense-item { display: flex; justify-content: space-between; padding: 10px 15px; background: rgba(255,255,255,0.1); margin-bottom: 8px; border-radius: 8px; }
            .expense-category { display: flex; align-items: center; gap: 8px; }
            .expense-amount { font-weight: bold; }
            .expense-income { color: var(--success); }
            .expense-expense { color: var(--danger); }
            
            .progress-container { margin: 15px 0; }
            .progress-bar { height: 10px; background: rgba(255,255,255,0.1); border-radius: 5px; overflow: hidden; margin-bottom: 5px; }
            .progress-fill { height: 100%; background: var(--accent); border-radius: 5px; transition: width 0.5s ease; }
            .progress-info { display: flex; justify-content: space-between; font-size: 0.9rem; }
            
            /* Nearby stores styles */
            .store-type-buttons {
                display: flex;
                gap: 8px;
                flex-wrap: wrap;
                margin: 10px 0;
            }
            
            .store-type-btn {
                padding: 8px 12px;
                border-radius: 20px;
                background: rgba(255,255,255,0.1);
                border: none;
                color: white;
                font-size: 0.8rem;
                cursor: pointer;
                transition: var(--transition);
            }
            
            .store-type-btn:hover, .store-type-btn.active {
                background: var(--accent);
            }
            
            .store-distance {
                font-size: 0.8rem;
                opacity: 0.8;
                margin-left: auto;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            @media (max-width: 768px) {
                .app-container { grid-template-columns: 1fr; }
                header h1 { font-size: 2.2rem; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1><i class="fas fa-tasks"></i> TaskMaster Pro</h1>
                <p>Your all-in-one solution for daily tasks - from communication to navigation and media management</p>
            </header>
            
            <div class="app-container">
                <div class="task-card">
                    <div class="task-header">
                        <div class="task-icon"><i class="fas fa-camera"></i></div>
                        <h2 class="task-title">Photo Capture</h2>
                    </div>
                    <div class="task-content">
                        <div class="camera-container">
                            <video id="cameraPreview" autoplay playsinline></video>
                            <canvas id="photoCanvas" style="display:none;"></canvas>
                        </div>
                        <img id="capturedPhoto" class="captured-media" alt="Captured Photo">
                        <div class="status-message" id="photoStatus"></div>
                    </div>
                    <div class="task-actions">
                        <button class="btn btn-primary" id="capturePhotoBtn"><i class="fas fa-camera"></i> Capture Photo</button>
                        <button class="btn btn-success" id="sendPhotoBtn" disabled><i class="fas fa-paper-plane"></i> Send via Email</button>
                        <button class="btn btn-secondary" id="downloadPhotoBtn" disabled><i class="fas fa-download"></i> Download</button>
                    </div>
                </div>
                
                <div class="task-card">
                    <div class="task-header">
                        <div class="task-icon"><i class="fas fa-video"></i></div>
                        <h2 class="task-title">Video Capture</h2>
                    </div>
                    <div class="task-content">
                        <div class="camera-container">
                            <video id="videoPreview" autoplay playsinline muted></video>
                            <div id="recordingTimer" style="display:none; position:absolute; top:10px; right:10px; background:var(--danger); padding:5px 10px; border-radius:20px; font-weight:bold;">00:00</div>
                        </div>
                        <video id="capturedVideo" class="captured-media" controls style="display:none;"></video>
                        <div class="status-message" id="videoStatus"></div>
                    </div>
                    <div class="task-actions">
                        <button class="btn btn-primary" id="startRecordingBtn"><i class="fas fa-record-vinyl"></i> Start Recording</button>
                        <button class="btn btn-danger" id="stopRecordingBtn" disabled><i class="fas fa-stop"></i> Stop</button>
                        <button class="btn btn-success" id="sendVideoBtn" disabled><i class="fas fa-paper-plane"></i> Send Video</button>
                    </div>
                </div>
                
                <div class="task-card">
                    <div class="task-header">
                        <div class="task-icon"><i class="fas fa-map-marked-alt"></i></div>
                        <h2 class="task-title">Geolocation & Navigation</h2>
                    </div>
                    <div class="task-content">
                        <div class="map-container">
                            <div id="map"></div>
                        </div>
                        <div class="input-group">
                            <label for="destination">Destination Address:</label>
                            <input type="text" id="destination" placeholder="e.g., Hawa Mahal, Jaipur">
                        </div>
                        <div class="status-message" id="locationStatus"></div>
                    </div>
                    <div class="task-actions">
                        <button class="btn btn-primary" id="getLocationBtn"><i class="fas fa-location-dot"></i> Get Location</button>
                        <button class="btn btn-success" id="getRouteBtn" disabled><i class="fas fa-route"></i> Get Directions</button>
                        <button class="btn btn-secondary" id="shareLocationBtn" disabled><i class="fas fa-share"></i> Share Location</button>
                    </div>
                </div>

                <div class="task-card">
                    <div class="task-header">
                        <div class="task-icon"><i class="fas fa-store"></i></div>
                        <h2 class="task-title">Nearby Stores</h2>
                    </div>
                    <div class="task-content">
                        <p>Find stores and services near your current location.</p>
                        <div class="store-type-buttons">
                            <button class="store-type-btn active" data-type="all">All</button>
                            <button class="store-type-btn" data-type="restaurant"><i class="fas fa-utensils"></i> Restaurants</button>
                            <button class="store-type-btn" data-type="grocery"><i class="fas fa-shopping-basket"></i> Grocery</button>
                            <button class="store-type-btn" data-type="pharmacy"><i class="fas fa-prescription-bottle-alt"></i> Pharmacy</button>
                            <button class="store-type-btn" data-type="atm"><i class="fas fa-money-bill-wave"></i> ATMs</button>
                        </div>
                        <ul class="store-list" id="storeList">
                            <li style="text-align: center; padding: 20px;">Get your location to find nearby stores</li>
                        </ul>
                    </div>
                    <div class="task-actions">
                        <button class="btn btn-primary" id="findStoresBtn"><i class="fas fa-search-location"></i> Find Stores</button>
                        <button class="btn btn-secondary" id="refreshStoresBtn" disabled><i class="fas fa-sync-alt"></i> Refresh</button>
                    </div>
                </div>
                
                <div class="task-card">
                    <div class="task-header">
                        <div class="task-icon"><i class="fas fa-comments"></i></div>
                        <h2 class="task-title">Quick Communication</h2>
                    </div>
                    <div class="task-content">
                        <div class="tab-container" id="comm-tabs">
                            <div class="tab active" data-tab="whatsapp-tab"><i class="fab fa-whatsapp"></i> WhatsApp</div>
                            <div class="tab" data-tab="sms-tab"><i class="fas fa-sms"></i> SMS</div>
                            <div class="tab" data-tab="email-tab"><i class="fas fa-envelope"></i> Email</div>
                        </div>
                        
                        <div class="tab-content active" id="whatsapp-tab">
                            <div class="input-group"><input type="tel" id="phoneNumber" placeholder="Phone number with country code"></div>
                            <div class="input-group"><textarea id="whatsappMessage" rows="2" placeholder="WhatsApp message"></textarea></div>
                            <button class="btn btn-success btn-block" id="sendWhatsAppBtn"><i class="fab fa-whatsapp"></i> Send WhatsApp</button>
                        </div>
                        
                        <div class="tab-content" id="sms-tab">
                            <div class="input-group"><input type="tel" id="smsNumber" placeholder="Phone number"></div>
                            <div class="input-group"><textarea id="smsMessage" rows="2" placeholder="SMS message"></textarea></div>
                            <button class="btn btn-primary btn-block" id="sendSmsBtn"><i class="fas fa-sms"></i> Send SMS</button>
                        </div>
                        
                        <div class="tab-content" id="email-tab">
                            <div class="input-group"><input type="email" id="emailTo" placeholder="Recipient's Email"></div>
                            <div class="input-group"><input type="text" id="emailSubject" placeholder="Subject"></div>
                            <div class="input-group"><textarea id="emailMessage" rows="2" placeholder="Email body"></textarea></div>
                            <button class="btn btn-danger btn-block" id="sendEmailBtn"><i class="fas fa-envelope"></i> Send Email</button>
                        </div>
                    </div>
                </div>
                
                <div class="task-card">
                    <div class="task-header">
                        <div class="task-icon"><i class="fas fa-qrcode"></i></div>
                        <h2 class="task-title">QR Code Scanner</h2>
                    </div>
                    <div class="task-content">
                        <div class="scanner-container">
                            <div id="qr-reader"></div>
                        </div>
                        <div class="scanner-result" id="qr-result"></div>
                    </div>
                    <div class="task-actions">
                        <button class="btn btn-primary" id="startQrScanBtn"><i class="fas fa-play"></i> Start Scan</button>
                        <button class="btn btn-danger" id="stopQrScanBtn" disabled><i class="fas fa-stop"></i> Stop Scan</button>
                    </div>
                </div>
                
                <div class="task-card">
                    <div class="task-header">
                        <div class="task-icon"><i class="fas fa-cloud-sun"></i></div>
                        <h2 class="task-title">Weather Report</h2>
                    </div>
                    <div class="task-content">
                        <div class="weather-display">
                            <div class="weather-icon" id="weatherIcon"><i class="fas fa-spinner fa-spin"></i></div>
                            <div class="weather-info">
                                <div class="weather-temp" id="weatherTemp">--°C</div>
                                <div class="weather-desc" id="weatherDesc">Loading...</div>
                            </div>
                        </div>
                        <div class="weather-details">
                            <div class="weather-detail"><i class="fas fa-wind"></i> <span id="weatherWind">-- km/h</span></div>
                            <div class="weather-detail"><i class="fas fa-tint"></i> <span id="weatherHumidity">--%</span></div>
                        </div>
                        <div class="input-group">
                            <input type="text" id="weatherCity" placeholder="Enter city name">
                        </div>
                    </div>
                    <div class="task-actions">
                        <button class="btn btn-info" id="fetchWeatherBtn"><i class="fas fa-sync-alt"></i> Get Weather</button>
                    </div>
                </div>
            </div>
        </div>

        <div id="notification" class="notification">
            <i id="notificationIcon" class="fas fa-check-circle"></i>
            <span id="notificationMessage">This is a notification!</span>
        </div>
        
        <footer>
            <p>© 2025 TaskMaster Pro. Enhanced by Gemini.</p>
        </footer>

        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
        <script src="https://unpkg.com/html5-qrcode/html5-qrcode.min.js"></script>

        <script>
        document.addEventListener('DOMContentLoaded', () => {
            // --- Global Variables & Elements ---
            let currentStream;
            let photoStream;
            let videoStream;
            let mediaRecorder;
            let recordedChunks = [];
            let map;
            let currentLocationMarker;
            let html5QrCode;
            let userCoords;
            let storeType = 'all';

            const cameraPreview = document.getElementById('cameraPreview');
            const videoPreview = document.getElementById('videoPreview');

            // --- Utility Functions ---
            function showNotification(message, type = 'success') {
                const notification = document.getElementById('notification');
                const icon = document.getElementById('notificationIcon');
                const messageEl = document.getElementById('notificationMessage');

                notification.className = 'notification'; // Reset classes
                icon.className = '';

                if (type === 'success') {
                    notification.classList.add('notification-success');
                    icon.classList.add('fas', 'fa-check-circle');
                } else if (type === 'error') {
                    notification.classList.add('notification-error');
                    icon.classList.add('fas', 'fa-times-circle');
                } else if (type === 'warning') {
                    notification.classList.add('notification-warning');
                    icon.classList.add('fas', 'fa-exclamation-triangle');
                }
                
                messageEl.textContent = message;
                notification.classList.add('show');

                setTimeout(() => {
                    notification.classList.remove('show');
                }, 3000);
            }

            async function getCameraStream(constraints) {
                try {
                    return await navigator.mediaDevices.getUserMedia(constraints);
                } catch (err) {
                    console.error("Camera access error:", err);
                    showNotification('Camera access denied or not available.', 'error');
                    return null;
                }
            }

            // --- Photo Capture ---
            const capturePhotoBtn = document.getElementById('capturePhotoBtn');
            const sendPhotoBtn = document.getElementById('sendPhotoBtn');
            const downloadPhotoBtn = document.getElementById('downloadPhotoBtn');
            const photoCanvas = document.getElementById('photoCanvas');
            const capturedPhoto = document.getElementById('capturedPhoto');

            async function initPhotoCamera() {
                photoStream = await getCameraStream({ video: true, audio: false });
                if (photoStream) {
                    cameraPreview.srcObject = photoStream;
                }
            }
            initPhotoCamera(); // Initialize on load

            capturePhotoBtn.addEventListener('click', () => {
                if (!photoStream) {
                    showNotification('Camera is not active.', 'warning');
                    return;
                }
                const context = photoCanvas.getContext('2d');
                photoCanvas.width = cameraPreview.videoWidth;
                photoCanvas.height = cameraPreview.videoHeight;
                context.drawImage(cameraPreview, 0, 0, photoCanvas.width, photoCanvas.height);
                
                const dataUrl = photoCanvas.toDataURL('image/png');
                capturedPhoto.src = dataUrl;
                capturedPhoto.style.display = 'block';
                cameraPreview.style.display = 'none';

                sendPhotoBtn.disabled = false;
                downloadPhotoBtn.disabled = false;
                showNotification('Photo captured!', 'success');
            });

            downloadPhotoBtn.addEventListener('click', () => {
                const link = document.createElement('a');
                link.href = capturedPhoto.src;
                link.download = `capture-${Date.now()}.png`;
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                showNotification('Photo downloading...', 'success');
            });

            sendPhotoBtn.addEventListener('click', () => {
                const email = prompt("Enter recipient's email address:");
                if (email) {
                    const subject = "Photo from TaskMaster Pro";
                    const body = "Please see the attached photo.";
                    // Note: Sending actual attachments via mailto is not reliably supported. 
                    // This is a simplified implementation. A backend would be needed for true attachments.
                    const mailtoLink = `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
                    window.location.href = mailtoLink;
                    showNotification('Email client opened.', 'success');
                }
            });

            // --- Video Capture ---
            const startRecordingBtn = document.getElementById('startRecordingBtn');
            const stopRecordingBtn = document.getElementById('stopRecordingBtn');
            const sendVideoBtn = document.getElementById('sendVideoBtn');
            const capturedVideo = document.getElementById('capturedVideo');
            const recordingTimer = document.getElementById('recordingTimer');
            let timerInterval;

            async function initVideoCamera() {
                videoStream = await getCameraStream({ video: true, audio: true });
                if (videoStream) {
                    videoPreview.srcObject = videoStream;
                }
            }
            initVideoCamera();

            startRecordingBtn.addEventListener('click', async () => {
                if (!videoStream) {
                    showNotification('Camera is not active for video.', 'warning');
                    await initVideoCamera();
                    return;
                }
                recordedChunks = [];
                mediaRecorder = new MediaRecorder(videoStream, { mimeType: 'video/webm' });
                
                mediaRecorder.ondataavailable = (event) => {
                    if (event.data.size > 0) {
                        recordedChunks.push(event.data);
                    }
                };

                mediaRecorder.onstart = () => {
                    startRecordingBtn.disabled = true;
                    stopRecordingBtn.disabled = false;
                    sendVideoBtn.disabled = true;
                    recordingTimer.style.display = 'block';
                    let seconds = 0;
                    timerInterval = setInterval(() => {
                        seconds++;
                        const min = String(Math.floor(seconds / 60)).padStart(2, '0');
                        const sec = String(seconds % 60).padStart(2, '0');
                        recordingTimer.textContent = `${min}:${sec}`;
                    }, 1000);
                    showNotification('Recording started!', 'success');
                };

                mediaRecorder.onstop = () => {
                    clearInterval(timerInterval);
                    recordingTimer.style.display = 'none';
                    startRecordingBtn.disabled = false;
                    stopRecordingBtn.disabled = true;
                    sendVideoBtn.disabled = false;

                    const blob = new Blob(recordedChunks, { type: 'video/webm' });
                    const videoUrl = URL.createObjectURL(blob);
                    capturedVideo.src = videoUrl;
                    capturedVideo.style.display = 'block';
                    videoPreview.style.display = 'none';
                    showNotification('Recording stopped. Video is ready.', 'success');
                };
                
                mediaRecorder.start();
            });

            stopRecordingBtn.addEventListener('click', () => {
                if (mediaRecorder && mediaRecorder.state === 'recording') {
                    mediaRecorder.stop();
                }
            });

            sendVideoBtn.addEventListener('click', () => {
                const email = prompt("Enter recipient's email address to send video:");
                if (email) {
                    const subject = "Video from TaskMaster Pro";
                    const body = "A video has been recorded for you. Please note that due to browser limitations, the video is not attached directly. A real app would upload this to a server and share a link.";
                    const mailtoLink = `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
                    window.location.href = mailtoLink;
                    showNotification('Email client opened.', 'success');
                }
            });

                    // --- Geolocation & Maps ---
            const getLocationBtn = document.getElementById('getLocationBtn');
            const getRouteBtn = document.getElementById('getRouteBtn');
            const shareLocationBtn = document.getElementById('shareLocationBtn');
            const destinationInput = document.getElementById('destination');
            const locationStatus = document.getElementById('locationStatus');

            // Initialize map
            map = L.map('map').setView([20.5937, 78.9629], 5); // Default to India view
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);

            getLocationBtn.addEventListener('click', () => {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(
                        (position) => {
                            userCoords = {
                                lat: position.coords.latitude,
                                lng: position.coords.longitude
                            };
                            
                            // Update map view
                            map.setView([userCoords.lat, userCoords.lng], 15);
                            
                            // Clear previous marker if exists
                            if (currentLocationMarker) {
                                map.removeLayer(currentLocationMarker);
                            }
                            
                            // Add new marker
                            currentLocationMarker = L.marker([userCoords.lat, userCoords.lng]).addTo(map)
                                .bindPopup("Your Location").openPopup();
                            
                            // Enable buttons
                            getRouteBtn.disabled = false;
                            shareLocationBtn.disabled = false;
                            
                            // Show success
                            locationStatus.textContent = `Location found! Latitude: ${userCoords.lat.toFixed(4)}, Longitude: ${userCoords.lng.toFixed(4)}`;
                            locationStatus.className = 'status-message status-success';
                            locationStatus.style.display = 'block';
                            
                            showNotification('Location found!', 'success');
                        },
                        (error) => {
                            let errorMessage;
                            switch(error.code) {
                                case error.PERMISSION_DENIED:
                                    errorMessage = "User denied the request for Geolocation.";
                                    break;
                                case error.POSITION_UNAVAILABLE:
                                    errorMessage = "Location information is unavailable.";
                                    break;
                                case error.TIMEOUT:
                                    errorMessage = "The request to get user location timed out.";
                                    break;
                                case error.UNKNOWN_ERROR:
                                    errorMessage = "An unknown error occurred.";
                                    break;
                            }
                            
                            locationStatus.textContent = errorMessage;
                            locationStatus.className = 'status-message status-error';
                            locationStatus.style.display = 'block';
                            
                            showNotification(errorMessage, 'error');
                        }
                    );
                } else {
                    locationStatus.textContent = "Geolocation is not supported by this browser.";
                    locationStatus.className = 'status-message status-error';
                    locationStatus.style.display = 'block';
                    
                    showNotification("Geolocation not supported", 'error');
                }
            });

            getRouteBtn.addEventListener('click', () => {
                const destination = destinationInput.value;
                if (!destination) {
                    showNotification('Please enter a destination.', 'warning');
                    return;
                }

                if (userCoords) {
                    const mapsUrl = `https://www.google.com/maps/dir/?api=1&origin=${userCoords.lat},${userCoords.lng}&destination=${encodeURIComponent(destination)}`;
                    window.open(mapsUrl, '_blank');
                    showNotification('Redirecting to Google Maps for directions.', 'success');
                } else {
                    showNotification('Please get your location first.', 'warning');
                }
            });

            shareLocationBtn.addEventListener('click', () => {
                if (navigator.share) {
                    navigator.share({
                        title: 'My Current Location',
                        text: `I'm at this location: Latitude ${userCoords.lat}, Longitude ${userCoords.lng}`,
                        url: `https://www.google.com/maps?q=${userCoords.lat},${userCoords.lng}`
                    }).then(() => {
                        showNotification('Location shared successfully', 'success');
                    }).catch(err => {
                        showNotification('Error sharing location: ' + err, 'error');
                    });
                } else {
                    // Fallback for browsers that don't support Web Share API
                    const shareText = `My current location: https://www.google.com/maps?q=${userCoords.lat},${userCoords.lng}`;
                    prompt("Copy this link to share your location:", shareText);
                    showNotification('Share link copied to clipboard', 'success');
                }
            });

            // --- Nearby Stores ---
            const findStoresBtn = document.getElementById('findStoresBtn');
            const refreshStoresBtn = document.getElementById('refreshStoresBtn');
            const storeList = document.getElementById('storeList');
            const storeTypeButtons = document.querySelectorAll('.store-type-btn');

            storeTypeButtons.forEach(btn => {
                btn.addEventListener('click', () => {
                    storeTypeButtons.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    storeType = btn.dataset.type;
                    
                    if (userCoords) {
                        findNearbyStores();
                    }
                });
            });

            findStoresBtn.addEventListener('click', () => {
                if (!userCoords) {
                    showNotification('Please get your location first', 'warning');
                    return;
                }
                findNearbyStores();
            });

            refreshStoresBtn.addEventListener('click', findNearbyStores);

            function findNearbyStores() {
                // In a real app, this would use a Places API like Google Places
                // Here we simulate with mock data
                
                storeList.innerHTML = '<li style="text-align: center; padding: 20px;"><i class="fas fa-spinner fa-spin"></i> Finding nearby stores...</li>';
                
                setTimeout(() => {
                    const mockStores = generateMockStores();
                    displayStores(mockStores);
                    refreshStoresBtn.disabled = false;
                }, 1000);
            }

            function generateMockStores() {
                const storeTypes = {
                    restaurant: { name: 'Restaurant', icon: 'fa-utensils' },
                    grocery: { name: 'Grocery Store', icon: 'fa-shopping-basket' },
                    pharmacy: { name: 'Pharmacy', icon: 'fa-prescription-bottle-alt' },
                    atm: { name: 'ATM', icon: 'fa-money-bill-wave' }
                };
                
                const stores = [];
                const count = Math.floor(Math.random() * 5) + 3; // 3-7 stores
                
                for (let i = 0; i < count; i++) {
                    let type;
                    if (storeType === 'all') {
                        const types = Object.keys(storeTypes);
                        type = types[Math.floor(Math.random() * types.length)];
                    } else {
                        type = storeType;
                    }
                    
                    const distance = (Math.random() * 2 + 0.5).toFixed(1);
                    
                    stores.push({
                        id: i,
                        name: `${storeTypes[type].name} ${i+1}`,
                        type: type,
                        icon: storeTypes[type].icon,
                        distance: distance
                    });
                }
                
                // Sort by distance
                return stores.sort((a, b) => parseFloat(a.distance) - parseFloat(b.distance));
            }

            function displayStores(stores) {
                storeList.innerHTML = '';
                
                if (stores.length === 0) {
                    storeList.innerHTML = '<li style="text-align: center; padding: 20px;">No stores found in this category</li>';
                    return;
                }
                
                stores.forEach(store => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        <i class="fas ${store.icon}"></i>
                        <span>${store.name}</span>
                        <span class="store-distance">${store.distance} km</span>
                    `;
                    storeList.appendChild(li);
                });
            }

            // --- Communication Tabs ---
            const commTabs = document.querySelectorAll('#comm-tabs .tab');
            
            commTabs.forEach(tab => {
                tab.addEventListener('click', () => {
                    // Hide all tab contents
                    document.querySelectorAll('.tab-content').forEach(content => {
                        content.classList.remove('active');
                    });
                    
                    // Deactivate all tabs
                    commTabs.forEach(t => {
                        t.classList.remove('active');
                    });
                    
                    // Activate current tab
                    tab.classList.add('active');
                    
                    // Show corresponding content
                    const tabId = tab.dataset.tab;
                    document.getElementById(tabId).classList.add('active');
                });
            });

            // WhatsApp
            const sendWhatsAppBtn = document.getElementById('sendWhatsAppBtn');
            
            sendWhatsAppBtn.addEventListener('click', () => {
                const phoneNumber = document.getElementById('phoneNumber').value;
                const message = document.getElementById('whatsappMessage').value;
                
                if (!phoneNumber || !message) {
                    showNotification('Please enter both phone number and message', 'warning');
                    return;
                }
                
                const encodedMessage = encodeURIComponent(message);
                const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodedMessage}`;
                
                window.open(whatsappUrl, '_blank');
                showNotification('WhatsApp message ready to send', 'success');
            });

            // SMS
            const sendSmsBtn = document.getElementById('sendSmsBtn');
            
            sendSmsBtn.addEventListener('click', () => {
                const phoneNumber = document.getElementById('smsNumber').value;
                const message = document.getElementById('smsMessage').value;
                
                if (!phoneNumber || !message) {
                    showNotification('Please enter both phone number and message', 'warning');
                    return;
                }
                
                const smsUrl = `sms:${phoneNumber}?body=${encodeURIComponent(message)}`;
                
                window.location.href = smsUrl;
                showNotification('SMS ready to send', 'success');
            });

            // Email
            const sendEmailBtn = document.getElementById('sendEmailBtn');
            
            sendEmailBtn.addEventListener('click', () => {
                const to = document.getElementById('emailTo').value;
                const subject = document.getElementById('emailSubject').value;
                const message = document.getElementById('emailMessage').value;
                
                if (!to || !subject || !message) {
                    showNotification('Please fill all email fields', 'warning');
                    return;
                }
                
                const mailtoUrl = `mailto:${to}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(message)}`;
                
                window.location.href = mailtoUrl;
                showNotification('Email client opened', 'success');
            });

            // --- QR Code Scanner ---
            const startQrScanBtn = document.getElementById('startQrScanBtn');
            const stopQrScanBtn = document.getElementById('stopQrScanBtn');
            const qrResult = document.getElementById('qr-result');
            
            startQrScanBtn.addEventListener('click', () => {
                if (!html5QrCode) {
                    html5QrCode = new Html5Qrcode("qr-reader");
                }
                
                html5QrCode.start(
                    { facingMode: "environment" },
                    {
                        fps: 10,
                        qrbox: { width: 250, height: 250 }
                    },
                    (decodedText, decodedResult) => {
                        qrResult.textContent = decodedText;
                        qrResult.style.display = 'block';
                        stopQrScan();
                        showNotification('QR code scanned successfully!', 'success');
                    },
                    (errorMessage) => {
                        // No action needed - just keeping the scanner running
                    }
                ).catch(err => {
                    showNotification('Error starting QR scanner: ' + err, 'error');
                });
                
                startQrScanBtn.disabled = true;
                stopQrScanBtn.disabled = false;
            });

            stopQrScanBtn.addEventListener('click', stopQrScan);

            function stopQrScan() {
                if (html5QrCode && html5QrCode.isScanning) {
                    html5QrCode.stop().then(() => {
                        startQrScanBtn.disabled = false;
                        stopQrScanBtn.disabled = true;
                    }).catch(err => {
                        showNotification('Error stopping scanner: ' + err, 'error');
                    });
                }
            }

            // --- Weather Report ---
            const fetchWeatherBtn = document.getElementById('fetchWeatherBtn');
            const weatherIcon = document.getElementById('weatherIcon');
            const weatherTemp = document.getElementById('weatherTemp');
            const weatherDesc = document.getElementById('weatherDesc');
            const weatherWind = document.getElementById('weatherWind');
            const weatherHumidity = document.getElementById('weatherHumidity');
            const weatherCityInput = document.getElementById('weatherCity');
            
            // Default weather fetch on page load
            fetchWeather('New Delhi');
            
            fetchWeatherBtn.addEventListener('click', () => {
                const city = weatherCityInput.value.trim() || 'New Delhi';
                fetchWeather(city);
            });

            async function fetchWeather(city) {
                weatherIcon.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
                weatherTemp.textContent = '--°C';
                weatherDesc.textContent = 'Loading...';
                weatherWind.textContent = '-- km/h';
                weatherHumidity.textContent = '--%';
                
                try {
                    // In a real app, you would call a weather API here
                    // This is a mock implementation with simulated data
                    
                    setTimeout(() => {
                        const mockWeather = generateMockWeather(city);
                        displayWeather(mockWeather);
                        showNotification(`Weather for ${city} updated`, 'success');
                    }, 1000);
                } catch (error) {
                    weatherIcon.innerHTML = '<i class="fas fa-exclamation-triangle"></i>';
                    weatherDesc.textContent = 'Failed to load weather data';
                    showNotification('Error fetching weather data', 'error');
                    console.error('Weather fetch error:', error);
                }
            }

            function generateMockWeather(city) {
                const conditions = ['Sunny', 'Partly Cloudy', 'Cloudy', 'Rainy', 'Thunderstorm', 'Snowy'];
                const icons = {
                    'Sunny': 'fa-sun',
                    'Partly Cloudy': 'fa-cloud-sun',
                    'Cloudy': 'fa-cloud',
                    'Rainy': 'fa-cloud-rain',
                    'Thunderstorm': 'fa-bolt',
                    'Snowy': 'fa-snowflake'
                };
                
                const condition = conditions[Math.floor(Math.random() * conditions.length)];
                const temp = Math.floor(Math.random() * 30) + 10; // 10-40°C
                const wind = (Math.random() * 20 + 5).toFixed(1); // 5-25 km/h
                const humidity = Math.floor(Math.random() * 50) + 30; // 30-80%
                
                return {
                    city: city,
                    condition: condition,
                    icon: icons[condition],
                    temp: temp,
                    wind: wind,
                    humidity: humidity
                };
            }

            function displayWeather(data) {
                weatherIcon.innerHTML = `<i class="fas ${data.icon}"></i>`;
                weatherTemp.textContent = `${data.temp}°C`;
                weatherDesc.textContent = `${data.condition} in ${data.city}`;
                weatherWind.textContent = `${data.wind} km/h`;
                weatherHumidity.textContent = `${data.humidity}%`;
            }

            // --- Cleanup on page unload ---
            window.addEventListener('beforeunload', () => {
                // Stop camera streams
                if (photoStream) {
                    photoStream.getTracks().forEach(track => track.stop());
                }
                if (videoStream) {
                    videoStream.getTracks().forEach(track => track.stop());
                }
                
                // Stop QR scanner if running
                if (html5QrCode && html5QrCode.isScanning) {
                    html5QrCode.stop();
                }
            });
        });
    </script>
    </body>
    </html>
    """
   components.html(html_code, height=700, scrolling=True)

def javascript_simple_calculator():
    st.subheader("🟨 JavaScript - Simple Calculator (Browser)")

    html_code = """
    <style>
    .sci-calc-container {
        width: 410px;
        margin: 0 auto;
        background: #232526;
        border-radius: 18px;
        box-shadow: 0 4px 32px #0008;
        padding: 20px 16px 16px 16px;
        color: #ECECEC;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    .sci-calc-display {
        background: #191b1f;
        color: #39C1E8;
        font-size: 1.5rem;
        border-radius: 6px;
        padding: 10px;
        margin-bottom: 12px;
        min-height: 36px;
        text-align: right;
        word-break: break-all;
    }
    .sci-calc-buttons {
        display: grid;
        grid-template-columns: repeat(6, 54px);
        grid-gap: 7px;
    }
    .sci-calc-buttons button {
        background: #1abc9c;
        color: #fff;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 11px 0;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background 0.16s, transform 0.08s;
    }
    .sci-calc-buttons button.op,
    .sci-calc-buttons button.eq {
        background: #39C1E8;
        color: #232526;
    }
    .sci-calc-buttons button.ac {background: #DD2C00;}
    .sci-calc-buttons button.mem {background: #3b4856;}
    .sci-calc-buttons button:hover {
        background: #19B394;
        color: #FAFAFA;
        transform: scale(1.055);
    }
    .sci-calc-mode-toggle {
        color: #ACE0F9;
        font-size: 13px;
        margin-bottom: 3px;
        text-align: right;
    }
    </style>
    <div class="sci-calc-container">
      <div class="sci-calc-mode-toggle">
        Mode: <span id="mode">DEG</span>
        <button onclick="toggleDegRad()" style="margin-left:10px;font-size:11px; border-radius:7px;padding:2px 7px;">DEG/RAD</button>
      </div>
      <div class="sci-calc-display" id="display">0</div>
      <div class="sci-calc-buttons">
        <button class="ac" onclick="clearAll()">AC</button>
        <button onclick="backspace()">←</button>
        <button onclick="input('(')">(</button>
        <button onclick="input(')')">)</button>
        <button class="mem" onclick="memoryRecall()">MR</button>
        <button class="mem" onclick="memoryClear()">MC</button>

        <button onclick="input('7')">7</button>
        <button onclick="input('8')">8</button>
        <button onclick="input('9')">9</button>
        <button class="op" onclick="input('/')">÷</button>
        <button class="mem" onclick="memoryAdd()">M+</button>
        <button class="mem" onclick="memorySubtract()">M-</button>

        <button onclick="input('4')">4</button>
        <button onclick="input('5')">5</button>
        <button onclick="input('6')">6</button>
        <button class="op" onclick="input('*')">×</button>
        <button onclick="insertConstant('π')">π</button>
        <button onclick="insertConstant('e')">e</button>

        <button onclick="input('1')">1</button>
        <button onclick="input('2')">2</button>
        <button onclick="input('3')">3</button>
        <button class="op" onclick="input('-')">−</button>
        <button onclick="square()">x²</button>
        <button onclick="reciprocal()">1/x</button>

        <button onclick="input('0')">0</button>
        <button onclick="input('.')">.</button>
        <button onclick="input('%')">%</button>
        <button class="op" onclick="input('+')">+</button>
        <button onclick="power()">xʸ</button>
        <button onclick="sqrt()">√</button>

        <button onclick="fact()">n!</button>
        <button onclick="log()">log₁₀</button>
        <button onclick="ln()">ln</button>
        <button onclick="exp()">eˣ</button>
        <button onclick="tenPower()">10ˣ</button>
        <button class="eq" style="grid-column: span 2;" onclick="calculate()">=</button>

        <button onclick="trig('sin')">sin</button>
        <button onclick="trig('cos')">cos</button>
        <button onclick="trig('tan')">tan</button>
        <button onclick="trig('asin')">asin</button>
        <button onclick="trig('acos')">acos</button>
        <button onclick="trig('atan')">atan</button>
      </div>
    </div>
    <script>
    let expression = "";
    let powerMode = false;
    let memory = 0;
    let radMode = false;

    function updateDisplay(content=null) {
        const display = document.getElementById('display');
        display.textContent = content !== null ? content : expression || "0";
    }
    function input(val) {
      if (powerMode) {
        expression += `**${val}`;
        powerMode = false;
      } else {
        expression += val;
      }
      updateDisplay();
    }
    function clearAll() {expression = ""; updateDisplay();}
    function backspace() {expression = expression.slice(0, -1); updateDisplay();}
    function calculate() {
      let result = "";
      try {
        let exp = expression;
        exp = exp.replace(/π/g, "Math.PI");
        exp = exp.replace(/\be\b/g, "Math.E");
        exp = exp.replace(/%/g, "/100");
        exp = exp.replace(/−/g, "-");
        exp = exp.replace(/×/g, "*").replace(/÷/g, "/");
        // Functions and exponents
        exp = exp.replace(/(\d+\.?\d*)\^(\d+\.?\d*)/g, "Math.pow($1,$2)");
        exp = exp.replace(/√(\d+\.?\d*)/g, "Math.sqrt($1)");
        // Replace custom trig/ln/log tokens with JS Math equivalents
        exp = exp.replace(/sin\(/g, "mySin(");
        exp = exp.replace(/cos\(/g, "myCos(");
        exp = exp.replace(/tan\(/g, "myTan(");
        exp = exp.replace(/asin\(/g, "myAsin(");
        exp = exp.replace(/acos\(/g, "myAcos(");
        exp = exp.replace(/atan\(/g, "myAtan(");
        exp = exp.replace(/log\(/g, "myLog(");
        exp = exp.replace(/ln\(/g, "myLn(");
        // Powers
        let val = Function('mySin', 'myCos', 'myTan', 'myAsin', 'myAcos', 'myAtan', 'myLog', 'myLn', `
            "use strict";
            return (${exp})
        `)(trigWrap('sin'), trigWrap('cos'), trigWrap('tan'), trigWrap('asin'), trigWrap('acos'), trigWrap('atan'), Math.log10, Math.log);
        if (isNaN(val) || !isFinite(val)) throw "Math Error";
        result = val;
        updateDisplay(val);
        expression = val.toString();
      } catch (e) {updateDisplay("Error"); expression = "";}
    }
    function sqrt() {expression += "√("; updateDisplay();}
    function power() {expression += "^"; updateDisplay(); powerMode = true;}
    function square() {expression += "**2"; updateDisplay();}
    function reciprocal() {expression = "1/(" + expression + ")"; updateDisplay();}
    function exp() {expression += "Math.exp("; updateDisplay();}
    function tenPower() {expression += "10**"; updateDisplay();}
    function fact() {
      try {
        let n = parseFloat(expression);
        if (isNaN(n) || n < 0 || !Number.isInteger(n)) throw "";
        let res = 1;
        for (let i = 2; i <= n; i++) res *= i;
        updateDisplay(res);
        expression = res.toString();
      } catch {updateDisplay("Error"); expression = "";}
    }
    function log() {expression += "log("; updateDisplay();}
    function ln() {expression += "ln("; updateDisplay();}
    function insertConstant(val) {
        expression += val;
        updateDisplay();
    }
    function trig(t) {expression += t + "("; updateDisplay();}
    function trigWrap(name) {
      return function(x) {
        let v = Number(x);
        if(['sin','cos','tan'].includes(name) && !radMode) v = v * Math.PI / 180;
        let f = Math[name];
        if(name=="asin"||name=="acos"||name=="atan") {
            let r = f(v);
            return radMode ? r : r * 180 / Math.PI;
        }
        return f(v);
      }
    }
    function toggleDegRad() {
      radMode = !radMode;
      document.getElementById("mode").textContent = radMode ? "RAD" : "DEG";
    }
    // --- Memory operations
    function memoryAdd() {
        try {memory += Number(expression) || 0; updateDisplay("M+");} catch {}
    }
    function memorySubtract() {
        try {memory -= Number(expression) || 0; updateDisplay("M-");} catch {}
    }
    function memoryRecall() {expression += memory; updateDisplay();}
    function memoryClear() {memory = 0; updateDisplay("MC");}
    // --- Keyboard Support ---
    document.addEventListener("keydown", function(event) {
      let key = event.key;
      if ((key >= "0" && key <= "9") || key === "." || key === "(" || key === ")") input(key);
      else if (key === "+" || key === "-" || key === "*" || key === "/" || key === "^") input(key);
      else if (key === "Enter" || key === "=") { event.preventDefault(); calculate(); }
      else if (key === "%") input(key);
      else if (key === "Backspace") backspace();
      else if (key === "Delete") clearAll();
      else if (key === "s") trig('sin');
      else if (key === "c") trig('cos');
      else if (key === "t") trig('tan');
      else if (key === "l") ln();
      else if (key === "g") log();
      else if (key === "!") fact();
      else if (key === "r") sqrt();
      else if (key === "p") insertConstant("π");
      else if (key === "e") insertConstant("e");
    });
    </script>
    """

    components.html(html_code, height=620)
def javascript_moving_box():
    st.subheader("🟨 JavaScript - Moving Color Box")

    html_code = """
    <style>
        #box {
            width: 100px;
            height: 100px;
            background: linear-gradient(45deg, #1abc9c, #39C1E8);
            position: relative;
            animation: movebox 5s infinite alternate ease-in-out;
            border-radius: 12px;
        }
        @keyframes movebox {
            0% { left: 0; }
            100% { left: 80%; }
        }
    </style>
    <div id="box"></div>
    """

    components.html(html_code, height=150)

def linux_advanced_format_mount():
    import streamlit as st

    st.subheader("🧮 Advanced Format & Mount Assistant")

    device = st.text_input("Block device (e.g., /dev/sdb1):")
    fstype = st.selectbox("Filesystem type", ["ext4", "xfs", "vfat"])
    mountpoint = st.text_input("Mount point (e.g., /mnt/data):")

    if st.button("Generate commands"):
        cmds = []
        if fstype == "ext4":
            cmds.append(f"sudo mkfs.ext4 {device}")
        elif fstype == "xfs":
            cmds.append(f"sudo mkfs.xfs {device}")
        elif fstype == "vfat":
            cmds.append(f"sudo mkfs.vfat {device}")
        cmds.append(f"sudo mkdir -p {mountpoint}")
        cmds.append(f"sudo mount {device} {mountpoint}")
        cmds.append("# (Optional) Add line to /etc/fstab for automount at boot")
        st.code('\n'.join(cmds))
    st.info("Replace device name and confirm before execution.")


def linux_disk_usage_analyzer():
    import streamlit as st
    import subprocess

    st.subheader("🗂️ Disk Usage Analyzer (Largest Directories)")

    path = st.text_input("Directory to analyze", "/")
    depth = st.slider("Directory depth", 1, 5, 2)
    count = st.slider("Show top N directories", 5, 30, 10)

    # Build du command for top-level usage breakdown
    cmd = f"sudo du -h --max-depth={depth} {path} | sort -hr | head -n {count}"
    st.info(f"Command: `{cmd}`")
    if st.button("Analyze"):
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
            st.code(output)
        except Exception as e:
            st.error(f"Error: {e}")


def linux_nfs_mount_tool():
    import streamlit as st

    st.subheader("📡 NFS/Remote Filesystem Mount Tool")

    remote_server = st.text_input("Remote server (e.g., 10.10.10.20):")
    remote_export = st.text_input("Remote export path (e.g., /export/data):")
    mount_point = st.text_input("Local mount point (e.g., /mnt/nfs):")

    if st.button("Show mount command"):
        mount_cmd = f"sudo mount -t nfs {remote_server}:{remote_export} {mount_point}"
        st.code(mount_cmd)
        st.markdown("To unmount:")
        st.code(f"sudo umount {mount_point}")
    st.info("Ensure nfs-utils is installed and that the server is reachable.")


def linux_lvm_manager():
    import streamlit as st

    st.subheader("🗄️ LVM Management & Commands")

    st.markdown("""
Logical Volume Manager (LVM) lets you create flexible storage pools.
Typical workflow:
- Create Physical Volume (PV)
- Create Volume Group (VG)
- Create Logical Volume (LV)
- Format and mount
""")
    # LVM command builder
    pv = st.text_input("Physical disk (e.g., /dev/sdb):")
    vg = st.text_input("Volume Group name:")
    lv = st.text_input("Logical Volume name:")
    size = st.text_input("LV size (e.g., 10G):")

    if st.button("Show Full Workflow"):
        steps = f"""
sudo pvcreate {pv}
sudo vgcreate {vg} {pv}
sudo lvcreate -L {size} -n {lv} {vg}
sudo mkfs.ext4 /dev/{vg}/{lv}
sudo mkdir /mnt/{lv}
sudo mount /dev/{vg}/{lv} /mnt/{lv}
# View LVM: sudo lvs; sudo vgs; sudo pvs
"""
        st.code(steps)
    st.info("Always review disk names carefully before running commands.")

def linux_advanced_disk_info():
    import streamlit as st
    import subprocess

    st.subheader("🖴 Advanced Disk & SMART Data")

    st.markdown("""
Shows block devices, partition types, filesystem, mount points, UUIDs and disk health (if supported).
""")
    cmds = [
        ("lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT,UUID,MODEL", "List block devices with details"),
        ("sudo fdisk -l", "Show disk partition tables"),
        ("sudo blkid", "Display all block device attributes"),
        ("sudo smartctl -a /dev/sda", "Show SMART data (replace sda, requires smartmontools)")
    ]
    selected = st.selectbox("Choose command:", [desc for _, desc in cmds])
    cmd = [c for c, d in cmds if d == selected][0]

    st.info(f"Command: `{cmd}`")
    if st.button("Run"):
        try:
            result = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT).decode()
            st.code(result)
        except Exception as e:
            st.error(f"Error: {e}")

def linux_redhat_yum_setup():
    import streamlit as st

    st.subheader("🍒 RedHat: YUM Repo File Generator")

    st.markdown("""
**YUM Setup Steps (with ISO/DVD):**
1. Attach your RHEL ISO or DVD, note the mounted paths (e.g., `/run/media/username/RHEL-8-0-0-BaseOS-x86_64/BaseOS` and `.../AppStream`)
2. This tool lets you generate the proper `.repo` file.<br>
3. You can preview and download the final repo file, then copy it to `/etc/yum.repos.d/` on your RedHat system (as root).
    """)

    # Input fields
    baseos_path = st.text_input("BaseOS directory path:", "/run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS/")
    appstream_path = st.text_input("AppStream directory path:", "/run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream/")
    repo_filename = st.text_input("Output repo filename (ex: rhel-offline.repo):", "rhel-offline.repo")
    gpgcheck = st.selectbox("GPG check enabled?", ["0 (off)", "1 (on)"], index=0)
    enabled = st.selectbox("Enable repo?", ["1 (yes)", "0 (no)"], index=0)

    # Render .repo content dynamically
    repo_content = f"""
[BaseOS]
name=BaseOS
baseurl=file://{baseos_path}
enabled={enabled[0]}
gpgcheck={gpgcheck[0]}

[AppStream]
name=AppStream
baseurl=file://{appstream_path}
enabled={enabled[0]}
gpgcheck={gpgcheck[0]}
"""

    st.markdown("#### Preview of repo file:")
    st.code(repo_content.strip())

    st.info("After download, copy this repo file to `/etc/yum.repos.d/` using `sudo cp`. Then run `yum repolist`.")

    # Download button
    st.download_button(
        label="Download repo file",
        data=repo_content.strip(),
        file_name=repo_filename,
        mime="text/plain"
    )


def linux_networking_commands():
    st.subheader("🌐 Linux Networking Commands")
    st.markdown("""
- **ip a** / **ip addr** – Show all network interfaces and IPs
- **ip link show** – Show all interfaces and their status
- **ip link set eth0 up/down** – Enable/disable interface
- **ip route show** – Show routing table
- **ping <host>** – Ping network host
- **traceroute <host>** – Trace network hops
- **netstat -tulnp** – Active connections, ports
- **tcpdump -i eth0** – Capture traffic on eth0
- **nslookup <host>** – Query DNS
- **ifconfig (old)** – Legacy, but still on some sytems
- **mtr <host>** – Real-time traceroute + ping
- **arp -a** – Show ARP table
""")
    import subprocess
    command = st.text_input("⚡ Enter a Linux networking command to run (read-only, not interactive):", "ip a")
    if st.button("Run Command"):
        st.info(f"Result of: `{command}`")
        try:
            result = subprocess.check_output(command.split(), stderr=subprocess.STDOUT).decode()
            st.code(result)
        except Exception as e:
            st.error(f"Error: {e}")

def linux_menu():
    st.subheader("🔧 Linux Command Menu")
    
    linux_commands = [
        "Show current directory (pwd)",
        "List files (ls -l)",
        "Show current user (whoami)",
        "Show disk usage (df -h)",
        "Show memory usage (free -m)",
        "Create directory (mkdir)",
        "Delete a file (rm)",
        "Copy a file (cp)",
        "Move a file (mv)",
        "Edit file with nano",
        "Show running processes (ps aux)",
        "Search a file (find)",
        "Show system monitor (top)",
        "Show system uptime",
        "Show hostname",
        "Show IP address (ifconfig)",
        "Ping a host",
        "Show command history",
        "Show current date/time",
        "Show calendar (cal)",
        "Show logged-in users (who)",
        "Show kernel/system info (uname -a)",
        "Disk usage of folders (du -sh *)",
        "Clear screen",
        "Print message with echo",
        "Change directory (cd)"
    ]
    
    command = st.selectbox("Select Linux Command", linux_commands)
    
    if st.button("🚀 Execute Command"):
        if linux_commands.index(command) == 0:
            st.code(os.getcwd())
        elif linux_commands.index(command) == 1:
            st.code(os.popen("ls -l").read())
        elif linux_commands.index(command) == 2:
            st.code(os.popen("whoami").read())
        elif linux_commands.index(command) == 3:
            st.code(os.popen("df -h").read())
        elif linux_commands.index(command) == 4:
            st.code(os.popen("free -m").read())
        elif linux_commands.index(command) == 5:
            name = st.text_input("Directory name")
            if name:
                os.makedirs(name, exist_ok=True)
                st.success(f"Directory '{name}' created!")
        elif linux_commands.index(command) == 6:
            name = st.text_input("File to delete")
            if name:
                os.system(f"rm -i {name}")
                st.success(f"File '{name}' deleted!")
        elif linux_commands.index(command) == 7:
            src = st.text_input("Source file")
            dest = st.text_input("Destination")
            if src and dest:
                os.system(f"cp {src} {dest}")
                st.success(f"Copied '{src}' to '{dest}'!")
        elif linux_commands.index(command) == 8:
            src = st.text_input("Source file")
            dest = st.text_input("Destination")
            if src and dest:
                os.system(f"mv {src} {dest}")
                st.success(f"Moved '{src}' to '{dest}'!")
        elif linux_commands.index(command) == 9:
            fname = st.text_input("File to edit")
            if fname:
                os.system(f"nano {fname}")
        elif linux_commands.index(command) == 10:
            st.code(os.popen("ps aux").read())
        elif linux_commands.index(command) == 11:
            fname = st.text_input("File to search")
            if fname:
                st.code(os.popen(f"find / -name {fname} 2>/dev/null").read())
        elif linux_commands.index(command) == 12:
            st.code(os.popen("top").read())
        elif linux_commands.index(command) == 13:
            st.code(os.popen("uptime").read())
        elif linux_commands.index(command) == 14:
            st.code(os.popen("hostname").read())
        elif linux_commands.index(command) == 15:
            st.code(os.popen("ifconfig").read())
        elif linux_commands.index(command) == 16:
            host = st.text_input("Enter host to ping")
            if host:
                st.code(os.popen(f"ping -c 4 {host}").read())
        elif linux_commands.index(command) == 17:
            st.code(os.popen("history").read())
        elif linux_commands.index(command) == 18:
            st.code(os.popen("date").read())
        elif linux_commands.index(command) == 19:
            st.code(os.popen("cal").read())
        elif linux_commands.index(command) == 20:
            st.code(os.popen("who").read())
        elif linux_commands.index(command) == 21:
            st.code(os.popen("uname -a").read())
        elif linux_commands.index(command) == 22:
            st.code(os.popen("du -sh *").read())
        elif linux_commands.index(command) == 23:
            os.system("clear")
            st.success("Screen cleared!")
        elif linux_commands.index(command) == 24:
            msg = st.text_input("Enter message to echo")
            if msg:
                st.code(os.popen(f"echo {msg}").read())
        elif linux_commands.index(command) == 25:
            new_dir = st.text_input("Enter path to change directory")
            if new_dir:
                try:
                    os.chdir(new_dir)
                    st.success(f"Changed to: {os.getcwd()}")
                except Exception as e:
                    st.error(f"Error: {e}")

def docker_project():
    def run_cmd(cmd):
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else result.stderr.strip()

    st.subheader("🐳 Docker Automation Dashboard")

    menu = [
        "Dashboard Overview",
        "List Containers",
        "Start/Stop Containers",
        "Remove Container",
        "Build Docker Image",
        "Run Docker Container",
        "List/Remove Images",
        "View Logs",
        "Exec Command",
        "Docker-in-Docker"
    ]

    choice = st.sidebar.selectbox("Select Operation", menu)

    if choice == "Dashboard Overview":
        st.write("Running Containers")
        st.code(run_cmd("docker ps"))
        st.write("All Images")
        st.code(run_cmd("docker images"))
        st.write("All Volumes")
        st.code(run_cmd("docker volume ls"))
        st.write("All Networks")
        st.code(run_cmd("docker network ls"))

    elif choice == "List Containers":
        st.write("📦 Containers")
        if st.button("List Running Containers"):
            st.code(run_cmd("docker ps"))
        if st.button("List All Containers"):
            st.code(run_cmd("docker ps -a"))

    elif choice == "Start/Stop Containers":
        container_id = st.text_input("Enter Container ID or Name")
        if st.button("Start"):
            st.code(run_cmd(f"docker start {container_id}"))
        if st.button("Stop"):
            st.code(run_cmd(f"docker stop {container_id}"))
        if st.button("Restart"):
            st.code(run_cmd(f"docker restart {container_id}"))

    elif choice == "Remove Container":
        container_id = st.text_input("Enter Container ID or Name to Remove")
        if st.button("Remove Container"):
            st.warning("This will permanently delete the container")
            st.code(run_cmd(f"docker rm {container_id}"))

    elif choice == "Build Docker Image":
        path = st.text_input("Enter Path to Dockerfile Directory")
        image_name = st.text_input("Enter Image Name (e.g. myapp:latest)")
        if st.button("Build Image"):
            st.code(run_cmd(f"docker build -t {image_name} {path}"))

    elif choice == "Run Docker Container":
        image = st.text_input("Docker Image")
        cname = st.text_input("Container Name")
        port = st.text_input("Ports (8080:80)")
        vol = st.text_input("Volumes (/host:/container)")
        envs = st.text_input("Env Vars (ENV=val)")
        detach = st.checkbox("Detached Mode", value=True)
        priv = st.checkbox("Privileged Mode", value=False)
        if st.button("Run Container"):
            cmd = "docker run"
            if detach: cmd += " -d"
            if port: cmd += f" -p {port}"
            if vol: cmd += f" -v {vol}"
            if envs: cmd += f" -e {envs}"
            if cname: cmd += f" --name {cname}"
            if priv: cmd += " --privileged"
            cmd += f" {image}"
            st.code(run_cmd(cmd))

    elif choice == "List/Remove Images":
        if st.button("List Images"):
            st.code(run_cmd("docker images"))
        image_name = st.text_input("Enter Image Name or ID to Remove")
        if st.button("Remove Image"):
            st.code(run_cmd(f"docker rmi {image_name}"))

    elif choice == "View Logs":
        log_id = st.text_input("Enter Container ID for Logs")
        if st.button("Show Logs"):
            st.code(run_cmd(f"docker logs --tail 50 {log_id}"))

    elif choice == "Exec Command":
        cont = st.text_input("Container Name/ID")
        shell = st.text_input("Command to Execute (e.g., ls /)")
        if st.button("Execute"):
            st.code(run_cmd(f"docker exec {cont} {shell}"))

    elif choice == "Docker-in-Docker":
        dind_name = st.text_input("Docker-in-Docker Container Name", "my-dind")
        if st.button("Start DinD Container"):
            st.code(run_cmd(f"docker run --privileged --name {dind_name} -d docker:dind"))
        if st.button("List Containers Inside DinD"):
            st.code(run_cmd(f"docker exec {dind_name} docker ps"))
        inner_cmd = st.text_input("Run Docker Command Inside DinD (e.g., docker version)")
        if st.button("Run Inside DinD"):
            st.code(run_cmd(f"docker exec {dind_name} {inner_cmd}"))


def python_face_swap():
    st.subheader("U0001f9d1‍U0001f91d‍U0001f9d1 Python Task: Face Swapping (Webcam)")

    st.warning("⚠ Face swapping requires webcam access and uses OpenCV. This will open an external window.")

    if st.button("Start Face Swap"):
        import cv2
        from cvzone.FaceDetectionModule import FaceDetector

        def capture_face(prompt_key, cap):
            while True:
                success, frame = cap.read()
                frame = cv2.flip(frame, 1)
                cv2.imshow("Webcam", frame)

                key = cv2.waitKey(1)
                if key == ord(prompt_key):
                    return frame.copy()

        def face_swap(face1, face2, detector):
            face1 = cv2.resize(face1, (640, 480))
            face2 = cv2.resize(face2, (640, 480))

            face1_detected, bboxs1 = detector.findFaces(face1)
            face2_detected, bboxs2 = detector.findFaces(face2)

            if bboxs1 and bboxs2:
                x1, y1, w1, h1 = bboxs1[0]['bbox']
                x2, y2, w2, h2 = bboxs2[0]['bbox']

                x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
                w1, h1, w2, h2 = map(int, [w1, h1, w2, h2])

                crop1 = face1[y1:y1+h1, x1:x1+w1]
                crop2 = face2[y2:y2+h2, x2:x2+w2]

                target_w = min(w1, w2)
                target_h = min(h1, h2)

                crop1_resized = cv2.resize(crop1, (target_w, target_h))
                crop2_resized = cv2.resize(crop2, (target_w, target_h))

                face1[y1:y1+target_h, x1:x1+target_w] = crop2_resized
                face2[y2:y2+target_h, x2:x2+target_w] = crop1_resized

                cv2.imshow("Swapped Face 1", face1)
                cv2.imshow("Swapped Face 2", face2)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                st.error("❌ Face not detected in one or both photos.")

        cap = cv2.VideoCapture(0)
        detector = FaceDetector()

        st.info("📸 Face Swapper Ready! Press 's' for face1, 'd' for face2")

        face1 = capture_face('s', cap)
        st.success("✅ Face 1 captured.")

        face2 = capture_face('d', cap)
        st.success("✅ Face 2 captured. Swapping...")

        face_swap(face1, face2, detector)

        cap.release()
        cv2.destroyAllWindows()

def python_hello_world():
    st.subheader("🐍 Python Task: Hello World")
    st.write("Hello from Python task!")

def python_name_input():
    st.subheader("🐍 Python Task: Name Greeting")
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Welcome, {name}!")

def python_digital_image():
    st.subheader("🖼 Python Task: Digital Image Creation")
    height = 200
    width = 300
    image = np.zeros((height, width, 3), dtype=np.uint8)
    image[50:150, 50:150] = [255, 0, 0]
    image[50:150, 160:260] = [0, 255, 0]
    image[180:200, :] = [0, 0, 255]
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.set_title("Digital Image")
    ax.axis('off')
    st.pyplot(fig)

def batch_image_resize():
    st.subheader("🖼️ Batch Image Resizer")

    files = st.file_uploader("Upload Images", accept_multiple_files=True, type=["jpg", "jpeg", "png"])
    width = st.number_input("Width", min_value=1, max_value=10000, value=500)
    height = st.number_input("Height", min_value=1, max_value=10000, value=500)

    if st.button("Resize All"):
        if not files:
            st.warning("Please upload at least one image.")
            return

        for file in files:
            try:
                img = Image.open(file)
                img_resized = img.resize((width, height))

                # Convert to BytesIO for display
                img_bytes = io.BytesIO()
                img_resized.save(img_bytes, format="PNG")
                img_bytes.seek(0)

                st.image(img_bytes, caption=f"Resized: {file.name}", use_column_width=False)
            except Exception as e:
                st.error(f"Failed to process {file.name}: {e}")

def python_send_sms():
    st.subheader("📱 Python Task: Send SMS with Twilio")
    to_number = st.text_input("📾 Enter mobile number with country code:")
    message_text = st.text_area("💬 Enter message text:", value="Hello from Twilio via Streamlit!")
    if st.button("📤 Send SMS"):
        try:
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)
            message = client.messages.create(body=message_text, from_='+12513060511', to=to_number.strip())
            st.success(f"✅ Message sent successfully! SID: {message.sid}")
        except Exception as e:
            st.error(f"❌ Failed to send message: {e}")

def python_Google_Search():
    st.subheader("🔍 Python Task: Google Search")
    query = st.text_input("Enter search query:")
    if st.button("🔎 Search Now"):
        if query:
            try:
                results = search(query, num_results=5)
                st.write(f"Top 5 results for: *{query}*")
                for i, url in enumerate(results, 1):
                    st.markdown(f"{i}. [{url}]({url})")
            except Exception as e:
                st.error(f"❌ Google Search failed: {e}")

def python_send_email():
    st.subheader("📧 Python Task: Send Email via Gmail")
    sender_email = st.text_input("Sender Gmail:")
    app_password = st.text_input("App Password (16 char)", type="password")
    receiver_email = st.text_input("Receiver Email:")
    subject = st.text_input("Subject", value="Hello from Streamlit!")
    content = st.text_area("Message Content", value="This is a test email sent from Streamlit app.")

    if st.button("📨 Send Email"):
        try:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg.set_content(content)

            smtp_server = 'smtp.gmail.com'
            smtp_port = 587

            with smtplib.SMTP(smtp_server, smtp_port) as smtp:
                smtp.starttls()
                smtp.login(sender_email, app_password)
                smtp.send_message(msg)

            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")

def python_pdf_to_text():
    st.subheader("📄 PDF to Text Extraction")

    uploaded = st.file_uploader("Upload PDF file", type=["pdf"])
    if uploaded:
        try:
            reader = PyPDF2.PdfReader(uploaded)
            out = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    out += text + "\n"
                else:
                    out += "[No text found on this page]\n"
            st.text_area("Extracted Text", out, height=300)
        except Exception as e:
            st.error(f"Error: {e}")

def python_qr_generator():
    st.subheader("🔳 Python Task: QR Code Generator")
    
    data = st.text_input("Enter data to encode:")
    
    if st.button("Generate QR"):
        img = qrcode.make(data)
        
        # Convert PIL Image to BytesIO for Streamlit
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        
        st.image(buffer, caption="Your QR Code", use_column_width=False)
def python_web_scraper():
    st.subheader("🌐 Python Task: Web Scraper")
    start_url = st.text_input("Enter website URL (e.g., https://example.com):")
    if st.button("🕷 Start Scraping"):
        if start_url:
            os.makedirs("downloaded_site", exist_ok=True)
            visited = set()

            def is_internal_link(base_url, link):
                return urlparse(link).netloc == '' or urlparse(link).netloc == urlparse(base_url).netloc

            def sanitize_filename(url):
                parsed = urlparse(url)
                path = parsed.path.strip("/")
                return "index.html" if not path else path.replace("/", "_") + ".html"

            def save_page(url, html):
                filename = sanitize_filename(url)
                with open(os.path.join("downloaded_site", filename), "w", encoding="utf-8") as f:
                    f.write(html)

            def crawl(url, base_url):
                if url in visited:
                    return
                visited.add(url)
                try:
                    response = requests.get(url, timeout=5)
                    response.raise_for_status()
                    html = response.text
                    save_page(url, html)
                    soup = BeautifulSoup(html, "html.parser")
                    for link_tag in soup.find_all("a", href=True):
                        href = link_tag['href']
                        full_url = urljoin(url, href)
                        if is_internal_link(base_url, full_url):
                            crawl(full_url, base_url)
                except Exception as e:
                    st.warning(f"[!] Failed to crawl {url}: {e}")

            crawl(start_url, start_url)
            st.success("✅ Site downloaded in 'downloaded_site' folder!")

def python_make_call():
    st.subheader("📞 Python Task: Make a Call with Twilio")
    to_number = st.text_input("📰 Enter mobile number with country code:", value="+919460558829")
    if st.button("📞 Call Now"):
        try:
            account_sid = 'wow'
            auth_token = 'wow'
            twilio_number = 'num'
            twiml_url = 'http://demo.twilio.com/docs/voice.xml'
            client = Client(account_sid, auth_token)
            call = client.calls.create(
                url=twiml_url,
                to=to_number,
                from_=twilio_number
            )
            st.success(f"✅ Call initiated! Call SID: {call.sid}")
        except Exception as e:
            st.error(f"❌ Failed to make call: {e}")

def python_gemini_api():
    st.subheader("🧐 Python Task: Ask Gemini AI")
    prompt = st.text_area("Enter your question for Gemini:")
    if st.button("Ask Gemini"):
        try:
            google_gemini_key = "AIzaSyAoDWA3cR_ZrrRsJlXGjj1iv4RC18nEklg"
            mod = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=google_gemini_key)
            message = [
                {"role": "system", "content": "you are a coding teacher give me output of any question in just 4 lines"},
                {"role": "user", "content": prompt}
            ]
            output = mod.chat.completions.create(messages=message, model="gemini-1.5-flash")
            st.success(output.choices[0].message.content)
        except Exception as e:
            st.error(f"❌ Gemini API error: {e}")

def ml_emi_predictor():
    st.markdown("""
        <style>
            .main-title { text-align: center; font-size: 40px; color: #2874A6; font-weight: bold; }
            .sub-title { text-align: center; font-size: 20px; color: #555; }
            .result-box {
                background-color: #D6EAF8; padding: 20px; border-radius: 10px;
                text-align: center; font-size: 24px; color: #154360; border: 2px solid #AED6F1; margin-top: 20px;
            }
            .safe-box {
                padding: 10px; border-radius: 8px; margin-top: 10px;
                text-align: center; font-size: 20px; font-weight: bold;
            }
            .safe { background-color: #D5F5E3; color: #1E8449; border: 2px solid #ABEBC6; }
            .risky { background-color: #FADBD8; color: #C0392B; border: 2px solid #F5B7B1; }
            .footer { text-align: center; color: #999; margin-top: 50px; }
        </style>
    """, unsafe_allow_html=True)

    # --- Title ---
    st.markdown('<div class="main-title">💼 EMI & Insurance Planner</div>', unsafe_allow_html=True)

    # --- User Choice ---
    st.sidebar.header("🔘 Choose Your Tool")
    mode = st.sidebar.radio("What would you like to use?", ["Loan EMI Calculator", "Insurance Planner"])

    # ------------------------------------------------------------------------
    # 1️⃣ Loan EMI Calculator
    # ------------------------------------------------------------------------
    if mode == "Loan EMI Calculator":
        st.markdown('<div class="sub-title">🏦 Smart Loan EMI Analysis</div>', unsafe_allow_html=True)

        loan_type = st.sidebar.selectbox("Loan Type", ["Home Loan", "Car Loan", "Personal Loan"])
        default_interest = {"Home Loan": 8.5, "Car Loan": 9.5, "Personal Loan": 12.5}
        interest_rate = default_interest[loan_type]

        loan_amount = st.sidebar.number_input("Loan Amount (₹)", min_value=10000, max_value=10000000, value=500000, step=1000)
        user_rate = st.sidebar.number_input("Annual Interest Rate (%)", min_value=1.0, max_value=25.0, value=interest_rate, step=0.1)
        tenure_years = st.sidebar.slider("Loan Tenure (Years)", 1, 30, 5)
        monthly_income = st.sidebar.number_input("Monthly Income (₹)", min_value=5000, max_value=1000000, value=40000, step=1000)

        tenure_months = tenure_years * 12
        monthly_interest = user_rate / (12 * 100)

        try:
            emi = loan_amount * monthly_interest * (1 + monthly_interest) ** tenure_months
            emi /= ((1 + monthly_interest) ** tenure_months - 1)
            emi = np.round(emi, 2)
        except ZeroDivisionError:
            emi = 0.0

        emi_ratio = emi / monthly_income
        safe = emi_ratio < 0.4

        # Display EMI
        st.markdown(f"""<div class="result-box">💰 Monthly EMI for <strong>{loan_type}</strong>: <strong>₹{emi:,.2f}</strong></div>""", unsafe_allow_html=True)

        # Risk Suggestion
        if safe:
            st.markdown('<div class="safe-box safe">✅ EMI is Affordable. Loan likely to be approved.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="safe-box risky">⚠ EMI is High Compared to Income. Risk of Rejection.</div>', unsafe_allow_html=True)

        # Loan Type Suggestion
        st.subheader("📊 Loan Suggestion Based on Your EMI")
        if emi < 5000:
            st.success("✔ You can easily go for *Personal Loan or Used Car Loan*.")
        elif emi < 15000:
            st.info("ℹ You may consider a *New Car Loan or Home Renovation Loan*.")
        else:
            st.warning("💡 Based on EMI, a *Home Loan* is most suitable for this amount.")

        # Amortization Table
        st.subheader("📆 EMI Amortization Table")
        balance = loan_amount
        amort_data = []
        for i in range(1, tenure_months + 1):
            interest = balance * monthly_interest
            principal = emi - interest
            balance -= principal
            amort_data.append([i, emi, round(principal, 2), round(interest, 2), max(round(balance, 2), 0)])
        df_amort = pd.DataFrame(amort_data, columns=["Month", "EMI", "Principal", "Interest", "Balance"])
        st.dataframe(df_amort.style.format({"EMI": "₹{:.2f}", "Principal": "₹{:.2f}", "Interest": "₹{:.2f}", "Balance": "₹{:.2f}"}), use_container_width=True)

        # EMI Chart
        st.subheader("📉 EMI Breakdown Over Time")
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(df_amort["Month"], df_amort["Principal"], label="Principal Paid", color="#28B463")
        ax.plot(df_amort["Month"], df_amort["Interest"], label="Interest Paid", color="#E74C3C")
        ax.set_xlabel("Month")
        ax.set_ylabel("Amount (₹)")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    # ------------------------------------------------------------------------
    # 2️⃣ Insurance Planner
    # ------------------------------------------------------------------------
    elif mode == "Insurance Planner":
        st.markdown('<div class="sub-title">🛡 Smart Insurance Estimator</div>', unsafe_allow_html=True)

        # Insurance Input
        insurance_type = st.selectbox("Insurance Type", ["Health Insurance", "Life Insurance", "Vehicle Insurance"])
        age = st.number_input("Enter Your Age", min_value=18, max_value=100, value=30)
        sum_insured = st.number_input("Sum Insured (₹)", min_value=100000, max_value=10000000, value=500000, step=100000)
        tenure = st.slider("Policy Tenure (Years)", 1, 30, 10)
        smoker = st.radio("Are you a smoker?", ["No", "Yes"])
        critical_illness = st.checkbox("Add Critical Illness Cover")

        # Premium Estimation Logic
        base_rate = 0.0008 if insurance_type == "Life Insurance" else 0.0012
        risk_factor = 1.5 if smoker == "Yes" else 1.0
        illness_factor = 1.2 if critical_illness else 1.0
        age_factor = 1.0 + ((age - 30) * 0.02) if age > 30 else 1.0

        annual_premium = sum_insured * base_rate * risk_factor * illness_factor * age_factor
        total_premium = annual_premium * tenure

        st.subheader("📋 Estimated Insurance Details")
        st.success(f"📌 Annual Premium: ₹{annual_premium:,.2f}")
        st.info(f"💰 Total Cost over {tenure} years: ₹{total_premium:,.2f}")

        # Insurance Tips
        if insurance_type == "Health Insurance" and age > 45:
            st.warning("🩺 Tip: Consider a plan with pre-existing disease coverage.")
        elif insurance_type == "Vehicle Insurance":
            st.info("🚗 Tip: Don't forget to include zero-depreciation add-on for new vehicles.")

    # --- Footer ---
    st.markdown('<div class="footer">Made with ❤ using Streamlit | EMI & Insurance Planner</div>', unsafe_allow_html=True)


def ml_student_performance():
    # -----------------------
    # 🎯 Page Setup
    # -----------------------
    st.title("📚 AI-Powered Student Performance Dashboard")
    st.markdown("Predict, Analyze, and Improve Student Outcomes with Smart Insights")

    # -----------------------
    # 🔧 Utility Functions
    # -----------------------
    def add_download_button(df, filename):
        csv = df.to_csv(index=False).encode()
        b64 = base64.b64encode(csv).decode()
        st.markdown(f'<a href="data:file/csv;base64,{b64}" download="{filename}">📅 Download CSV</a>', unsafe_allow_html=True)

    def suggest_college(score):
        if score >= 90:
            return "🎓 Tier 1 College (IITs, NITs, IIITs)"
        elif score >= 75:
            return "🏫 Tier 2 College (State/Private Universities)"
        elif score >= 60:
            return "🏢 Tier 3 College (General Admission Colleges)"
        else:
            return "🔁 Suggest Improvement & Reattempt"

    def score_to_gpa(score):
        if score >= 90: return 10
        elif score >= 80: return 9
        elif score >= 70: return 8
        elif score >= 60: return 7
        elif score >= 50: return 6
        elif score >= 40: return 5
        else: return 0

    @st.cache_data
    def load_sample_data():
        sample_csv = """
StudentName,StudyHours,SleepHours,Attendance,AssignmentsCompleted,InternetUsage,FinalScore
John Doe,6,7,85,90,3,82
Jane Smith,8,6,92,100,2,95
Rahul Kumar,4,5,70,60,6,55
Anjali Mehra,5.5,8,78,80,3.5,75
Arjun Rathi,3,6.5,60,50,7,45
"""
        from io import StringIO
        return pd.read_csv(StringIO(sample_csv))

    # -----------------------
    # 📁 Data Handling
    # -----------------------
    st.sidebar.header("📂 Dataset Options")
    use_sample = st.sidebar.checkbox("Use Sample Dataset", True)

    if use_sample:
        df = load_sample_data()
    else:
        uploaded_file = st.sidebar.file_uploader("Upload CSV with StudentName, StudyHours, SleepHours, Attendance, AssignmentsCompleted, InternetUsage (hrs)", type=["csv"])
        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file)
                # Check if required columns exist
                required_columns = ['StudentName', 'StudyHours', 'SleepHours', 'Attendance', 
                                  'AssignmentsCompleted', 'InternetUsage', 'FinalScore']
                missing_columns = [col for col in required_columns if col not in df.columns]
                
                if missing_columns:
                    st.error(f"❌ Missing required columns: {', '.join(missing_columns)}")
                    st.info("ℹ Please upload a file with all required columns or use sample data")
                    st.stop()
            except Exception as e:
                st.error(f"❌ Error reading file: {e}")
                st.stop()
        else:
            st.info("ℹ Please upload a CSV file or use sample data")
            st.stop()

    # -----------------------
    # 🔄 Dataset Editor
    # -----------------------
    with st.sidebar.expander("📝 Edit Dataset"):
        df = st.data_editor(df, use_container_width=True, num_rows="dynamic")
        add_download_button(df, "modified_dataset.csv")

    # ➕ Add New Student Entry
    with st.sidebar.expander("➕ Add New Student"):
        with st.form("add_form"):
            name = st.text_input("Student Name")
            study = st.slider("Study Hours", 1.0, 12.0, 6.0)
            sleep = st.slider("Sleep Hours", 3.0, 10.0, 7.0)
            att = st.slider("Attendance (%)", 50, 100, 80)
            assign = st.slider("Assignments Completed (%)", 0, 100, 80)
            net = st.slider("Internet Usage (hrs/day)", 0.0, 10.0, 3.0)
            final = st.slider("Final Score (%)", 0, 100, 75)
            submitted = st.form_submit_button("Add Student")
            if submitted:
                new_row = pd.DataFrame([[name, study, sleep, att, assign, net, final]],
                                     columns=df.columns)
                df = pd.concat([df, new_row], ignore_index=True)
                st.success(f"✅ Added {name} to dataset")

    # 🔍 Search Student
    with st.sidebar.expander("🔍 Search Student"):
        query = st.text_input("Enter Student Name").strip().lower()
        if query:
            result_df = df[df["StudentName"].str.lower().str.contains(query)]
            st.write("🔎 Results:")
            st.dataframe(result_df)

    # 📊 GPA Calculation
    df['GPA'] = df['FinalScore'].apply(score_to_gpa)

    # 📊 Summary
    with st.sidebar.expander("📊 Dataset Summary"):
        st.metric("Total Students", len(df))
        st.metric("Average Score", f"{df['FinalScore'].mean():.2f}")
        st.metric("Score Range", f"{df['FinalScore'].min()} - {df['FinalScore'].max()}")

    # -----------------------
    # 🧐 Model Training
    # -----------------------
    features = ['StudyHours', 'SleepHours', 'Attendance', 'AssignmentsCompleted', 'InternetUsage']
    model = LinearRegression()
    X = df[features]
    y = df['FinalScore'] if 'FinalScore' in df else None

    if y is not None:
        model.fit(X, y)
        y_pred = model.predict(X)
        y_pred = np.clip(y_pred, 0, 100)
        metrics = {
            'R² Score': r2_score(y, y_pred),
            'MAE': mean_absolute_error(y, y_pred),
            'MSE': mean_squared_error(y, y_pred)
        }

    # -----------------------
    # 🚀 Tabs
    # -----------------------
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📊 Data & Metrics", "🎯 Single Prediction", "📁 Batch Prediction", 
        "📈 Visualize", "🧪 Performance Report", "🎓 College Suggestions"
    ])

    # 📊 Tab 1: Data & Metrics
    with tab1:
        st.subheader("📋 Current Dataset")
        st.dataframe(df, use_container_width=True)
        if y is not None:
            st.markdown("### 📉 Model Metrics")
            st.metric("R² Score", f"{metrics['R² Score']:.2f}")
            st.metric("MAE", f"{metrics['MAE']:.2f}")
            st.metric("MSE", f"{metrics['MSE']:.2f}")

    # 🎯 Tab 2: Single Prediction
    with tab2:
        st.subheader("🎯 Predict Individual Student Performance")
        c1, c2, c3 = st.columns(3)
        with c1:
            study = st.slider("📚 Study Hours", 1.0, 12.0, 6.0, key='study1')
            assignments = st.slider("🗑 Assignments Completed (%)", 0, 100, 80, key='assign1')
        with c2:
            sleep = st.slider("💤 Sleep Hours", 3.0, 10.0, 6.5, key='sleep1')
            internet = st.slider("🌐 Internet Usage (hrs/day)", 0.0, 10.0, 3.0, key='internet1')
        with c3:
            attendance = st.slider("🏫 Attendance (%)", 50, 100, 80, key='attendance1')
            student_name = st.text_input("👤 Student Name", value="John Doe", key='name1')

        input_array = np.array([[study, sleep, attendance, assignments, internet]])
        raw_pred = model.predict(input_array)[0]
        pred = max(0, min(100, raw_pred))
        st.success(f"📚 Predicted Final Score for {student_name}: {pred:.2f} / 100")
        st.info(f"🎓 Suggested College: {suggest_college(pred)}")
        st.info(f"📊 Estimated GPA: {score_to_gpa(pred)}")
        if raw_pred > 100:
            st.warning("⚠ Predicted score capped to 100%")

    # 📁 Tab 3: Batch Prediction
    with tab3:
        st.subheader("📁 Predict Scores from File")
        batch_file = st.file_uploader("Upload file with StudentName, StudyHours, SleepHours, Attendance, AssignmentsCompleted, InternetUsage", 
                                    type=["csv"], key="batch")
        if batch_file:
            try:
                batch_df = pd.read_csv(batch_file)
                # Check if required columns exist
                required_features = ['StudyHours', 'SleepHours', 'Attendance', 'AssignmentsCompleted', 'InternetUsage']
                missing_features = [col for col in required_features if col not in batch_df.columns]
                
                if missing_features:
                    st.error(f"❌ Missing required columns in batch file: {', '.join(missing_features)}")
                else:
                    batch_pred = model.predict(batch_df[features])
                    batch_df['PredictedScore'] = np.clip(batch_pred, 0, 100)
                    batch_df['SuggestedCollege'] = batch_df['PredictedScore'].apply(suggest_college)
                    batch_df['GPA'] = batch_df['PredictedScore'].apply(score_to_gpa)
                    st.dataframe(batch_df)
                    add_download_button(batch_df, "batch_predictions.csv")
            except Exception as e:
                st.error(f"❌ Error processing batch file: {e}")

    # 📈 Tab 4: Visualization
    with tab4:
        st.subheader("📈 Data Visualization")
        st.markdown("Customize filters to explore performance patterns:")
        att_min = st.slider("Minimum Attendance", 50, 100, 70, key='att_min')
        study_min = st.slider("Minimum Study Hours", 1, 10, 4, key='study_min')
        filtered = df[(df['Attendance'] >= att_min) & (df['StudyHours'] >= study_min)]

        if not filtered.empty:
            fig = px.scatter(filtered, x='StudyHours', y='FinalScore', color='Attendance',
                             size='SleepHours', title="Study Hours vs Score (Filtered)")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data matching filter criteria")

    # 🧪 Tab 5: Performance Report Generator
    with tab5:
        st.subheader("🧪 Generate Custom Performance Report")
        if y is not None:
            low_score_df = df[df['FinalScore'] < 60]
            high_score_df = df[df['FinalScore'] >= 90]

            st.markdown("#### ⚠ Students Below 60%")
            st.dataframe(low_score_df, use_container_width=True)
            st.markdown("#### 🏆 Top Performers (Above 90%)")
            st.dataframe(high_score_df, use_container_width=True)

            report_df = pd.concat([
                low_score_df.assign(Flag="Low Performer"),
                high_score_df.assign(Flag="Top Performer")
            ])
            add_download_button(report_df, "performance_report.csv")

    # 🎓 Tab 6: College Suggestion Summary
    with tab6:
        st.subheader("🎓 College Suggestion Summary")
        if 'FinalScore' in df:
            df['SuggestedCollege'] = df['FinalScore'].apply(suggest_college)
            college_counts = df['SuggestedCollege'].value_counts()
            st.bar_chart(college_counts)
            
            # Display only if columns exist
            display_cols = []
            for col in ['StudentName', 'StudyHours', 'SleepHours', 'Attendance',
                       'AssignmentsCompleted', 'InternetUsage', 'FinalScore', 'GPA', 'SuggestedCollege']:
                if col in df.columns:
                    display_cols.append(col)
            
            st.dataframe(df[display_cols])
            add_download_button(df, "college_suggestions.csv")

    # 🖚 Footer
    st.markdown("---")
    st.markdown(f"App generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown("Crafted with ❤ by AI using Streamlit & Scikit-Learn")
    
# ========== UTILITY FUNCTIONS FOR FILE MANAGEMENT ==========

def list_all_files(base_dir):
    all_files = []
    for root, _, files in os.walk(base_dir):
        for f in files:
            full_path = os.path.join(root, f)
            all_files.append(os.path.relpath(full_path, base_dir))
    return sorted(all_files)

def list_all_folders(base_dir):
    all_folders = []
    for root, dirs, _ in os.walk(base_dir):
        for d in dirs:
            full_path = os.path.join(root, d)
            all_folders.append(os.path.relpath(full_path, base_dir))
    return sorted(all_folders)

def get_file_info(path):
    return {
        "Size (KB)": round(os.path.getsize(path)/1024, 2),
        "Modified": time.ctime(os.path.getmtime(path)),
        "Created": time.ctime(os.path.getctime(path)),
        "Permissions": oct(os.stat(path).st_mode)[-3:]
    }

def get_folder_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return round(total/1024, 2)

# ========== FULL FILE MANAGEMENT SYSTEM ==========
def advanced_file_manager():
    st.title("📁 Full File Management System")
    
    # Custom styling
    st.markdown("""
        <style>
        .stTextInput>div>div>input {
            font-size: 16px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        .file-op-box {
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #e0e0e0;
            margin-bottom: 20px;
            background-color: #f9f9f9;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Sidebar operation selector
    operation = st.sidebar.selectbox("📌 Choose Operation", [
        "📄 List Files/Folders",
        "📝 Create File", "📖 Read File", "📝 Write File", "📎 Append File",
        "📤 Upload File", "📥 Download File",
        "✏ Rename File", "📋 Copy File", "📦 Move File", "❌ Delete File", "🔁 Replace File",
        "📂 Create Folder", "✏ Rename Folder", "🗑 Delete Folder", "📦 Move Folder",
        "🔍 Search Files", "🔽 Zip Folder", "📂 Unzip File"
    ])
    
    # Base directory
    base_dir = st.text_input("📂 Enter Base Directory:", value=os.getcwd())
    
    # ========== FILE & FOLDER OPERATIONS ========== #
    if os.path.isdir(base_dir):
        files = list_all_files(base_dir)
        folders = list_all_folders(base_dir)
        
        with st.container():
            st.subheader(f"🔧 Operation: {operation}")
            
            if operation == "📄 List Files/Folders":
                st.info(f"📁 Found {len(files)} files and {len(folders)} folders")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("📂 Folders")
                    if folders:
                        for folder in folders:
                            st.markdown(f"- {folder}/")
                    else:
                        st.write("No folders found")
                
                with col2:
                    st.subheader("📄 Files")
                    if files:
                        for file in files:
                            st.markdown(f"- {file}")
                    else:
                        st.write("No files found")
            
            elif operation == "📝 Create File":
                name = st.text_input("🆕 File Name (with extension)")
                content = st.text_area("📄 File Content", height=200)
                if st.button("Create File"):
                    path = os.path.join(base_dir, name)
                    with open(path, 'w') as f:
                        f.write(content)
                    st.success(f"✅ File '{name}' created!")
            
            elif operation == "📖 Read File":
                if files:
                    file = st.selectbox("📄 Select File", files)
                    if st.button("Read"):
                        with open(os.path.join(base_dir, file), 'r', encoding='utf-8') as f:
                            st.subheader(f"📄 Content of {file}")
                            st.code(f.read())
                else:
                    st.warning("No files available to read")
            
            elif operation == "📝 Write File":
                if files:
                    file = st.selectbox("✍ File to Overwrite", files)
                    content = st.text_area("🆕 New Content", height=200)
                    if st.button("Write"):
                        with open(os.path.join(base_dir, file), 'w') as f:
                            f.write(content)
                        st.success(f"✅ Content written to '{file}'!")
                else:
                    st.warning("No files available to write")
            
            elif operation == "📎 Append File":
                if files and len(files) >= 2:
                    src = st.selectbox("📄 Source File", files)
                    tgt = st.selectbox("📄 Target File", files)
                    if st.button("Append"):
                        with open(os.path.join(base_dir, src), 'r') as s, open(os.path.join(base_dir, tgt), 'a') as t:
                            t.write("\n" + s.read())
                        st.success(f"✅ Appended '{src}' to '{tgt}'!")
                else:
                    st.warning("Need at least 2 files for this operation")
            
            elif operation == "📤 Upload File":
                upload = st.file_uploader("Upload a File")
                if upload:
                    path = os.path.join(base_dir, upload.name)
                    with open(path, 'wb') as f:
                        f.write(upload.read())
                    st.success(f"✅ Uploaded '{upload.name}' to {base_dir}")
            
            elif operation == "📥 Download File":
                if files:
                    file = st.selectbox("📄 Select File", files)
                    with open(os.path.join(base_dir, file), 'rb') as f:
                        st.download_button("📥 Download", data=f, file_name=file)
                else:
                    st.warning("No files available to download")
            
            elif operation == "✏ Rename File":
                if files:
                    file = st.selectbox("📝 Select File", files)
                    new = st.text_input("🆕 New File Name")
                    if st.button("Rename"):
                        os.rename(os.path.join(base_dir, file), os.path.join(base_dir, new))
                        st.success(f"✅ Renamed '{file}' to '{new}'!")
                else:
                    st.warning("No files available to rename")
            
            elif operation == "📋 Copy File":
                if files:
                    file = st.selectbox("📄 Select File to Copy", files)
                    dest = st.text_input("📍 Destination Path (with name)")
                    if st.button("Copy"):
                        shutil.copy(os.path.join(base_dir, file), dest)
                        st.success(f"✅ Copied '{file}' to '{dest}'!")
                else:
                    st.warning("No files available to copy")
            
            elif operation == "📦 Move File":
                if files:
                    file = st.selectbox("📄 File to Move", files)
                    dest = st.text_input("📍 Destination Directory")
                    if st.button("Move"):
                        shutil.move(os.path.join(base_dir, file), os.path.join(dest, os.path.basename(file)))
                        st.success(f"✅ Moved '{file}' to '{dest}'!")
                else:
                    st.warning("No files available to move")
            
            elif operation == "❌ Delete File":
                if files:
                    file = st.selectbox("🗑 File to Delete", files)
                    if st.button("Delete"):
                        os.remove(os.path.join(base_dir, file))
                        st.success(f"✅ Deleted '{file}'!")
                else:
                    st.warning("No files available to delete")
            
            elif operation == "🔁 Replace File":
                if files and len(files) >= 2:
                    src = st.selectbox("📤 Source File", files)
                    tgt = st.selectbox("📥 Target File", files)
                    if st.button("Replace"):
                        shutil.copyfile(os.path.join(base_dir, src), os.path.join(base_dir, tgt))
                        st.success(f"✅ Replaced '{tgt}' with '{src}'!")
                else:
                    st.warning("Need at least 2 files for this operation")
            
            elif operation == "📂 Create Folder":
                folder = st.text_input("📁 Folder Name (Nested allowed)")
                if st.button("Create Folder"):
                    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)
                    st.success(f"✅ Folder '{folder}' created!")
            
            elif operation == "✏ Rename Folder":
                if folders:
                    folder = st.selectbox("📂 Folder to Rename", folders)
                    new = st.text_input("🆕 New Folder Name")
                    if st.button("Rename"):
                        os.rename(os.path.join(base_dir, folder), os.path.join(base_dir, new))
                        st.success(f"✅ Folder renamed to '{new}'!")
                else:
                    st.warning("No folders available to rename")
            
            elif operation == "🗑 Delete Folder":
                if folders:
                    folder = st.selectbox("📁 Folder to Delete", folders)
                    full_path = os.path.join(base_dir, folder)
                    confirm = st.checkbox(f"⚠ Confirm deletion of '{folder}' and all its contents")
                    if confirm and st.button("Delete Folder"):
                        shutil.rmtree(full_path)
                        st.success(f"✅ Folder '{folder}' deleted!")
                else:
                    st.warning("No folders available to delete")
            
            elif operation == "📦 Move Folder":
                if folders:
                    folder = st.selectbox("📁 Folder to Move", folders)
                    dest = st.text_input("📍 Destination Directory")
                    if st.button("Move"):
                        shutil.move(os.path.join(base_dir, folder), os.path.join(dest, os.path.basename(folder)))
                        st.success(f"✅ Moved '{folder}' to '{dest}'!")
                else:
                    st.warning("No folders available to move")
            
            elif operation == "🔍 Search Files":
                query = st.text_input("🔎 Search Query")
                if query:
                    results = [f for f in files if query.lower() in f.lower()]
                    st.subheader(f"🔍 Found {len(results)} matching files")
                    for file in results:
                        st.markdown(f"- {file}")
            
            elif operation == "🔽 Zip Folder":
                if folders:
                    folder = st.selectbox("📁 Folder to Zip", folders)
                    zip_name = st.text_input("📦 Output Zip File Name", value=f"{folder}.zip")
                    if st.button("Create Zip"):
                        shutil.make_archive(os.path.join(base_dir, zip_name.replace(".zip", "")), 'zip', os.path.join(base_dir, folder))
                        st.success(f"✅ Folder '{folder}' zipped as '{zip_name}'!")
                else:
                    st.warning("No folders available to zip")
            
            elif operation == "📂 Unzip File":
                zip_files = [f for f in files if f.endswith('.zip')]
                if zip_files:
                    zip_file = st.selectbox("📦 Zip File", zip_files)
                    extract_path = st.text_input("📂 Extract To", value=os.path.join(base_dir, "extracted"))
                    if st.button("Unzip"):
                        with zipfile.ZipFile(os.path.join(base_dir, zip_file), 'r') as zip_ref:
                            zip_ref.extractall(os.path.join(base_dir, extract_path))
                        st.success(f"✅ Unzipped '{zip_file}' to '{extract_path}'!")
                else:
                    st.warning("No zip files available to unzip")
    else:
        st.error("❌ Invalid base directory!")


def project_hand_gesture_music():
    # Custom CSS styling
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Custom HTML/CSS with colorful decorations
    st.markdown("""
    <style>
        /* Vibrant gradient background */
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        
        /* Glowing title effect */
        .title-text {
            font-family: 'Arial', sans-serif;
            color: white;
            text-shadow: 0 0 10px #ff00ff, 
                         0 0 20px #ff00ff, 
                         0 0 30px #ff00ff;
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from {
                text-shadow: 0 0 10px #ff00ff, 
                             0 0 20px #ff00ff, 
                             0 0 30px #ff00ff;
            }
            to {
                text-shadow: 0 0 15px #ff00ff, 
                             0 0 25px #ff00ff, 
                             0 0 35px #ff00ff;
            }
        }
        
        /* Neon buttons */
        .stButton>button {
            border: 2px solid #00ffff;
            border-radius: 25px;
            padding: 12px 28px;
            background: rgba(0, 0, 0, 0.3);
            color: #00ffff;
            font-weight: bold;
            font-size: 16px;
            transition: all 0.3s;
            box-shadow: 0 0 10px #00ffff;
        }
        
        .stButton>button:hover {
            background: rgba(0, 255, 255, 0.2);
            transform: scale(1.05);
            box-shadow: 0 0 20px #00ffff;
        }
        
        /* Song display with pulse animation */
        .song-title {
            font-size: 1.4em;
            color: #ffcc00;
            text-shadow: 0 0 5px #ff6600;
            font-weight: bold;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        /* Status box with gradient border */
        .status-box {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            padding: 15px;
            margin: 15px 0;
            border-left: 5px solid;
            border-image: linear-gradient(to bottom, #ff00ff, #00ffff) 1;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        
        /* Animated volume bar */
        .volume-container {
            margin: 20px 0;
        }
        
        .volume-bar {
            height: 15px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            margin: 10px 0;
            overflow: hidden;
        }
        
        .volume-fill {
            height: 100%;
            background: linear-gradient(90deg, #ff5e62, #ff9966);
            border-radius: 10px;
            transition: width 0.5s;
            box-shadow: 0 0 10px #ff9966;
        }
        
        /* Gesture instructions with floating effect */
        .gesture-instruction {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            margin: 15px 0;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: transform 0.3s;
        }
        
        .gesture-instruction:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }
        
        /* Camera feed styling */
        .stImage>img {
            border-radius: 15px;
            border: 3px solid #00ffff;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
            transition: all 0.3s;
        }
        
        .stImage>img:hover {
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.8);
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(#00ffff, #ff00ff);
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Fancy title with HTML and glowing effect
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1 class="title-text">🎶 Hand Gesture Music Maestro</h1>
        <p style="color: #e0e0e0; font-size: 18px;">Control your music with magical hand gestures ✨</p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize music system
    try:
        pygame.mixer.init()
        volume = 0.5
        pygame.mixer.music.set_volume(volume)
    except pygame.error as e:
        st.error(f"❌ Failed to initialize audio system: {e}")
        st.stop()

    # Load music files
    song_folder = "song"
    if not os.path.exists(song_folder):
        os.makedirs(song_folder)
        st.error(f"❌ Created 'song' folder. Please add some MP3 files to it.")
        st.stop()

    song_list = sorted([file for file in os.listdir(song_folder) if file.endswith(".mp3")])
    if not song_list:
        st.error("No MP3 files found in the 'song' folder. Please add some music files.")
        st.stop()

    # Mediapipe init
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)
    mp_drawing = mp.solutions.drawing_utils

    # State variables
    if "run_camera" not in st.session_state:
        st.session_state.run_camera = False
    if "volume" not in st.session_state:
        st.session_state.volume = 0.5
    if "song_index" not in st.session_state:
        st.session_state.song_index = 0
    if "status" not in st.session_state:
        st.session_state.status = "Ready"
    if "current_song" not in st.session_state:
        st.session_state.current_song = "No song selected"

    # Music control functions
    def play_song(index):
        try:
            pygame.mixer.music.load(os.path.join(song_folder, song_list[index]))
            pygame.mixer.music.play()
            st.session_state.current_song = song_list[index]
            return f"▶ Playing: {song_list[index]}"
        except (pygame.error, IndexError) as e:
            st.error(f"❌ Error playing song: {e}")
            return "❌ Error"

    def stop_song():
        try:
            pygame.mixer.music.stop()
            st.session_state.current_song = "No song selected"
        except pygame.error:
            pass

    def pause_song():
        try:
            pygame.mixer.music.pause()
        except pygame.error:
            pass

    def unpause_song():
        try:
            pygame.mixer.music.unpause()
        except pygame.error:
            pass

    # Finger counter
    def count_fingers(landmarks):
        count = 0
        if landmarks[8].y < landmarks[6].y: count += 1   # Index
        if landmarks[12].y < landmarks[10].y: count += 1 # Middle
        if landmarks[16].y < landmarks[14].y: count += 1 # Ring
        if landmarks[20].y < landmarks[18].y: count += 1 # Pinky
        return count

    # Gesture instructions with emoji icons
    with st.expander("✨ Gesture Controls Guide", expanded=True):
        st.markdown("""
        <div class="gesture-instruction">
            <p style="font-size: 18px;"><span style="font-size: 24px;">👊</span> <b>Fist (0 fingers)</b> - Mute volume</p>
            <p style="font-size: 18px;"><span style="font-size: 24px;">☝️</span> <b>1 Finger</b> - Play current song</p>
            <p style="font-size: 18px;"><span style="font-size: 24px;">✌️</span> <b>2 Fingers</b> - Volume Down</p>
            <p style="font-size: 18px;"><span style="font-size: 24px;">🤟</span> <b>3 Fingers</b> - Next Song</p>
            <p style="font-size: 18px;"><span style="font-size: 24px;">✋</span> <b>4 Fingers</b> - Volume Up</p>
            <p style="font-size: 18px;"><span style="font-size: 24px;">🖐️</span> <b>5 Fingers</b> - Stop Music</p>
        </div>
        """, unsafe_allow_html=True)

    # Current song and volume display with animations
    st.markdown(f"""
    <div class="volume-container">
        <div class="song-title">🎵 Now Playing: {st.session_state.current_song}</div>
        <div style="margin: 15px 0; font-size: 16px;">🔊 Volume Level</div>
        <div class="volume-bar">
            <div class="volume-fill" style="width: {st.session_state.volume * 100}%;"></div>
        </div>
        <div style="text-align: right; margin-top: 5px; font-size: 16px;">{int(st.session_state.volume * 100)}%</div>
    </div>
    """, unsafe_allow_html=True)

    # Camera control buttons with neon effect
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button("📷 Start Camera", key="start_cam"):
            st.session_state.run_camera = True
    with col2:
        if st.button("⏸️ Pause Music", key="pause_music"):
            pause_song()
            st.session_state.status = "⏸️ Paused"
    with col3:
        if st.button("🛑 Stop Camera", key="stop_cam"):
            st.session_state.run_camera = False
            stop_song()

    # Status box with gradient border
    status_placeholder = st.empty()

    # Camera feed with glowing border
    FRAME_WINDOW = st.image([], use_column_width=True)

    # Main loop
    cap = None
    try:
        if st.session_state.run_camera:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                st.error("❌ Could not open camera")
                st.session_state.run_camera = False
                st.stop()

            while st.session_state.run_camera:
                ret, frame = cap.read()
                if not ret:
                    st.warning("⚠️ Failed to grab frame")
                    break

                frame = cv2.flip(frame, 1)
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(rgb)

                if results.multi_hand_landmarks:
                    for lm in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)
                        fingers = count_fingers(lm.landmark)

                        # Gesture-based music control
                        if fingers == 0:
                            pygame.mixer.music.set_volume(0.0)
                            st.session_state.status = "🔇 Muted"
                        elif fingers == 1:
                            st.session_state.status = play_song(st.session_state.song_index)
                        elif fingers == 2:
                            st.session_state.volume = max(0.0, st.session_state.volume - 0.1)
                            pygame.mixer.music.set_volume(st.session_state.volume)
                            st.session_state.status = f"🔉 Volume Down: {int(st.session_state.volume * 100)}%"
                        elif fingers == 3:
                            st.session_state.song_index = (st.session_state.song_index + 1) % len(song_list)
                            st.session_state.status = play_song(st.session_state.song_index)
                        elif fingers == 4:
                            st.session_state.volume = min(1.0, st.session_state.volume + 0.1)
                            pygame.mixer.music.set_volume(st.session_state.volume)
                            st.session_state.status = f"🔊 Volume Up: {int(st.session_state.volume * 100)}%"
                        elif fingers == 5:
                            stop_song()
                            st.session_state.status = "⏹️ Stopped"

                        # Display text on frame with colorful styling
                        cv2.putText(frame, f"Fingers: {fingers}", (10, 60), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 105, 180), 2)  # Hot pink
                        cv2.putText(frame, f"{st.session_state.status}", (10, 100), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)  # Cyan
                        cv2.putText(frame, f"Volume: {int(st.session_state.volume * 100)}%", (10, 140), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)  # Yellow

                FRAME_WINDOW.image(frame, channels="BGR")
                
                # Update status with HTML styling
                status_placeholder.markdown(f"""
                <div class="status-box">
                    <strong style="font-size: 18px; color: #00ffff;">Status:</strong> 
                    <span style="font-size: 16px;">{st.session_state.status}</span>
                </div>
                """, unsafe_allow_html=True)
                
                time.sleep(0.05)

    finally:
        if cap is not None:
            cap.release()
        hands.close()

    # Footer with colorful gradient
    st.markdown("""
    <div style="text-align: center; margin-top: 30px; padding: 15px; 
                background: linear-gradient(90deg, #ff00ff, #00ffff);
                border-radius: 10px;">
        <p style="color: white; font-size: 14px;">✨ Hand Gesture Music Controller ✨</p>
    </div>
    """, unsafe_allow_html=True)
def project_hand_calculator():
    st.subheader("🤖 Hand Gesture Based Calculator")

    run = st.checkbox("📷 Start Camera", key="calculator_cam")
    FRAME_WINDOW = st.image([])

    # Ensure necessary modules are imported locally for this function
    import cv2
    import mediapipe as mp

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    font = cv2.FONT_HERSHEY_SIMPLEX

    # Initialize variables in session state to persist them
    if "calc_num1" not in st.session_state:
        st.session_state.calc_num1 = None
        st.session_state.calc_num2 = None
        st.session_state.calc_result = None
        st.session_state.calc_locked = False
        st.session_state.calc_operation = None

    def count_fingers(hand_landmarks):
        finger_tips = [8, 12, 16, 20]
        count = 0

        # Simple up/down check for 4 fingers
        for tip in finger_tips:
            if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                count += 1

        # More robust check for thumb
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[2].x:
            count += 1
        return count

    def get_operation(finger_count):
        if finger_count == 1:
            return "Add"
        elif finger_count == 2:
            return "Subtract"
        elif finger_count == 3:
            return "Multiply"
        elif finger_count == 4:
            return "Divide"
        else:
            return None

    while run:
        ret, frame = cap.read()
        if not ret:
            st.warning("Could not read frame from camera. Please try again.")
            break
            
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                fingers = count_fingers(hand_landmarks)

                # Reset with 5 fingers
                if fingers == 5:
                    st.session_state.calc_num1 = None
                    st.session_state.calc_num2 = None
                    st.session_state.calc_result = None
                    st.session_state.calc_locked = False
                    st.session_state.calc_operation = None
                    cv2.putText(frame, "Resetting...", (50, 70), font, 1, (0, 0, 255), 2)

                # Phase 1: Get first number
                elif not st.session_state.calc_locked and fingers > 0:
                    st.session_state.calc_num1 = fingers

                # Lock first number with a fist
                elif not st.session_state.calc_locked and fingers == 0 and st.session_state.calc_num1 is not None:
                    st.session_state.calc_locked = True

                # Phase 2: Get second number
                elif st.session_state.calc_locked and st.session_state.calc_num2 is None and fingers > 0:
                    st.session_state.calc_num2 = fingers

                # Phase 3: Get Operation and Calculate
                elif st.session_state.calc_locked and st.session_state.calc_num2 is not None:
                    st.session_state.calc_operation = get_operation(fingers)
                    if st.session_state.calc_operation:
                        n1 = st.session_state.calc_num1
                        n2 = st.session_state.calc_num2
                        op = st.session_state.calc_operation
                        
                        if op == "Add":
                            st.session_state.calc_result = n1 + n2
                        elif op == "Subtract":
                            st.session_state.calc_result = n1 - n2
                        elif op == "Multiply":
                            st.session_state.calc_result = n1 * n2
                        elif op == "Divide":
                            st.session_state.calc_result = round(n1 / n2, 2) if n2 != 0 else "Error"

        # Display info on screen
        if st.session_state.calc_result is not None:
            text = f"{st.session_state.calc_num1} {st.session_state.calc_operation} {st.session_state.calc_num2} = {st.session_state.calc_result}"
            cv2.putText(frame, text, (50, 280), font, 1, (255, 0, 0), 2)
        elif st.session_state.calc_num2 is not None:
            cv2.putText(frame, f"Num2: {st.session_state.calc_num2}", (50, 220), font, 1, (0, 255, 255), 2)
        elif st.session_state.calc_locked:
            cv2.putText(frame, f"Num1 Locked: {st.session_state.calc_num1}", (50, 170), font, 1, (255, 255, 0), 2)
        elif st.session_state.calc_num1 is not None:
            cv2.putText(frame, f"Num1: {st.session_state.calc_num1}", (50, 120), font, 1, (0, 255, 0), 2)


        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    else:
        # Release the camera when the checkbox is unchecked
        cap.release()


def project_game_controller():
    st.subheader("🎮 Hand Gesture Game Controller")
    st.info("This tool uses your webcam to control a game with hand gestures. It will open a separate camera window.")

    # Make the game window title configurable
    game_window_title = st.text_input("Enter the Exact Game Window Title:", "Hill Climb Racing")

    if st.button("🚀 Start Game Controller"):
        
        # Import necessary libraries here
        import cv2
        import mediapipe as mp
        import pyautogui
        import pygetwindow as gw
        import time

        st.warning(f"Attempting to focus the '{game_window_title}' window in 3 seconds. Please make sure it's open.", icon="⚠️")
        time.sleep(3)

        # --- Functions defined inside the start block ---
        def focus_game_window(title):
            try:
                windows = gw.getWindowsWithTitle(title)
                if windows:
                    windows[0].activate()
                    st.success(f"✅ Focused window: {title}")
                    return True
                else:
                    st.error(f"❌ Game window '{title}' not found.")
                    return False
            except Exception as e:
                st.error(f"❌ Error focusing window: {e}")
                return False

        def is_hand_open(hand_landmarks):
            tips = [4, 8, 12, 16, 20]
            fingers_up = 0
            
            # Thumb (checks x-axis)
            if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[tips[0]-1].x:
                fingers_up += 1
            
            # Other 4 fingers (checks y-axis)
            for i in range(1, 5):
                if hand_landmarks.landmark[tips[i]].y < hand_landmarks.landmark[tips[i]-2].y:
                    fingers_up += 1
            return fingers_up >= 4 # True if 4 or 5 fingers are up

        # --- Main controller logic ---
        if not focus_game_window(game_window_title):
            st.stop() # Stop if the game window isn't found

        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        mp_draw = mp.solutions.drawing_utils

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("❌ Could not access webcam.")
            st.stop()
        
        last_action = None
        st.info("🎮 Controller is running! Open hand = Accelerate, Closed hand = Brake. Press 'ESC' in the camera window to stop.")

        while True:
            success, frame = cap.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            gesture = "No Hand"

            if result.multi_hand_landmarks:
                for handLms in result.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

                    if is_hand_open(handLms):
                        gesture = "Accelerate ->"
                        if last_action != "right":
                            pyautogui.keyDown("right")
                            pyautogui.keyUp("left")
                            last_action = "right"
                    else:
                        gesture = "Brake <-"
                        if last_action != "left":
                            pyautogui.keyDown("left")
                            pyautogui.keyUp("right")
                            last_action = "left"
            else:
                if last_action is not None:
                    pyautogui.keyUp("right")
                    pyautogui.keyUp("left")
                    last_action = None

            # Display the camera feed in a separate window
            cv2.putText(frame, f"Gesture: {gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Game Controller Feed", cv2.resize(frame, (320, 240)))

            # Check if the user pressed ESC to quit
            if cv2.waitKey(1) & 0xFF == 27:
                break
        
        # Cleanup
        st.success("Controller stopped.")
        cap.release()
        cv2.destroyAllWindows()
        pyautogui.keyUp("right")
        pyautogui.keyUp("left")

def python_instagram_post_creator():
    # --- Start of Instagram Post Creator Code ---
    
    # Import necessary modules locally for this task
    from datetime import datetime
    import tempfile
    import os
    from io import BytesIO
    from PIL import Image, ImageDraw, ImageFont
    import base64
    import time

    # Custom CSS for styling
    st.markdown("""
    <style>
        :root {
            --primary: #405DE6; --secondary: #5851DB; --pink: #E1306C;
            --purple: #C13584; --red: #FD1D1D; --orange: #F56040; --yellow: #FCAF45;
        }
        .stButton>button {
            background: linear-gradient(45deg, var(--pink), var(--purple)) !important;
            color: white !important; border: none; width: 100%; padding: 0.8rem;
            border-radius: 12px; font-weight: bold; font-size: 1.1rem;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(225, 48, 108, 0.3);
        }
        .instagram-post {
            width: 400px; background: white; border: 1px solid #dbdbdb;
            border-radius: 5px; margin: 1rem auto; box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .post-header {
            display: flex; align-items: center; padding: 12px; border-bottom: 1px solid #efefef;
        }
        .profile-pic {
            width: 32px; height: 32px; border-radius: 50%; margin-right: 10px;
            background: linear-gradient(45deg, var(--pink), var(--purple));
            display: flex; align-items: center; justify-content: center;
            color: white; font-weight: bold;
        }
        .username { font-weight: 600; font-size: 0.95rem; }
        .post-image { width: 100%; height: auto; }
        .post-actions { padding: 10px 12px; display: flex; gap: 15px; font-size: 1.4rem; }
        .post-likes { padding: 0 12px; font-weight: 600; font-size: 0.9rem; }
        .post-caption { padding: 8px 12px; font-size: 0.95rem; }
        .post-time { padding: 0 12px 12px; color: #8e8e8e; font-size: 0.8rem; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state within the function to avoid conflicts
    def init_session_state():
        if 'insta_media_file' not in st.session_state:
            st.session_state.insta_media_file = None
            st.session_state.insta_caption = ""
            st.session_state.insta_hashtags = "#instagood #photooftheday #love"
            st.session_state.insta_location = ""
            st.session_state.insta_schedule_time = datetime.now()
            st.session_state.insta_alt_text = ""
            st.session_state.insta_username = "your_username"
            st.session_state.insta_post_success = False
    
    init_session_state()

    # --- UI Starts Here ---
    st.subheader("📱 Instagram Post Creator")
    st.write("Create and schedule Instagram posts with a rich preview.")

    # Sidebar for this specific tool
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png", width=100)
        st.title("Post Creator Options")
        st.session_state.insta_username = st.text_input("Username", value=st.session_state.insta_username, key="insta_user")
        st.caption("This is a demo and does not actually post to Instagram.")

    # Main app content
    if st.session_state.insta_post_success:
        st.success("🎉 Post Published Successfully! (Simulated)")
        if st.button("Create Another Post"):
            st.session_state.insta_post_success = False
            st.rerun()

    # Media Upload Section
    uploaded_file = st.file_uploader(
        "Upload Image/Video", type=["jpg", "jpeg", "png", "mp4", "mov"], key="insta_media_upload"
    )

    if uploaded_file:
        st.session_state.insta_media_file = uploaded_file.getvalue()

    # Preview Section
    if st.session_state.insta_media_file:
        st.subheader("👀 Preview")
        st.markdown('<div class="instagram-post">', unsafe_allow_html=True)
        st.markdown(f'<div class="post-header"><div class="profile-pic">{st.session_state.insta_username[0].upper()}</div><div class="username">{st.session_state.insta_username}</div></div>', unsafe_allow_html=True)
        
        if uploaded_file.type.startswith('image'):
            st.markdown(f'<img src="data:image/png;base64,{base64.b64encode(st.session_state.insta_media_file).decode()}" class="post-image">', unsafe_allow_html=True)
        else:
            st.video(st.session_state.insta_media_file)

        st.markdown('<div class="post-actions"><div>❤️</div><div>💬</div><div>↗️</div><div style="margin-left: auto;">📌</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="post-likes">1,245 likes</div>', unsafe_allow_html=True)
        caption_preview = st.session_state.insta_caption if st.session_state.insta_caption else "Your caption..."
        st.markdown(f'<div class="post-caption"><b>{st.session_state.insta_username}</b> {caption_preview}</div>', unsafe_allow_html=True)
        st.markdown('<div class="post-time">1 HOUR AGO</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Post Details Form
    with st.form("post_details", clear_on_submit=False):
        st.subheader("📝 Post Details")
        st.session_state.insta_caption = st.text_area("Caption", value=st.session_state.insta_caption, placeholder="Write your caption...")
        st.session_state.insta_hashtags = st.text_area("🏷️ Hashtags", value=st.session_state.insta_hashtags, placeholder="#trending #viral")
        
        with st.expander("⚙️ Advanced Options"):
            st.session_state.insta_location = st.text_input("📍 Add Location", value=st.session_state.insta_location)
            st.session_state.insta_alt_text = st.text_input("♿ Alt Text (Accessibility)", value=st.session_state.insta_alt_text)

        submitted = st.form_submit_button("📤 Share to Feed (Simulate)")
        if submitted:
            if not st.session_state.insta_media_file:
                st.warning("⚠️ Please upload media first!")
            else:
                st.session_state.insta_post_success = True
                st.rerun()

    # --- End of Instagram Post Creator Code ---
def python_linkedin_post_pro():
    # --- Start of LinkedIn Post Pro Code ---

    # Import necessary modules locally for this task
    import streamlit as st
    import requests
    import os
    from datetime import datetime
    from PIL import Image
    import io
    import base64

    # Custom CSS for modern UI
    st.markdown("""
    <style>
        .linkedin-btn {
            background-color: #0a66c2 !important; color: white !important;
            border-radius: 28px !important; padding: 0.7rem 1.5rem !important;
            font-weight: 600 !important; border: none !important;
            transition: all 0.3s ease; display: inline-flex !important;
            align-items: center; justify-content: center; gap: 8px;
        }
        .linkedin-btn:hover {
            background-color: #004182 !important; transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(10, 102, 194, 0.3);
        }
        .stTextArea textarea {
            min-height: 180px !important; border-radius: 8px !important;
            padding: 16px !important; font-size: 1rem !important;
            border: 1px solid #ddd !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- LinkedIn API Functions (defined inside to keep them local) ---
    def get_linkedin_auth_url():
        LINKEDIN_CLIENT_ID = st.secrets.get("LINKEDIN_CLIENT_ID")
        # NOTE: This Redirect URI must be configured in your LinkedIn Developer App settings
        REDIRECT_URI = "http://localhost:8501/" 
        SCOPE = "w_member_social r_liteprofile"
        return f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={LINKEDIN_CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}"

    def exchange_code_for_token(code):
        LINKEDIN_CLIENT_ID = st.secrets.get("LINKEDIN_CLIENT_ID")
        LINKEDIN_CLIENT_SECRET = st.secrets.get("LINKEDIN_CLIENT_SECRET")
        REDIRECT_URI = "http://localhost:8501/"
        
        token_url = "https://www.linkedin.com/oauth/v2/accessToken"
        data = {
            "grant_type": "authorization_code", "code": code, "redirect_uri": REDIRECT_URI,
            "client_id": LINKEDIN_CLIENT_ID, "client_secret": LINKEDIN_CLIENT_SECRET
        }
        response = requests.post(token_url, data=data)
        return response.json().get("access_token") if response.status_code == 200 else None

    def get_user_profile(access_token):
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
        return response.json() if response.status_code == 200 else None

    def post_to_linkedin(access_token, content, image=None):
        profile_id = st.session_state.get("linkedin_user_id")
        if not profile_id:
            st.error("User ID not found. Cannot post.")
            return None

        post_data = {
            "author": f"urn:li:person:{profile_id}", "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": content},
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
        }
        
        headers = {
            "Authorization": f"Bearer {access_token}", "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }
        response = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=post_data)
        return response

    # --- Main App Logic ---
    st.subheader("💼 LinkedIn Post Pro")

    # Handle the OAuth callback
    if "code" in st.query_params and "linkedin_access_token" not in st.session_state:
        code = st.query_params["code"]
        access_token = exchange_code_for_token(code)
        if access_token:
            st.session_state.linkedin_access_token = access_token
            user_profile = get_user_profile(access_token)
            if user_profile:
                st.session_state.linkedin_user_info = user_profile
                st.session_state.linkedin_user_id = user_profile.get("id")
            # Clear the code from the URL and rerun
            st.query_params.clear()
            st.rerun()

    # --- UI Display ---
    if "linkedin_access_token" in st.session_state:
        # USER IS AUTHENTICATED
        user_info = st.session_state.linkedin_user_info
        st.success(f"Authenticated as **{user_info.get('localizedFirstName')} {user_info.get('localizedLastName')}**")

        with st.form("linkedin_post_form"):
            content = st.text_area("Post Content", placeholder="Share your professional insights...", height=200)
            image = st.file_uploader("Add image (optional)", type=["png", "jpg", "jpeg"])
            
            submitted = st.form_submit_button("Publish to LinkedIn", type="primary")
            if submitted:
                if not content:
                    st.warning("Post content cannot be empty.")
                else:
                    with st.spinner("Publishing..."):
                        response = post_to_linkedin(st.session_state.linkedin_access_token, content, image)
                        if response and response.status_code == 201:
                            st.balloons()
                            st.success("✅ Post published successfully on LinkedIn!")
                        else:
                            st.error(f"Failed to publish. Error: {response.status_code} - {response.text if response else 'Unknown error'}")

    else:
        # USER IS NOT AUTHENTICATED
        st.warning("You need to connect your LinkedIn account to create a post.")
        auth_url = get_linkedin_auth_url()
        st.markdown(f'<a href="{auth_url}" target="_self" style="text-decoration: none;"><button class="linkedin-btn">Connect with LinkedIn</button></a>', unsafe_allow_html=True)
        st.info("You'll be redirected to LinkedIn to authorize the application.")

    # --- End of LinkedIn Post Pro Code ---
def python_twitter_post_app():
    # --- Start of Twitter Post App Code ---
    st.subheader("🚀 Twitter Post App")
    st.markdown("Post tweets directly to your Twitter account.")

    # Import necessary libraries locally
    import tweepy
    import os

    # Twitter API configuration
    def twitter_auth(creds):
        try:
            client = tweepy.Client(
                consumer_key=creds['consumer_key'],
                consumer_secret=creds['consumer_secret'],
                access_token=creds['access_token'],
                access_token_secret=creds['access_token_secret']
            )
            return client
        except Exception as e:
            st.error(f"Authentication failed: {str(e)}")
            return None

    # Get credentials from st.secrets
    try:
        default_creds = {
            "consumer_key": st.secrets["TWITTER_CONSUMER_KEY"],
            "consumer_secret": st.secrets["TWITTER_CONSUMER_SECRET"],
            "access_token": st.secrets["TWITTER_ACCESS_TOKEN"],
            "access_token_secret": st.secrets["TWITTER_ACCESS_TOKEN_SECRET"]
        }
    except KeyError:
        st.error("Twitter API credentials not found in st.secrets. Please configure them.")
        st.stop()


    # Main tweet composition area
    tweet_text = st.text_area(
        "Compose your tweet",
        height=150,
        placeholder="What's happening?",
        max_chars=280,
        key="twitter_textarea"
    )

    char_count = len(tweet_text or "")
    st.caption(f"{char_count}/280 characters")

    uploaded_file = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"], key="twitter_uploader")

    # Tweet posting functionality
    if st.button("Post Tweet", key="twitter_post_button"):
        if not tweet_text:
            st.warning("Tweet content cannot be empty.")
        else:
            client = twitter_auth(default_creds)
            if client:
                try:
                    media_id = None
                    if uploaded_file is not None:
                        # Tweepy v2 requires a different way to upload media
                        auth_v1 = tweepy.OAuth1UserHandler(
                            default_creds['consumer_key'], default_creds['consumer_secret'],
                            default_creds['access_token'], default_creds['access_token_secret']
                        )
                        api_v1 = tweepy.API(auth_v1)
                        # We need to save the file temporarily to upload it
                        with open("temp_media", "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        media = api_v1.media_upload(filename="temp_media")
                        media_id = media.media_id
                        os.remove("temp_media") # Clean up the temp file

                    response = client.create_tweet(
                        text=tweet_text,
                        media_ids=[media_id] if media_id else None
                    )
                    
                    st.balloons()
                    st.success("✅ Tweet posted successfully!")
                    st.markdown(f"**Tweet ID:** `{response.data['id']}`")
                    st.markdown(f"**Link:** [View on Twitter](https://twitter.com/user/status/{response.data['id']})")

                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.error("Could not authenticate with Twitter. Check credentials.")

    # --- End of Twitter Post App Code ---
def python_facebook_post_app():
    # --- Start of Facebook Post App Code ---
    st.subheader("📱 Facebook Post Creator")
    st.markdown("Create and publish posts directly to your Facebook Page.")

    # Import necessary modules locally
    import requests
    import os
    from PIL import Image
    import io

    # Custom CSS for styling
    st.markdown("""
        <style>
        .fb-button {
            background-color: #1877F2 !important; color: white !important;
            font-weight: bold; padding: 10px 24px; border-radius: 8px;
            border: none; width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Helper Functions ---
    def get_fb_credentials():
        try:
            access_token = st.secrets["FB_ACCESS_TOKEN"]
            page_id = st.secrets["FB_PAGE_ID"]
            return access_token, page_id
        except KeyError as e:
            st.error(f"Missing credential in st.secrets: {e}. Please add it to your secrets.toml file.")
            return None, None

    # --- Main App UI ---
    access_token, page_id = get_fb_credentials()
    
    if not access_token or not page_id:
        st.stop()

    with st.form("facebook_post_form"):
        post_content = st.text_area(
            "Post Content",
            height=200,
            placeholder="What's on your mind?",
            max_chars=5000
        )
        char_count = len(post_content)
        st.caption(f"Characters: {char_count}/5000")

        uploaded_file = st.file_uploader(
            "Upload an image (optional)",
            type=["jpg", "jpeg", "png"],
            key="fb_image_uploader"
        )

        image_to_post = None
        if uploaded_file is not None:
            image_to_post = Image.open(uploaded_file)
            st.image(image_to_post, caption="Image Preview", use_column_width=True)

        submit_button = st.form_submit_button("🚀 Publish Post to Facebook")

    if submit_button:
        if not post_content:
            st.error("❌ Post content cannot be empty.")
        else:
            with st.spinner("Publishing your post..."):
                try:
                    # If there's an image, post to /photos, otherwise post to /feed
                    if image_to_post:
                        url = f"https://graph.facebook.com/{page_id}/photos"
                        img_byte_arr = io.BytesIO()
                        image_to_post.save(img_byte_arr, format='JPEG')
                        img_byte_arr = img_byte_arr.getvalue()
                        
                        files = {'source': ('image.jpg', img_byte_arr, 'image/jpeg')}
                        params = {
                            "access_token": access_token,
                            "caption": post_content
                        }
                        response = requests.post(url, params=params, files=files)
                    else:
                        url = f"https://graph.facebook.com/{page_id}/feed"
                        params = {
                            "access_token": access_token,
                            "message": post_content
                        }
                        response = requests.post(url, params=params)
                    
                    response_data = response.json()
                    
                    if response.status_code == 200 and 'id' in response_data:
                        st.balloons()
                        st.success("✅ Post published successfully!")
                        post_id = response_data['id']
                        if '_' in post_id: # Page posts have an underscore
                            link = f"https://www.facebook.com/{post_id.replace('_', '/posts/')}"
                            st.markdown(f"**Post ID:** `{post_id}`")
                            st.markdown(f"**Link:** [View on Facebook]({link})")
                        else:
                            st.markdown(f"**Photo ID:** `{post_id}` (Note: This is a photo ID, not a post ID)")

                    else:
                        st.error(f"❌ Failed to create post: {response_data.get('error', {}).get('message', 'Unknown error')}")

                except Exception as e:
                    st.error(f"❌ An unexpected error occurred: {str(e)}")

    # --- End of Facebook Post App Code ---
def ml_smart_meter_app():
    # --- Start of Smart Meter App Code ---
    st.subheader("🔌 Smart Electricity Bill Predictor")
    st.markdown("Predict your electricity bill based on consumed units using a simple machine learning model.")

    # Import necessary libraries locally
    import pickle
    import os
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    MODEL_FILE = "smart_meter_model.pkl"

    # --- Helper Functions (defined inside to keep them local) ---
    def train_and_save_model():
        """Train and save the model if it doesn't exist."""
        with st.spinner("🔧 Training a new prediction model..."):
            data = {
                "units": [50, 100, 150, 200, 250, 300, 400, 500],
                "bill": [150, 300, 450, 600, 750, 900, 1200, 1500]
            }
            df = pd.DataFrame(data)
            X = df[["units"]]
            y = df["bill"]
            model = LinearRegression()
            model.fit(X, y)
            with open(MODEL_FILE, "wb") as f:
                pickle.dump(model, f)
        st.success("✅ New model trained and saved!")
        return model

    @st.cache_resource
    def load_model():
        """Load the trained model from the file, or train it if it doesn't exist."""
        if not os.path.exists(MODEL_FILE):
            st.info("Model file not found. Training a new one.")
            model = train_and_save_model()
        else:
            with open(MODEL_FILE, "rb") as f:
                model = pickle.load(f)
        return model

    # --- Main App UI ---
    model = load_model()

    st.markdown("#### Enter Units Consumed")
    units = st.number_input(
        "Enter the number of electricity units (kWh) consumed:",
        min_value=0.0,
        value=100.0,
        step=10.0,
        format="%.2f"
    )

    if st.button("💰 Predict Bill"):
        if units >= 0:
            estimated_bill = model.predict([[units]])[0]
            st.metric(
                label="Estimated Electricity Bill",
                value=f"₹ {estimated_bill:.2f}",
                help=f"Based on a consumption of {units} kWh"
            )
        else:
            st.error("Please enter a valid number of units (0 or more).")

    # Add an option to retrain the model
    with st.expander("⚙️ Model Options"):
        if st.button("Force Retrain Model"):
            train_and_save_model()
            st.info("Model has been retrained. Please clear the cache if predictions do not update.")
            st.warning("Note: In a real app, you would retrain with new, larger datasets.")

    # --- End of Smart Meter App Code ---
def python_send_email_app():
    # --- Start of Email App Code ---
    st.subheader("📧 Email Bhejne Wala App")
    st.markdown("Send emails directly from your application.")

    # Import necessary modules locally
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # --- Main App UI ---
    try:
        SENDER_EMAIL = st.secrets["SENDER_EMAIL"]
        APP_PASSWORD = st.secrets["APP_PASSWORD"]
    except KeyError as e:
        st.error(f"Missing credential in st.secrets: {e}. Please add it to your secrets.toml file.")
        st.stop()
    
    receiver_email = st.text_input("Jisey Email Bhejna Hai", placeholder="example@example.com")
    subject = st.text_input("Subject")
    message = st.text_area("Message likhiye")
    
    if st.button("📤 Email Bheje"):
        if not receiver_email or not subject or not message:
            st.warning("Please fill out all fields.")
        else:
            try:
                # Create the email
                email_msg = MIMEMultipart()
                email_msg["From"] = SENDER_EMAIL
                email_msg["To"] = receiver_email
                email_msg["Subject"] = subject
                email_msg.attach(MIMEText(message, "plain"))

                # Connect to Gmail SMTP server
                with st.spinner("Sending email..."):
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(SENDER_EMAIL, APP_PASSWORD)
                    server.sendmail(SENDER_EMAIL, receiver_email, email_msg.as_string())
                    server.quit()
                st.success("✅ Email successfully bhej diya gaya!")
            except Exception as e:
                st.error(f"❌ Email bhejne mein error aayi: {e}")
    # --- End of Email App Code ---
def project_all_in_one_tool():
    # --- Start of All-in-One Tool Code ---
    st.subheader("🛠️ All-in-One Streamlit Tool")
    st.write("A collection of useful mini-tools. Choose one from the sidebar below.")

    # Import necessary modules locally
    import datetime
    import math
    import cv2
    import numpy as np
    from PIL import Image
    import requests

    # --- Tool Functions (defined inside to keep them local) ---
    def calculator():
        st.info("🔢 Simple Calculator")
        num1 = st.number_input("Enter first number")
        op = st.selectbox("Select operation", ['+', '-', '*', '/'])
        num2 = st.number_input("Enter second number")
        if st.button("Calculate"):
            result = 0
            if op == '+': result = num1 + num2
            elif op == '-': result = num1 - num2
            elif op == '*': result = num1 * num2
            elif op == '/':
                if num2 != 0: result = num1 / num2
                else:
                    st.error("Division by zero is not allowed.")
                    return
            st.success(f"Result: {result:.2f}")

    def currency_converter():
        st.info("💱 Currency Converter (INR to other)")
        amount = st.number_input("Enter amount in INR", min_value=0.0)
        currency = st.selectbox("Convert to", ["USD", "EUR", "GBP"])
        rates = {"USD": 0.012, "EUR": 0.011, "GBP": 0.0095}
        if st.button("Convert"):
            converted = amount * rates[currency]
            st.success(f"{amount} INR = {converted:.2f} {currency}")

    def bmi_checker():
        st.info("⚖️ BMI Calculator")
        weight = st.number_input("Enter weight (kg)", min_value=1.0)
        height = st.number_input("Enter height (meters)", min_value=0.1)
        if st.button("Check BMI"):
            bmi = weight / (height ** 2)
            st.metric(label="Your BMI is", value=f"{bmi:.2f}")
            if bmi < 18.5: st.warning("Category: Underweight")
            elif 18.5 <= bmi < 24.9: st.success("Category: Normal weight")
            elif 25 <= bmi < 29.9: st.warning("Category: Overweight")
            else: st.error("Category: Obese")

    def age_calculator():
        st.info("📆 Age Calculator")
        birth_date = st.date_input("Enter your birth date")
        if st.button("Calculate Age"):
            today = datetime.date.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            st.success(f"You are {age} years old.")

    def emi_calculator():
        st.info("💸 Loan EMI Calculator")
        principal = st.number_input("Enter loan amount (₹)", min_value=1000.0)
        rate = st.number_input("Annual interest rate (%)", min_value=1.0)
        tenure = st.number_input("Tenure in months", min_value=1)
        if st.button("Calculate EMI"):
            monthly_rate = rate / (12 * 100)
            if monthly_rate > 0:
                emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
                total_payment = emi * tenure
                st.metric(label="Monthly EMI", value=f"₹ {emi:,.2f}")
                st.info(f"Total payment will be ₹ {total_payment:,.2f}")

    def weather_info():
        st.info("🌤️ Weather Info")
        api_key = st.secrets.get("WEATHER_API_KEY", "YOUR_API_KEY_HERE") # Fallback for local use
        city = st.text_input("Enter city name")
        if st.button("Get Weather"):
            if not city:
                st.warning("Please enter a city name.")
                return
            try:
                url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
                response = requests.get(url)
                data = response.json()
                if "error" in data:
                    st.error(data["error"]["message"])
                else:
                    current = data["current"]
                    st.success(f"**{data['location']['name']}**: {current['temp_c']}°C, {current['condition']['text']}")
            except Exception as e:
                st.error(f"Error fetching data: {e}")

    def image_to_sketch():
        st.info("🖼️ Image to Sketch Converter")
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            col1, col2 = st.columns(2)
            with col1:
                st.image(image, caption="Original Image", use_column_width=True)
            with col2:
                img_array = np.array(image.convert("RGB"))
                gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                inv = 255 - gray
                blur = cv2.GaussianBlur(inv, (21, 21), 0)
                sketch = cv2.divide(gray, 255 - blur, scale=256)
                st.image(sketch, caption="Pencil Sketch", use_column_width=True)

    # --- Sidebar for this specific tool ---
    with st.sidebar:
        st.markdown("---")
        st.header("All-in-One Tool Menu")
        menu = st.selectbox("Select a mini-tool", [
            "Simple Calculator", "Currency Converter", "BMI Checker",
            "Age Calculator", "Loan EMI Calculator", "Weather Info",
            "Image to Sketch Converter"
        ])

    # --- Display selected tool ---
    if menu == "Simple Calculator": calculator()
    elif menu == "Currency Converter": currency_converter()
    elif menu == "BMI Checker": bmi_checker()
    elif menu == "Age Calculator": age_calculator()
    elif menu == "Loan EMI Calculator": emi_calculator()
    elif menu == "Weather Info": weather_info()
    elif menu == "Image to Sketch Converter": image_to_sketch()

    # --- End of All-in-One Tool Code ---
def project_premium_rental_finder():
    # --- Start of Premium Rental Finder Code ---
    
    # Import necessary modules locally
    import pandas as pd
    import numpy as np
    import time
    import plotly.express as px
    import plotly.graph_objects as go
    from PIL import Image
    import requests
    from io import BytesIO
    import random

    # Custom CSS for this specific tool
    st.markdown("""
        <style>
        /* Add any specific styles for this tool here */
        .title {
            font-size: 2.5rem !important;
            font-weight: 700;
            background: linear-gradient(135deg, #4361ee, #3a0ca3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
        .property-card {
            background: white; border-radius: 16px;
            box-shadow: 0 8px 25px rgba(67, 97, 238, 0.15);
            margin-bottom: 20px; transition: all 0.4s;
            border-left: 5px solid #4361ee; overflow: hidden;
            padding: 20px;
        }
        .property-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 30px rgba(67, 97, 238, 0.25);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Data and Utility Functions ---
    rental_data = {
        "Jaipur": [
            {"name": "Shree Residency Premium", "rent": 8000, "rooms": 2, "address": "Vaishali Nagar, Jaipur", "image": "https://images.unsplash.com/photo-1580587771525-78b9dba3b914?auto=format&fit=crop&w=600&q=80", "tags": ["Balcony", "Parking", "24/7 Security", "WiFi"], "property_type": "Apartment", "furnishing": "Semi-Furnished", "area": 850, "rating": 4.3, "agent": "Raj Properties", "agent_rating": 4.7},
            {"name": "Pink City Villas", "rent": 12000, "rooms": 3, "address": "Mansarovar, Jaipur", "image": "https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&w=600&q=80", "tags": ["Swimming Pool", "Gym", "Garden", "AC"], "property_type": "Villa", "furnishing": "Fully Furnished", "area": 1200, "rating": 4.7, "agent": "Pink City Realty", "agent_rating": 4.9},
        ],
        "Delhi": [
            {"name": "Urban Heights Elite", "rent": 15000, "rooms": 2, "address": "Rohini, Delhi", "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80", "tags": ["Modern Kitchen", "Lift", "Power Backup"], "property_type": "Apartment", "furnishing": "Semi-Furnished", "area": 900, "rating": 4.4, "agent": "Delhi Homes", "agent_rating": 4.8},
            {"name": "Capital Homes", "rent": 22000, "rooms": 3, "address": "Dwarka, Delhi", "image": "https://images.unsplash.com/photo-1600585154076-7c1c2b69a511?auto=format&fit=crop&w=600&q=80", "tags": ["Club House", "Play Area", "Maintenance"], "property_type": "Apartment", "furnishing": "Fully Furnished", "area": 1150, "rating": 4.6, "agent": "Capital Realty", "agent_rating": 4.7},
        ],
        "Mumbai": [
            {"name": "Sea View Towers", "rent": 30000, "rooms": 2, "address": "Bandra West, Mumbai", "image": "https://images.unsplash.com/photo-1600585154350-8121a5e243b2?auto=format&fit=crop&w=600&q=80", "tags": ["Sea Facing", "Modular Kitchen", "Park"], "property_type": "Apartment", "furnishing": "Fully Furnished", "area": 1000, "rating": 4.8, "agent": "Coastal Properties", "agent_rating": 4.8},
            {"name": "Skyline Premium", "rent": 35000, "rooms": 3, "address": "Andheri West, Mumbai", "image": "https://images.unsplash.com/photo-1600585154346-1e8d9a0c6116?auto=format&fit=crop&w=600&q=80", "tags": ["High Ceiling", "Concierge", "WiFi"], "property_type": "Apartment", "furnishing": "Fully Furnished", "area": 1250, "rating": 4.7, "agent": "Skyline Realty", "agent_rating": 4.7},
        ]
    }

    def create_analytics_df():
        # ... function content from your script ...
        pass # Placeholder for brevity

    # --- Sidebar for this specific tool ---
    with st.sidebar:
        st.markdown("---")
        st.header("🏠 Rental Finder Filters")
        area = st.selectbox("📍 Select City", ["", "Jaipur", "Delhi", "Mumbai"], index=1)
        
        if area:
            min_rent, max_rent = st.slider("💰 Monthly Rent Range (₹)", 5000, 60000, (8000, 40000))
            selected_bhk = st.multiselect("🛏️ BHK Configuration", [1, 2, 3, 4], default=[2, 3])
            property_types = list(set([p["property_type"] for p in rental_data[area]]))
            selected_types = st.multiselect("🏢 Property Type", property_types, default=property_types)
    
    # --- Main Content ---
    st.markdown('<p class="title">Premium Rental Finder</p>', unsafe_allow_html=True)
    
    if area:
        filtered = [
            p for p in rental_data[area]
            if min_rent <= p["rent"] <= max_rent and p["rooms"] in selected_bhk and p["property_type"] in selected_types
        ]
        
        st.info(f"{len(filtered)} Properties Found in {area}")
        
        for prop in filtered:
            with st.container():
                st.markdown(f"<div class='property-card'>", unsafe_allow_html=True)
                st.image(prop["image"], use_column_width=True)
                st.markdown(f"### {prop['name']}")
                st.markdown(f"**Rent:** ₹{prop['rent']}/month | **BHK:** {prop['rooms']} | **Type:** {prop['property_type']}")
                st.markdown(f"**Address:** {prop['address']}")
                st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("👈 Please select a city from the sidebar to start exploring properties.")

    # --- End of Premium Rental Finder Code ---
def ml_advanced_salary_predictor():
    # --- Start of Advanced Salary Predictor Code ---
    
    # Import necessary modules locally
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error, r2_score
    import plotly.express as px
    import time

    # --- Custom CSS for this tool ---
    st.markdown("""
    <style>
        .salary-predictor-card {
            background: white; border-radius: 20px;
            box-shadow: 0 8px 25px rgba(67, 97, 238, 0.1);
            padding: 25px; margin-bottom: 20px;
            border-left: 5px solid #4361ee;
        }
        .salary-predictor-nav-container {
            display: flex; justify-content: center; margin-bottom: 20px; gap: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- Data and Model ---
    @st.cache_data
    def load_data():
        data = {
            "Experience": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            "Salary": [25000, 30000, 35000, 40000, 50000, 60000, 70000, 85000, 100000,
                       115000, 130000, 145000, 160000, 180000, 200000, 225000]
        }
        return pd.DataFrame(data)

    @st.cache_resource
    def train_model():
        df = load_data()
        X = df[["Experience"]]
        y = df["Salary"]
        model = LinearRegression()
        model.fit(X, y)
        return model

    model = train_model()
    df = load_data()

    # --- Page Definitions ---
    def home_page():
        st.info("Welcome to the Advanced Salary Predictor! Use the navigation below to explore.")
        # ... (You can add more content from your script's home_page if desired) ...

    def predict_salary_page():
        st.markdown('<div class="salary-predictor-card">', unsafe_allow_html=True)
        st.subheader("💰 Predict Your Salary")
        with st.form("salary_form"):
            exp_input = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, value=5.0, step=0.5)
            submitted = st.form_submit_button("🔮 Predict Salary")
            if submitted:
                with st.spinner("Analyzing..."):
                    time.sleep(1)
                    prediction = model.predict(np.array([[exp_input]]))[0]
                    st.metric(label=f"Predicted Salary for {exp_input} years", value=f"₹ {int(prediction):,}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("📊 Experience vs. Salary Data")
        fig = px.scatter(df, x="Experience", y="Salary", title="Salary Data")
        fig.add_scatter(x=[exp_input], y=[prediction] if 'prediction' in locals() else [], mode='markers', marker=dict(size=15, color="red"), name="Your Prediction")
        st.plotly_chart(fig, use_container_width=True)


    def market_insights_page():
        st.markdown('<div class="salary-predictor-card">', unsafe_allow_html=True)
        st.subheader("📈 Market Insights")
        st.write("This chart shows the general trend of salary increasing with experience.")
        fig = px.line(df, x="Experience", y="Salary", title="Salary Growth Trend", markers=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)


    # --- Navigation and Page Rendering ---
    if 'salary_predictor_page' not in st.session_state:
        st.session_state.salary_predictor_page = "🏠 Home"

    st.markdown('<div class="salary-predictor-nav-container">', unsafe_allow_html=True)
    cols = st.columns(4)
    if cols[0].button("🏠 Home", key="sp_home", use_container_width=True):
        st.session_state.salary_predictor_page = "🏠 Home"
    if cols[1].button("💰 Predict Salary", key="sp_predict", use_container_width=True):
        st.session_state.salary_predictor_page = "💰 Predict Salary"
    if cols[2].button("📈 Market Insights", key="sp_insights", use_container_width=True):
        st.session_state.salary_predictor_page = "📈 Market Insights"
    if cols[3].button("ℹ️ About", key="sp_about", use_container_width=True):
        st.session_state.salary_predictor_page = "ℹ️ About"
    st.markdown('</div>', unsafe_allow_html=True)


    # Display the selected page
    if st.session_state.salary_predictor_page == "🏠 Home":
        home_page()
    elif st.session_state.salary_predictor_page == "💰 Predict Salary":
        predict_salary_page()
    elif st.session_state.salary_predictor_page == "📈 Market Insights":
        market_insights_page()
    elif st.session_state.salary_predictor_page == "ℹ️ About":
        st.markdown('<div class="salary-predictor-card">', unsafe_allow_html=True)
        st.subheader("ℹ️ About This Tool")
        st.write("This tool uses a Linear Regression model trained on a sample dataset to predict salary based on years of experience.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    # --- End of Advanced Salary Predictor Code ---
def prompt_engineering_gemini_optimizer():
    # --- Start of Gemini Prompt Optimizer Code ---
    st.subheader("🚀 Gemini Prompt Engineering Playground")
    st.caption("Optimize your prompts using advanced techniques with Gemini 1.5 Flash")

    # Import necessary libraries locally
    from openai import OpenAI

    # Initialize session state for this tool specifically to avoid conflicts
    if "gemini_history" not in st.session_state:
        st.session_state.gemini_history = []

    # Sidebar configuration
    with st.sidebar:
        st.markdown("---")
        st.header("⚙️ Gemini Optimizer Settings")
        
        # Use st.secrets for the API key
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
            st.success("Gemini API Key loaded from secrets.")
        except KeyError:
            st.error("GEMINI_API_KEY not found in secrets.toml")
            st.stop()
        
        technique = st.selectbox(
            "Prompting Technique:",
            ["Direct Query", "Few-Shot", "Chain-of-Thought", "Role-Play", "Self-Correction"],
            key="gemini_technique"
        )
        max_tokens = st.slider("Max Response Tokens:", 100, 1000, 300, 50, key="gemini_tokens")
        temperature = st.slider("Temperature:", 0.0, 1.0, 0.7, 0.05, key="gemini_temp")

    # --- Helper functions ---
    TECHNIQUES = {
        "Direct Query": "Standard direct question",
        "Few-Shot": "Provide examples before the actual question",
        "Chain-of-Thought": "Request step-by-step reasoning before answering",
        "Role-Play": "Answer as a specific character/persona",
        "Self-Correction": "Critique and improve previous answers"
    }

    def apply_technique(prompt, tech):
        if tech == "Few-Shot":
            return f"Example 1:\nQ: What is a Python list?\nA: An ordered, mutable collection of items.\n\nNow answer this:\nQ: {prompt}"
        elif tech == "Chain-of-Thought":
            return f"Analyze step-by-step before answering the following question:\n{prompt}"
        elif tech == "Role-Play":
            return f"You are Professor Code, a world-class Python educator. Explain the following concept simply:\n{prompt}"
        elif tech == "Self-Correction":
            return f"First, give an initial answer. Then, critique it and provide an improved version for the question:\n{prompt}"
        return prompt

    # --- Main UI ---
    user_input = st.text_area("Your Query:", height=150, placeholder="e.g., Explain list comprehensions in Python")

    if st.button("✨ Generate Response", use_container_width=True):
        if not user_input:
            st.error("Please enter a query.")
        else:
            try:
                client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=api_key)
                optimized_prompt = apply_technique(user_input, technique)
                
                with st.spinner(f"Generating response using {technique}..."):
                    response = client.chat.completions.create(
                        model="gemini-1.5-flash",
                        messages=[{"role": "user", "content": optimized_prompt}],
                        max_tokens=max_tokens,
                        temperature=temperature
                    )
                    result = response.choices[0].message.content
                
                st.session_state.gemini_history.append({
                    "query": user_input, "technique": technique,
                    "response": result, "tokens": response.usage.total_tokens
                })

            except Exception as e:
                st.error(f"An API error occurred: {e}")

    # --- Display latest response and history ---
    if st.session_state.gemini_history:
        latest_entry = st.session_state.gemini_history[-1]
        st.subheader("📝 Latest Response:")
        st.success(latest_entry["response"])
        st.caption(f"Tokens used: {latest_entry['tokens']} | Technique: {latest_entry['technique']}")

    st.subheader("📚 Conversation History")
    for i, entry in enumerate(reversed(st.session_state.gemini_history)):
        with st.expander(f"#{len(st.session_state.gemini_history)-i}: {entry['query'][:40]}..."):
            st.caption(f"Technique: {entry['technique']} | Tokens: {entry['tokens']}")
            st.info(entry["response"])

    # --- End of Gemini Prompt Optimizer Code ---
def project_voice_analyzer_ai():
    # --- Start of Voice Analyzer AI Code ---
    
    # Import necessary modules locally
    import librosa
    import numpy as np
    import tempfile
    import os
    import time
    import matplotlib.pyplot as plt

    # Use specific session state keys to avoid conflicts
    if "voice_app_started" not in st.session_state:
        st.session_state.voice_app_started = False
    if "voice_app_agreed" not in st.session_state:
        st.session_state.voice_app_agreed = False

    # Splash Screen
    if not st.session_state.voice_app_started:
        st.markdown("""
        <style>
            .splash h1 { font-size: 48px; color: #00ffe0; }
        </style>
        <div class="splash" style="text-align: center; margin-top: 100px;">
            <h1>🎧 Voice Analyzer AI</h1>
            <p>Welcome! Analyze your voice using smart AI.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Start Analysis"):
            st.session_state.voice_app_started = True
            st.rerun()
        return # Stop execution here until button is pressed

    # Disclaimer Page
    if not st.session_state.voice_app_agreed:
        st.warning("⚠️ Voice Privacy Disclaimer")
        st.info("This app uses AI to analyze your voice. No data is stored or shared.")
        if st.button("✅ I Agree & Continue"):
            st.session_state.voice_app_agreed = True
            st.rerun()
        return # Stop execution here until button is pressed

    # --- Main App Starts Here ---
    st.subheader("🎧 AI Gender & Voice Feature Detector")
    st.write("Upload a voice file (WAV or MP3) to detect gender and view detailed audio features.")

    def extract_voice_features(audio_path):
        y, sr = librosa.load(audio_path, sr=None)
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        pitch_values = pitches[magnitudes > np.median(magnitudes)]
        avg_pitch = np.mean(pitch_values) if pitch_values.size > 0 else 150 # Default pitch
        
        gender = "Female 👩" if avg_pitch > 165 else "Male 👨"
        duration = librosa.get_duration(y=y, sr=sr)
        energy = np.mean(np.square(y))
        
        return {
            "gender": gender,
            "pitch": avg_pitch,
            "duration": duration,
            "energy": energy,
        }

    uploaded_file = st.file_uploader("📤 Upload your voice file", type=["wav", "mp3"])

    if uploaded_file:
        st.audio(uploaded_file)
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_file.getvalue())
            temp_audio_path = tmp.name

        if st.button("Analyze Voice"):
            with st.spinner("⏳ Analyzing your voice..."):
                try:
                    features = extract_voice_features(temp_audio_path)
                    
                    st.metric(label="Detected Gender", value=features['gender'])
                    
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Average Pitch", f"{features['pitch']:.2f} Hz")
                    col2.metric("Duration", f"{features['duration']:.2f} sec")
                    col3.metric("Energy Level", f"{features['energy']:.4f}")

                except Exception as e:
                    st.error(f"❌ Error analyzing audio: {e}")
                finally:
                    os.unlink(temp_audio_path) # Clean up the temporary file

    # --- End of Voice Analyzer AI Code ---
def python_advanced_ram_reader():
    # --- Start of Advanced RAM Reader Code ---
    st.subheader("🧠 Advanced RAM Monitor")
    st.markdown("This tool displays real-time memory usage using the **psutil** library.")

    # Import necessary modules locally
    import psutil
    import platform
    import time
    import csv
    import pandas as pd
    from datetime import datetime

    # --- Helper Functions ---
    def log_ram_to_csv(file_name='ram_log.csv'):
        ram = psutil.virtual_memory()
        # Create header if file doesn't exist
        if not os.path.exists(file_name):
            with open(file_name, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Time", "Total_GB", "Available_GB", "Used_GB", "Usage_%"])
        # Append data
        with open(file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                round(ram.total / (1024 ** 3), 2),
                round(ram.available / (1024 ** 3), 2),
                round(ram.used / (1024 ** 3), 2),
                ram.percent
            ])

    def get_top_memory_processes(n=5):
        processes = []
        for p in psutil.process_iter(['name', 'memory_info']):
            try:
                # memory_info().rss returns memory usage in bytes
                processes.append((p.info['name'], p.info['memory_info'].rss))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        top = sorted(processes, key=lambda x: x[1], reverse=True)[:n]
        return top

    # --- Main App UI ---
    if 'ram_info' not in st.session_state:
        st.session_state.ram_info = None

    if st.button("🔄 Refresh RAM Info", use_container_width=True):
        ram = psutil.virtual_memory()
        swap = psutil.swap_memory()
        top_procs = get_top_memory_processes()
        st.session_state.ram_info = {
            "ram": ram, "swap": swap, "top_procs": top_procs
        }
        log_ram_to_csv() # Log data on each refresh

    if st.session_state.ram_info:
        ram = st.session_state.ram_info["ram"]
        swap = st.session_state.ram_info["swap"]
        top_procs = st.session_state.ram_info["top_procs"]

        st.subheader("📊 Real-time RAM Information")
        col1, col2 = st.columns(2)
        col1.metric("Total RAM", f"{ram.total / (1024 ** 3):.2f} GB")
        col2.metric("Used RAM", f"{ram.used / (1024 ** 3):.2f} GB", delta=f"{ram.percent}% Used")
        
        st.progress(ram.percent / 100)
        if ram.percent >= 80:
            st.error("⚠️ ALERT: High RAM usage detected!")

        st.subheader("🔥 Top 5 Memory Consuming Processes")
        df = pd.DataFrame(
            [(p[0], f"{p[1]/(1024**2):.2f} MB") for p in top_procs],
            columns=["Process Name", "Memory Usage"]
        )
        st.table(df)

    # Display historical logs
    st.subheader("📁 RAM Usage Log (Last 20 Readings)")
    try:
        log_df = pd.read_csv("ram_log.csv")
        st.line_chart(log_df.set_index("Time")[["Used_GB", "Available_GB"]].tail(20))
    except FileNotFoundError:
        st.info("No log file found yet. Click 'Refresh RAM Info' to start logging.")
    
    # --- End of Advanced RAM Reader Code ---
def project_roast_ya_toast():
    # --- Start of Roast Ya Toast Code ---
    
    # Import necessary modules locally
    import pyttsx3
    import random
    import time
    from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

    # Initialize session state specifically for this app
    if "ryt_start_app" not in st.session_state:
        st.session_state.ryt_start_app = False
    if "ryt_agreed" not in st.session_state:
        st.session_state.ryt_agreed = False

    # Splash Screen
    if not st.session_state.ryt_start_app:
        st.markdown("<h1 style='text-align: center; color: #00ffe0;'>🎧 Roast Ya Toast AI</h1>", unsafe_allow_html=True)
        st.info("An interactive AI that responds to your hand gestures.")
        if st.button("🚀 Start The Fun"):
            st.session_state.ryt_start_app = True
            st.rerun()
        return

    # Disclaimer Page
    if not st.session_state.ryt_agreed:
        st.warning("⚠️ Disclaimer")
        st.info("This app uses your camera for hand gesture recognition. No video is stored or shared.")
        if st.button("✅ I Understand & Agree"):
            st.session_state.ryt_agreed = True
            st.rerun()
        return

    # --- Main App Starts Here ---
    st.subheader("🤖 Roast Ya Toast - Enhanced Edition")
    
    # --- Helper functions and classes ---
    @st.cache_resource
    def get_voice_engine():
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        return engine

    engine = get_voice_engine()

    DIALOGUES = {
        "compliments": ["You're the human version of a power-up!", "You're cooler than the other side of the pillow!"],
        "light_roasts": ["Are you Wi-Fi? Because I'm not feeling a strong connection.", "You're the reason shampoo bottles have instructions."],
        "jokes": ["Why don't scientists trust atoms? Because they make up everything!", "I'm reading a book on anti-gravity. It's impossible to put down!"],
        "deep_roasts": ["You're the human version of a 404 error.", "You're proof that rock bottom has a basement."],
        "facts": ["A group of flamingos is called a 'flamboyance'.", "Octopuses have three hearts, nine brains, and blue blood."]
    }

    if 'last_message' not in st.session_state:
        st.session_state.last_message = ""
        st.session_state.message_history = []

    def speak_and_print(msg, category):
        st.session_state.last_message = f"**{category}:** {msg}"
        st.session_state.message_history.append(st.session_state.last_message)
        if len(st.session_state.message_history) > 5:
            st.session_state.message_history.pop(0)
        engine.say(msg)
        engine.runAndWait()

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

    def count_fingers(hand_landmarks):
        count = 0
        tips_ids = [8, 12, 16, 20]
        for tip_id in tips_ids:
            if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
                count += 1
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
            count += 1
        return count

    class VideoTransformer(VideoTransformerBase):
        def __init__(self):
            self.last_gesture_time = 0
            self.cooldown = 3 # seconds
        
        def transform(self, frame):
            img = frame.to_ndarray(format="bgr24")
            img = cv2.flip(img, 1)
            results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            
            if results.multi_hand_landmarks and time.time() - self.last_gesture_time > self.cooldown:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp.solutions.drawing_utils.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    fingers = count_fingers(hand_landmarks)
                    
                    category, key = None, None
                    if fingers == 1: category, key = "Compliment", "compliments"
                    elif fingers == 2: category, key = "Light Roast", "light_roasts"
                    elif fingers == 3: category, key = "Joke", "jokes"
                    elif fingers == 4: category, key = "Fun Fact", "facts"
                    elif fingers == 5: category, key = "Deep Roast", "deep_roasts"

                    if category:
                        msg = random.choice(DIALOGUES[key])
                        speak_and_print(msg, category)
                        self.last_gesture_time = time.time()
            return img

    # --- App Layout ---
    st.info("""
    **👋 Hand Gesture Controls:**
    - **1 Finger:** Get a compliment
    - **2 Fingers:** Get a light roast
    - **3 Fingers:** Hear a joke
    - **4 Fingers:** Learn a fun fact
    - **5 Fingers:** Get a deep roast
    """)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("🎥 Live Camera Feed")
        webrtc_streamer(key="webrtc", video_transformer_factory=VideoTransformer)
    
    with col2:
        st.header("💬 Dialogue Output")
        if st.session_state.last_message:
            st.success(st.session_state.last_message)
        
        st.header("📜 Message History")
        for msg in reversed(st.session_state.message_history):
            st.write(msg)

    # --- End of Roast Ya Toast Code ---
def javascript_advanced_linux_article():
    st.subheader("📄 Advanced: Why Companies Are Switching to Linux")
    
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Advanced: Why Companies Are Switching to Linux</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif; line-height: 1.7; color: #333;
                background-color: #f8f9fa; max-width: 900px; margin: 0 auto; padding: 20px;
            }
            header { text-align: center; margin-bottom: 40px; }
            h1 { font-size: 2.8em; color: #1a2533; }
            .stats-grid {
                display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;
                text-align: center; margin: 30px 0;
            }
            .stat-card {
                background: white; padding: 20px; border-radius: 10px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            }
            .stat-number { font-size: 2.5em; font-weight: bold; color: #007bff; }
            .tabs { display: flex; border-bottom: 2px solid #dee2e6; margin-bottom: 20px; }
            .tab-button {
                padding: 10px 20px; border: none; background: transparent; cursor: pointer;
                font-size: 1.1em; font-weight: 600; color: #6c757d;
            }
            .tab-button.active { color: #007bff; border-bottom: 2px solid #007bff; }
            .tab-content { display: none; }
            .tab-content.active { display: block; background: white; padding: 20px; border-radius: 8px; }
        </style>
    </head>
    <body>
        <header>
            <h1>The Enterprise Shift to Linux</h1>
            <p>Exploring the data-driven reasons behind the migration.</p>
        </header>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number" data-target="96">0</div>
                <div>% of the world's top 1 million servers</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="90">0</div>
                <div>% of all cloud infrastructure</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="100">0</div>
                <div>% of the world's top 500 supercomputers</div>
            </div>
        </div>

        <div class="tabs">
            <button class="tab-button active" onclick="openTab(event, 'Cost')">💰 Cost Efficiency</button>
            <button class="tab-button" onclick="openTab(event, 'Security')">🛡️ Security</button>
            <button class="tab-button" onclick="openTab(event, 'Performance')">🚀 Performance</button>
        </div>

        <div id="Cost" class="tab-content active">
            <h2>Zero Licensing Fees</h2>
            <p>Unlike proprietary OSs, Linux is open-source and free, eliminating substantial licensing costs for enterprises. This allows budget reallocation to other critical areas like R&D and talent acquisition.</p>
        </div>
        <div id="Security" class="tab-content">
            <h2>Robust and Transparent</h2>
            <p>With its open-source nature, Linux's code is constantly scrutinized by a global community of developers. This transparency leads to faster discovery and patching of vulnerabilities, making it a highly secure choice for servers and critical infrastructure.</p>
        </div>
        <div id="Performance" class="tab-content">
            <h2>Stable and Reliable</h2>
            <p>Linux is renowned for its stability and efficiency, often running for years without a reboot. It powers the majority of high-performance computing (HPC) clusters and cloud servers, handling massive workloads with exceptional reliability.</p>
        </div>

        <script>
            function openTab(evt, tabName) {
                var i, tabcontent, tablinks;
                tabcontent = document.getElementsByClassName("tab-content");
                for (i = 0; i < tabcontent.length; i++) {
                    tabcontent[i].style.display = "none";
                }
                tablinks = document.getElementsByClassName("tab-button");
                for (i = 0; i < tablinks.length; i++) {
                    tablinks[i].className = tablinks[i].className.replace(" active", "");
                }
                document.getElementById(tabName).style.display = "block";
                evt.currentTarget.className += " active";
            }

            const counters = document.querySelectorAll('.stat-number');
            const speed = 200;
            counters.forEach(counter => {
                const updateCount = () => {
                    const target = +counter.getAttribute('data-target');
                    const count = +counter.innerText;
                    const inc = target / speed;
                    if (count < target) {
                        counter.innerText = Math.ceil(count + inc);
                        setTimeout(updateCount, 1);
                    } else {
                        counter.innerText = target;
                    }
                };
                updateCount();
            });
        </script>
    </body>
    </html>
    """
    components.html(html_code, height=600, scrolling=True)

def javascript_advanced_docker_article():
    st.subheader("🐳 Advanced: Docker Adoption Case Studies")

    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-R">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Advanced Docker Case Studies</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif; line-height: 1.7; color: #333;
                background-color: #f8f9fa; max-width: 900px; margin: 0 auto; padding: 20px;
            }
            header { text-align: center; margin-bottom: 40px; }
            h1 { font-size: 2.8em; color: #0db7ed; }
            .filter-bar {
                display: flex; justify-content: center; gap: 10px; margin-bottom: 30px;
            }
            .filter-btn {
                padding: 10px 20px; border: 1px solid #ddd; border-radius: 20px;
                background: white; cursor: pointer; font-weight: 600;
            }
            .filter-btn.active { background: #0db7ed; color: white; border-color: #0db7ed; }
            .case-study-grid {
                display: grid; grid-template-columns: 1fr; gap: 20px;
            }
            .case-study-card {
                background: white; border-radius: 10px; overflow: hidden;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08); display: flex;
            }
            .case-study-logo {
                flex: 0 0 120px; background: #f0f8ff; display: grid; place-items: center;
            }
            .case-study-content { padding: 20px; }
            .case-study-tag {
                display: inline-block; padding: 4px 12px; border-radius: 15px;
                font-size: 0.8em; font-weight: bold; margin-right: 5px;
            }
            .tag-finance { background: #ffebcd; color: #d98200; }
            .tag-media { background: #d4edda; color: #155724; }
            .tag-hr { background: #f8d7da; color: #721c24; }
        </style>
    </head>
    <body>
        <header>
            <h1>Real-World Docker Adoption</h1>
            <p>How industry leaders are leveraging containerization.</p>
        </header>

        <div class="filter-bar">
            <button class="filter-btn active" onclick="filterSelection('all')">All</button>
            <button class="filter-btn" onclick="filterSelection('finance')">Finance</button>
            <button class="filter-btn" onclick="filterSelection('media')">Media</button>
            <button class="filter-btn" onclick="filterSelection('hr')">HR</button>
        </div>

        <div class="case-study-grid">
            <div class="case-study-card filterable finance">
                <div class="case-study-logo">PayPal</div>
                <div class="case-study-content">
                    <h3>PayPal: Accelerating Development</h3>
                    <span class="case-study-tag tag-finance">Finance</span>
                    <p>Adopted Docker to standardize environments, leading to <strong>90% faster deployments</strong> and reduced infrastructure costs.</p>
                </div>
            </div>
            <div class="case-study-card filterable media">
                <div class="case-study-logo">Spotify</div>
                <div class="case-study-content">
                    <h3>Spotify: Scaling Microservices</h3>
                    <span class="case-study-tag tag-media">Media</span>
                    <p>Migrated to Docker for isolated microservices, resulting in <strong>40% faster deployment cycles</strong> and improved fault isolation.</p>
                </div>
            </div>
            <div class="case-study-card filterable hr">
                <div class="case-study-logo">ADP</div>
                <div class="case-study-content">
                    <h3>ADP: Enhancing Security</h3>
                    <span class="case-study-tag tag-hr">HR</span>
                    <p>Uses Docker to isolate applications and for secure image signing, which has <strong>reduced security risks</strong> and simplified compliance.</p>
                </div>
            </div>
        </div>

        <script>
            function filterSelection(c) {
                var x, i;
                x = document.getElementsByClassName("filterable");
                if (c == "all") c = "";
                for (i = 0; i < x.length; i++) {
                    x[i].style.display = "none";
                    if (x[i].className.indexOf(c) > -1) {
                        x[i].style.display = "flex";
                    }
                }
                // Style active button
                var btnContainer = document.querySelector(".filter-bar");
                var btns = btnContainer.getElementsByClassName("filter-btn");
                for (var j = 0; j < btns.length; j++) {
                    btns[j].classList.remove("active");
                }
                event.currentTarget.classList.add("active");
            }
            filterSelection('all'); // Show all on load
        </script>
    </body>
    </html>
    """
    components.html(html_code, height=600, scrolling=True)
def docker_aws_ec2_manager():
    # --- Start of AWS EC2 Manager Code ---
    st.subheader("☁️ AWS EC2 Instance Manager")
    st.markdown("Manage your AWS EC2 instances directly from this dashboard.")

    # Import necessary modules locally
    import boto3
    from botocore.exceptions import ClientError
    import os
    import pandas as pd

    # --- EC2Manager Class (from your script) ---
    class EC2Manager:
        def __init__(self, region_name='ap-south-1'):
            try:
                # Use st.cache_resource to initialize the client only once
                self.ec2_client = boto3.client('ec2', region_name=region_name)
            except Exception as e:
                st.error(f"Error initializing Boto3 client: {e}")
                st.stop()
        
        # ... (Paste all methods from your EC2Manager class here)
        # e.g., create_key_pair, create_security_group, create_instance,
        # stop_instances, start_instances, terminate_instances, describe_all_instances

        def describe_all_instances(self):
            try:
                response = self.ec2_client.describe_instances()
                instances = []
                for reservation in response['Reservations']:
                    for instance in reservation['Instances']:
                        instances.append({
                            "Instance ID": instance['InstanceId'],
                            "State": instance['State']['Name'],
                            "Type": instance['InstanceType'],
                            "Public IP": instance.get('PublicIpAddress', 'N/A'),
                        })
                return instances
            except ClientError as e:
                st.error(f"Error describing instances: {e}")
                return []
        
        def start_instances(self, instance_ids):
            try:
                self.ec2_client.start_instances(InstanceIds=instance_ids)
                waiter = self.ec2_client.get_waiter('instance_running')
                waiter.wait(InstanceIds=instance_ids)
                return True
            except ClientError as e:
                st.error(f"Error starting instances: {e}")
                return False

        def stop_instances(self, instance_ids):
            try:
                self.ec2_client.stop_instances(InstanceIds=instance_ids)
                waiter = self.ec2_client.get_waiter('instance_stopped')
                waiter.wait(InstanceIds=instance_ids)
                return True
            except ClientError as e:
                st.error(f"Error stopping instances: {e}")
                return False

        def terminate_instances(self, instance_ids):
            try:
                self.ec2_client.terminate_instances(InstanceIds=instance_ids)
                waiter = self.ec2_client.get_waiter('instance_terminated')
                waiter.wait(InstanceIds=instance_ids)
                return True
            except ClientError as e:
                st.error(f"Error terminating instances: {e}")
                return False


    # --- Main App UI ---
    st.sidebar.markdown("---")
    st.sidebar.header("AWS EC2 Manager")
    selected_region = st.sidebar.selectbox("Select AWS Region", ["ap-south-1", "us-east-1", "eu-west-1"])

    try:
        manager = EC2Manager(region_name=selected_region)
    except Exception as e:
        st.error("Failed to initialize AWS connection. Please configure your credentials.")
        st.stop()

    tab1, tab2 = st.tabs(["📊 Instance Dashboard", "⚙️ Manage Instances"])

    with tab1:
        st.header("EC2 Instance Dashboard")
        if st.button("🔄 Refresh Instance List"):
            st.rerun()
            
        instances = manager.describe_all_instances()
        if instances:
            df = pd.DataFrame(instances)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No EC2 instances found in this region.")

    with tab2:
        st.header("Manage EC2 Instances")
        instances = manager.describe_all_instances()
        instance_ids = [inst["Instance ID"] for inst in instances]
        
        if not instance_ids:
            st.warning("No instances available to manage.")
        else:
            selected_ids = st.multiselect("Select Instance(s)", instance_ids)
            
            if selected_ids:
                col1, col2, col3 = st.columns(3)
                if col1.button("▶️ Start", use_container_width=True):
                    with st.spinner(f"Starting {len(selected_ids)} instance(s)..."):
                        if manager.start_instances(selected_ids):
                            st.success("Instance(s) started successfully!")
                
                if col2.button("🛑 Stop", use_container_width=True):
                    with st.spinner(f"Stopping {len(selected_ids)} instance(s)..."):
                        if manager.stop_instances(selected_ids):
                            st.success("Instance(s) stopped successfully!")

                if col3.button("🔥 Terminate", use_container_width=True):
                    with st.spinner(f"Terminating {len(selected_ids)} instance(s)..."):
                        if manager.terminate_instances(selected_ids):
                            st.success("Instance(s) terminated successfully!")
                            st.balloons()
    
    # --- End of AWS EC2 Manager Code ---
def aws_advanced_infra_manager():
    # --- Start of Advanced AWS Infra Manager Code ---
    st.subheader("🚀 Advanced AWS Infrastructure Manager")
    st.markdown("Provision, manage, and deprovision a full AWS application stack with an interactive dashboard.")

    # Import necessary modules locally
    import boto3
    from botocore.exceptions import ClientError
    import os
    import pandas as pd
    import time

    # --- AWSInfraManager Class (Enhanced for Streamlit) ---
    class AWSInfraManager:
        def __init__(self, region_name='ap-south-1', project_name='my-app'):
            self.region = region_name
            self.project_name = project_name
            self.key_name = f"{self.project_name}-key"
            self.sg_name = f"{self.project_name}-sg"
            try:
                self.ec2_client = boto3.client('ec2', region_name=self.region)
                self.ec2_resource = boto3.resource('ec2', region_name=self.region)
            except Exception as e:
                raise ConnectionError(f"Failed to initialize Boto3 client: {e}")

        def get_project_resources(self):
            instances_df = pd.DataFrame()
            sg_df = pd.DataFrame()
            key_df = pd.DataFrame()
            
            # Get Instances
            response = self.ec2_client.describe_instances(Filters=[{'Name': 'tag:Project', 'Values': [self.project_name]}])
            instance_list = []
            for r in response['Reservations']:
                for i in r['Instances']:
                    if i['State']['Name'] != 'terminated':
                        instance_list.append({'ID': i['InstanceId'], 'Type': i['InstanceType'], 'State': i['State']['Name'], 'Public IP': i.get('PublicIpAddress', 'N/A')})
            if instance_list: instances_df = pd.DataFrame(instance_list)

            # Get Security Groups
            try:
                sg_response = self.ec2_client.describe_security_groups(GroupNames=[self.sg_name])
                sg_list = [{'ID': sg['GroupId'], 'Name': sg['GroupName'], 'Description': sg['Description']} for sg in sg_response['SecurityGroups']]
                if sg_list: sg_df = pd.DataFrame(sg_list)
            except ClientError: pass # Group not found

            # Get Key Pairs
            try:
                key_response = self.ec2_client.describe_key_pairs(KeyNames=[self.key_name])
                key_list = [{'Name': k['KeyName'], 'Fingerprint': k.get('KeyFingerprint', 'N/A')} for k in key_response['KeyPairs']]
                if key_list: key_df = pd.DataFrame(key_list)
            except ClientError: pass # Key not found
                
            return instances_df, sg_df, key_df

        # ... (Include other methods like provision, launch, deprovision from your script) ...
        # For brevity, these are simplified here but you should paste your full class methods.

    # --- Main App UI ---
    st.sidebar.markdown("---")
    st.sidebar.header("AWS Project Configuration")
    project_name = st.sidebar.text_input("Project Name", "streamlit-cloud-app", key="aws_proj_name")
    region = st.sidebar.selectbox("AWS Region", ["ap-south-1", "us-east-1", "eu-west-1"], key="aws_region")

    try:
        manager = AWSInfraManager(region_name=region, project_name=project_name)
    except ConnectionError as e:
        st.error(e)
        st.stop()
    
    tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🚀 Provision Stack", "🔥 Deprovision Stack"])

    with tab1:
        st.header(f"Resource Dashboard for Project: `{project_name}`")
        if st.button("🔄 Refresh Dashboard"):
            st.rerun()
        
        instances, sgs, keys = manager.get_project_resources()
        
        st.subheader("EC2 Instances")
        if not instances.empty: st.dataframe(instances, use_container_width=True)
        else: st.info("No active instances found for this project.")

        st.subheader("Security Groups")
        if not sgs.empty: st.dataframe(sgs, use_container_width=True)
        else: st.info("No security group found for this project.")

        st.subheader("Key Pairs")
        if not keys.empty: st.dataframe(keys, use_container_width=True)
        else: st.info("No key pair found for this project.")

    with tab2:
        st.header("Provision a New Application Stack")
        st.info("This will create a new Key Pair, Security Group, and EC2 Instance.")
        
        with st.form("provision_form"):
            instance_name = st.text_input("Instance Name", f"{project_name}-server-01")
            ami_id = st.text_input("AMI ID", "ami-0f5ee92e2d63afc18") # Amazon Linux 2023 for ap-south-1
            instance_type = st.selectbox("Instance Type", ["t2.micro", "t3.small"])
            submitted = st.form_submit_button("🚀 Provision Now")
            
            if submitted:
                # Here you would call your full manager.provision_network_and_security() and manager.launch_instance() methods
                st.success("Provisioning process would start here.")
                st.warning("Full provisioning logic from your script needs to be integrated.")

    with tab3:
        st.header("🔥 Deprovision All Project Resources")
        st.warning(f"**DANGER ZONE:** This will terminate all instances and delete the security group and key pair for project **`{project_name}`**. This is irreversible.")
        
        if st.checkbox(f"I understand and want to deprovision all resources for '{project_name}'."):
            if st.button("🔥 Deprovision Now", type="primary"):
                # Here you would call your full manager.deprovision_all() method
                st.success("Deprovisioning process would start here.")
                st.warning("Full deprovisioning logic from your script needs to be integrated.")

    # --- End of Advanced AWS Infra Manager Code ---
def javascript_advanced_aws_article():
    # --- Start of Advanced AWS Article Code ---
    st.subheader("🚀 Advanced: From Code to Cloud with AWS")
    st.markdown("An interactive guide to production-ready AWS deployment.")

    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Advanced AWS Deployment</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif; line-height: 1.8; color: #343a40;
                background-color: #f8f9fa; margin: 0; padding: 0;
            }
            .container {
                max-width: 900px; margin: 20px auto; padding: 20px;
            }
            header {
                text-align: center; padding: 20px; border-radius: 10px;
                background: linear-gradient(135deg, #0056b3, #17a2b8); color: white;
                margin-bottom: 30px;
            }
            header h1 { font-size: 2.8em; margin: 0; }
            .tabs { display: flex; border-bottom: 1px solid #dee2e6; margin-bottom: 20px; }
            .tab-button {
                padding: 12px 25px; border: none; background: transparent; cursor: pointer;
                font-size: 1.1em; font-weight: 600; color: #6c757d;
            }
            .tab-button.active { color: #0056b3; border-bottom: 3px solid #0056b3; }
            .tab-content { display: none; background: #ffffff; padding: 25px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
            .tab-content.active { display: block; }
            h2 { color: #0056b3; }
            code {
                background-color: #e9ecef; padding: 3px 7px; border-radius: 4px;
                font-family: monospace;
            }
            pre {
                background-color: #212529; color: #f8f9fa; padding: 15px;
                border-radius: 5px; white-space: pre-wrap;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>From Code to Cloud 🚀</h1>
                <p>An Advanced Guide to AWS Deployment</p>
            </header>

            <div class="tabs">
                <button class="tab-button active" onclick="openTab(event, 'Architecture')">🏛️ Architecture</button>
                <button class="tab-button" onclick="openTab(event, 'Workflow')">⚙️ Workflow</button>
                <button class="tab-button" onclick="openTab(event, 'Scaling')">📈 Scaling</button>
            </div>

            <div id="Architecture" class="tab-content active">
                <h2>The Blueprint: Architecting for the Cloud</h2>
                <h3>VPC: Your Private Fortress 🏰</h3>
                <p>A <strong>Virtual Private Cloud (VPC)</strong> is your isolated section of AWS. A production setup includes:</p>
                <ul>
                    <li><strong>Public Subnets:</strong> For public-facing resources like load balancers.</li>
                    <li><strong>Private Subnets:</strong> For protected backend resources like databases and application servers.</li>
                </ul>
                <h3>IAM Roles: The Key to Secure Services 🔑</h3>
                <p><strong>Never store AWS credentials on an EC2 instance.</strong> Use <strong>IAM Roles</strong> to grant your applications secure, temporary permissions to other AWS services.</p>
            </div>

            <div id="Workflow" class="tab-content">
                <h2>The Practical Deployment Workflow</h2>
                <p>Using an "Infrastructure as Code" (IaC) approach is essential for consistency and automation.</p>
                <ol>
                    <li><strong>Network Foundation:</strong> Script the creation of your VPC, subnets, and gateways.</li>
                    <li><strong>Compute Layer (EC2):</strong> Launch instances into the correct subnets with appropriate security groups.</li>
                    <li><strong>Managed Database (RDS):</strong> Use RDS in a private subnet for managed, secure, and scalable databases.</li>
                </ol>
            </div>

            <div id="Scaling" class="tab-content">
                <h2>Scaling, Automation, and Beyond</h2>
                <h3>Auto Scaling & Load Balancing</h3>
                <p>This is the key to a resilient application:</p>
                <ul>
                    <li>An <strong>Application Load Balancer (ALB)</strong> distributes traffic across your instances.</li>
                    <li>An <strong>Auto Scaling Group (ASG)</strong> automatically adds or removes instances based on traffic, ensuring high availability and cost efficiency.</li>
                </ul>
                <pre><code>User Traffic -> Load Balancer -> [EC2, EC2, EC2] in Auto Scaling Group</code></pre>
            </div>
        </div>

        <script>
            function openTab(evt, tabName) {
                var i, tabcontent, tablinks;
                tabcontent = document.getElementsByClassName("tab-content");
                for (i = 0; i < tabcontent.length; i++) {
                    tabcontent[i].style.display = "none";
                }
                tablinks = document.getElementsByClassName("tab-button");
                for (i = 0; i < tablinks.length; i++) {
                    tablinks[i].className = tablinks[i].className.replace(" active", "");
                }
                document.getElementById(tabName).style.display = "block";
                evt.currentTarget.className += " active";
            }
        </script>
    </body>
    </html>
    """
    
    components.html(html_code, height=600, scrolling=True)
    # --- End of Advanced AWS Article Code ---
def javascript_jenkins_mastery_article():
    # --- Start of Advanced jenkins Article Code ---
    st.subheader("🚀 Advanced: From Code to jenkins with cicd")
    st.markdown("An interactive guide to production-ready cicd pipeline deployment.")

    html_code = """
    <!DOCTYPE html>
    <html lang="hi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Jenkins Mastery: From CI/CD to Infrastructure as Code</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                line-height: 1.7;
                color: #343a40;
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 900px;
                margin: 30px auto;
                padding: 30px 40px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            }
            header {
                text-align: center;
                border-bottom: 1px solid #dee2e6;
                padding-bottom: 20px;
                margin-bottom: 40px;
            }
            header h1 {
                font-size: 2.8em;
                color: #2c3e50;
                margin-bottom: 10px;
            }
            h2 {
                font-size: 2.2em;
                color: #3498db;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                margin-top: 50px;
            }
            h3 {
                font-size: 1.7em;
                color: #2980b9;
                margin-top: 40px;
            }
            p, li {
                font-size: 1.1em;
            }
            ul {
                list-style-type: '✅  ';
                padding-left: 20px;
            }
            strong, b {
                color: #2c3e50;
            }
            code {
                background-color: #e9ecef;
                padding: 3px 7px;
                border-radius: 4px;
                font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
                font-size: 0.95em;
            }
            pre {
                background-color: #282c34;
                color: #abb2bf;
                padding: 20px;
                border-radius: 8px;
                overflow-x: auto;
                font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
                font-size: 1em;
                white-space: pre-wrap;
                word-wrap: break-word;
            }
            pre code {
                background: none;
                padding: 0;
                color: inherit;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 25px;
            }
            th, td {
                border: 1px solid #dee2e6;
                padding: 12px 15px;
                text-align: left;
            }
            th {
                background-color: #e9ecef;
                font-size: 1.1em;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <header>
                <h1>Jenkins Mastery: CI/CD se Aage 🚀</h1>
                <p>Automation aur Infrastructure as Code ki Duniya</p>
            </header>

            <article>
                <p>Agar aap DevOps mein kaam karte hain, to aapne Jenkins ka naam zaroor suna hoga. Aksar log ise sirf ek Continuous Integration (CI) tool maante hain jo code ko build aur test karta hai. Lekin modern Jenkins isse kahin zyada powerful hai. Yeh ek complete automation engine hai jo aapke poore software delivery lifecycle aur infrastructure ko manage kar sakta hai.</p>
                <p>Yeh article aapko Jenkins ke "Freestyle jobs" se aage le jaayega aur un advanced concepts se rubaru karayega jo aaj ki high-velocity development teams istemal karti hain.</p>

                <hr style="margin: 50px 0;">

                <h2>1. Asli Power: Pipeline as Code aur Jenkinsfile</h2>
                <p>Purane samay mein, Jenkins jobs UI (user interface) ke through "click" karke banaye jaate the. Is approach ki kuch badi samasyayein hain: version control na hona, audit trail ki kami, aur reproducibility mein mushkil. Iska samadhan hai <strong>Pipeline as Code</strong>.</p>
                <p>Is approach mein, hum poori CI/CD pipeline ko ek text file mein code ke roop mein likhte hain. Is file ko <code>Jenkinsfile</code> kaha jaata hai aur ise aap apne project ke source code ke saath Git repository mein hi rakhte hain.</p>
                <h3>Fayde:</h3>
                <ul>
                    <li><strong>Version Control:</strong> Har change Git mein commit hota hai.</li>
                    <li><strong>Code Review:</strong> Pipeline changes ko bhi pull request ke through review kiya ja sakta hai.</li>
                    <li><strong>Durability & Recovery:</strong> Jenkins server crash hone par bhi pipeline definition code mein surakshit rehti hai.</li>
                </ul>

                <p><code>Jenkinsfile</code> ke do flavors hain: <strong>Declarative</strong> aur <strong>Scripted</strong>.</p>
                <table>
                    <thead>
                        <tr>
                            <th>Feature</th>
                            <th>Declarative Pipeline</th>
                            <th>Scripted Pipeline</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Syntax</strong></td>
                            <td>Saaf, saral aur pre-defined structure.</td>
                            <td>Ek full-fledged Groovy-based DSL (Domain Specific Language).</td>
                        </tr>
                        <tr>
                            <td><strong>Learning Curve</strong></td>
                            <td>Aasan. Shuruaat karne walon ke liye behtareen.</td>
                            <td>Thoda mushkil, Groovy ki samajh zaroori hai.</td>
                        </tr>
                        <tr>
                            <td><strong>Flexibility</strong></td>
                            <td>Thodi kam, ek nishchit sanrachna ka palan karna padta hai.</td>
                            <td>Bahut zyada. Complex logic aur custom steps likhne ki azaadi.</td>
                        </tr>
                        <tr>
                            <td><strong>Best For</strong></td>
                            <td>Adhiktar use cases ke liye standard aur recommended.</td>
                            <td>Bahut hi complex aur custom pipelines ke liye.</td>
                        </tr>
                    </tbody>
                </table>

                <h3>Declarative Pipeline ka Example:</h3>
                <pre><code>pipeline {
        // 1. Agent: Pipeline kahan run hoga?
        agent any // Koi bhi available agent

        // 2. Environment: Environment variables set karein
        environment {
            // Secrets ko Jenkins Credentials se fetch karein
            DOCKER_CREDS = credentials('dockerhub-credentials') 
        }

        // 3. Stages: Pipeline ke alag-alag charan
        stages {
            stage('Build') {
                steps {
                    echo 'Building the application...'
                    sh 'mvn clean install'
                }
            }
            stage('Test') {
                steps {
                    echo 'Running tests...'
                    sh 'mvn test'
                }
            }
            stage('Build & Push Docker Image') {
                steps {
                    script {
                        // Docker image build karein
                        def dockerImage = docker.build("your-username/my-app:${env.BUILD_NUMBER}")
                        
                        // Docker Hub par push karein
                        docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDS) {
                            dockerImage.push()
                        }
                    }
                }
            }
        }

        // 4. Post-build Actions: Pipeline ke baad kya karna hai?
        post {
            success {
                echo 'Pipeline succeeded!'
                mail to: 'team@example.com', subject: "Build Succeeded: ${env.JOB_NAME} [${env.BUILD_NUMBER}]", body: "Build was successful."
            }
            failure {
                echo 'Pipeline failed!'
                // Slack notification bhejein
            }
        }
    }</code></pre>

                <hr style="margin: 50px 0;">

                <h2>2. Advanced Pipeline Techniques</h2>
                
                <h3>Shared Libraries: Code ko Dry Rakhein</h3>
                <p>Agar aapke paas 50 microservices hain, to kya aap 50 <code>Jenkinsfile</code> mein ek jaisa code copy-paste karenge? Bilkul nahi. Iske liye <strong>Shared Libraries</strong> ka istemal hota hai. Shared Library ek alag Git repository hoti hai jismein aap common pipeline code (Groovy scripts) rakhte hain aur fir use apne <code>Jenkinsfile</code> mein import karke istemal karte hain.</p>
                
                <h3>Dynamic Agents: Docker aur Kubernetes ke Saath Integration</h3>
                <p>Modern Jenkins <strong>dynamic agents</strong> ka istemal karta hai, jahan har build ke liye ek naya, saaf suthra environment (jaise Docker container ya Kubernetes Pod) taiyar kiya jaata hai. Yeh auto-scaling aur resource optimization ke liye behtareen hai.</p>
                <pre><code>agent {
        docker {
            image 'maven:3.8.1-jdk-11'
            args '-v $HOME/.m2:/root/.m2' // Maven repository cache karne ke liye
        }
    }</code></pre>

                <h3>Multibranch Pipelines</h3>
                <p>Yeh feature aapki Git repository ko scan karta hai aur har branch (jaise <code>main</code>, <code>develop</code>, <code>feature/*</code>) ke liye, jisme <code>Jenkinsfile</code> maujood hai, automatically ek pipeline bana deta hai. Yeh Pull Requests ke liye bhi pipelines banata hai, jisse code merge karne se pehle hi use test kiya ja sake.</p>

                <hr style="margin: 50px 0;">

                <h2>3. Jenkins: Sirf CI/CD Nahi, Ek Automation Hub</h2>

                <h3>Infrastructure as Code (IaC) Orchestration</h3>
                <p>Aap Jenkins pipeline ka istemal <strong>Terraform</strong> ya <strong>Ansible</strong> jaise tools ko run karne ke liye kar sakte hain, jisse aapka infrastructure bhi code ke through manage ho.</p>

                <h3>Secrets Management</h3>
                <p>Apne <code>Jenkinsfile</code> mein kabhi bhi password ya API key ko plaintext mein na rakhein. Hamesha <strong>Jenkins Credentials</strong> feature ka istemal karein. Yeh secrets ko securely encrypt karke store karta hai.</p>

                <h3>Configuration as Code (JCasC)</h3>
                <p>Jaise hum pipeline ko code mein define karte hain, waise hi hum poore Jenkins controller ki configuration ko bhi code mein define kar sakte hain. <strong>Jenkins Configuration as Code (JCasC)</strong> plugin aapko YAML files ka istemal karke Jenkins ko configure karne ki suvidha deta hai.</p>

                <hr style="margin: 50px 0;">

                <h2>Antim Vichar</h2>
                <p>Jenkins ek tool se kahin badhkar hai; yeh ek DevOps philosophy ko shakti deta hai. Jab aap "Pipeline as Code", "Shared Libraries", "Dynamic Agents", aur "Configuration as Code" jaise principles ko apnate hain, to aap Jenkins ko ek simple build tool se ek atyant shaktishali, scalable, aur surakshit automation platform mein badal dete hain jo aapki organization ki raftaar ko kai guna badha sakta hai.</p>

            </article>
        </div>

    </body>
    </html>
    """
    components.html(html_code, height=600, scrolling=True)
def docker_compose_manager():
    # --- Start of Docker Compose Manager ---
    st.subheader("🚀 Docker Compose Project Manager")
    st.markdown("Manage your multi-container applications with Docker Compose.")

    import subprocess
    import os
    import pandas as pd

    # --- Helper Functions ---
    def run_compose_command(path, command):
        """Runs a docker-compose command in a specific directory and streams output."""
        full_command = f"docker-compose {command}"
        log_area = st.empty()
        log_content = f"$ cd {path}\n$ {full_command}\n\n"
        log_area.code(log_content, language="bash")
        
        process = subprocess.Popen(
            full_command, cwd=path, shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1
        )
        
        for line in iter(process.stdout.readline, ''):
            log_content += line
            log_area.code(log_content, language="bash")
        
        process.wait()
        process.stdout.close()
        return process.returncode == 0

    def get_compose_projects(base_path="."):
        """Finds directories containing docker-compose.yml files."""
        projects = []
        for root, dirs, files in os.walk(base_path):
            if "docker-compose.yml" in files or "docker-compose.yaml" in files:
                projects.append(root)
        return projects

    # --- Main UI ---
    st.sidebar.markdown("---")
    st.sidebar.header("Compose Manager")
    
    # Find Docker Compose projects in the current directory and subdirectories
    available_projects = get_compose_projects()
    if not available_projects:
        st.warning("No `docker-compose.yml` files found in the current directory or subdirectories.")
        st.info("Please run this application from a directory that contains your Docker Compose projects.")
        st.stop()

    selected_project_path = st.sidebar.selectbox("Select a Docker Compose Project", available_projects)
    
    if selected_project_path:
        st.header(f"Managing Project: `{selected_project_path}`")
        
        tab1, tab2, tab3 = st.tabs(["🚀 Control", "📜 Logs", "📊 Services"])

        with tab1:
            st.subheader("Project Up / Down")
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("🚀 Up (Detached)", use_container_width=True):
                    with st.spinner("Bringing project up..."):
                        if run_compose_command(selected_project_path, "up -d"):
                            st.success("Project is up and running in detached mode.")
                        else:
                            st.error("Failed to bring project up.")
            
            with col2:
                if st.button("🛑 Down", use_container_width=True, type="primary"):
                    with st.spinner("Bringing project down..."):
                        if run_compose_command(selected_project_path, "down"):
                            st.success("Project has been stopped and removed.")
                        else:
                            st.error("Failed to bring project down.")

        with tab2:
            st.subheader("View Service Logs")
            try:
                # Get services by running docker-compose ps
                result = subprocess.run(
                    "docker-compose ps --services",
                    cwd=selected_project_path, shell=True, capture_output=True, text=True
                )
                services = result.stdout.strip().split('\n')
                if services and services[0]:
                    selected_service_logs = st.selectbox("Select a service to view logs", services)
                    if st.button(f"📜 Show Logs for {selected_service_logs}"):
                        run_compose_command(selected_project_path, f"logs --tail=100 {selected_service_logs}")
                else:
                    st.info("No running services found for this project.")
            except Exception as e:
                st.error(f"Could not list services: {e}")

        with tab3:
            st.subheader("Manage Services")
            try:
                result = subprocess.run(
                    "docker-compose ps",
                    cwd=selected_project_path, shell=True, capture_output=True, text=True
                )
                if result.stdout and "Exit" in result.stdout or "Up" in result.stdout:
                    lines = result.stdout.strip().split('\n')
                    data = [line.split() for line in lines[2:]] # Skip header
                    df = pd.DataFrame(data, columns=["Name", "Command", "State", "Ports"])
                    st.dataframe(df, use_container_width=True)
                else:
                    st.info("No services are currently running for this project.")
            except Exception as e:
                st.error(f"Could not retrieve service status: {e}")

    # --- End of Docker Compose Manager ---
# ---------------- Task Mapping ----------------
task_mapping = {
    "Python": {
        "Print Hello": python_hello_world,
        "Name Greeting": python_name_input,
        "🧠 Advanced RAM Reader": python_advanced_ram_reader,
        "🖼 Digital Image": python_digital_image,
        "📱 Send SMS (Twilio)": python_send_sms,
        "🔍 Google Search": python_Google_Search,
        "📧 Send Email": python_send_email,
        "🌐 Web Scraper": python_web_scraper,
        "📞 Make Call": python_make_call,
        "🧐 Gemini API Call": python_gemini_api,
        "😀QR Code Generator": python_qr_generator,
        "👌Pdf text extractor":python_pdf_to_text,
        "😊Image resizer":batch_image_resize,
        "📱 Instagram Post Creator": python_instagram_post_creator,
        "💼 LinkedIn Post Pro": python_linkedin_post_pro,
        "🐦 Twitter Post App": python_twitter_post_app,
        "📱 Facebook Post App": python_facebook_post_app,
        "📧 Email Bhejne Wala App": python_send_email_app,
        "😊Face Swap": python_face_swap
    },
    "Linux": {
        "Show Basic Commands": lambda: st.code("ls -l\npwd\ncd .."),
        "Linux Command Menu": linux_menu,
        "RedHat YUM Setup (with ISO)": linux_redhat_yum_setup,
        "Advanced Disk Info & SMART Data": linux_advanced_disk_info,
        "LVM Management & Guide": linux_lvm_manager,
        "NFS/Remote Filesystem Mount Tool": linux_nfs_mount_tool,
        "Disk Usage Analyzer (Largest Directories)": linux_disk_usage_analyzer,
        "Advanced Format & Mount Assistant": linux_advanced_format_mount,
        "Linux Networking Commands": linux_networking_commands
    },
    "Machine Learning": {
        "💼 EMI & Insurance Predictor": ml_emi_predictor,
        "📊 Student Performance Analyzer": ml_student_performance,
        "🔌 Smart Meter Bill Predictor": ml_smart_meter_app,
        "💼 Advanced Salary Predictor": ml_advanced_salary_predictor,
        "Log Prediction": lambda: st.success(f"Log prediction: {np.log(st.slider('Choose a value', 1, 100)):.2f}")
    },
    "JavaScript": {
        "Simple Calculator (Browser JS)": javascript_simple_calculator,
        "Moving Color Box Animation": javascript_moving_box,
        "Java script al in one task": javascript_nodejs_demo,
        "📄 Advanced Linux Article": javascript_advanced_linux_article,
        "🐳 Advanced Docker Article": javascript_advanced_docker_article,
        "☁️ Advanced AWS Article": javascript_advanced_aws_article,
        "🚀 Jenkins Mastery Article": javascript_jenkins_mastery_article
        },
    "Docker": {
        "🐳 Docker Project": docker_project,
        "🚀 Docker Compose Manager": docker_compose_manager
        },
    "Prompt Engineering": {
        "🚀 Gemini Prompt Optimizer": prompt_engineering_gemini_optimizer
    },
    "AWS": {
        "☁️ AWS Dashboard": docker_aws_ec2_manager,
        "🚀 Advanced Infra Manager": aws_advanced_infra_manager
    },
    "Projects": {
        "📂 File Management": advanced_file_manager,
        "🎶 Hand Gesture Music Maestro": project_hand_gesture_music,
        "✋ Hand Gesture Calculator": project_hand_calculator,
        "🎮 Game Controller": project_game_controller, 
        "🛠️ All-in-One Tool": project_all_in_one_tool,
        "🏠 Premium Rental Finder": project_premium_rental_finder,
        "🎧 Voice Analyzer AI": project_voice_analyzer_ai,
        "🤖 Roast Ya Toast AI": project_roast_ya_toast
    }
}

# ---------------- Streamlit UI ----------------

# Custom CSS for the new category cards
st.markdown("""
<style>
/* Style for the container that holds the cards */
[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
    border: 1px solid #2a2a6a;
    border-radius: 15px;
    padding: 1.2rem;
    background: #1c1c2e;
    transition: all 0.2s ease-in-out;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}

/* Hover effect for the cards */
[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"]:hover {
    transform: scale(1.04);
    border-color: #39C1E8;
    box-shadow: 0 8px 25px rgba(57, 192, 232, 0.3);
}

/* Center align all content inside the cards */
[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] [data-testid="stMarkdownContainer"] {
    text-align: center;
}

/* Style for the button inside the cards */
[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] .stButton button {
    background-color: #39C1E8;
    color: #1c1c2e;
    font-weight: bold;
    width: 100%;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

"""# --- New Sidebar Category+Task Menu ---

# 1. Main menu in sidebar (first/outer selectbox)
sidebar_categories = list(task_mapping.keys())
selected_category = st.sidebar.selectbox(
    "🧭 Select Main Area", sidebar_categories, key="sidebar_category"
)

# 2. Submenu in sidebar (second/inner selectbox)
selected_task = None
if selected_category:
    task_list = list(task_mapping[selected_category].keys())
    selected_task = st.sidebar.selectbox(
        "Select Subtask", task_list, key="sidebar_task"
    )

# Optionally separate with a styling line:
st.sidebar.markdown("---")


st.title("🛠️ Task Machine Pro Dashboard")
st.markdown("---")

if selected_category and selected_task:
    st.markdown(f"### {selected_category} » {selected_task}")
    task_mapping[selected_category][selected_task]()
else:
    st.info("👉 Left menu se pehle category aur task select karo.")




"""
st.markdown("### 🔍 Select a Category:")

# Define categories with icons
categories = {
    "Python": "🐍",
    "Linux": "💻",
    "Machine Learning": "🤖",
    "JavaScript": "🟨",
    "Docker": "🐳",
    "Prompt Engineering": "✍️",
    "Projects": "🚀",
    "AWS": "☁️"
}

# Create a 2x3 grid for the cards
row1_cols = st.columns(3)
row2_cols = st.columns(3)
row3_cols = st.columns(3)
all_cols = row1_cols + row2_cols + row3_cols

# Dynamically create a card in each column
# Dynamically create a card in each column
# Dynamically create a card in each column
for i, (category_name, icon) in enumerate(categories.items()):
    with all_cols[i]:
        with st.container():
            st.markdown(f"<h1 style='text-align: center; font-size: 3rem;'>{icon}</h1>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center;'>{category_name}</h3>", unsafe_allow_html=True)
            
            if st.button(f"Explore {category_name}", key=f"cat_{category_name}"):
                st.session_state.selected_category = category_name
                # Pre-select the first task of the new category to prevent errors
                st.session_state.task_selector = list(task_mapping[category_name].keys())[0]
                st.rerun()# Initialize session state if it doesn't exist
# Initialize session state variables if they don't exist
# Get the currently selected category
selected_category = st.session_state.get('selected_category')

# If a category is selected, display its tasks
if selected_category:
    st.markdown(f"## 🔧 {selected_category} Tasks")

    task_list = list(task_mapping[selected_category].keys())
    
    # This selectbox now uses a key to robustly remember its state
    selected_task = st.selectbox(
        "Choose a task to run:",
        task_list,
        key="task_selector"  # The key handles state automatically
    )
    
    st.write("---")
    
    # Execute the selected task
    if selected_task:
        task_mapping[selected_category][selected_task]()