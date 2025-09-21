# 📄 **Finfelo – Product Feature Specification Document (PFSD) – MVP**

**Document Owner:** Product Manager
**Version:** 1.0
**Date:** 2025-09-21
**Scope:** MVP – focused on client management, workspace, AI assistant, and ITR computation

---

## 1️⃣ **Feature Overview**

| Feature                  | Description                                                                                   |
| ------------------------ | --------------------------------------------------------------------------------------------- |
| **Client Workflow**      | Create, view, edit, delete clients; search/filter dashboard                                   |
| **Client Workspace**     | Multi-pane workspace: left sidebar (files), center (document viewer), right sidebar (AI chat) |
| **AI Assistant Sidebar** | Context-aware AI chat for computations, document generation, and insights                     |
| **ITR Computation**      | Automatic calculation of taxable income, deductions, and pre-filling ITR forms                |

---

## 2️⃣ **Feature Details**

### 2.1 Client Workflow

**Objective:** Enable CA users to manage multiple clients efficiently.

**User Stories:**

* As a CA, I want to create a client so I can start managing their documents.
* As a CA, I want to edit client details so I can keep information up-to-date.
* As a CA, I want to delete clients I no longer serve.
* As a CA, I want to search/filter clients so I can quickly find them.

**UI Elements:**

* **Client Dashboard:** Table/grid view of clients
* **Buttons:** Add Client, Edit, Delete
* **Search Bar / Filters**: By name, client type, last activity

**Acceptance Criteria:**

1. CA can create a client with mandatory fields (name, type, ID).
2. Dashboard lists all clients with pagination.
3. Search/filter returns correct results.
4. Edit and delete operations are logged in audit trail.

---

### 2.2 Client Workspace

**Objective:** Provide a unified workspace for each client.

**User Stories:**

* As a CA, I want a **file tree** to organize documents.
* As a CA, I want a **document viewer** to open multiple document types.
* As a CA, I want a **AI chat sidebar** to perform computations on selected files.

**UI Layout:**

```
+------------------+-------------------+------------------+
| Left Sidebar     | Center Document   | Right Sidebar    |
| (File Tree)      | Viewer (PDF/CSV) | AI Chat/Assistant|
+------------------+-------------------+------------------+
```

**Functional Requirements:**

* Upload/download documents in various formats (PDF, CSV, Excel, TXT).
* File organization via folders/tags.
* Center pane supports viewing multiple formats; inline rendering where possible.
* Right sidebar AI is **context-aware** to current client and selected file(s).

**Acceptance Criteria:**

1. Clicking a file opens it in the center viewer.
2. Uploaded files appear immediately in the file tree.
3. AI chat is always aware of current workspace context.

---

### 2.3 AI Assistant Sidebar

**Objective:** Help CAs automate computations, generate documents, and provide insights.

**User Stories:**

* As a CA, I want to ask AI to compute taxable income from uploaded files.
* As a CA, I want AI to generate ITR documents and financial statements.
* As a CA, I want AI to answer questions about client data.

**Functional Requirements:**

* AI receives context: selected client + selected file(s)
* Supports commands such as:

  * “Compute total taxable income”
  * “Generate ITR form pre-filled”
  * “Summarize client financials”
* AI responses are **actionable**: allow export, download, or insert into workspace

**Acceptance Criteria:**

1. AI correctly uses the client’s context and files.
2. Output documents are downloadable in standard formats.
3. AI chat retains history per client.

---

### 2.4 ITR Computation

**Objective:** Automate Indian tax computation workflows.

**User Stories:**

* As a CA, I want to compute ITR automatically to save time.
* As a CA, I want pre-filled ITR forms ready for submission.

**Functional Requirements:**

* Support ITR 1 / ITR 2 (initial MVP scope)
* Compute taxable income, deductions, and taxes owed
* Validate uploaded client documents for necessary fields
* Generate pre-filled ITR PDF and Excel summaries

**Acceptance Criteria:**

1. Computation results match manual calculations.
2. Generated ITR can be reviewed before submission.
3. AI can explain how numbers were computed on request.

---

## 3️⃣ **Technical Notes / Considerations**

* **File Storage:** Per-client isolated storage (cloud/DB)
* **Security:** End-to-end encryption, role-based access
* **AI Engine:** GPT-style LLM fine-tuned or prompt-engineered for CA context
* **Frontend:** React/Next.js (for SPA experience, multi-pane layout)
* **Backend:** Node.js/Express or Python FastAPI for API layer
* **Data Format:** PDF, CSV, XLSX, TXT supported in workspace

---

## 4️⃣ **Dependencies**

* Income Tax API (for validation)
* File viewer libraries for multi-format rendering
* AI engine (LLM with secure prompt context)
* User authentication & RBAC module

---

## 5️⃣ **MVP Scope Boundaries**

**In-Scope:**

* Client workflow (CRUD)
* Multi-pane client workspace
* AI chat for computations and document generation
* ITR computation & template generation

**Out-of-Scope (for future releases):**

* GST filing automation
* Client self-service portal
* E-signature integrations
* Integration with accounting software

---

## 6️⃣ **Success Metrics**

* > 80% of users successfully create/manage 5+ clients within first week
* AI chat usage per client > 3 interactions per week
* ITR computation correctness > 95% against manual calculation
* File uploads/downloads work seamlessly for supported formats

---

## 7️⃣ **Wireframes / Mockups (Optional)**

* Multi-pane layout with left file tree, center document viewer, right AI chat
* Client dashboard showing list of clients and action buttons
* AI chat modal for generating computations/documents

---
