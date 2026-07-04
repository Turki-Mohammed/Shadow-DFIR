Shadow-DFIR-Analyzer

An automated Digital Forensics and Incident Response (DFIR) tool that leverages AI to analyze memory dumps. It extracts process lists using Volatility 3 and performs automated threat analysis via Gemini AI.

Features

Automated Memory Analysis: Extracts process data using Volatility 3.

AI-Powered Investigation: Uses Gemini AI to identify suspicious processes and potential threats.

Professional Reporting: Generates brief and actionable security reports.

Setup

Clone the repo: git clone https://github.com/Turki-Mohammed/Shadow-DFIR-Analyzer.git

Install dependencies: pip install -r volatility3 

Configure API: Create a .env file and add: GOOGLE_API_KEY=your_actual_key_here

Disclaimer

This tool is for educational and authorized forensic purposes only. Ensure you have the necessary permissions before analyzing any memory dumps
