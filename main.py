# Main application entry point
import streamlit as st
from core.app import initialize_app
from modules.linux.commands import linux_commands_menu, linux_network_tools
from modules.linux.advanced_commands import advanced_linux_commands_menu
from modules.python.communication import communication_menu
from modules.python.file_tools import file_tools_menu
from modules.python.web_tools import web_tools_menu
from modules.python.advanced_tools import advanced_python_tools_menu
from modules.machine_learning.calculators import machine_learning_menu
from modules.projects.utility_tools import utility_projects_menu
from modules.projects.hand_gesture_tools import hand_gesture_projects_menu
from modules.devops.docker_tools import docker_tools_menu
from modules.devops.aws_tools import aws_tools_menu
from modules.javascript.demos import javascript_demos_menu
import user

def main():
    """Main application function"""
    # Initialize the app
    initialize_app()
    
    # Get query parameters to handle navigation
    query_params = st.query_params
    category = query_params.get("category", ["dashboard"])[0]
    
    # Main content area based on query parameter or button click
    if st.session_state.get("category"):
        category = st.session_state.get("category")
    
    # JavaScript for handling button clicks
    st.markdown("""
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const navButtons = document.querySelectorAll('.nav-button');
        navButtons.forEach(button => {
            button.addEventListener('click', function() {
                const category = this.getAttribute('data-category');
                if (category) {
                    window.location.search = `?category=${category}`;
                }
            });
        });
    });
    </script>
    """, unsafe_allow_html=True)
    
    # Display content based on category
    if category == "linux":
        show_linux_tools()
    elif category == "python":
        show_python_utilities()
    elif category == "ml":
        show_machine_learning()
    elif category == "devops":
        show_devops_tools()
    elif category == "projects":
        show_projects()
    elif category == "javascript":
        show_javascript_demos()
    elif category == "user":
        user.user_page()
    else:
        # Default to dashboard
        show_dashboard()

