"""
OIC Gen 3 Training Guide - Comprehensive Streamlit Application
A complete learning resource for Oracle Integration Cloud Generation 3
"""

import streamlit as st
import sys
from pathlib import Path

# Add modules directory to path
sys.path.append(str(Path(__file__).parent))

# Import modules
from modules import (
    module_1_getting_started,
    module_2_core_concepts,
    module_3_management,
    module_4_advanced,
    module_5_file_ops,
    module_6_database,
    module_7_web_services,
    module_8_enterprise
)

# Page configuration
st.set_page_config(
    page_title="OIC Gen 3 Training Guide",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    /* Main styling */
    .main {
        padding: 2rem;
    }
    
    /* Headers */
    h1 {
        color: #312D2A;
        font-weight: 700;
        padding-bottom: 1rem;
        border-bottom: 3px solid #FF0000;
    }
    
    h2 {
        color: #C74634;
        margin-top: 2rem;
    }
    
    h3 {
        color: #312D2A;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #F8F8F8;
    }
    
    /* Code blocks */
    .stCodeBlock {
        background-color: #F5F5F5;
        border-left: 4px solid #FF0000;
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 8px;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #FF0000;
        color: white;
        border-radius: 6px;
        padding: 0.5rem 2rem;
        font-weight: 600;
    }
    
    .stButton>button:hover {
        background-color: #C74634;
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background-color: #FF0000;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #F8F8F8;
        border-radius: 6px;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #FF0000;
    }
</style>
""", unsafe_allow_html=True)

# Module configuration
MODULES = {
    "🏠 Home": None,
    "1️⃣ Getting Started": module_1_getting_started,
    "2️⃣ Core Integration Concepts": module_2_core_concepts,
    "3️⃣ Integration Management": module_3_management,
    "4️⃣ Advanced Features": module_4_advanced,
    "5️⃣ File Operations": module_5_file_ops,
    "6️⃣ Database Integration": module_6_database,
    "7️⃣ Web Services & APIs": module_7_web_services,
    "8️⃣ Enterprise Patterns": module_8_enterprise,
    "📚 Resources": None,
}

def render_home():
    """Render the home page."""
    st.title("☁️ Oracle Integration Cloud Gen 3 Training Guide")
    st.markdown("### Your Complete Learning Path to OIC Mastery")
    
    st.markdown("""
    Welcome to the comprehensive Oracle Integration Cloud (OIC) Generation 3 training guide! 
    This interactive learning resource is based on a complete 26-day training series, 
    organized into 8 logical modules for structured learning.
    """)
    
    # Overview cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Modules", "8", help="Comprehensive learning modules")
    
    with col2:
        st.metric("Training Days", "26", help="Days of detailed content")
    
    with col3:
        st.metric("Topics", "50+", help="Key topics covered")
    
    with col4:
        st.metric("Difficulty", "Beginner to Advanced", help="Complete learning path")
    
    st.markdown("---")
    
    # Learning path
    st.markdown("## 🎯 Learning Path")
    
    modules_info = [
        ("Module 1: Getting Started", "Days 1-2", "Introduction to OIC Gen 3, UI overview, first integration"),
        ("Module 2: Core Integration Concepts", "Days 3-7", "Scheduled integrations, REST adapters, data mapping"),
        ("Module 3: Integration Management", "Days 8-10", "Status tracking, versioning, monitoring"),
        ("Module 4: Advanced Features", "Days 11-13", "Global variables, fault handling, import/export"),
        ("Module 5: File Operations", "Days 14-17", "Stage file actions, FTP connections"),
        ("Module 6: Database Integration", "Days 18-20", "ATP connections, CRUD operations, stored procedures"),
        ("Module 7: Web Services & APIs", "Days 21-23", "SOAP vs REST, Oracle Fusion integration"),
        ("Module 8: Enterprise Patterns", "Days 24-26", "FBDI, bulk loading, callbacks, BIP reports"),
    ]
    
    for i, (title, days, description) in enumerate(modules_info, 1):
        with st.expander(f"**{title}** ({days})"):
            st.markdown(f"📖 {description}")
            st.markdown(f"*Click on '{i}️⃣ {title.split(': ')[1]}' in the sidebar to start learning*")
    
    st.markdown("---")
    
    # Key features
    st.markdown("## ✨ What You'll Learn")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - ✅ OIC Gen 3 architecture and UI
        - ✅ Creating and managing integrations
        - ✅ Working with connections and adapters
        - ✅ Data mapping and transformations
        - ✅ Monitoring and troubleshooting
        """)
    
    with col2:
        st.markdown("""
        **Advanced Topics:**
        - ✅ Fault handling and error management
        - ✅ File processing and FTP operations
        - ✅ Database integrations with ATP
        - ✅ SOAP and REST web services
        - ✅ Enterprise patterns (FBDI, callbacks)
        """)
    
    st.markdown("---")
    
    # Getting started
    st.markdown("## 🚀 Getting Started")
    st.info("👈 **Select a module from the sidebar to begin your learning journey!**")
    
    st.markdown("""
    **Recommended Learning Approach:**
    1. Start with Module 1 if you're new to OIC
    2. Follow the modules in sequence for a structured learning path
    3. Practice with the hands-on exercises in each module
    4. Refer back to earlier modules as needed
    5. Use the Resources section for additional references
    """)

