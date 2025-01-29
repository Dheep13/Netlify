import streamlit as st
import pandas as pd
import os
from datetime import datetime
import streamlit.components.v1 as components
from dotenv import load_dotenv
from encoded_profile import PROFILE_IMAGE
import base64
from utils.db import init_db, increment_download_count, get_total_downloads

# Initialize database
init_db()

# Page configuration
st.set_page_config(
    page_title="Deepan Shanmugam | Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS with modern design
st.markdown("""
<style>
    /* Modern color scheme */
    :root {
        --primary-color: #2563eb;
        --secondary-color: #1d4ed8;
        --accent-color: #dbeafe;
        --text-color: #1f2937;
        --bg-color: #ffffff;
    }
    
    /* Global styles */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Header and text styles */
    h1, h2, h3 {
        color: var(--text-color);
        font-family: 'Inter', sans-serif;
    }
    
    /* Profile section */
    .profile-container {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .profile-image {
        border-radius: 50%;
        border: 4px solid white;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .profile-image:hover {
        transform: scale(1.05);
    }
    
    /* Card styles */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        border: 1px solid #e5e7eb;
        transition: transform 0.2s ease;
    }
    
    .card:hover {
        transform: translateY(-2px);
    }
    
    /* Skill tags */
    .skill-tag {
        display: inline-block;
        background: var(--accent-color);
        color: var(--primary-color);
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        margin: 0.25rem;
        font-size: 0.875rem;
        transition: all 0.2s ease;
    }
    
    .skill-tag:hover {
        background: var(--primary-color);
        color: white;
    }
    
    /* Timeline styles */
    .timeline-item {
        border-left: 2px solid var(--primary-color);
        padding-left: 1.5rem;
        margin-bottom: 1.5rem;
        position: relative;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -0.5rem;
        top: 0;
        width: 1rem;
        height: 1rem;
        background: var(--primary-color);
        border-radius: 50%;
    }
    
    /* Button styles */
    .custom-button {
        background-color: var(--primary-color);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        text-decoration: none;
        transition: background-color 0.2s ease;
        display: inline-block;
        margin: 0.5rem;
    }
    
    .custom-button:hover {
        background-color: var(--secondary-color);
    }
    
    /* Video container */
    .video-container {
        background: white;
        border-radius: 0.75rem;
        overflow: hidden;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* Blog card */
    .blog-card {
        background: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
        border: 1px solid #e5e7eb;
        transition: all 0.2s ease;
    }
    
    .blog-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="data:image/jpeg;base64,{PROFILE_IMAGE}" 
                 class="profile-image"
                 style="width:250px; height:250px; object-fit:cover;" />
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="profile-container">
            <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">Deepan Shanmugam</h1>
            <h3 style="color: #4b5563; margin-bottom: 1rem;">SAP 4X Certified | Lead Consultant @ MuniCons GmbH</h3>
            <p style="font-size: 1.1rem; color: #4b5563;">
                📍 Chennai, India<br>
                📧 deepanshanmugam13@gmail.com<br>
                📱 +91 9003055370
            </p>
            <div style="display: flex; gap: 1rem; margin-top: 1rem;">
                <a href="https://www.linkedin.com/in/deepanshanmugam/" target="_blank" class="custom-button">
                    LinkedIn
                </a>
                <a href="https://github.com/Dheep13/KaggleContest/tree/main/assignments" target="_blank" class="custom-button">
                    GitHub
                </a>
                <a href="data:application/pdf;base64,{get_cv_base64()}" 
                   download="CV_Deepan_Shanmugam.pdf" 
                   class="custom-button">
                    Download CV
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Profile Summary
st.markdown("""
<div class="card" style="margin-top: 2rem;">
    <h2>🚀 Profile Summary</h2>
    <p style="font-size: 1.1rem; line-height: 1.6;">
        Data Integration expert with 14 years of experience specializing in SAP's Sales Performance Management ecosystem 
        and enterprise-scale data operations. Proven track record in strategizing and implementing complex data integration 
        solutions, with expertise in ETL processes and cloud services. Passionate about leveraging AI/ML to transform 
        traditional data workflows - from optimizing SPM systems and automating complex processes to building intelligent 
        integrations.
    </p>
</div>
""", unsafe_allow_html=True)

# Skills Section with modern design
st.markdown("<h2 style='margin-top: 2rem;'>💻 Technical Expertise</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3 style="color: var(--primary-color);">SAP Ecosystem</h3>
        <div style="margin-top: 1rem;">
    """, unsafe_allow_html=True)
    
    for skill in ["SAP Commissions", "SAP Integration Suite", "SAP HANA", "SAP Datasphere", 
                 "SAP BTP", "SAP Build Apps", "SAP Automation Pilot", "SAP XDL"]:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3 style="color: var(--primary-color);">Data & AI</h3>
        <div style="margin-top: 1rem;">
    """, unsafe_allow_html=True)
    
    for skill in ["Python", "Machine Learning", "Computer Vision", "PyTorch", 
                 "Generative AI", "REST APIs", "Git"]:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3 style="color: var(--primary-color);">Programming & DB</h3>
        <div style="margin-top: 1rem;">
    """, unsafe_allow_html=True)
    
    for skill in ["HANA SQL Script", "Oracle PL/SQL", "SQL Server", 
                 "Shell scripting", "Knockout JS"]:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

