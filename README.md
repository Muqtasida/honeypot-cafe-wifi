Honeypot for Café Wi-Fi
This is a cybersecurity research project developed during the DigiSuraksha Cybersecurity Internship, conducted by Shaikh Muqtasida and Arya Gawit.

📌 Project Overview
The goal of this research is to study how honeypots can be deployed in public café Wi-Fi networks to log and observe potential attacker behavior without harming real users or systems.

A simple Python-based honeypot was designed to simulate a service running on port 8000. When a connection is made, the honeypot logs the IP address, time, and basic request data.

We submitted this as a research paper and presentation. The tool is included as a code sample and can be run if requested.

📁 Files Included
research_paper.docx

presentation.pptx

src/honeypot.py

README.md

LICENSE

demo_video_link.txt

💡 How the Tool Works 
The honeypot runs locally and logs incoming TCP connections. A test was performed by accessing the service via http://localhost:8000, which generated a log entry.

Sample log entry:
[2025-05-11 08:07:13] Connection from 127.0.0.1 - Data: GET / HTTP/1.1

🙋‍♀️ Authors
Shaikh Muqtasida
Arya Gawit