def show_dashboard():
    """Show the main dashboard"""
    # Header with project and developer information
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: #ffffff; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(106, 13, 173, 0.2);">
        <h2 style="color: #6a0dad; font-size: 1.8rem; margin-bottom: 20px;">Menu Based Project</h2>
        <p style="color: #000000; font-size: 1.3rem; margin-bottom: 5px;">Made by <span style="color: #6a0dad; font-weight: bold;">Aryan Saini</span></p>
        <p style="color: #000000; font-size: 1.1rem; margin-bottom: 20px;">Summer Internship Project</p>
        <p style="color: #000000; font-size: 1.1rem; margin-bottom: 25px;">Under Guidance of <span style="color: #6a0dad; font-weight: bold;">Mr. Vimal Daga Sir</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Social media links
    st.markdown("""
    <div style="display: flex; justify-content: center; gap: 20px; margin-top: 15px; margin-bottom: 30px;">
        <a href="https://www.linkedin.com/in/aryan-saini067?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank" style="text-decoration: none;">
            <div style="background-color: #6a0dad; color: white; padding: 8px 15px; border-radius: 8px; display: flex; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 5px 15px rgba(106,13,173,0.3)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 2px 5px rgba(0,0,0,0.1)'">
                <span style="font-size: 20px; margin-right: 8px;">📱</span> LinkedIn
            </div>
        </a>
        <a href="https://github.com/androaryaani" target="_blank" style="text-decoration: none;">
            <div style="background-color: #000000; color: white; padding: 8px 15px; border-radius: 8px; display: flex; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 5px 15px rgba(0,0,0,0.3)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 2px 5px rgba(0,0,0,0.1)'">
                <span style="font-size: 20px; margin-right: 8px;">💻</span> GitHub
            </div>
        </a>
        <a href="https://verdant-jelly-904ae2.netlify.app/" target="_blank" style="text-decoration: none;">
            <div style="background-color: #6a0dad; color: white; padding: 8px 15px; border-radius: 8px; display: flex; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 5px 15px rgba(106,13,173,0.3)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 2px 5px rgba(0,0,0,0.1)'">
                <span style="font-size: 20px; margin-right: 8px;">🌐</span> Portfolio
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Project overview
    st.markdown("""
    <div style="background-color: #ffffff; padding: 25px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 4px 24px rgba(106, 13, 173, 0.2);">
        <h3 style="color: #6a0dad; margin-bottom: 15px; text-align: center; font-weight: 600;">Project Overview</h3>
        <p style="color: #000000; font-size: 1.1rem; line-height: 1.6; text-align: center;">
            This project is a comprehensive menu-based application that provides tools and utilities for Linux, Python, Machine Learning, DevOps, and JavaScript development. It serves as a one-stop solution for developers looking to access various tools and resources in these domains.
        </p>
        <p style="color: #000000; font-size: 1.1rem; line-height: 1.6; text-align: center; margin-top: 10px;">
            The application is built using Streamlit, a powerful Python library for creating web applications with minimal effort. The modular design allows for easy navigation between different sections and tools.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key features in cards with hover effect
    st.markdown("""
    <style>
    .feature-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        width: 280px;
        box-shadow: 0 4px 24px rgba(106, 13, 173, 0.2);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 30px rgba(106, 13, 173, 0.3);
        background-color: #f9f9f9;
    }
    
    .feature-icon {
        font-size: 2.2rem;
        color: #6a0dad;
        margin-bottom: 15px;
        text-align: center;
    }
    
    .feature-title {
        color: #6a0dad;
        margin-bottom: 10px;
        text-align: center;
        font-weight: 600;
    }
    
    .feature-desc {
        color: #000000;
        font-size: 1rem;
        text-align: center;
    }
    </style>
    
    <h3 style="color: #6a0dad; margin-bottom: 20px; text-align: center; font-weight: 600;">Key Features</h3>
    
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-bottom: 30px;">
        <div class="feature-card">
            <div class="feature-icon">🐧</div>
            <h4 class="feature-title">Linux Tools</h4>
            <p class="feature-desc">Access common Linux commands and utilities with easy-to-use interfaces.</p>
        </div>
        
        <div class="feature-card">
            <div class="feature-icon">🐍</div>
            <h4 class="feature-title">Python Tools</h4>
            <p class="feature-desc">Python utilities, code generators, and debugging helpers all in one place.</p>
        </div>
        
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h4 class="feature-title">ML Tools</h4>
            <p class="feature-desc">Machine learning model builders, data visualization, and analysis tools.</p>
        </div>
    </div>
    
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-bottom: 30px;">
        <div class="feature-card">
            <div class="feature-icon">🐳</div>
            <h4 class="feature-title">DevOps Tools</h4>
            <p class="feature-desc">Docker, CI/CD, and infrastructure management utilities for DevOps professionals.</p>
        </div>
        
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h4 class="feature-title">Projects</h4>
            <p class="feature-desc">Sample projects and templates to kickstart your development journey.</p>
        </div>
        
        <div class="feature-card">
            <div class="feature-icon">🟨</div>
            <h4 class="feature-title">JavaScript Tools</h4>
            <p class="feature-desc">JavaScript utilities, frameworks, and web development resources.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # System stats footer
    st.markdown("""
    <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; margin-top: 30px; box-shadow: 0 4px 24px rgba(106, 13, 173, 0.2);">
        <h4 style="color: #6a0dad; margin-bottom: 15px; text-align: center; font-weight: 600;">System Stats</h4>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div style="text-align: center; padding: 10px;">
                <p style="color: #000000; font-size: 0.9rem; margin-bottom: 5px;">Server Uptime</p>
                <p style="color: #6a0dad; font-size: 1.2rem; font-weight: bold;">5 days</p>
            </div>
            <div style="text-align: center; padding: 10px;">
                <p style="color: #000000; font-size: 0.9rem; margin-bottom: 5px;">CPU Load</p>
                <p style="color: #6a0dad; font-size: 1.2rem; font-weight: bold;">0.67</p>
            </div>
            <div style="text-align: center; padding: 10px;">
                <p style="color: #000000; font-size: 0.9rem; margin-bottom: 5px;">RAM Usage</p>
                <p style="color: #6a0dad; font-size: 1.2rem; font-weight: bold;">3.2 GB / 8 GB</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_linux_tools():
    """Show Linux tools section"""
    st.title("🔧 Linux Tools")
    
    # All Linux tools are now integrated into linux_commands_menu()
    linux_commands_menu()

def show_python_utilities():
    """Show Python utilities section"""
    st.title("🐍 Python Utilities")
    
    python_tab1, python_tab2, python_tab3, python_tab4 = st.tabs(["Communication", "File Processing", "Web Tools", "Advanced Tools"])
    
    with python_tab1:
        communication_menu()
    
    with python_tab2:
        file_tools_menu()
    
    with python_tab3:
        web_tools_menu()
    
    with python_tab4:
        advanced_python_tools_menu()

def show_machine_learning():
    """Show Machine Learning section"""
    st.title("🤖 Machine Learning Tools")
    machine_learning_menu()

def show_devops_tools():
    """Show DevOps tools section"""
    st.title("🐳 DevOps Tools")
    
    devops_tab1, devops_tab2 = st.tabs(["🐳 Docker Tools", "☁️ AWS Tools"])
    
    with devops_tab1:
        docker_tools_menu()
    
    with devops_tab2:
        aws_tools_menu()

def show_projects():
    """Show Projects section"""
    st.title("🚀 Projects")
    
    project_tab1, project_tab2 = st.tabs(["🛠️ Utility Projects", "✋ Hand Gesture Projects"])
    
    with project_tab1:
        utility_projects_menu()
    
    with project_tab2:
        hand_gesture_projects_menu()

def show_javascript_demos():
    """Show JavaScript demos section"""
    st.title("🟨 JavaScript Demos")
    
    javascript_demos_menu()

if __name__ == "__main__":
    main()
