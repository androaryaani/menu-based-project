// Custom JavaScript for Task Machine Pro

// Utility functions
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Add to page
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add loading states to buttons
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', function() {
        if (this.textContent.includes('Execute') || this.textContent.includes('Send') || this.textContent.includes('Run')) {
            const originalText = this.textContent;
            this.textContent = '⏳ Processing...';
            this.disabled = true;
            
            // Re-enable after 2 seconds (adjust based on actual processing time)
            setTimeout(() => {
                this.textContent = originalText;
                this.disabled = false;
            }, 2000);
        }
    });
});

// Add copy functionality to code blocks
document.querySelectorAll('code').forEach(codeBlock => {
    const copyButton = document.createElement('button');
    copyButton.textContent = '📋 Copy';
    copyButton.className = 'copy-button';
    copyButton.style.cssText = `
        position: absolute;
        top: 5px;
        right: 5px;
        background: #1abc9c;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 4px 8px;
        font-size: 12px;
        cursor: pointer;
    `;
    
    copyButton.addEventListener('click', function() {
        navigator.clipboard.writeText(codeBlock.textContent).then(() => {
            this.textContent = '✅ Copied!';
            setTimeout(() => {
                this.textContent = '📋 Copy';
            }, 2000);
        });
    });
    
    // Make code block container relative for absolute positioning
    codeBlock.style.position = 'relative';
    codeBlock.appendChild(copyButton);
});

// Add search functionality
function addSearchFunctionality() {
    const searchInput = document.createElement('input');
    searchInput.type = 'text';
    searchInput.placeholder = '🔍 Search tools...';
    searchInput.className = 'search-input';
    searchInput.style.cssText = `
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        margin-bottom: 20px;
        background: white;
        color: #333;
    `;
    
    // Insert search at the top of the main content
    const mainContent = document.querySelector('.main .block-container');
    if (mainContent) {
        mainContent.insertBefore(searchInput, mainContent.firstChild);
    }
    
    // Search functionality
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        const elements = document.querySelectorAll('h1, h2, h3, h4, p, button');
        
        elements.forEach(element => {
            if (element.textContent.toLowerCase().includes(searchTerm)) {
                element.style.display = 'block';
                element.style.backgroundColor = searchTerm ? 'rgba(26, 188, 156, 0.1)' : 'transparent';
            } else if (searchTerm) {
                element.style.display = 'none';
            } else {
                element.style.display = 'block';
                element.style.backgroundColor = 'transparent';
            }
        });
    });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    addSearchFunctionality();
    
    // Add fade-in animation to elements
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    });
    
    document.querySelectorAll('.st-emotion-cache-0, .stButton, .stAlert').forEach(el => {
        observer.observe(el);
    });
});

// Export functions for use in Streamlit
window.TaskMachinePro = {
    showNotification,
    addSearchFunctionality
};
