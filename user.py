# User page module
import streamlit as st
import os
import json
from datetime import datetime
from dotenv import load_dotenv, dotenv_values
import os.path

# Apply custom CSS for purple background and white text in selection lists
st.markdown("""
<style>
/* Style for selectbox */
div[data-baseweb="select"] > div {
    background-color: #6a0dad;
    color: white;
}

/* Style for dropdown items */
ul[data-baseweb="menu"] li {
    background-color: #6a0dad;
    color: white;
}

ul[data-baseweb="menu"] li:hover {
    background-color: #8a2be2;
    color: white;
}

/* Style for tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    background-color: #f0f0f0;
    border-radius: 4px 4px 0 0;
    padding: 8px 16px;
    border: none;
}

.stTabs [aria-selected="true"] {
    background-color: #6a0dad;
    color: white;
}

/* Style for buttons */
.stButton button {
    background-color: #6a0dad;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    transition: all 0.3s ease;
}

.stButton button:hover {
    background-color: #8a2be2;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Path to the .env file
ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')

# Path to store user history
HISTORY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'user_history.json')

# Ensure the data directory exists
os.makedirs(os.path.dirname(HISTORY_PATH), exist_ok=True)

# Initialize history file if it doesn't exist
if not os.path.exists(HISTORY_PATH):
    with open(HISTORY_PATH, 'w') as f:
        json.dump([], f)

def load_env_variables():
    """Load environment variables from .env file"""
    if os.path.exists(ENV_PATH):
        return dotenv_values(ENV_PATH)
    return {}

def save_env_variables(env_vars):
    """Save environment variables to .env file"""
    with open(ENV_PATH, 'w') as f:
        for key, value in env_vars.items():
            f.write(f"{key}={value}\n")

def add_to_history(category, action):
    """Add an action to the user history"""
    try:
        with open(HISTORY_PATH, 'r') as f:
            history = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        history = []
    
    history.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "category": category,
        "action": action
    })
    
    # Keep only the last 50 actions
    if len(history) > 50:
        history = history[-50:]
    
    with open(HISTORY_PATH, 'w') as f:
        json.dump(history, f, indent=4)

def load_history():
    """Load user history from file"""
    try:
        with open(HISTORY_PATH, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def show_user_dashboard():
    """Show the user dashboard"""
    # Header with project and developer information
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: #ffffff; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(106, 13, 173, 0.2);">
        <h2 style="color: #6a0dad; font-size: 1.8rem; margin-bottom: 20px;">User Dashboard</h2>
        <p style="color: #000000; font-size: 1.3rem; margin-bottom: 5px;">Welcome <span style="color: #6a0dad; font-weight: bold;">User</span></p>
        <p style="color: #000000; font-size: 1.1rem; margin-bottom: 20px;">Your personal dashboard</p>
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
    """, unsafe_allow_html=True)
    
    # Display feature cards in two rows
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card"> 
            <div class="feature-icon">🐍</div> 
            <h4 class="feature-title">Python Tools</h4> 
            <p class="feature-desc">Python utilities, code generators, and debugging helpers all in one place.</p> 
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="feature-card"> 
            <div class="feature-icon">🤖</div> 
            <h4 class="feature-title">ML Tools</h4> 
            <p class="feature-desc">Machine learning model builders, data visualization, and analysis tools.</p> 
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="feature-card"> 
            <div class="feature-icon">📊</div> 
            <h4 class="feature-title">Projects</h4> 
            <p class="feature-desc">Sample projects and templates to kickstart your development journey.</p> 
        </div>
        """, unsafe_allow_html=True)
    
    # Second row of feature cards
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown("""
        <div class="feature-card"> 
            <div class="feature-icon">🐧</div> 
            <h4 class="feature-title">Linux Tools</h4> 
            <p class="feature-desc">Access common Linux commands and utilities with easy-to-use interfaces.</p> 
        </div>
        """, unsafe_allow_html=True)
        
    with col5:
        st.markdown("""
        <div class="feature-card"> 
            <div class="feature-icon">🐳</div> 
            <h4 class="feature-title">DevOps Tools</h4> 
            <p class="feature-desc">Docker, CI/CD, and infrastructure management utilities for DevOps professionals.</p> 
        </div>
        """, unsafe_allow_html=True)
        
    with col6:
        st.markdown("""
        <div class="feature-card"> 
            <div class="feature-icon">🟨</div> 
            <h4 class="feature-title">JavaScript Tools</h4> 
            <p class="feature-desc">JavaScript utilities, frameworks, and web development resources.</p> 
        </div>
        """, unsafe_allow_html=True)
    
    # User stats
    st.markdown("""
    <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; margin-top: 30px; box-shadow: 0 4px 24px rgba(106, 13, 173, 0.2);">
        <h4 style="color: #6a0dad; margin-bottom: 15px; text-align: center; font-weight: 600;">User Stats</h4>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div style="text-align: center; padding: 10px;">
                <p style="color: #000000; font-size: 0.9rem; margin-bottom: 5px;">Projects</p>
                <p style="color: #6a0dad; font-size: 1.2rem; font-weight: bold;">5</p>
            </div>
            <div style="text-align: center; padding: 10px;">
                <p style="color: #000000; font-size: 0.9rem; margin-bottom: 5px;">Tools Used</p>
                <p style="color: #6a0dad; font-size: 1.2rem; font-weight: bold;">12</p>
            </div>
            <div style="text-align: center; padding: 10px;">
                <p style="color: #000000; font-size: 0.9rem; margin-bottom: 5px;">Last Login</p>
                <p style="color: #6a0dad; font-size: 1.2rem; font-weight: bold;">Today</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_settings():
    """Show settings page with credentials management"""
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: #ffffff; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(106, 13, 173, 0.2);">
        <h2 style="color: #6a0dad; font-size: 1.8rem; margin-bottom: 20px;">Settings</h2>
        <p style="color: #000000; font-size: 1.1rem; margin-bottom: 20px;">Manage your credentials and application settings</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load current environment variables
    env_vars = load_env_variables()
    
    # Group credentials by service
    email_creds = {k: v for k, v in env_vars.items() if 'EMAIL' in k or 'GMAIL' in k}
    twilio_creds = {k: v for k, v in env_vars.items() if 'TWILIO' in k or 'WHATSAPP' in k}
    social_creds = {k: v for k, v in env_vars.items() if any(x in k for x in ['INSTAGRAM', 'LINKEDIN', 'CONSUMER', 'ACCESS_TOKEN', 'FB_'])}
    api_creds = {k: v for k, v in env_vars.items() if 'API' in k or 'KEY' in k}
    ssh_creds = {k: v for k, v in env_vars.items() if 'SSH' in k}
    other_creds = {k: v for k, v in env_vars.items() if k not in email_creds and k not in twilio_creds and k not in social_creds and k not in api_creds and k not in ssh_creds}
    
    # Create tabs for different credential groups
    tabs = st.tabs(["📧 Email", "📱 Twilio & WhatsApp", "🌐 Social Media", "🔑 API Keys", "🖥️ SSH", "⚙️ Other"])
    
    # Function to create credential input fields
    def create_credential_inputs(creds, tab):
        updated_creds = {}
        with tab:
            for key, value in creds.items():
                # Create a more user-friendly label
                label = key.replace('_', ' ').title()
                # Determine if this is a password/token field
                is_sensitive = any(x in key.lower() for x in ['password', 'token', 'secret', 'key', 'sid'])
                
                if is_sensitive:
                    updated_value = st.text_input(label, value, type="password", key=f"{tab._name}_{key}_sensitive")
                else:
                    updated_value = st.text_input(label, value, key=f"{tab._name}_{key}")
                
                updated_creds[key] = updated_value
            
            # Add button to save changes
            if st.button("Save Changes", key=f"save_{tab._name}"):
                # Update the original env_vars with the new values
                for key, value in updated_creds.items():
                    env_vars[key] = value
                
                # Save the updated environment variables
                save_env_variables(env_vars)
                st.success("Settings saved successfully!")
                add_to_history("Settings", f"Updated {tab._name} credentials")
    
    # Fill each tab with the corresponding credentials
    create_credential_inputs(email_creds, tabs[0])
    create_credential_inputs(twilio_creds, tabs[1])
    create_credential_inputs(social_creds, tabs[2])
    create_credential_inputs(api_creds, tabs[3])
    create_credential_inputs(ssh_creds, tabs[4])
    create_credential_inputs(other_creds, tabs[5])

