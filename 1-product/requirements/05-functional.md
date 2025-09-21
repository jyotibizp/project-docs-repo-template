# Functional Requirements – Finfelo MVP

Defines the core functionality for development and QA teams.

---

## 1️⃣ Client Management

| Requirement | Description | Acceptance Criteria |
|------------|-------------|------------------|
| Add Client | Create a new client profile | Profile saved, appears in dashboard |
| Edit Client | Update client details | Changes persisted and audit logged |
| Delete Client | Remove client and workspace | All data removed, logged for audit |
| Search/Filter | Locate clients by name, type, or ID | Returns correct results within 2 seconds |

---

## 2️⃣ Client Workspace

| Requirement | Description | Acceptance Criteria |
|------------|-------------|------------------|
| File Tree Sidebar | Organize client files | Display uploaded files, support folders/tags |
| Document Viewer | Open multiple document types | PDF, CSV, XLSX, TXT supported, renders inline |
| File Upload/Download | Add or retrieve documents | Upload/download completes successfully; file stored securely |
| Workspace Context | AI and files isolated per client | AI only sees current client’s files |

---

## 3️⃣ AI Assistant Sidebar

| Requirement | Description | Acceptance Criteria |
|------------|-------------|------------------|
| Context-Aware AI | AI receives current client context | Only operates on selected client files |
| Computation Commands | Compute taxable income, deductions | Results match manual calculation ≥95% accuracy |
| Document Generation | Generate ITR, financial statements | Outputs downloadable PDFs/Excel sheets |
| Chat History | Maintain per-client AI chat | Accessible within client workspace; persisted securely |

---

## 4️⃣ ITR Computation

| Requirement | Description | Acceptance Criteria |
|------------|-------------|------------------|
| ITR Forms | Support ITR 1 / ITR 2 | Correct pre-filled forms generated |
| Calculations | Compute taxable income & deductions | Matches expected results |
| Validation | Check uploaded files for required fields | Prompts user if missing |
| Export | PDF/Excel summaries | Generated files downloadable and correct |

---

## 5️⃣ General Requirements

- **Security:** Role-based access, per-client isolation, encrypted storage  
- **Performance:** File uploads/downloads complete in <3s, AI response <5s per request  
- **Audit Trail:** All edits, uploads, and deletions logged  
- **UI/UX:** Minimal, distraction-free, 3-pane layout inspired by Cursor

---

