"""Mermaid diagram templates for OIC Training Guide."""

def integration_flow_diagram():
    """Basic integration flow diagram."""
    return """
    graph LR
        A[Source System] -->|Trigger| B[OIC Integration]
        B -->|Transform| C[Data Mapping]
        C -->|Send| D[Target System]
        B -->|Error| E[Fault Handler]
        E -->|Notify| F[Admin]
    """

def oic_architecture_diagram():
    """OIC Gen 3 architecture overview."""
    return """
    graph TB
        A[Client Applications] --> B[OIC Gen 3]
        B --> C[Connections]
        B --> D[Integrations]
        B --> E[Lookups]
        B --> F[Libraries]
        C --> G[REST APIs]
        C --> H[SOAP Services]
        C --> I[Databases]
        C --> J[File Servers]
        D --> K[Scheduled]
        D --> L[App-Driven]
        D --> M[Event-Driven]
    """

def rest_integration_pattern():
    """REST integration pattern."""
    return """
    sequenceDiagram
        participant Client
        participant OIC
        participant REST API
        Client->>OIC: HTTP Request
        OIC->>OIC: Validate & Transform
        OIC->>REST API: API Call
        REST API-->>OIC: Response
        OIC->>OIC: Map Response
        OIC-->>Client: Formatted Response
    """

def scheduled_integration_pattern():
    """Scheduled integration pattern."""
    return """
    graph LR
        A[Schedule Trigger] -->|Start| B[OIC Integration]
        B -->|Read| C[Source Data]
        C -->|Process| D[Transform]
        D -->|Write| E[Target System]
        E -->|Complete| F[Log Status]
    """

def fault_handling_flow():
    """Fault handling flow diagram."""
    return """
    graph TD
        A[Integration Execution] -->|Success| B[Complete]
        A -->|Error| C{Error Type}
        C -->|Retriable| D[Retry Logic]
        C -->|Non-Retriable| E[Fault Handler]
        D -->|Max Retries| E
        D -->|Success| B
        E -->|Log| F[Error Tracking]
        E -->|Notify| G[Alert Admin]
    """

def file_processing_flow():
    """File processing flow with Stage File action."""
    return """
    graph LR
        A[FTP Server] -->|Read| B[Stage File]
        B -->|List Files| C[Process Each]
        C -->|Read Content| D[Transform]
        D -->|Write| E[Target System]
        E -->|Archive| F[Processed Folder]
    """

def database_integration_flow():
    """Database integration pattern."""
    return """
    graph TB
        A[Trigger] --> B[OIC Integration]
        B --> C{Operation Type}
        C -->|Insert| D[Insert Records]
        C -->|Update| E[Update Records]
        C -->|Invoke| F[Stored Procedure]
        D --> G[Commit]
        E --> G
        F --> G
        G --> H[Return Status]
    """

def fbdi_pattern():
    """FBDI (File-Based Data Import) pattern."""
    return """
    graph LR
        A[Source Data] -->|Generate| B[CSV File]
        B -->|Create| C[ZIP Archive]
        C -->|Upload| D[UCM Server]
        D -->|Submit| E[ESS Job]
        E -->|Process| F[Import to Fusion]
        F -->|Status| G[Monitor Job]
    """
