"""Module 7: Web Services & APIs"""

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
from utils.diagrams import *

def render():
    """Render Module 7 content."""
    
    render_header(
        "Module 7: Web Services & APIs",
        "Days 21-23 | SOAP, REST, and Oracle Fusion integration"
    )
    
    render_module_info(
        module_num=7,
        title="Web Services & APIs",
        duration="~6 hours",
        topics=[
            "SOAP vs REST comparison",
            "Creating SOAP and REST connections",
            "Oracle Fusion API integration",
            "Purchase order creation"
        ]
    )
    
    # Day 21
    st.markdown("## 📅 Day 21: Web Services & APIs - SOAP vs REST")
    
    st.markdown("""
    ### SOAP vs REST: Understanding the Difference
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **SOAP (Simple Object Access Protocol)**
        - XML-based protocol
        - Strict standards (WSDL)
        - Built-in error handling
        - WS-Security support
        - Stateful operations
        - Enterprise-focused
        
        **Best For:**
        - Enterprise applications
        - Financial transactions
        - High security requirements
        - Legacy system integration
        """)
    
    with col2:
        st.markdown("""
        **REST (Representational State Transfer)**
        - Architectural style
        - Multiple formats (JSON, XML)
        - Lightweight
        - Stateless
        - HTTP methods (GET, POST, PUT, DELETE)
        - Modern and flexible
        
        **Best For:**
        - Modern web applications
        - Mobile applications
        - Public APIs
        - Microservices
        """)
    
    st.markdown("""
    ### Creating REST Connections
    """)
    
    render_code_example(
        title="REST Connection Configuration",
        code='''Connection Name: CustomerAPI_REST
Connection Type: REST API Base URL
Base URL: https://api.example.com/v1

Security:
- Basic Authentication
- OAuth 2.0
- API Key
- No Security (for testing)

Headers:
- Content-Type: application/json
- Accept: application/json
- Custom headers as needed''',
        language="text"
    )
    
    st.markdown("""
    ### Creating SOAP Connections
    """)
    
    render_code_example(
        title="SOAP Connection Configuration",
        code='''Connection Name: OrderService_SOAP
Connection Type: SOAP
WSDL URL: https://api.example.com/OrderService?wsdl

Security:
- Username Token
- SAML Token
- WS-Security
- Basic Authentication

Operations: (Auto-discovered from WSDL)
- CreateOrder
- UpdateOrder
- GetOrderStatus
- CancelOrder''',
        language="text"
    )
    
    st.markdown("---")
    
    # Day 22
    st.markdown("## 📅 Day 22: Create Purchase Orders in Oracle Fusion using API")
    
    st.markdown("""
    ### Oracle Fusion Cloud Integration
    
    Oracle Fusion applications provide REST APIs for integration:
    
    **Common Fusion APIs:**
    - Purchase Orders
    - Suppliers
    - Invoices
    - Customers
    - Sales Orders
    - Inventory
    """)
    
    render_code_example(
        title="Fusion REST API Connection",
        code='''Connection Type: Oracle ERP Cloud
Instance URL: https://your-instance.fa.us2.oraclecloud.com
Security: Basic Authentication (or OAuth)
Username: integration.user
Password: ********

API Endpoint Example:
POST /fscmRestApi/resources/11.13.18.05/purchaseOrders

Headers:
Content-Type: application/json
Authorization: Basic base64(username:password)''',
        language="text"
    )
    
    st.markdown("""
    ### Purchase Order Creation
    """)
    
    render_code_example(
        title="Purchase Order JSON Payload",
        code='''{
  "ProcurementBUId": 204,
  "SoldToLegalEntity": "US1 Legal Entity",
  "BuyerId": 100010004471139,
  "CurrencyCode": "USD",
  "Description": "PO created from OIC",
  "lines": [
    {
      "LineNumber": 1,
      "ItemDescription": "Laptop Computer",
      "ItemId": 300000047414679,
      "Quantity": 5,
      "Price": 1200.00,
      "UOM": "Ea",
      "DestinationTypeCode": "EXPENSE",
      "RequesterId": 100010004471139
    }
  ]
}''',
        language="json"
    )
    
    render_tip(
        "Use Fusion's REST API documentation to find required fields and valid values. The documentation includes sample payloads and response structures."
    )
    
    st.markdown("---")
    
    # Day 23
    st.markdown("## 📅 Day 23: Oracle Integration to Create Purchase Orders")
    
    st.markdown("""
    ### Complete PO Creation Integration
    
    **Integration Flow:**
    1. Receive PO request (REST trigger or scheduled)
    2. Validate input data
    3. Transform to Fusion format
    4. Call Fusion PO API
    5. Handle response
    6. Return confirmation or error
    """)
    
    render_exercise(
        title="Build Purchase Order Integration",
        description="Create an integration to submit POs to Oracle Fusion",
        steps=[
            "Create Oracle ERP Cloud connection",
            "Create App-Driven integration with REST trigger",
            "Define input schema for PO request",
            "Add data validation logic",
            "Map input to Fusion PO format",
            "Invoke Fusion PO creation API",
            "Handle success response (extract PO number)",
            "Implement error handling",
            "Return response to caller",
            "Test with sample PO data"
        ]
    )
    
    render_code_example(
        title="Response Handling",
        code='''// Success Response from Fusion
{
  "POHeaderId": 300000123456789,
  "OrderNumber": "PO-2024-001234",
  "Status": "APPROVED",
  "TotalAmount": 6000.00
}

// Map to integration response
{
  "success": true,
  "poNumber": $fusionResponse.OrderNumber,
  "poId": $fusionResponse.POHeaderId,
  "message": "Purchase Order created successfully"
}

// Error Response
{
  "success": false,
  "errorCode": "VALIDATION_ERROR",
  "message": "Invalid supplier ID",
  "details": $fusionError.detail
}''',
        language="json"
    )
    
    render_best_practice(
        "Always validate input data before calling external APIs. This prevents unnecessary API calls and provides better error messages to users."
    )
    
    st.markdown("---")
    
    # Key Takeaways
    st.markdown("## 🎯 Key Takeaways")
    
    render_key_points([
        "SOAP is protocol-based with strict standards; REST is an architectural style",
        "REST is generally preferred for modern integrations due to simplicity",
        "Oracle Fusion provides comprehensive REST APIs for all modules",
        "Always handle both success and error responses from external APIs",
        "Use connection pooling and caching for better performance",
        "Validate input data before making external API calls"
    ])
    
    st.markdown("---")
    
    st.markdown("## ⏭️ What's Next?")
    st.info("""
    In **Module 8**, you'll learn about:
    - FBDI (File-Based Data Import) pattern
    - Bulk data loading into Fusion
    - Callback integrations
    - BIP (Business Intelligence Publisher) reports
    
    Continue to Module 8 for the final module! 👉
    """)
    
    with st.expander("📺 Video References"):
        for day in range(21, 24):
            st.markdown(f"📺 **Day {day}** - [View on YouTube](https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN)")
