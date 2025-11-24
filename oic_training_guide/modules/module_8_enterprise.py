"""Module 8: Enterprise Patterns"""

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
from utils.diagrams import *

def render():
    """Render Module 8 content."""
    
    render_header(
        "Module 8: Enterprise Patterns",
        "Days 24-26 | Advanced enterprise integration patterns"
    )
    
    render_module_info(
        module_num=8,
        title="Enterprise Patterns",
        duration="~6 hours",
        topics=[
            "FBDI (File-Based Data Import)",
            "Bulk data loading",
            "Callback integrations",
            "BIP reports integration"
        ]
    )
    
    # Day 24
    st.markdown("## 📅 Day 24: Deep Dive into Purchase Order FBDI")
    
    st.markdown("""
    ### What is FBDI?
    
    **File-Based Data Import (FBDI)** is Oracle Fusion's mechanism for bulk data loading:
    
    **Key Characteristics:**
    - CSV file-based import
    - Handles large data volumes
    - Asynchronous processing
    - Validation and error reporting
    - Supports all Fusion modules
    """)
    
    st.markdown("```mermaid\n" + fbdi_pattern() + "\n```")
    
    st.markdown("""
    ### FBDI vs API: When to Use Each
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Use FBDI When:**
        - Loading large volumes (1000+ records)
        - Initial data migration
        - Batch processing acceptable
        - Complex data relationships
        - Historical data import
        """)
    
    with col2:
        st.markdown("""
        **Use API When:**
        - Real-time processing needed
        - Small transaction volumes
        - Immediate validation required
        - Synchronous response needed
        - Simple data structures
        """)
    
    st.markdown("""
    ### FBDI Process Overview
    
    **Steps:**
    1. Generate CSV file with required format
    2. Create ZIP archive
    3. Upload to UCM (Universal Content Management)
    4. Submit ESS (Enterprise Scheduler Service) job
    5. Monitor job status
    6. Download error report if needed
    """)
    
    render_code_example(
        title="Purchase Order FBDI CSV Format",
        code='''POHeadersInterface.csv:
INTERFACE_HEADER_KEY,ACTION,BATCH_ID,DOCUMENT_NUM,CURRENCY_CODE,BUYER_ID,VENDOR_ID,VENDOR_SITE_ID
1,ORIGINAL,BATCH001,PO-001,USD,100010004471139,300000047414679,300000047414680

POLinesInterface.csv:
INTERFACE_LINE_KEY,INTERFACE_HEADER_KEY,LINE_NUM,ITEM_DESCRIPTION,QUANTITY,UNIT_PRICE,UOM_CODE
1,1,1,Laptop Computer,10,1200.00,Ea
2,1,2,Mouse,10,25.00,Ea

PODistributionsInterface.csv:
INTERFACE_DISTRIBUTION_KEY,INTERFACE_LINE_KEY,DISTRIBUTION_NUM,QUANTITY,CHARGE_ACCOUNT_ID
1,1,1,10,300000047414681
2,2,1,10,300000047414681''',
        language="csv"
    )
    
    st.markdown("---")
    
    # Day 25
    st.markdown("## 📅 Day 25: Bulk Load Purchase Orders Using FBDI")
    
    st.markdown("""
    ### Complete FBDI Integration
    
    **Integration Components:**
    """)
    
    render_key_points([
        "**Data Transformation**: Convert source data to FBDI CSV format",
        "**File Generation**: Create CSV files for headers, lines, distributions",
        "**ZIP Creation**: Package CSV files into ZIP archive",
        "**UCM Upload**: Upload ZIP to Oracle Content Management",
        "**ESS Job Submission**: Trigger import job",
        "**Status Monitoring**: Poll job status until complete",
        "**Error Handling**: Download and process error reports"
    ])
    
    render_code_example(
        title="ESS Job Submission",
        code='''// Submit FBDI Import Job
Job Name: oracle/apps/ess/projects/po/import/ImportPurchaseOrders
Parameters:
  - ImportType: ORIGINAL
  - BatchId: BATCH001
  - DocumentNumber: null (import all)
  - CreateOrUpdateItems: false
  - CreateSourcedAttribute: false

// Response
{
  "requestId": "123456789",
  "status": "RUNNING"
}

// Poll for status
GET /fscmRestApi/resources/11.13.18.05/erpintegrations/{requestId}

// Final status
{
  "requestId": "123456789",
  "status": "SUCCEEDED",
  "processedRecords": 100,
  "errorRecords": 0
}''',
        language="json"
    )
    
    render_exercise(
        title="Build FBDI Integration",
        description="Create end-to-end FBDI integration for Purchase Orders",
        steps=[
            "Create scheduled integration",
            "Read source data (database/file/API)",
            "Transform to FBDI CSV format",
            "Generate CSV files for headers, lines, distributions",
            "Create ZIP archive with all CSV files",
            "Upload ZIP to UCM",
            "Submit ESS import job",
            "Poll job status (with timeout)",
            "Download error report if job fails",
            "Send notification with results"
        ]
    )
    
    st.markdown("---")
    
    # Day 26
    st.markdown("## 📅 Day 26: Callback Integrations & BIP Reports")
    
    st.markdown("""
    ### Callback Integrations
    
    **Callback Pattern**: Asynchronous request-response pattern
    
    **Use Cases:**
    - Long-running processes
    - External system notifications
    - Event-driven workflows
    """)
    
    render_code_example(
        title="Callback Pattern Flow",
        code='''1. Client submits request to OIC
   POST /api/processOrder
   Response: { "requestId": "REQ-12345", "status": "PROCESSING" }

2. OIC processes asynchronously
   - Validate data
   - Call external systems
   - Perform transformations

3. OIC calls back to client when complete
   POST {callbackUrl}
   Body: {
     "requestId": "REQ-12345",
     "status": "COMPLETED",
     "result": {...}
   }

4. Client receives notification and retrieves results''',
        language="text"
    )
    
    st.markdown("""
    ### BIP Reports Integration
    
    **Business Intelligence Publisher (BIP)** generates reports in Oracle Fusion:
    
    **Integration Capabilities:**
    - Run BIP reports from OIC
    - Pass parameters to reports
    - Retrieve report output (PDF, Excel, CSV)
    - Schedule report generation
    - Email reports to users
    """)
    
    render_code_example(
        title="BIP Report Invocation",
        code='''// Run BIP Report
POST /xmlpserver/services/ExternalReportWSSService

SOAP Request:
<runReport>
  <reportRequest>
    <attributeFormat>pdf</attributeFormat>
    <reportAbsolutePath>/Custom/PurchaseOrderReport.xdo</reportAbsolutePath>
    <sizeOfDataChunkDownload>-1</sizeOfDataChunkDownload>
    <parameterNameValues>
      <item>
        <name>P_PO_NUMBER</name>
        <values>
          <item>PO-2024-001234</item>
        </values>
      </item>
    </parameterNameValues>
  </reportRequest>
</runReport>

// Response includes base64-encoded PDF
<reportBytes>JVBERi0xLjQKJeLjz9MKMy...</reportBytes>''',
        language="xml"
    )
    
    render_best_practice(
        "For large reports, use asynchronous pattern: submit report job, poll for completion, then download. This prevents timeout issues."
    )
    
    st.markdown("---")
    
    # Key Takeaways
    st.markdown("## 🎯 Key Takeaways")
    
    render_key_points([
        "FBDI is the preferred method for bulk data loading into Oracle Fusion",
        "FBDI uses CSV files uploaded to UCM and processed by ESS jobs",
        "Always validate FBDI files before upload to catch errors early",
        "Callback pattern enables asynchronous processing for long-running operations",
        "BIP reports can be generated and retrieved programmatically from OIC",
        "Monitor ESS job status and handle errors appropriately"
    ])
    
    st.markdown("---")
    
    # Course Completion
    st.markdown("## 🎉 Congratulations!")
    
    st.success("""
    **You've completed all 8 modules of the OIC Gen 3 Training Guide!**
    
    You now have comprehensive knowledge of:
    - OIC Gen 3 fundamentals and architecture
    - Integration patterns and best practices
    - File and database operations
    - Web services and API integration
    - Enterprise patterns like FBDI and callbacks
    
    **Next Steps:**
    - Practice building integrations in your OIC instance
    - Explore the Resources section for additional learning
    - Join Oracle Cloud communities for support
    - Stay updated with new OIC features and capabilities
    """)
    
    st.markdown("---")
    
    st.markdown("## 📚 Additional Resources")
    st.info("""
    - Review earlier modules as needed
    - Check the Resources page for documentation links
    - Watch the original video series for demonstrations
    - Practice with real-world integration scenarios
    """)
    
    with st.expander("📺 Video References"):
        for day in range(24, 27):
            st.markdown(f"📺 **Day {day}** - [View on YouTube](https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN)")
