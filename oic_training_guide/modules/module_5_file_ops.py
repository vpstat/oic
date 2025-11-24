"""Module 5: File Operations"""

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils.helpers import *
from utils.diagrams import *

def render():
    """Render Module 5 content."""
    
    render_header(
        "Module 5: File Operations",
        "Days 14-17 | Master file processing with Stage File and FTP"
    )
    
    render_module_info(
        module_num=5,
        title="File Operations",
        duration="~8 hours",
        topics=[
            "Stage File action (3-day deep dive)",
            "FTP adapter and connections",
            "File reading and writing",
            "File archiving and management"
        ]
    )
    
    # Days 14-16: Stage File
    st.markdown("## 📅 Days 14-16: Introduction to Stage File Action")
    
    st.markdown("""
    ### What is Stage File?
    
    The **Stage File** action provides temporary file storage during integration execution:
    
    **Key Capabilities:**
    - Read files from external sources
    - Write files to external targets
    - List files in directories
    - Zip/Unzip files
    - Delete files after processing
    """)
    
    st.markdown("```mermaid\n" + file_processing_flow() + "\n```")
    
    st.markdown("""
    ### Stage File Operations
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Read Operations:**
        - Read File
        - Read File in Segments
        - List Files
        - Download File
        """)
    
    with col2:
        st.markdown("""
        **Write Operations:**
        - Write File
        - Append to File
        - Zip Files
        - Delete File
        """)
    
    render_code_example(
        title="Stage File - List Files Example",
        code='''Stage File Configuration:
Operation: List Files
Directory: /inbound/orders
File Pattern: *.csv
Include Subdirectories: No

Returns:
- File names
- File sizes
- Last modified timestamps

Use For-Each to process each file:
For-Each $file in $fileList
  Read File: $file.name
  Process content
  Archive to /processed/
  Delete from /inbound/''',
        language="text"
    )
    
    st.markdown("""
    ### Common File Processing Pattern
    """)
    
    render_exercise(
        title="Build a File Processing Integration",
        description="Process CSV files from FTP server",
        steps=[
            "Create scheduled integration",
            "Add FTP connection for source",
            "Use Stage File to list files (*.csv)",
            "Add For-Each loop for file list",
            "Read each file content",
            "Parse CSV data",
            "Process each record",
            "Archive processed files",
            "Delete from source directory"
        ]
    )
    
    render_tip(
        "Always archive processed files before deleting them. This provides an audit trail and recovery option if issues occur."
    )
    
    st.markdown("---")
    
    # Day 17: FTP Connection
    st.markdown("## 📅 Day 17: Introduction to FTP Connection")
    
    st.markdown("""
    ### FTP Adapter Overview
    
    The FTP adapter enables file transfer operations:
    
    **Supported Protocols:**
    - FTP (File Transfer Protocol)
    - FTPS (FTP over SSL/TLS)
    - SFTP (SSH File Transfer Protocol)
    """)
    
    render_code_example(
        title="FTP Connection Configuration",
        code='''Connection Type: FTP
FTP Server Host: ftp.example.com
Port: 22 (SFTP) or 21 (FTP)
Protocol: SFTP
Username: ftpuser
Authentication: Password / Private Key
Directory: /home/ftpuser/files''',
        language="text"
    )
    
    st.markdown("""
    ### FTP Operations
    
    **Available Operations:**
    """)
    
    render_key_points([
        "**List Files**: Get directory contents",
        "**Download File**: Read file from FTP server",
        "**Upload File**: Write file to FTP server",
        "**Delete File**: Remove file from server",
        "**Move File**: Relocate file on server"
    ])
    
    render_best_practice(
        "Use SFTP over FTP whenever possible for better security. SFTP encrypts both authentication and data transfer."
    )
    
    st.markdown("""
    ### File Processing Best Practices
    """)
    
    render_key_points([
        "Use file naming conventions with timestamps",
        "Implement file locking to prevent concurrent processing",
        "Archive processed files with retention policy",
        "Log all file operations for audit trail",
        "Handle large files with streaming or segmentation",
        "Implement error handling for file operations"
    ])
    
    render_code_example(
        title="File Naming Convention Example",
        code='''File naming pattern:
{type}_{environment}_{timestamp}_{sequence}.{ext}

Examples:
ORDER_PROD_20240124_153045_001.csv
INVOICE_TEST_20240124_153046_002.xml
CUSTOMER_PROD_20240124_153047_003.json

Benefits:
- Easy to sort chronologically
- Environment identification
- Unique sequence number
- Clear file type''',
        language="text"
    )
    
    st.markdown("---")
    
    # Key Takeaways
    st.markdown("## 🎯 Key Takeaways")
    
    render_key_points([
        "Stage File provides temporary storage for file operations",
        "Use List Files + For-Each pattern for batch file processing",
        "FTP adapter supports FTP, FTPS, and SFTP protocols",
        "Always archive files before deleting for audit purposes",
        "Implement proper error handling for file operations",
        "Use meaningful file naming conventions with timestamps"
    ])
    
    st.markdown("---")
    
    st.markdown("## ⏭️ What's Next?")
    st.info("""
    In **Module 6**, you'll learn about:
    - ATP (Autonomous Transaction Processing) database connections
    - Insert and update operations
    - Stored procedure invocations
    - Database integration patterns
    
    Continue to Module 6! 👉
    """)
    
    with st.expander("📺 Video References"):
        for day in range(14, 18):
            st.markdown(f"📺 **Day {day}** - [View on YouTube](https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN)")
