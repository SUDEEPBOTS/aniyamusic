# 🛡️ Security Policy — AniyaMusic

At **SUDEEPBOTS**, security and user privacy are foundational. We take security disclosures seriously and are committed to resolving vulnerabilities promptly.

---

## 📦 Supported Versions

Only the latest release running on the `main` branch receives proactive security patches.

| Version | Supported          | Status |
| :--- | :---: | :--- |
| **v2.x (Latest `main`)** | :white_check_mark: | Actively Maintained & Patched |
| **v1.x** | :x: | End of Life (Deprecated) |

---

## 🚨 Reporting a Vulnerability

If you discover a vulnerability or potential exploit:

1. **Do NOT open a public GitHub issue.**
2. Send an advisory report via private contact:
   - **Lead Developer**: [@heartstealer_x](https://t.me/heartstealer_x)
   - **Support Portal**: [Join Community Group](https://t.me/+N08m5L1mCTU2NTE1)
3. Please provide:
   - A description of the issue and potential impact
   - Minimal reproduction steps, proof-of-concept script, or payloads
   - Affected Python environment and operating system

We aim to acknowledge reports within **24 hours** and provide a patch or mitigation within **72 hours**.

---

## 🔒 Best Practices for Deployment

- **Never** share or commit your `BOT_TOKEN`, `STRING_SESSION`, or `MONGO_DB_URI` publicly.
- Always use encrypted environment variables or `.env` files with restricted permissions (`chmod 600 .env`).
- Regularly update dependencies using Dependabot.
