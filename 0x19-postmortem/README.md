# Account Creation Failure

![Postmortem Img](account_creation_post_moterm.jpg)

## Issue Summary:
* **Duration of the Outage:** 48 hrs, from 06:00 AM, 19 January, - 06:00 AM, 21 January 2024 CAT
* **Impact:** Users experienced a complete inability to create new accounts during the outage, affecting 20% of the user base.
* **Root Cause:** Database connectivity issue due to a misconfigured firewall rule.

---

## Timeline:
* **19 January 2024:**
  - **06:00 AM:** Issue detected through a surge in customer complaints.
  - **06:15 AM:** Customer support escalates the issue to the engineering team.

* **Investigation:**
  - **06:30 AM:** Initial assumption made that the application servers might be overloaded.
  - **07:00 AM:** System logs reviewed, no indication of server overload.
  - **07:30 AM:** Escalation to the database team as the issue seems database-related.
  - **08:00 AM:** Database team investigates query performance, finds no anomalies.

* **Misleading Paths:**
  - **08:30 AM:** Consideration of a potential DDoS attack, leading to engagement with security team.
  - **09:00 AM:** Security team rules out DDoS, focus returns to database issues.

* **Escalation:**
  - **09:30 AM:** Escalation to network infrastructure team as the database team suspects network issues.
  - **10:00 AM:** Network team discovers a misconfigured firewall rule blocking database connections.

* **Resolution:**
  - **11:00 AM:** Firewall rule corrected, restoring database connectivity.
  - **11:30 AM:** Account creation service verified as operational.
  - **12:00 PM:** Public announcement of issue resolution.

---

## Root Cause and Resolution:
* **Root Cause:**
  - A misconfigured firewall rule was blocking incoming connections to the database servers, preventing account creation.

* **Resolution:**
  - The misconfigured firewall rule was corrected promptly by the network infrastructure team, restoring database connectivity and resolving the account creation issue.

---

## Corrective and Preventative Measures:
* **Improvements/Fixes:**
  - **Firewall Configuration Review:** Implement a regular review process for firewall rules to catch and rectify misconfigurations promptly.
  - **Monitoring Enhancement:** Enhance monitoring for database connectivity, ensuring early detection of similar issues in the future.
  - **Incident Response Training:** Provide additional training to the support and engineering teams on efficient incident response protocols.

* **Tasks to Address the Issue:**
  - **Automate Firewall Audits:** Develop scripts or tools to automate regular firewall audits, flagging potential misconfigurations.
  - **Enhance Monitoring Alerts:** Fine-tune monitoring systems to provide more specific alerts for database connectivity issues.
  - **Regular Simulation Exercises:** Conduct periodic simulation exercises to train teams in responding to different types of incidents effectively.

---

## Conclusion:
In conclusion, the 48-hour account creation outage stemmed from a misconfigured firewall rule blocking database connections. The incident detection and resolution timeline highlights the challenges in pinpointing the root cause and the importance of collaborative problem-solving across different teams. Implementing corrective measures, including automated firewall audits and enhanced monitoring, aims to prevent similar issues in the future, ensuring a more robust and resilient system.