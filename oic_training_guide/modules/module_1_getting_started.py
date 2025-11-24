"""Module 1: Getting Started with OIC Gen 3"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.helpers import *
from utils.diagrams import *

def render():
    """Render Module 1 content."""
    
    render_header(
        "Module 1: Getting Started with OIC Gen 3",
        "Days 1-2 | Introduction to Oracle Integration Cloud Generation 3"
    )
    
    # Module overview
    render_module_info(
        module_num=1,
        title="Getting Started",
        duration="~4 hours",
        topics=[
            "Introduction to OIC Gen 3",
            "Gen2 vs Gen3 UI comparison",
            "Creating your first integration",
            "Understanding the OIC architecture"
        ]
    )
    
    # Day 1 Content
    st.markdown("## 📅 Day 1: Complete Beginner to Advanced Guide")
    
    st.markdown("""
    ### What is Oracle Integration Cloud (OIC)?
    
    Oracle Integration Cloud (OIC) is a comprehensive cloud integration platform that enables you to:
    - Connect applications in the cloud and on-premises
    - Automate business processes
    - Develop visual applications
    - Gain insights from data
    
    **Key Capabilities:**
    """)
    
    render_key_points([
        "**Application Integration**: Connect SaaS and on-premises applications",
        "**Process Automation**: Automate business workflows",
        "**Visual Builder**: Create custom applications without coding",
        "**API Management**: Design, secure, and manage APIs",
        "**Insight**: Monitor and analyze integration performance"
    ])
    
    st.markdown("### OIC Gen 3 Architecture")
    
    st.markdown("```mermaid\n" + oic_architecture_diagram() + "\n```")
    
    st.markdown("""
    ### Core Components
    
    **1. Integrations**
    - The main building blocks of OIC
    - Define how data flows between systems
    - Three types: Scheduled, App-Driven, Event-Driven
    
    **2. Connections**
    - Define connectivity to external systems
    - Reusable across multiple integrations
    - Support various adapters (REST, SOAP, FTP, Database, etc.)
    
    **3. Lookups**
    - Store configuration and mapping data
    - Avoid hardcoding values in integrations
    - Easy to update without changing integration logic
    
    **4. Libraries**
    - Reusable integration components
    - Share common logic across integrations
    - Promote consistency and reduce duplication
    """)
    
    render_best_practice(
        "Always use connections and lookups to make your integrations configurable and environment-independent."
    )
    
    st.markdown("---")
    
    # Day 2 Content
    st.markdown("## 📅 Day 2: OIC Gen2 vs Gen3 UI & Your First Integration")
    
    st.markdown("""
    ### Gen2 vs Gen3: What's New?
    
    Oracle has redesigned the OIC interface in Generation 3 with significant improvements:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Gen2 Interface:**
        - Classic Oracle UI
        - Multiple navigation levels
        - Separate pages for different functions
        - Traditional menu structure
        """)
    
    with col2:
        st.markdown("""
        **Gen3 Interface:**
        - Modern, streamlined design
        - Unified navigation
        - Contextual actions
        - Improved search and filtering
        - Better performance
        """)
    
    st.markdown("""
    ### Key UI Improvements in Gen3
    """)
    
    render_key_points([
        "**Unified Home Page**: Quick access to all resources from a single dashboard",
        "**Enhanced Search**: Find integrations, connections, and resources faster",
        "**Contextual Menus**: Actions appear based on context",
        "**Better Monitoring**: Improved dashboards and analytics",
        "**Responsive Design**: Works better on different screen sizes"
    ])
    
    st.markdown("### Creating Your First Integration")
    
    st.markdown("""
    Let's create a simple "Hello World" integration to get familiar with the OIC interface.
    
    **Integration Type**: App-Driven (REST Trigger)
    
    **Objective**: Create a REST endpoint that returns a greeting message
    """)
    
    render_exercise(
        title="Create a Hello World Integration",
        description="Build your first OIC integration with a REST trigger and response",
        steps=[
            "Navigate to **Integrations** from the home page",
            "Click **Create** button",
            "Select **App Driven Orchestration**",
            "Enter integration name: `HelloWorld`",
            "Add a REST trigger connection",
            "Configure endpoint: `/hello`",
            "Add a Map action to create response",
            "Map a static message: `Hello from OIC Gen 3!`",
            "Activate the integration",
            "Test using the endpoint URL"
        ]
    )
    
    st.markdown("### Sample Integration Flow")
    
    st.markdown("```mermaid\n" + rest_integration_pattern() + "\n```")
    
    st.markdown("### Understanding Integration Canvas")
    
    st.markdown("""
    The **Integration Canvas** is where you design your integration flow:
    
    **Main Elements:**
    - **Trigger**: Starts the integration (REST, SOAP, Schedule, etc.)
    - **Actions**: Processing steps (Map, Assign, Switch, For-Each, etc.)
    - **Invokes**: Call external systems
    - **Return**: Send response back (for App-Driven integrations)
    """)
    
    render_code_example(
        title="Sample REST Response Mapping",
        code='''// In the Map action, create a JSON response
{
  "message": "Hello from OIC Gen 3!",
  "timestamp": fn:current-dateTime(),
  "status": "success"
}''',
        language="json"
    )
    
    render_tip(
        "Use descriptive names for your integrations and include version numbers (e.g., HelloWorld_v1.0) to track changes easily."
    )
    
    st.markdown("---")
    
    # Key Takeaways
    st.markdown("## 🎯 Key Takeaways")
    
    render_key_points([
        "OIC Gen 3 provides a modern, unified interface for integration development",
        "Three main integration types: Scheduled, App-Driven, and Event-Driven",
        "Connections are reusable and separate from integration logic",
        "The Integration Canvas is your visual design environment",
        "Always test integrations before activating in production"
    ])
    
    st.markdown("---")
    
    # What's Next
    st.markdown("## ⏭️ What's Next?")
    st.info("""
    In **Module 2**, you'll learn about:
    - Scheduled integrations with parameters
    - REST adapters in detail
    - App-driven integration patterns
    - Data mapping techniques
    
    Continue to Module 2 to deepen your OIC knowledge! 👉
    """)
    
    # Video References
    with st.expander("📺 Video References"):
        render_video_reference(
            1,
            "Oracle Integration Cloud (OIC) Gen3 Training: Complete Beginner to Advanced Guide",
            "https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN"
        )
        render_video_reference(
            2,
            "Oracle Integration Cloud (OIC) Training | OIC Gen2 vs Gen3 UI & Create Your First Integration",
            "https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN"
        )
