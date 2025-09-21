# 📄 **Finfelo – MVP Scope Document**

**Document Owner:** Product Manager
**Version:** 1.0
**Date:** 2025-09-21

---

## 1️⃣ **Purpose**

The purpose of this document is to define the **minimum set of features, workflows, and functionality** required to launch the Finfelo MVP. This ensures a **focused release** that delivers core value to Chartered Accountants while reducing complexity and risk.

---

## 2️⃣ **MVP Objectives**

* Provide CAs with a **unified client workspace**.
* Enable **efficient management of multiple clients**.
* Automate **ITR computation and document generation**.
* Offer a **context-aware AI assistant** for workflow automation and financial insights.
* Deliver a **clean, distraction-free UI** similar to the experience of Cursor for coding.

---

## 3️⃣ **In-Scope Features**

### **3.1 Client Workflow**

* Create, view, edit, delete clients
* Search/filter clients in the dashboard
* Display client summary and status

### **3.2 Client Workspace**

* Left Sidebar → File tree (PDF, CSV, XLSX, TXT)
* Center Pane → Multi-document viewer
* Right Sidebar → AI chat assistant (context-aware per client)
* File upload/download and organization

### **3.3 AI Assistant**

* Compute ITR from uploaded documents
* Generate financial statements and pre-filled ITR forms
* Provide insights on client data
* Maintain chat history per client

### **3.4 ITR Computation**

* Support ITR 1 / ITR 2 forms
* Calculate taxable income, deductions, and taxes owed
* Generate downloadable PDF/Excel summaries
* Validate uploaded documents for required fields

---

## 4️⃣ **Out-of-Scope (For MVP)**

* GST filing automation
* Client self-service portal
* E-signature integration
* Tally/QuickBooks or other accounting system integrations
* Mobile app version
* Advanced predictive analytics or regulatory alerts

---

## 5️⃣ **MVP Constraints**

* Focus on **desktop/web interface** only
* Support for **Indian tax rules only** in MVP
* Max concurrent users for MVP: \~500
* AI assistant handles **one client context at a time**

---

## 6️⃣ **Success Criteria**

* > 80% of CA users can onboard and manage 5+ clients without support
* AI assistant performs computations correctly ≥ 95% of the time
* User is able to generate and download ITR and financial statements without errors
* File management and workspace interactions are **fast and reliable**

---

## 7️⃣ **Assumptions**

* Users have basic CA knowledge
* Users provide accurate input documents for computation
* AI assistant will require curated prompt engineering for accurate computations
* MVP release will gather feedback for future features

---

## 8️⃣ **Future Considerations (Post-MVP)**

* Expand AI capabilities to predictive suggestions and compliance alerts
* Mobile-first version for on-the-go CAs
* Client self-service portal
* Integration with accounting platforms like Tally, QuickBooks, Zoho Books
* Multi-language support for Indian regional languages

---
