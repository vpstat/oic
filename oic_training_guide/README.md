# OIC Gen 3 Training Guide - Streamlit Application

A comprehensive, interactive training guide for Oracle Integration Cloud (OIC) Generation 3, based on a complete 26-day training series.

## 📚 Overview

This Streamlit application provides an organized, interactive learning experience for OIC Gen 3, covering everything from basic concepts to advanced enterprise patterns.

### Features

- **8 Comprehensive Modules** covering 26 days of training content
- **Interactive Navigation** with sidebar menu
- **Code Examples** with syntax highlighting
- **Visual Diagrams** using Mermaid
- **Hands-on Exercises** for practical learning
- **Best Practices** and tips throughout
- **Video References** to original training series

### Module Structure

1. **Getting Started** (Days 1-2) - Introduction to OIC Gen 3
2. **Core Integration Concepts** (Days 3-7) - Fundamentals and patterns
3. **Integration Management** (Days 8-10) - Versioning and monitoring
4. **Advanced Features** (Days 11-13) - Global variables and fault handling
5. **File Operations** (Days 14-17) - Stage File and FTP
6. **Database Integration** (Days 18-20) - ATP and database operations
7. **Web Services & APIs** (Days 21-23) - SOAP, REST, and Fusion APIs
8. **Enterprise Patterns** (Days 24-26) - FBDI, callbacks, and BIP reports

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**

```bash
cd oic_training_guide
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
streamlit run app.py
```

4. **Open your browser**

The application will automatically open at `http://localhost:8501`

## 📖 Usage

### Navigation

- Use the **sidebar** to select different modules
- Click on **module titles** to expand/collapse content
- Use **exercises** to practice concepts
- Refer to **video references** for detailed demonstrations

### Learning Path

**For Beginners:**
1. Start with Module 1: Getting Started
2. Progress through modules sequentially
3. Complete exercises in each module
4. Review Resources section for additional materials

**For Experienced Users:**
- Jump to specific modules based on your needs
- Use as a reference guide
- Focus on advanced modules (4-8)

## 🎯 What You'll Learn

### Fundamentals
- OIC Gen 3 architecture and UI
- Creating and managing integrations
- Working with connections and adapters
- Data mapping and transformations
- Monitoring and troubleshooting

### Advanced Topics
- Fault handling and error management
- File processing and FTP operations
- Database integrations with ATP
- SOAP and REST web services
- Enterprise patterns (FBDI, callbacks)

## 📁 Project Structure

```
oic_training_guide/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── modules/                    # Module content files
│   ├── __init__.py
│   ├── module_1_getting_started.py
│   ├── module_2_core_concepts.py
│   ├── module_3_management.py
│   ├── module_4_advanced.py
│   ├── module_5_file_ops.py
│   ├── module_6_database.py
│   ├── module_7_web_services.py
│   └── module_8_enterprise.py
├── utils/                      # Utility functions
│   ├── __init__.py
│   ├── helpers.py             # UI helper functions
│   └── diagrams.py            # Mermaid diagram templates
└── assets/                     # Static assets (if needed)
```

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Deploy your app by selecting the repository
5. Share the generated URL

### Local Deployment

Run locally for offline access:

```bash
streamlit run app.py --server.port 8501
```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:

```bash
docker build -t oic-training-guide .
docker run -p 8501:8501 oic-training-guide
```

## 🎥 Video Training Series

This guide is based on the comprehensive OIC Gen 3 Training Series:
- [YouTube Playlist](https://www.youtube.com/playlist?list=PL3X62LScvI_Jv63W_k8PG0Chfzr4n_QEN)
- 26 detailed training sessions
- Beginner to advanced topics
- Hands-on demonstrations

## 📚 Additional Resources

- [Oracle Integration Cloud Documentation](https://docs.oracle.com/en/cloud/paas/integration-cloud/)
- [OIC Gen 3 Release Notes](https://docs.oracle.com/en/cloud/paas/integration-cloud/whats-new/)
- [Oracle Learning Library](https://apexapps.oracle.com/pls/apex/f?p=44785:1)
- [Oracle Cloud Customer Connect](https://cloudcustomerconnect.oracle.com/)

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this training guide:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This training guide is provided as-is for educational purposes.

## 🙏 Acknowledgments

- Based on the OIC Gen 3 Training Series
- Oracle Integration Cloud documentation
- Oracle Cloud community

## 📧 Support

For questions or issues:
- Check the Resources section in the app
- Refer to Oracle documentation
- Join Oracle Cloud communities

---

**Happy Learning! 🚀**

Start your OIC Gen 3 journey today and become an integration expert!
