# Feature Requests – Finfelo MVP

This document captures all feature ideas and requests for the **Finfelo platform**, prioritized based on **impact, effort, and alignment with the MVP vision**. It distinguishes between **MVP-critical features** and **post-MVP enhancements**.

---

## ✅ Core MVP Features

### 1. Client Management
**Purpose:** Enable CAs to manage multiple clients efficiently.

- **Add / Create Client**  
  Capture essential client information (individual or organization) to start managing documents and workflows.
- **View Client**  
  Dashboard overview of client summary, status, and recent activity.
- **Edit Client**  
  Update client details to ensure information remains current.
- **Delete Client**  
  Remove inactive clients; all workspace data should be securely deleted.
- **Search & Filter Clients**  
  Quickly locate clients by name, ID, type, or last activity.

---

### 2. Client Workspace
**Purpose:** Provide a unified, context-aware workspace per client.

- **File Tree Sidebar (Left Pane)**  
  Organize all client documents (PDF, CSV, Excel, TXT) with folders and tags.
- **Document Viewer (Center Pane)**  
  View multiple document types inline without switching applications.
- **AI Chat Sidebar (Right Pane)**  
  Interact with AI to:
  - Perform computations (e.g., ITR, financial summaries)  
  - Generate documents and templates (pre-filled ITR, statements, NDAs)  
  - Provide insights and contextual recommendations
- **File Upload / Download**  
  Add new files or retrieve existing ones easily.
- **File Organization & Tagging**  
  Keep client documents structured and searchable.

---

### 3. Computation & Automation
**Purpose:** Reduce manual effort and improve accuracy in client servicing.

- **ITR Computation**  
  Automatically calculate taxable income, deductions, and taxes owed.
- **Document Generation**  
  Pre-fill ITR forms and other templates based on uploaded client files.
- **Audit Trail / Versioning**  
  Track edits, uploads, and deletions for compliance and review.

---

## 🕐 Post-MVP / Nice-to-Have Features
**Purpose:** Enhance platform productivity and scalability for future releases.

- E-signature integration for NDAs and engagement letters  
- Client self-service portal for document submission and status tracking  
- Integration with accounting platforms (Tally, QuickBooks, Xero)  
- Predictive suggestions for filing and document generation  
- Regulatory alerts and compliance reminders

---

## 💡 Design & Operational Notes

- All features are **client-context aware**; AI should operate strictly within the selected client workspace.  
- UI should remain **minimal, fast, and distraction-free**, inspired by Cursor.  
- Document generation must allow **review and edits** before final download.  
- Audit and logging mechanisms are critical for both **compliance** and **debugging**.  
- MVP should focus on **core workflows**; all post-MVP features are deferred until stable adoption.

---

