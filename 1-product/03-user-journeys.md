# User Journeys – Finfelo MVP

This document outlines **real-world scenarios** for how a CA interacts with the Finfelo platform.

---

## 1️⃣ Journey: Onboarding a New Client

**Goal:** Add a new client to manage their ITR and documents.

**Steps:**
1. CA logs into Finfelo dashboard.
2. Clicks "Add Client."
3. Fills mandatory fields: Name, Type (Individual/Organization), PAN, Contact info.
4. Clicks "Save" → client appears in dashboard.
5. Optional: Upload initial documents (income proof, investment statements).

**Outcome:** New client is listed in dashboard, ready for workspace interaction.

---

## 2️⃣ Journey: Managing Existing Client

**Goal:** Access and update client information.

**Steps:**
1. CA searches/filters client from dashboard.
2. Clicks client → opens Client Workspace.
3. Updates details via "Edit Client" form.
4. Changes saved automatically and logged in audit trail.

**Outcome:** Client details are accurate and up-to-date.

---

## 3️⃣ Journey: Using Client Workspace

**Goal:** View documents and interact with AI assistant.

**Steps:**
1. Select client from dashboard.
2. Workspace opens:
   - Left Sidebar: File tree of uploaded documents.
   - Center Pane: Document viewer (PDF, CSV, XLSX, TXT).
   - Right Sidebar: AI Chat.
3. CA uploads new documents or selects existing ones.
4. CA interacts with AI:
   - "Compute taxable income from uploaded files."
   - "Generate pre-filled ITR form."
   - "Summarize client financials."

**Outcome:** Computations are completed, documents generated, and AI chat history maintained per client.

---

## 4️⃣ Journey: Deleting a Client

**Goal:** Remove a client no longer serviced.

**Steps:**
1. CA selects client in dashboard.
2. Clicks "Delete Client."
3. Confirms deletion → all client data and workspace removed.
4. Action logged for audit purposes.

**Outcome:** Client is fully removed, ensuring compliance and clean workspace.

---

## 5️⃣ Notes

- Each journey is **client-centric**, all AI and file operations are **isolated per client**.
- AI assistant always **knows the client context** to prevent cross-client data issues.
