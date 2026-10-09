# 🤝 Contributing to AniyaMusic

Thank you for your interest in contributing to **AniyaMusic**! We welcome contributions ranging from bug reports and documentation enhancements to major feature additions.

---

## 📜 Code of Conduct

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) before interacting with the repository or submitting pull requests.

---

## 🛠️ Development Workflow

1. **Fork the Repository**:
   Click the "Fork" button on the top right of the GitHub page.

2. **Clone your fork**:
   ```bash
   git clone https://github.com/<your-username>/aniyamusic.git
   cd aniyamusic
   ```

3. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/my-awesome-improvement
   ```

4. **Install Dependencies & Set Up Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cp sample.env .env
   ```

5. **Make Changes and Test**:
   Ensure all Python files compile cleanly:
   ```bash
   python -m py_compile $(find . -name "*.py" -not -path "*/.*")
   ```

6. **Commit & Push**:
   ```bash
   git commit -m "feat(stream): optimize audio buffer allocation"
   git push origin feature/my-awesome-improvement
   ```

7. **Submit a Pull Request**:
   Open a PR against the `main` branch of `SUDEEPBOTS/aniyamusic`.

---

## 📌 Coding Standards

- Write clean, asynchronous code utilizing modern `asyncio` best practices.
- Ensure all Telegram API operations comply with Pyrogram v2 guidelines.
- Do not commit sensitive tokens, secrets, or personal MongoDB connection strings.
- Add descriptive docstrings and inline comments where necessary.