def render_resources():
    """Render the resources page."""
    st.title("📚 Resources & References")
    
    st.markdown("## 🔗 Official Documentation")
    st.markdown("""
    - [Oracle Integration Cloud Documentation](https://docs.oracle.com/en/cloud/paas/integration-cloud/)
    - [OIC Gen 3 Release Notes](https://docs.oracle.com/en/cloud/paas/integration-cloud/whats-new/)
    - [Oracle Learning Library](https://apexapps.oracle.com/pls/apex/f?p=44785:1)
    - [Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/home.htm)
    """)
    
    st.markdown("---")
    
    st.markdown("## 🎥 Video Training Series")
    st.markdown("""
    This guide is based on the comprehensive OIC Gen 3 Training Series:
    - [Complete Playlist on YouTube](https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN)
    - 26 detailed training sessions
    - Beginner to advanced topics
    - Hands-on demonstrations
    """)
    
    st.markdown("---")
    
    st.markdown("## 📖 Quick Reference Guides")
    
    with st.expander("🔌 Common Adapter Types"):
        st.markdown("""
        | Adapter | Use Case | Key Features |
        |---------|----------|--------------|
        | REST | RESTful APIs | JSON/XML, OAuth, Basic Auth |
        | SOAP | SOAP Web Services | WSDL-based, WS-Security |
        | FTP | File Transfer | SFTP, FTPS, File operations |
        | Database | Database Operations | Insert, Update, Stored Procedures |
        | Oracle ERP Cloud | Fusion Applications | Pre-built integrations |
        | File | Local File Operations | Read, Write, List |
        """)
    
    with st.expander("⚙️ Integration Patterns"):
        st.markdown("""
        **Scheduled Integration:**
        - Time-based execution
        - Batch processing
        - No external trigger required
        
        **App-Driven Integration:**
        - REST/SOAP endpoint exposure
        - Synchronous processing
        - Request-response pattern
        
        **Event-Driven Integration:**
        - Triggered by events
        - Asynchronous processing
        - Event subscription model
        """)
    
    with st.expander("🛠️ Best Practices Checklist"):
        st.markdown("""
        - ✅ Use meaningful names for integrations and connections
        - ✅ Implement proper error handling in all integrations
        - ✅ Use tracking variables for monitoring
        - ✅ Document your integrations with descriptions
        - ✅ Test thoroughly before activation
        - ✅ Use lookups for configuration values
        - ✅ Implement retry logic for transient errors
        - ✅ Monitor integration performance regularly
        - ✅ Version control your integration packages
        - ✅ Follow naming conventions consistently
        """)
    
    st.markdown("---")
    
    st.markdown("## 💡 Tips for Success")
    st.success("""
    **Learning Tips:**
    - Practice in a development environment first
    - Start with simple integrations and gradually increase complexity
    - Review error logs to understand issues
    - Join Oracle Cloud communities for support
    - Keep up with OIC updates and new features
    """)
    
    st.markdown("---")
    
    st.markdown("## 🤝 Community & Support")
    st.markdown("""
    - [Oracle Cloud Customer Connect](https://cloudcustomerconnect.oracle.com/)
    - [Oracle Integration Blog](https://blogs.oracle.com/integration/)
    - [Oracle Forums](https://community.oracle.com/)
    - [Stack Overflow - OIC Tag](https://stackoverflow.com/questions/tagged/oracle-integration-cloud)
    """)

def main():
    """Main application logic."""
    
    # Sidebar
    st.sidebar.title("📖 Navigation")
    st.sidebar.markdown("Select a module to explore:")
    
    # Module selection
    selected_module = st.sidebar.radio(
        "Modules",
        list(MODULES.keys()),
        label_visibility="collapsed"
    )
    
    st.sidebar.markdown("---")
    
    # Progress tracker (placeholder - can be enhanced with session state)
    st.sidebar.markdown("### 📊 Your Progress")
    st.sidebar.progress(0.0)
    st.sidebar.caption("Complete modules to track your progress")
    
    st.sidebar.markdown("---")
    
    # About section
    with st.sidebar.expander("ℹ️ About"):
        st.markdown("""
        **OIC Gen 3 Training Guide**
        
        Version 1.0
        
        A comprehensive learning resource for Oracle Integration Cloud Generation 3.
        
        Based on the 26-day training series covering beginner to advanced topics.
        """)
    
    # Render selected module
    if selected_module == "🏠 Home":
        render_home()
    elif selected_module == "📚 Resources":
        render_resources()
    else:
        module = MODULES[selected_module]
        if module:
            module.render()

if __name__ == "__main__":
    main()
