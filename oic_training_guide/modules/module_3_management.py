"""Module 3: Integration Management"""

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
from utils.diagrams import *

def render():
    """Render Module 3 content."""
    
    render_header(
        "Module 3: Integration Management",
        "Days 8-10 | Managing, monitoring, and maintaining integrations"
    )
    
    render_module_info(
        module_num=3,
        title="Integration Management",
        duration="~6 hours",
        topics=[
            "Integration status and metadata",
            "Versioning and cloning",
            "iCall expressions",
            "Integration monitoring and troubleshooting"
        ]
    )
    
    # Day 8
    st.markdown("## 📅 Day 8: Integration Status, Metadata & Versioning")
    
    st.markdown("""
    ### Integration Lifecycle States
    
    An integration can be in one of several states:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Development States:**
        - **Configured**: Created but not activated
        - **Draft**: Being edited
        - **Invalid**: Has configuration errors
        """)
    
    with col2:
        st.markdown("""
        **Runtime States:**
        - **Activated**: Running and processing
        - **Deactivated**: Stopped
        - **Suspended**: Temporarily paused
        """)
    
    st.markdown("""
    ### Integration Metadata
    
    Metadata helps organize and track integrations:
    """)
    
    render_key_points([
        "**Identifier**: Unique integration ID",
        "**Version**: Version number (e.g., 01.00.0000)",
        "**Description**: Purpose and functionality",
        "**Tags**: Categorization labels",
        "**Created/Modified**: Timestamps and user info"
    ])
    
    st.markdown("""
    ### Versioning Best Practices
    """)
    
    render_best_practice(
        "Use semantic versioning: MAJOR.MINOR.PATCH (e.g., 01.02.0003). Increment MAJOR for breaking changes, MINOR for new features, PATCH for bug fixes."
    )
    
    render_code_example(
        title="Version Naming Convention",
        code='''Integration Name: ProcessOrder_v01.02.0003
- v01: Major version (breaking changes)
- 02: Minor version (new features)
- 0003: Patch version (bug fixes)

Example progression:
01.00.0000 → Initial version
01.00.0001 → Bug fix
01.01.0000 → New feature added
02.00.0000 → Breaking change''',
        language="text"
    )
    
    st.markdown("---")
    
    # Day 9
    st.markdown("## 📅 Day 9: Cloning Integrations, Mapping, Editions & Roles")
    
    st.markdown("""
    ### Cloning Integrations
    
    Cloning creates a copy of an existing integration, useful for:
    - Creating similar integrations
    - Testing changes without affecting production
    - Deploying across environments
    
    **Steps to Clone:**
    1. Select the integration to clone
    2. Click the Clone action
    3. Provide a new name and identifier
    4. Review and update connections
    5. Modify as needed
    """)
    
    render_tip(
        "When cloning, always update connection references to match the target environment (Dev, Test, Prod)."
    )
    
    st.markdown("""
    ### OIC Editions and Roles
    
    **OIC Editions:**
    - **Standard**: Basic integration capabilities
    - **Enterprise**: Advanced features, higher limits
    - **Bring Your Own License (BYOL)**: Use existing Oracle licenses
    
    **User Roles:**
    """)
    
    render_key_points([
        "**ServiceAdministrator**: Full access to all features",
        "**ServiceDeveloper**: Create and manage integrations",
        "**ServiceMonitor**: View monitoring and logs only",
        "**ServiceUser**: Execute integrations only"
    ])
    
    st.markdown("---")
    
    # Day 10
    st.markdown("## 📅 Day 10: iCall Expressions & Integration Monitoring")
    
    st.markdown("""
    ### iCall Expressions
    
    iCall expressions provide advanced capabilities for dynamic integration behavior:
    
    **Common Uses:**
    - Dynamic endpoint URLs
    - Conditional connection selection
    - Runtime configuration
    """)
    
    render_code_example(
        title="iCall Expression Examples",
        code='''// Dynamic endpoint based on environment
$endpoint = if ($environment = "PROD") 
            then "https://api.prod.example.com" 
            else "https://api.test.example.com"

// Dynamic connection selection
$connectionId = concat("ERP_", $region, "_Connection")

// Conditional processing
$processFlag = if ($amount > 10000) then "HIGH_VALUE" else "STANDARD"''',
        language="javascript"
    )
    
    st.markdown("""
    ### Integration Monitoring
    
    OIC provides comprehensive monitoring capabilities:
    
    **Monitoring Features:**
    """)
    
    render_key_points([
        "**Dashboard**: Overview of integration health",
        "**Activity Stream**: Real-time integration execution",
        "**Tracking**: Follow specific business transactions",
        "**Errors**: View and analyze failures",
        "**Performance**: Response times and throughput"
    ])
    
    st.markdown("""
    ### Troubleshooting Tips
    """)
    
    render_tip(
        "Use tracking variables to add breadcrumbs throughout your integration. This makes debugging much easier when issues occur."
    )
    
    render_exercise(
        title="Monitor and Debug an Integration",
        description="Practice using OIC monitoring tools",
        steps=[
            "Activate an integration with tracking variables",
            "Execute the integration multiple times",
            "Navigate to Monitoring → Tracking",
            "Search using business identifier",
            "View the activity stream",
            "Analyze any errors in the error log",
            "Download diagnostic logs if needed"
        ]
    )
    
    st.markdown("---")
    
    # Key Takeaways
    st.markdown("## 🎯 Key Takeaways")
    
    render_key_points([
        "Integration versioning helps track changes and manage deployments",
        "Cloning is useful for creating similar integrations and environment promotion",
        "Different OIC roles provide appropriate access levels for different users",
        "iCall expressions enable dynamic, runtime-configurable integrations",
        "Comprehensive monitoring is essential for production integrations",
        "Use tracking variables and business identifiers for easier troubleshooting"
    ])
    
    st.markdown("---")
    
    st.markdown("## ⏭️ What's Next?")
    st.info("""
    In **Module 4**, you'll learn about:
    - Global variables for configuration management
    - Comprehensive fault handling strategies
    - Import/export for deployment automation
    - Lookups and libraries for reusability
    
    Continue to Module 4! 👉
    """)
    
    with st.expander("📺 Video References"):
        for day in range(8, 11):
            st.markdown(f"📺 **Day {day}** - [View on YouTube](https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN)")
