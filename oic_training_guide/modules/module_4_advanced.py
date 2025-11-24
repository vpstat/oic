"""Module 4: Advanced Features"""

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
from utils.diagrams import *

def render():
    """Render Module 4 content."""
    
    render_header(
        "Module 4: Advanced Features",
        "Days 11-13 | Global variables, fault handling, and reusable components"
    )
    
    render_module_info(
        module_num=4,
        title="Advanced Features",
        duration="~6 hours",
        topics=[
            "Global variables",
            "Fault handling and error management",
            "Import/export functionality",
            "Lookups and libraries"
        ]
    )
    
    # Day 11
    st.markdown("## 📅 Day 11: Global Variables & Fault Handling")
    
    st.markdown("""
    ### Global Variables
    
    Global variables store configuration values that can be used across multiple integrations:
    
    **Benefits:**
    - Centralized configuration management
    - Environment-specific values
    - Easy updates without changing integrations
    - Improved security (credentials, API keys)
    """)
    
    render_code_example(
        title="Global Variable Examples",
        code='''// Define global variables
API_BASE_URL = "https://api.example.com/v1"
MAX_RETRY_COUNT = 3
TIMEOUT_SECONDS = 30
NOTIFICATION_EMAIL = "admin@example.com"

// Use in integration
$endpoint = $API_BASE_URL + "/orders"
$retries = $MAX_RETRY_COUNT''',
        language="text"
    )
    
    render_best_practice(
        "Use global variables for all environment-specific values. This makes promoting integrations between environments much easier."
    )
    
    st.markdown("""
    ### Introduction to Fault Handling
    
    Fault handling ensures your integrations gracefully handle errors:
    """)
    
    st.markdown("```mermaid\n" + fault_handling_flow() + "\n```")
    
    render_key_points([
        "**System Faults**: Infrastructure or connectivity issues",
        "**Business Faults**: Application logic errors",
        "**Validation Faults**: Data validation failures",
        "**Timeout Faults**: Operations exceeding time limits"
    ])
    
    st.markdown("---")
    
    # Day 12
    st.markdown("## 📅 Day 12: Fault Handling & Error Management")
    
    st.markdown("""
    ### Fault Handler Configuration
    
    **Scope-Level Fault Handlers:**
    - Catch errors within a specific scope
    - Different handlers for different error types
    - Can re-throw or handle errors
    
    **Global Fault Handler:**
    - Catches unhandled errors
    - Last line of defense
    - Typically logs and notifies
    """)
    
    render_code_example(
        title="Fault Handler Structure",
        code='''Integration Flow:
├── Trigger
├── Scope: ProcessOrder
│   ├── Invoke: ValidateOrder
│   ├── Invoke: CreateOrder
│   └── Fault Handler
│       ├── Catch: ValidationError → Return error response
│       ├── Catch: SystemError → Retry logic
│       └── Catch: All → Log and notify
└── Global Fault Handler
    └── Send notification email''',
        language="text"
    )
    
    st.markdown("""
    ### Error Handling Best Practices
    """)
    
    render_best_practice(
        "Always implement fault handlers for external system calls. Network issues and API failures are common in integrations."
    )
    
    render_key_points([
        "Log all errors with sufficient context for debugging",
        "Implement retry logic for transient errors",
        "Send notifications for critical failures",
        "Return meaningful error messages to callers",
        "Use different handlers for different error types"
    ])
    
    render_exercise(
        title="Implement Comprehensive Fault Handling",
        description="Add fault handling to an existing integration",
        steps=[
            "Open an existing integration",
            "Add a Scope around external invocations",
            "Configure Scope fault handler",
            "Add Catch blocks for specific errors",
            "Implement retry logic for system errors",
            "Add logging in fault handlers",
            "Configure global fault handler",
            "Test by simulating various failures"
        ]
    )
    
    st.markdown("---")
    
    # Day 13
    st.markdown("## 📅 Day 13: Import & Export, Lookups & Libraries")
    
    st.markdown("""
    ### Import & Export
    
    Import/Export enables integration lifecycle management:
    
    **Export Package Contents:**
    - Integrations
    - Connections
    - Lookups
    - Libraries
    - Certificates
    """)
    
    render_tip(
        "Export packages as .iar files (Integration Archive). These can be version controlled in Git for proper change management."
    )
    
    st.markdown("""
    **Deployment Workflow:**
    1. **Develop** in DEV environment
    2. **Export** integration package
    3. **Import** to TEST environment
    4. **Test** thoroughly
    5. **Export** from TEST
    6. **Import** to PROD
    7. **Activate** in PROD
    """)
    
    st.markdown("""
    ### Lookups
    
    Lookups store mapping data used in integrations:
    
    **Common Use Cases:**
    - Status code mappings
    - Country code conversions
    - Product category mappings
    - Error code translations
    """)
    
    render_code_example(
        title="Lookup Example: Status Code Mapping",
        code='''Lookup Name: OrderStatusMapping

Source Value | Target Value
-------------|-------------
NEW          | 01
PROCESSING   | 02
SHIPPED      | 03
DELIVERED    | 04
CANCELLED    | 99

// Use in mapping
$targetStatus = dvm:lookupValue("OrderStatusMapping", 
                                "Source Value", 
                                $sourceStatus, 
                                "Target Value", 
                                "00")''',
        language="text"
    )
    
    st.markdown("""
    ### Libraries
    
    Libraries contain reusable integration components:
    
    **Library Types:**
    - **Integration Libraries**: Reusable sub-flows
    - **JavaScript Libraries**: Custom functions
    - **XSLT Libraries**: Transformation templates
    """)
    
    render_best_practice(
        "Create libraries for common patterns like error handling, logging, or data transformations. This promotes consistency and reduces duplication."
    )
    
    st.markdown("---")
    
    # Key Takeaways
    st.markdown("## 🎯 Key Takeaways")
    
    render_key_points([
        "Global variables centralize configuration and simplify environment management",
        "Comprehensive fault handling is essential for production integrations",
        "Different error types require different handling strategies",
        "Import/Export enables proper lifecycle management and deployment",
        "Lookups eliminate hardcoded mapping values",
        "Libraries promote reusability and consistency across integrations"
    ])
    
    st.markdown("---")
    
    st.markdown("## ⏭️ What's Next?")
    st.info("""
    In **Module 5**, you'll learn about:
    - Stage File actions for file processing
    - FTP adapter and file operations
    - Reading, writing, and archiving files
    - File-based integration patterns
    
    Continue to Module 5! 👉
    """)
    
    with st.expander("📺 Video References"):
        for day in range(11, 14):
            st.markdown(f"📺 **Day {day}** - [View on YouTube](https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN)")
