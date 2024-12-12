# Flask Vulnerability Demo with CodeQL Analysis

This repository demonstrates a simple Flask application with intentional security vulnerabilities. It is set up to run a **CodeQL** security scan via GitHub Actions to detect and analyze common vulnerabilities like **SQL Injection**, **Cross-Site Scripting (XSS)**, and **Insecure File Handling**.

## Vulnerabilities Introduced

### 1. **SQL Injection**
In the `/search` route, user input is directly inserted into an SQL query without proper sanitization, making it vulnerable to SQL injection attacks.

### 2. **Cross-Site Scripting (XSS)**
In the `/greet` route, user input is returned in the response without escaping, which could lead to XSS vulnerabilities where malicious scripts could be executed in the user's browser.

### 3. **Insecure File Handling**
In the `/write` route, user input is written directly to a file (`user_data.txt`) without validation or sanitization, allowing arbitrary data to be written to the server.

## CodeQL Analysis with GitHub Actions

### GitHub Actions Workflow

This repository includes a GitHub Actions workflow that runs **CodeQL analysis** on the codebase. The workflow will automatically run every time changes are pushed to the `main` branch or a pull request is created. The CodeQL analysis detects potential vulnerabilities in the Python code, including the ones mentioned above.

### How to Trigger CodeQL Analysis

1. **Push Code to GitHub**: Every time you push changes to the repository or create a pull request, the CodeQL analysis will be triggered.
2. **View Analysis Results**: After the analysis runs, the results will be available in the **Security** tab of your GitHub repository, where you can view the detected vulnerabilities.

## How to Run the Application Locally

### Prerequisites

- Python 3.x
- Flask
- SQLite3 (or any compatible database for SQL queries)

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