# Experience Timeline
st.markdown("<h2 style='margin-top: 3rem;'>💼 Professional Journey</h2>", unsafe_allow_html=True)

experiences = [
    {
        "company": "MuniCons GmbH",
        "role": "Lead Consultant",
        "duration": "2024-Present",
        "location": "Chennai",
        "description": "Leading SAP Commissions implementations and integrations"
    },
    {
        "company": "SAP India",
        "role": "Senior Business Process Consultant",
        "duration": "2019-2024",
        "location": "Hyderabad",
        "description": "Spearheaded multiple SPM implementations across APAC"
    },
    # Add other experiences...
]

for exp in experiences:
    st.markdown(f"""
    <div class="timeline-item">
        <h3>{exp['company']}</h3>
        <p style="color: var(--primary-color); margin: 0.5rem 0;">{exp['role']}</p>
        <p style="color: #6b7280; margin-bottom: 0.5rem;">
            📅 {exp['duration']} | 📍 {exp['location']}
        </p>
        <p>{exp['description']}</p>
    </div>
    """, unsafe_allow_html=True)

# Projects Section
st.markdown("<h2 style='margin-top: 3rem;'>🎯 Key Projects</h2>", unsafe_allow_html=True)

with st.expander("View Major Projects"):
    col1, col2 = st.columns(2)
    
    projects = [
        "Telefonica Germany", "AIA Singapore", "Prudential Malaysia",
        "HSBC", "AIG Japan", "Kaiser Permanente"
    ]
    
    half = len(projects) // 2
    
    with col1:
        for project in projects[:half]:
            st.markdown(f"""
            <div class="card">
                <h4>{project}</h4>
                <p style="color: #6b7280;">SAP Commissions Implementation</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        for project in projects[half:]:
            st.markdown(f"""
            <div class="card">
                <h4>{project}</h4>
                <p style="color: #6b7280;">SAP Commissions Implementation</p>
            </div>
            """, unsafe_allow_html=True)

# Add the rest of your sections (Blogs, Videos, etc.) with similar styling...

# Chat Interface with modern design
st.markdown("<h2 style='margin-top: 3rem;'>💬 Ask AI Assistant</h2>", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat container
st.markdown("""
<div style="background: white; padding: 1.5rem; border-radius: 0.75rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
""", unsafe_allow_html=True)

# Rest of your chat implementation...

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: white; border-radius: 0.75rem;">
    <p style="color: #6b7280;">Built with ❤️ using Streamlit</p>
    <p style="color: #6b7280;">© 2024 Deepan Shanmugam. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)