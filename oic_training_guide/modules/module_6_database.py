"""Module 6: Database Integration"""

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
from utils.diagrams import *

def render():
    """Render Module 6 content."""
    
    render_header(
        "Module 6: Database Integration",
        "Days 18-20 | Connect and interact with databases"
    )
    
    render_module_info(
        module_num=6,
        title="Database Integration",
        duration="~6 hours",
        topics=[
            "ATP database connections",
            "Insert and update operations",
            "Stored procedure invocations",
            "Database integration patterns"
        ]
    )
    
    # Day 18
    st.markdown("## 📅 Day 18: ATP Database Connection - Insert & Update")
    
    st.markdown("""
    ### What is ATP?
    
    **Autonomous Transaction Processing (ATP)** is Oracle's self-driving database:
    
    **Key Features:**
    - Self-tuning and self-patching
    - Automatic scaling
    - Built-in security
    - High availability
    """)
    
    st.markdown("```mermaid\n" + database_integration_flow() + "\n```")
    
    st.markdown("""
    ### Database Adapter Configuration
    """)
    
    render_code_example(
        title="ATP Connection Setup",
        code='''Connection Type: Oracle Database
Connection Method: Wallet
Wallet File: Upload ATP wallet ZIP
Service Name: dbname_high (or _medium, _low)
Username: ADMIN (or application user)
Password: ********

Connection String Example:
(description= (retry_count=20)(retry_delay=3)
  (address=(protocol=tcps)(port=1522)
    (host=adb.region.oraclecloud.com))
  (connect_data=(service_name=dbname_high.adb.oraclecloud.com))
  (security=(ssl_server_cert_dn="CN=...")))''',
        language="text"
    )
    
    st.markdown("""
    ### Insert Operation
    
    Insert new records into database tables:
    """)
    
    render_code_example(
        title="Insert Operation Example",
        code='''Operation: Insert
Table: ORDERS

SQL Generated:
INSERT INTO ORDERS (
  ORDER_ID,
  CUSTOMER_ID,
  ORDER_DATE,
  TOTAL_AMOUNT,
  STATUS
) VALUES (
  ?,  -- Mapped from $orderId
  ?,  -- Mapped from $customerId
  ?,  -- Mapped from $orderDate
  ?,  -- Mapped from $totalAmount
  ?   -- Mapped from 'PENDING'
)

Mapping:
ORDER_ID      ← $orderId
CUSTOMER_ID   ← $customerId
ORDER_DATE    ← fn:current-dateTime()
TOTAL_AMOUNT  ← $totalAmount
STATUS        ← "PENDING"''',
        language="sql"
    )
    
    st.markdown("---")
    
    # Day 19
    st.markdown("## 📅 Day 19: ATP Database - Insert & Update Part 2")
    
    st.markdown("""
    ### Update Operation
    
    Modify existing records in database tables:
    """)
    
    render_code_example(
        title="Update Operation Example",
        code='''Operation: Update
Table: ORDERS
Where Clause: ORDER_ID = #orderId

SQL Generated:
UPDATE ORDERS
SET
  STATUS = ?,
  UPDATED_DATE = ?,
  UPDATED_BY = ?
WHERE ORDER_ID = ?

Mapping:
STATUS       ← $newStatus
UPDATED_DATE ← fn:current-dateTime()
UPDATED_BY   ← $userId
ORDER_ID     ← $orderId (where clause)''',
        language="sql"
    )
    
    render_warning(
        "Always include a WHERE clause in UPDATE operations to avoid updating all rows. Test updates in a development environment first."
    )
    
    st.markdown("""
    ### Upsert Pattern (Insert or Update)
    
    Handle both insert and update in a single integration:
    """)
    
    render_code_example(
        title="Upsert Logic",
        code='''1. Query database to check if record exists
   SELECT COUNT(*) FROM ORDERS WHERE ORDER_ID = ?

2. Use Switch action based on count:
   Case count = 0:
     → Insert new record
   Case count > 0:
     → Update existing record

3. Return success response''',
        language="text"
    )
    
    st.markdown("---")
    
    # Day 20
    st.markdown("## 📅 Day 20: ATP Database - Invoke Stored Procedure")
    
    st.markdown("""
    ### Stored Procedures
    
    Call database stored procedures from OIC:
    
    **Benefits:**
    - Encapsulate complex business logic in database
    - Better performance for data-intensive operations
    - Reuse existing database logic
    - Maintain data integrity with transactions
    """)
    
    render_code_example(
        title="Stored Procedure Example",
        code='''-- Database Stored Procedure
CREATE OR REPLACE PROCEDURE PROCESS_ORDER (
  p_order_id IN NUMBER,
  p_action IN VARCHAR2,
  p_result OUT VARCHAR2,
  p_error_msg OUT VARCHAR2
) AS
BEGIN
  -- Business logic here
  IF p_action = 'APPROVE' THEN
    UPDATE ORDERS 
    SET STATUS = 'APPROVED'
    WHERE ORDER_ID = p_order_id;
    p_result := 'SUCCESS';
  ELSE
    p_result := 'INVALID_ACTION';
  END IF;
EXCEPTION
  WHEN OTHERS THEN
    p_error_msg := SQLERRM;
    p_result := 'ERROR';
END;

-- OIC Invocation
Operation: Run a Stored Procedure
Procedure: PROCESS_ORDER
Input Parameters:
  p_order_id   ← $orderId
  p_action     ← $action
Output Parameters:
  p_result     → $result
  p_error_msg  → $errorMessage''',
        language="sql"
    )
    
    render_best_practice(
        "Use stored procedures for complex database operations involving multiple tables or complex business logic. This reduces network round-trips and improves performance."
    )
    
    render_exercise(
        title="Build a Database Integration",
        description="Create an integration that manages customer records",
        steps=[
            "Create ATP database connection",
            "Create App-Driven integration with REST trigger",
            "Add Switch based on operation type (INSERT/UPDATE/DELETE)",
            "Implement Insert branch for new customers",
            "Implement Update branch for existing customers",
            "Add error handling for database operations",
            "Test with sample customer data",
            "Monitor database operations in OIC"
        ]
    )
    
    st.markdown("---")
    
    # Key Takeaways
    st.markdown("## 🎯 Key Takeaways")
    
    render_key_points([
        "ATP provides a fully managed, self-driving database for OIC integrations",
        "Database adapter supports Insert, Update, Delete, and Select operations",
        "Always use WHERE clauses in UPDATE and DELETE operations",
        "Stored procedures encapsulate complex logic and improve performance",
        "Implement proper error handling for database operations",
        "Use connection pooling for better performance in high-volume scenarios"
    ])
    
    st.markdown("---")
    
    st.markdown("## ⏭️ What's Next?")
    st.info("""
    In **Module 7**, you'll learn about:
    - SOAP vs REST web services
    - Creating SOAP and REST connections
    - Oracle Fusion API integration
    - Purchase order creation via APIs
    
    Continue to Module 7! 👉
    """)
    
    with st.expander("📺 Video References"):
        for day in range(18, 21):
            st.markdown(f"📺 **Day {day}** - [View on YouTube](https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN)")
