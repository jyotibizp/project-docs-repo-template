# Non-Functional Requirements – Finfelo MVP

Defines the system qualities beyond functional behavior, ensuring the platform is **secure, reliable, and performant**.

---

## 1️⃣ Performance

- The system must support **up to 500 concurrent users** in MVP.  
- File uploads/downloads should complete **within 3 seconds** for typical document sizes (<10MB).  
- AI chat responses should be returned **within 5 seconds** per request.  
- Dashboard and workspace UI must render **instantly (<2s) for up to 100 clients per CA**.

---

## 2️⃣ Availability & Reliability

- System should maintain **99.5% uptime** monthly.  
- Automatic recovery in case of server failure.  
- Scheduled maintenance notifications should be displayed to users.  

---

## 3️⃣ Security

- **Per-client isolation**: Each client’s data is isolated from other clients.  
- **Encryption**:
  - At rest: AES-256 for all files and database entries.  
  - In transit: TLS 1.2+ for all API calls.  
- **Role-based access control (RBAC)**: Only authorized users can access client data.  
- Regular vulnerability scans and patching of critical dependencies.  
- AI assistant cannot access files outside the selected client workspace.  

---

## 4️⃣ Compliance

- Data storage and handling compliant with **Indian IT Act**.  
- Designed to be **GDPR-ready** for potential global rollout.  
- Audit trails for all edits, uploads, deletions, and AI interactions.  

---

## 5️⃣ Usability

- 3-pane workspace (files, document viewer, AI chat) must be **intuitive and minimal**.  
- All major workflows must be completed in **3 clicks or fewer**.  
- Accessible design compliant with **WCAG 2.1**.  
- Consistent error handling and user-friendly messages.  

---

## 6️⃣ Scalability (Post-MVP Considerations)

- Architecture should allow easy **horizontal scaling** to support multiple firms and thousands of clients.  
- AI assistant should support **multi-client contexts** in future versions.  
- Storage and processing should support **large volumes of documents** (PDFs, Excel, CSV) without performance degradation.  

---

## 7️⃣ Maintainability

- Modular code design to allow **easy addition of new document types and AI features**.  
- Logging and monitoring for debugging and performance tracking.  
- Clear documentation for onboarding new developers or QA personnel.  

---

## 8️⃣ Monitoring & Alerts

- System should track key metrics:
  - AI usage frequency per client
  - File upload/download failures
  - ITR computation errors
- Alert notifications for system failures or SLA breaches.  

