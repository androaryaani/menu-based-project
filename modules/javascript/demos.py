# JavaScript demos module
import streamlit as st
import streamlit.components.v1 as components

def javascript_nodejs_demo():
    """JavaScript Task: Custom HTML + JS Integration"""
    st.markdown("<h3 style='color: #6a0dad; text-align: center; margin-bottom: 20px; font-weight: 600;'>🟨 JavaScript & Node.js Integration</h3>", unsafe_allow_html=True)
    
    # Display a card with information instead of showing the code
    st.markdown("""
    <div style="background-color: #ffffff; padding: 25px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 4px 24px rgba(106, 13, 173, 0.2);">
        <h4 style="color: #6a0dad; margin-bottom: 15px; text-align: center; font-weight: 600;">TaskMaster Pro Web Application</h4>
        <p style="color: #000000; font-size: 1.1rem; line-height: 1.6; text-align: center;">
            This interactive web application demonstrates the integration of HTML, CSS, and JavaScript to create a modern user interface.
        </p>
        <p style="color: #000000; font-size: 1.1rem; line-height: 1.6; text-align: center; margin-top: 10px;">
            Features include animated UI elements, responsive design, and interactive components.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hidden HTML code that will be rendered but not shown in the UI
    html_code = r"""
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
                overflow-y: auto;
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
            
            .task-card h3 {
                color: var(--accent);
                margin-bottom: 15px;
                font-size: 1.4rem;
            }
            
            .task-card p {
                color: var(--light);
                margin-bottom: 20px;
                line-height: 1.6;
                flex-grow: 1;
            }
            
            .task-card .btn {
                background: linear-gradient(45deg, var(--primary), var(--accent));
                color: white;
                padding: 12px 24px;
                border: none;
                border-radius: 25px;
                cursor: pointer;
                font-weight: 600;
                transition: var(--transition);
                text-decoration: none;
                text-align: center;
                display: inline-block;
            }
            
            .task-card .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            }
            
            .task-card .icon {
                font-size: 2.5rem;
                margin-bottom: 15px;
                color: var(--success);
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            @keyframes slideIn {
                from { opacity: 0; transform: translateX(-30px); }
                to { opacity: 1; transform: translateX(0); }
            }
            
            .task-card:nth-child(1) { animation: slideIn 0.6s ease 0.1s both; }
            .task-card:nth-child(2) { animation: slideIn 0.6s ease 0.2s both; }
            .task-card:nth-child(3) { animation: slideIn 0.6s ease 0.3s both; }
            .task-card:nth-child(4) { animation: slideIn 0.6s ease 0.4s both; }
            .task-card:nth-child(5) { animation: slideIn 0.6s ease 0.5s both; }
            .task-card:nth-child(6) { animation: slideIn 0.6s ease 0.6s both; }
            
            .floating-shapes {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: -1;
            }
            
            .shape {
                position: absolute;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 50%;
                animation: float 6s ease-in-out infinite;
            }
            
            .shape:nth-child(1) {
                width: 80px;
                height: 80px;
                top: 20%;
                left: 10%;
                animation-delay: 0s;
            }
            
            .shape:nth-child(2) {
                width: 120px;
                height: 120px;
                top: 60%;
                right: 10%;
                animation-delay: 2s;
            }
            
            .shape:nth-child(3) {
                width: 60px;
                height: 60px;
                bottom: 20%;
                left: 20%;
                animation-delay: 4s;
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(-20px) rotate(180deg); }
            }
            
            .responsive-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            
            @media (max-width: 768px) {
                header h1 { font-size: 2rem; }
                .app-container { grid-template-columns: 1fr; }
                .responsive-grid { grid-template-columns: 1fr; }
            }
        </style>
    </head>
    <body>
        <div class="floating-shapes">
            <div class="shape"></div>
            <div class="shape"></div>
            <div class="shape"></div>
        </div>
        
        <div class="container">
            <header>
                <h1>
                    <i class="fas fa-tasks"></i>
                    TaskMaster Pro
                </h1>
                <p>Your all-in-one utility application for productivity and organization</p>
            </header>
            
            <div class="app-container">
                <div class="task-card">
                    <div class="icon">
                        <i class="fas fa-calendar-check"></i>
                    </div>
                    <h3>Task Management</h3>
                    <p>Organize your daily tasks, set priorities, and track progress with our intuitive task management system.</p>
                    <button class="btn" onclick="openTaskManager()">Get Started</button>
                </div>
                
                <div class="task-card">
                    <div class="icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <h3>Analytics Dashboard</h3>
                    <p>Visualize your productivity data with interactive charts and real-time insights to optimize your workflow.</p>
                    <button class="btn" onclick="openAnalytics()">View Analytics</button>
                </div>
                
                <div class="task-card">
                    <div class="icon">
                        <i class="fas fa-users"></i>
                    </div>
                    <h3>Team Collaboration</h3>
                    <p>Work seamlessly with your team through shared workspaces, real-time updates, and integrated communication tools.</p>
                    <button class="btn" onclick="openTeamCollab()">Join Team</button>
                </div>
                
                <div class="task-card">
                    <div class="icon">
                        <i class="fas fa-mobile-alt"></i>
                    </div>
                    <h3>Mobile App</h3>
                    <p>Access your tasks and projects on the go with our responsive mobile application available on all platforms.</p>
                    <button class="btn" onclick="downloadMobileApp()">Download App</button>
                </div>
                
                <div class="task-card">
                    <div class="icon">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <h3>Security & Privacy</h3>
                    <p>Your data is protected with enterprise-grade security, encryption, and compliance with industry standards.</p>
                    <button class="btn" onclick="showSecurityInfo()">Learn More</button>
                </div>
                
                <div class="task-card">
                    <div class="icon">
                        <i class="fas fa-cog"></i>
                    </div>
                    <h3>Customization</h3>
                    <p>Personalize your experience with customizable themes, layouts, and workflow preferences to match your style.</p>
                    <button class="btn" onclick="openCustomization()">Customize</button>
                </div>
            </div>
            
            <div class="responsive-grid">
                <div class="task-card">
                    <h3>Quick Actions</h3>
                    <p>Access frequently used features and shortcuts for maximum efficiency in your daily workflow.</p>
                    <button class="btn" onclick="showQuickActions()">Show Actions</button>
                </div>
                
                <div class="task-card">
                    <h3>Recent Projects</h3>
                    <p>Quick access to your recent projects and ongoing work for seamless continuation.</p>
                    <button class="btn" onclick="showRecentProjects()">View Projects</button>
                </div>
            </div>
        </div>
        
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
        <script src="https://unpkg.com/html5-qrcode/html5-qrcode.min.js"></script>
        
        <script>
            // Interactive functionality
            function showQuickActions() {
                const actions = ['Create Task', 'Start Timer', 'Send Report', 'Schedule Meeting'];
                const actionList = actions.map(action => `<li>${action}</li>`).join('');
                showModal('Quick Actions', `<ul style="list-style: none; padding: 0;">${actionList}</ul>`);
            }
            
            function showRecentProjects() {
                const projects = [
                    {name: 'Website Redesign', status: 'In Progress', progress: '75%'},
                    {name: 'Mobile App', status: 'Planning', progress: '25%'},
                    {name: 'Marketing Campaign', status: 'Completed', progress: '100%'},
                    {name: 'Data Analysis', status: 'In Progress', progress: '60%'}
                ];
                const projectList = projects.map(project => 
                    `<div style="margin: 10px 0; padding: 10px; background: rgba(255,255,255,0.1); border-radius: 8px;">
                        <strong>${project.name}</strong><br>
                        <small>Status: ${project.status} | Progress: ${project.progress}</small>
                    </div>`
                ).join('');
                showModal('Recent Projects', projectList);
            }
            
            function openTaskManager() {
                showModal('Task Manager', `
                    <div style="text-align: center;">
                        <h4>📋 Task Management System</h4>
                        <p>Create, organize, and track your tasks efficiently</p>
                        <div style="margin: 20px 0;">
                            <input type="text" id="newTask" placeholder="Enter new task..." style="padding: 8px; border-radius: 4px; border: none; width: 200px;">
                            <button onclick="addTask()" style="margin-left: 10px; padding: 8px 16px; background: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">Add Task</button>
                        </div>
                        <div id="taskList" style="text-align: left; max-height: 200px; overflow-y: auto;">
                            <div style="padding: 8px; margin: 5px 0; background: rgba(255,255,255,0.1); border-radius: 4px;">✅ Complete project documentation</div>
                            <div style="padding: 8px; margin: 5px 0; background: rgba(255,255,255,0.1); border-radius: 4px;">⏳ Review code changes</div>
                            <div style="padding: 8px; margin: 5px 0; background: rgba(255,255,255,0.1); border-radius: 4px;">📅 Schedule team meeting</div>
                        </div>
                    </div>
                `);
            }
            
            function openAnalytics() {
                showModal('Analytics Dashboard', `
                    <div style="text-align: center;">
                        <h4>📊 Analytics Overview</h4>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0;">
                            <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px;">
                                <h5>Tasks Completed</h5>
                                <div style="font-size: 2em; color: #4CAF50;">24</div>
                            </div>
                            <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px;">
                                <h5>Productivity Score</h5>
                                <div style="font-size: 2em; color: #2196F3;">87%</div>
                            </div>
                        </div>
                        <p>Your productivity has increased by 15% this week!</p>
                    </div>
                `);
            }
            
            function openTeamCollab() {
                showModal('Team Collaboration', `
                    <div style="text-align: center;">
                        <h4>👥 Team Workspace</h4>
                        <p>Join your team's collaborative workspace</p>
                        <div style="margin: 20px 0;">
                            <input type="text" placeholder="Enter team code..." style="padding: 8px; border-radius: 4px; border: none; width: 200px;">
                            <button style="margin-left: 10px; padding: 8px 16px; background: #2196F3; color: white; border: none; border-radius: 4px; cursor: pointer;">Join Team</button>
                        </div>
                        <p>Or create a new team workspace</p>
                        <button style="padding: 8px 16px; background: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">Create Team</button>
                    </div>
                `);
            }
            
            function downloadMobileApp() {
                showModal('Mobile App', `
                    <div style="text-align: center;">
                        <h4>📱 Mobile App Download</h4>
                        <p>Get TaskMaster Pro on your mobile device</p>
                        <div style="margin: 20px 0;">
                            <button style="margin: 5px; padding: 12px 20px; background: #000; color: white; border: none; border-radius: 8px; cursor: pointer;">
                                <i class="fab fa-apple"></i> App Store
                            </button>
                            <button style="margin: 5px; padding: 12px 20px; background: #3DDC84; color: white; border: none; border-radius: 8px; cursor: pointer;">
                                <i class="fab fa-google-play"></i> Google Play
                            </button>
                        </div>
                        <p>Scan QR code to download</p>
                        <div style="width: 100px; height: 100px; background: #333; margin: 20px auto; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white;">
                            QR Code
                        </div>
                    </div>
                `);
            }
            
            function showSecurityInfo() {
                showModal('Security & Privacy', `
                    <div style="text-align: center;">
                        <h4>🛡️ Security Features</h4>
                        <div style="text-align: left; margin: 20px 0;">
                            <div style="margin: 10px 0; padding: 10px; background: rgba(255,255,255,0.1); border-radius: 8px;">
                                <strong>🔐 End-to-End Encryption</strong><br>
                                <small>All data is encrypted in transit and at rest</small>
                            </div>
                            <div style="margin: 10px 0; padding: 10px; background: rgba(255,255,255,0.1); border-radius: 8px;">
                                <strong>🔒 Two-Factor Authentication</strong><br>
                                <small>Enhanced security with 2FA support</small>
                            </div>
                            <div style="margin: 10px 0; padding: 10px; background: rgba(255,255,255,0.1); border-radius: 8px;">
                                <strong>📋 GDPR Compliance</strong><br>
                                <small>Full compliance with data protection regulations</small>
                            </div>
                        </div>
                    </div>
                `);
            }
            
            function openCustomization() {
                showModal('Customization', `
                    <div style="text-align: center;">
                        <h4>🎨 Customize Your Experience</h4>
                        <p>Personalize TaskMaster Pro to match your style</p>
                        <div style="margin: 20px 0;">
                            <label style="display: block; margin: 10px 0;">Theme:</label>
                            <select id="themeSelect" style="padding: 8px; border-radius: 4px; border: none; width: 200px;">
                                <option value="default">Default Theme</option>
                                <option value="dark">Dark Mode</option>
                                <option value="light">Light Mode</option>
                                <option value="colorful">Colorful</option>
                            </select>
                        </div>
                        <div style="margin: 20px 0;">
                            <label style="display: block; margin: 10px 0;">Layout:</label>
                            <select id="layoutSelect" style="padding: 8px; border-radius: 4px; border: none; width: 200px;">
                                <option value="grid">Grid Layout</option>
                                <option value="list">List Layout</option>
                                <option value="compact">Compact Layout</option>
                            </select>
                        </div>
                        <button onclick="applyCustomization()" style="padding: 8px 16px; background: #9C27B0; color: white; border: none; border-radius: 4px; cursor: pointer;">Apply Changes</button>
                    </div>
                `);
            }
            
            function showModal(title, content) {
                // Remove existing modal if any
                const existingModal = document.getElementById('taskModal');
                if (existingModal) {
                    existingModal.remove();
                }
                
                const modal = document.createElement('div');
                modal.id = 'taskModal';
                modal.style.cssText = `
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0,0,0,0.8);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    z-index: 1000;
                    backdrop-filter: blur(5px);
                `;
                
                const modalContent = document.createElement('div');
                modalContent.style.cssText = `
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 15px;
                    max-width: 500px;
                    width: 90%;
                    max-height: 80vh;
                    overflow-y: auto;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
                    border: 1px solid rgba(255,255,255,0.2);
                `;
                
                modalContent.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                        <h3 style="margin: 0;">${title}</h3>
                        <button onclick="this.closest('#taskModal').remove()" style="background: none; border: none; color: white; font-size: 24px; cursor: pointer; padding: 0;">&times;</button>
                    </div>
                    ${content}
                `;
                
                modal.appendChild(modalContent);
                document.body.appendChild(modal);
                
                // Close modal on outside click
                modal.addEventListener('click', function(e) {
                    if (e.target === modal) {
                        modal.remove();
                    }
                });
            }
            
            function addTask() {
                const input = document.getElementById('newTask');
                const taskList = document.getElementById('taskList');
                if (input.value.trim()) {
                    const taskDiv = document.createElement('div');
                    taskDiv.style.cssText = 'padding: 8px; margin: 5px 0; background: rgba(255,255,255,0.1); border-radius: 4px;';
                    taskDiv.innerHTML = `⏳ ${input.value}`;
                    taskList.appendChild(taskDiv);
                    input.value = '';
                }
            }
            
            function applyCustomization() {
                const theme = document.getElementById('themeSelect').value;
                const layout = document.getElementById('layoutSelect').value;
                showModal('Customization Applied', `
                    <div style="text-align: center;">
                        <h4>✅ Changes Applied!</h4>
                        <p>Theme: ${theme}</p>
                        <p>Layout: ${layout}</p>
                        <p>Your preferences have been saved.</p>
                    </div>
                `);
                setTimeout(() => {
                    const modal = document.getElementById('taskModal');
                    if (modal) modal.remove();
                }, 2000);
            }
            
            // Add smooth scrolling
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
            
            // Add hover effects
            document.querySelectorAll('.task-card').forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-10px) scale(1.02)';
                });
                
                card.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0) scale(1)';
                });
            });
            
            // Add click tracking
            document.querySelectorAll('.btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    console.log('Button clicked:', this.textContent);
                    // Here you could add analytics tracking
                });
            });
            
            // Add keyboard navigation
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Tab') {
                    // Handle tab navigation
                    console.log('Tab navigation active');
                }
            });
            
            // Add responsive behavior
            function handleResize() {
                const cards = document.querySelectorAll('.task-card');
                if (window.innerWidth < 768) {
                    cards.forEach(card => {
                        card.style.marginBottom = '20px';
                    });
                } else {
                    cards.forEach(card => {
                        card.style.marginBottom = '0';
                    });
                }
            }
            
            window.addEventListener('resize', handleResize);
            handleResize(); // Initial call
            
            // Add loading animation
            window.addEventListener('load', function() {
                document.body.style.opacity = '0';
                document.body.style.transition = 'opacity 0.5s ease';
                setTimeout(() => {
                    document.body.style.opacity = '1';
                }, 100);
            });
            
            // Add intersection observer for animations
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, observerOptions);
            
            // Observe all task cards
            document.querySelectorAll('.task-card').forEach(card => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(30px)';
                card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                observer.observe(card);
            });
        </script>
    </body>
    </html>
    """
    
    components.html(html_code, height=800)

def javascript_simple_calculator():
    """JavaScript - Simple Calculator (Browser)"""
    st.subheader("🟨 JavaScript - Simple Calculator (Browser)")
    
    html_code = r"""
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
    """JavaScript - Moving Color Box"""
    st.subheader("🟨 JavaScript - Moving Color Box")
    
    html_code = r"""
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

def javascript_demos_menu():
    """Main JavaScript demos menu"""
    st.title("🟨 JavaScript Demos")
    
    st.markdown("---")
    
    st.subheader("🔰 Basic JavaScript Demos")
    demo1, demo2, demo3 = st.tabs(["TaskMaster Pro", "Scientific Calculator", "Moving Box"])
    
    with demo1:
        javascript_nodejs_demo()
    with demo2:
        javascript_simple_calculator()
    with demo3:
        javascript_moving_box()
    
    st.markdown("---")
