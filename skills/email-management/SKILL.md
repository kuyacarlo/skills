---
name: email-management
description: System for classifying, archiving, and routing automated/corporate emails and generating mail filter configurations. Defaults to outputting in the chat.
---

# 📧 Email Management Skill

This skill manages the automated email classification, archiving, and routing system for user accounts. It dynamically adapts to the email clients, servers, or MCP interfaces available on your system.

---

## 🔍 System Context & Architecture

The system coordinates between your active email client or server (using local MCP extensions or APIs) and your mail server-side labels/archives.

### Dynamic Connection Path
Email connection configurations and API details are discovered dynamically by checking:
1. Active environment variables (such as client connection configs or credentials).
2. Connected MCP servers or integrations (e.g. mail client extensions, IMAP/SMTP helper daemons).
3. Standard configuration locations or fallback paths.

### Folder Mapping & Fallback Logic
* **Dynamic Folder Detection**: The organizer queries folder structures and matches folders by type (e.g., archives, junk, specific categories) instead of using hardcoded paths. This ensures compatibility across multiple mail providers.
* **All Mail / Archive Fallback**: If a target category folder is missing or fails to index, the system automatically falls back to moving the messages to the native Archive folder. This cleanly archives the message from the inbox while preserving server-side tags/labels.

---

## 🛠️ Workflows & Operations

Whenever you need to sweep the inbox or adjust rules:

### Step 1: Audit Uncategorized Senders
Run an audit script or function to fetch current inbox messages and summarize the remaining uncategorized senders. 

### Step 2: Update Classification Rules
1. **Identify Category**: Decide which folder/label the new sender or domain belongs to.
2. **Update Rules**: Add the new domain or email address to the matching category check in the configuration file or classifier script.
3. **Update Filter Configurations**: Keep external rules (such as mail client filter rules or XML configurations) in sync by updating the matching entry blocks.
4. **Default Output:** By default, output any generated filters, rule structures, or reports directly in the chat, creating a markdown artifact only when necessary (in lieu of chat).

### Step 3: Run the Sweep
Execute the main sweep process to categorize and archive messages in bulk across all email accounts.