def show_history():
    """Show user history page"""
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: #ffffff; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(106, 13, 173, 0.2);">
        <h2 style="color: #6a0dad; font-size: 1.8rem; margin-bottom: 20px;">Activity History</h2>
        <p style="color: #000000; font-size: 1.1rem; margin-bottom: 20px;">Your recent activities and actions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load user history
    history = load_history()
    
    if not history:
        st.info("No activity history found.")
        return
    
    # Display history in a table with custom styling
    st.markdown("""
    <style>
    .history-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
    }
    .history-table th {
        background-color: #6a0dad;
        color: white;
        padding: 12px;
        text-align: left;
    }
    .history-table td {
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }
    .history-table tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    .history-table tr:hover {
        background-color: #f1f1f1;
    }
    </style>
    
    <table class="history-table">
        <tr>
            <th>Timestamp</th>
            <th>Category</th>
            <th>Action</th>
        </tr>
    """, unsafe_allow_html=True)
    
    # Add each history item to the table
    for item in reversed(history):  # Show newest first
        st.markdown(f"""
        <tr>
            <td>{item['timestamp']}</td>
            <td>{item['category']}</td>
            <td>{item['action']}</td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown("</table>", unsafe_allow_html=True)
    
    # Add button to clear history
    if st.button("Clear History"):
        with open(HISTORY_PATH, 'w') as f:
            json.dump([], f)
        st.success("History cleared successfully!")
        st.experimental_rerun()

def user_page():
    """Main user page function"""
    st.title("👤 User Page")
    
    # Create tabs for dashboard, settings, and history
    tabs = st.tabs(["📊 Dashboard", "⚙️ Settings", "📜 History"])
    
    # Display content based on selected tab
    with tabs[0]:
        show_user_dashboard()
    
    with tabs[1]:
        show_settings()
    
    with tabs[2]:
        show_history()
        
    # Add history entry for page visit
    add_to_history("Navigation", "Visited User Page")