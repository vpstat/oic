"""Module 2: Core Integration Concepts"""

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
from utils.diagrams import *

def render():
    """Render Module 2 content."""
    
    render_header(
        "Module 2: Core Integration Concepts",
        "Days 3-7 | Master the fundamentals of OIC integrations"
    )
    
    render_module_info(
        module_num=2,
        title="Core Integration Concepts",
        duration="~10 hours",
        topics=[
            "Scheduled integrations with parameters",
            "REST adapters and connections",
            "App-driven integration patterns",
            "Integration canvas and actions",
            "Data mapping with Assign and Map actions"
        ]
    )
    
    # Day 3: Scheduled Integration
    st.markdown("## 📅 Day 3: Scheduled Integration with Parameters & Tracking Variables")
    
    st.markdown("""
    ### What is a Scheduled Integration?
    
    A **Scheduled Integration** runs automatically at specified intervals without external triggers.
    
    **Use Cases:**
    - Batch data synchronization
    - Periodic report generation
    - Scheduled data cleanup
    - Regular data imports/exports
    """)
    
    st.markdown("```mermaid\n" + scheduled_integration_pattern() + "\n```")
    
    st.markdown("""
    ### Parameters in Scheduled Integrations
    
    Parameters make your integrations flexible and reusable:
    """)
    
    render_code_example(
        title="Defining Integration Parameters",
        code='''// Example parameters for a scheduled integration
{
  "batchSize": 100,
  "sourceSystem": "ERP",
  "targetSystem": "CRM",
  "processDate": "2024-01-01"
}''',
        language="json"
    )
    
    render_key_points([
        "**Schedule Parameters**: Define at integration level, passed during execution",
        "**Tracking Variables**: Monitor integration flow and debug issues",
        "**Business Identifiers**: Track specific records through the integration"
    ])
    
    render_exercise(
        title="Create a Scheduled Integration",
        description="Build a scheduled integration that processes data daily",
        steps=[
            "Create new integration, select 'Schedule'",
            "Configure schedule: Daily at 2:00 AM",
            "Add parameters: batchSize, startDate",
            "Add tracking variable: recordCount",
            "Implement data processing logic",
            "Test with different parameter values"
        ]
    )
    
    st.markdown("---")
    
    # Day 4: REST Adapters
    st.markdown("## 📅 Day 4: REST Adapters, Connections & App-Driven Integration")
    
    st.markdown("""
    ### REST Adapter Overview
    
    The REST adapter is one of the most commonly used adapters in OIC:
    
    **Capabilities:**
    - Invoke REST APIs (GET, POST, PUT, DELETE, PATCH)
    - Expose REST endpoints
    - Support for JSON and XML
    - Authentication: Basic, OAuth 2.0, API Key
    """)
    
    render_code_example(
        title="REST Connection Configuration",
        code='''Connection Type: REST API Base URL
Base URL: https://api.example.com/v1
Security Policy: OAuth 2.0
Grant Type: Client Credentials
Client ID: your-client-id
Client Secret: your-client-secret''',
        language="text"
    )
    
    st.markdown("""
    ### App-Driven Integration Pattern
    
    App-Driven integrations expose a REST or SOAP endpoint that can be called by external applications.
    
    **Characteristics:**
    - Synchronous processing
    - Request-response pattern
    - Real-time data exchange
    - Suitable for API-based integrations
    """)
    
    render_best_practice(
        "Use App-Driven integrations when you need real-time, synchronous responses. Use Scheduled integrations for batch processing."
    )
    
    st.markdown("---")
    
    # Day 5: Parameters in App-Driven
    st.markdown("## 📅 Day 5: Master Parameters in App-Driven Integration")
    
    st.markdown("""
    ### Query Parameters vs Path Parameters
    
    **Query Parameters**: Passed in the URL query string
    ```
    GET /api/users?status=active&limit=10
    ```
    
    **Path Parameters**: Part of the URL path
    ```
    GET /api/users/{userId}/orders/{orderId}
    ```
    
    **Header Parameters**: Passed in HTTP headers
    ```
    Authorization: Bearer token123
    X-Custom-Header: value
    ```
    """)
    
    render_code_example(
        title="Configuring REST Trigger with Parameters",
        code='''Endpoint: /api/orders/{orderId}
Method: GET
Path Parameters:
  - orderId (string, required)
Query Parameters:
  - includeDetails (boolean, optional)
  - format (string, optional, default: json)''',
        language="text"
    )
    
    st.markdown("---")
    
    # Day 6: Integration Canvas
    st.markdown("## 📅 Day 6: Integration Canvas, Assign & Switch Actions")
    
    st.markdown("""
    ### Integration Canvas Actions
    
    The Integration Canvas provides various actions to build your integration logic:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Data Actions:**
        - **Assign**: Set variable values
        - **Map**: Transform data structures
        - **Data Stitch**: Combine data from multiple sources
        """)
    
    with col2:
        st.markdown("""
        **Control Actions:**
        - **Switch**: Conditional branching
        - **For-Each**: Loop through collections
        - **While**: Conditional looping
        - **Scope**: Group actions together
        """)
    
    st.markdown("""
    ### Assign Action
    
    Use **Assign** to set values for variables:
    """)
    
    render_code_example(
        title="Assign Action Examples",
        code='''// Set a simple variable
$orderStatus = "PENDING"

// Calculate a value
$totalAmount = $quantity * $unitPrice

// Concatenate strings
$fullName = concat($firstName, " ", $lastName)

// Current timestamp
$processedDate = fn:current-dateTime()''',
        language="javascript"
    )
    
    st.markdown("""
    ### Switch Action
    
    Use **Switch** for conditional logic (similar to if-else):
    """)
    
    render_code_example(
        title="Switch Action Example",
        code='''// Switch based on order amount
Switch ($orderAmount)
  Case $orderAmount > 10000:
    // High value order processing
    Route to: HighValueOrderHandler
  Case $orderAmount > 1000:
    // Medium value order processing
    Route to: StandardOrderHandler
  Otherwise:
    // Low value order processing
    Route to: BasicOrderHandler''',
        language="text"
    )
    
    st.markdown("---")
    
    # Day 7: Data Mapping
    st.markdown("## 📅 Day 7: Map Data with Assign & Data Mapping")
    
    st.markdown("""
    ### Data Mapping in OIC
    
    Data mapping transforms data from source format to target format.
    
    **Mapping Types:**
    1. **Direct Mapping**: One-to-one field mapping
    2. **Expression Mapping**: Using XPath/XSLT functions
    3. **Conditional Mapping**: Based on conditions
    4. **Lookup Mapping**: Using lookup tables
    """)
    
    render_code_example(
        title="Common Mapping Functions",
        code='''// String functions
concat($firstName, " ", $lastName)
substring($text, 1, 10)
upper-case($name)
lower-case($email)

// Date functions
fn:current-dateTime()
fn:format-dateTime($date, "[Y0001]-[M01]-[D01]")

// Number functions
number($stringValue)
round($decimal, 2)

// Conditional
if ($status = "ACTIVE") then "Y" else "N"''',
        language="javascript"
    )
    
    render_tip(
        "Use the mapper's built-in functions instead of writing complex XPath expressions. They're easier to maintain and debug."
    )
    
    render_exercise(
        title="Complex Data Mapping",
        description="Transform an order JSON to a different structure",
        steps=[
            "Create an App-Driven integration with REST trigger",
            "Add a Map action",
            "Map source fields to target structure",
            "Use concat() to combine address fields",
            "Use if-then-else for conditional mapping",
            "Add current timestamp to output",
            "Test with sample JSON payload"
        ]
    )
    
    st.markdown("---")
    
    # Key Takeaways
    st.markdown("## 🎯 Key Takeaways")
    
    render_key_points([
        "Scheduled integrations run on a timer, App-Driven integrations respond to requests",
        "REST adapter is versatile and supports various authentication methods",
        "Use parameters to make integrations flexible and reusable",
        "Assign action sets variables, Map action transforms data structures",
        "Switch action enables conditional logic in your integrations",
        "Tracking variables help monitor and debug integration flows"
    ])
    
    st.markdown("---")
    
    st.markdown("## ⏭️ What's Next?")
    st.info("""
    In **Module 3**, you'll learn about:
    - Integration status and metadata
    - Versioning and cloning integrations
    - Integration monitoring and troubleshooting
    - iCall expressions for advanced logic
    
    Continue to Module 3! 👉
    """)
    
    with st.expander("📺 Video References"):
        for day in range(3, 8):
            st.markdown(f"📺 **Day {day}** - [View on YouTube](https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN)")
