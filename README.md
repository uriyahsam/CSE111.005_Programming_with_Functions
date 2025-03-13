# CSE111.005 - Programming with Functions

## 📌 Overview
This repository contains my coursework for **CSE111.005 - Programming with Functions** at **BYU-Idaho**.  
It includes all activities, tests, and projects completed throughout the course.

---

## 📅 Course Content
Each week covers key programming concepts related to Python functions:

- **Week 01** - 🖥️ Python Review & Calling Functions  
- **Week 02** - ✍️ Writing Functions  
- **Week 03** - 🔍 Testing and Fixing Functions  
- **Week 04** - 📋 Lists and Dictionaries  
- **Week 05** - 📂 Text Files and Exceptions  
- **Week 06** - 🎭 Objects and Programming Project  
- **Week 07** - 🏆 Student Project  

---

## 🚀 Projects and Milestones
Each project builds on core programming skills.

### **🛞 Week 01**
- ✅ **W01 Project Milestone: Tire Volume**  
  _Initial step towards calculating tire volume._  
- ✅ **W01 Project: Tire Volume**  
  _A program that calculates the volume of a tire based on user input._  

### **📝 Week 02**
- ✅ **W02 Project Milestone: Writing Functions**  
  _Basic function writing exercises._  
- ✅ **W02 Project: Sentences**  
  _A program that generates sentences using functions._  

### **💦 Week 03**
- ✅ **W03 Project Milestone: Water Pressure**  
  _Early implementation of water pressure calculations._  
- ✅ **W03 Project: Water Pressure**  
  _A program that calculates water pressure at different depths._  

### **🔬 Week 04**
- ✅ **W04 Project Milestone: Chemistry**  
  _Introductory work on chemical element data processing._  
- ✅ **W04 Project: Chemistry**  
  _A program that retrieves and displays information about chemical elements._  

### **🛒 Week 05**
- ✅ **W05 Project Milestone: Grocery Store**  
  _The foundation of a grocery store inventory system._  
- ✅ **W05 Project: Grocery Store**  
  _A program that manages grocery store products and prices._  
- ✅ **W05 Assignment: Final Project Proposal**  
  _Proposal for the final project: Website Vulnerability Scanner._  

---

## 🛡️ **Final Project: Website Vulnerability Scanner**
### **🔍 Problem Statement**
Many websites have security vulnerabilities due to misconfigured headers, open ports, weak SSL settings, or outdated server software. This program helps identify such weaknesses by scanning websites and providing security insights.

### **🧑‍💻 What I Learned**
- Understanding **security headers** and their role in website protection.
- Performing **basic port scanning** using Python.
- Evaluating **SSL/TLS configurations** for security risks.
- Using **Python libraries** like `requests`, `socket`, and `ssl` for security analysis.
- Writing and running **test cases** with `pytest`.

### **📦 Python Modules Used**
- `requests` → For making HTTP requests  
- `socket` → For checking open ports  
- `ssl` → For analyzing SSL certificates  
- `bs4` (BeautifulSoup) → For parsing HTML  
- `pytest` → For testing functions  

### **⚙️ Functions Implemented**
```python
def check_headers(url):
    """Checks the security headers of a given website."""
    
def port_scan(domain, ports=[80, 443, 22, 21, 25]):
    """Scans common ports to detect open ones."""
    
def ssl_check(domain):
    """Evaluates SSL/TLS security settings."""
    
def get_server_info(url):
    """Retrieves and analyzes the server details."""
    
def run_scan(url):
    """Performs a full security scan on a website."""


✅ Test Functions

def test_check_headers():
    """Tests if the function correctly identifies security headers."""
    
def test_port_scan():
    """Tests the port scanning function with a predefined test server."""
    
def test_ssl_check():
    """Tests if SSL analysis returns expected results."""

🔧 How to Run the Scanner

1. **Clone this repository** to your local machine:  
   ```bash
   git clone https://github.com/uriyahsam/CSE111.005_Programming_with_Functions.git

2. **Navigate to the final project directory.**

3. **Run the scanner script:**
   ```bash
   python website_vulnerability_scanner.py

4. **Enter a website URL when prompted.**

5. **Review the security insights provided.**

📬 Contact
If you have any questions or suggestions, feel free to reach out! 😊