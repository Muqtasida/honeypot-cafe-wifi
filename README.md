Here's the revised version with bullets added to the subpoints:

---

# Honeypot for Café Wi-Fi: A Decoy-Based Cybersecurity Model☕️🔒

📌 **Project Overview**:
The goal of this research is to study how honeypots can be deployed in public café Wi-Fi networks to log and observe potential attacker behavior without harming real users or systems.

A simple Python-based honeypot was designed to simulate a service running on port 8000. When a connection is made, the honeypot logs the IP address, time, and basic request data.

We submitted this as a research paper and presentation. The tool is included as a code sample and can be run if requested.

---

💡 **Key Features:**

* **Simulated Service**

  * Runs on port 8000 to mimic a vulnerable service.
* **Connection Logging**

  * Records IP addresses, timestamps, and basic request data for every connection attempt.
* **Real-Time Detection**

  * Instantly logs and flags unauthorized attempts to access the system.

---

📁 **Files Included**

* **research\_paper.pdf** - Full research paper
* **presentation.pptx** - PowerPoint presentation of the project
* **src/honeypot.py** - Python code for the honeypot
* **README.md** - This file
* **LICENSE** - License information
* **demo\_video\_link.txt** - Link to the demo video showcasing the tool in action

---

💡 **How the Tool Works**:
The honeypot runs locally and logs incoming TCP connections. A test was performed by accessing the service via [http://localhost:8000](http://localhost:8000), which generated a log entry.

---

🔒 **Sample log entry:**

```
[2025-05-11 08:07:13] Connection from 127.0.0.1 - Data: GET / HTTP/1.1
```

---

🙋‍♀️ **Authors**

* **Shaikh Muqtasida**
* **Arya Gawit**
  Developed as part of the **DigiSuraksha Cybersecurity Internship 2025**

---

