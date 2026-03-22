<div align="center">

# 🏦 Secure Cloud Banking System ☁️

*A modern, enterprise-grade cloud banking application built with Flask and MySQL.*

> **"mtlb jo bhi dekhe bole kya lagra hai"** 💫 <br>
> *— A commitment to delivering an awe-inspiring, professional, and visually stunning user experience.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-00758F?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

</div>

## 📖 Overview

**Secure Cloud Banking System** is a full-stack, state-of-the-art web application simulating a real-world digital banking platform. Engineered with security, scalability, and an intuitive user interface, it provides a seamless financial management experience for users and robust monitoring tools for administrators.

From AES-encrypted PII and Bcrypt password hashing to OTP-based email verification, every feature is designed to ensure data integrity and user trust.

🌐 **Live Demo:** Run locally on `http://127.0.0.1:5000`

---

## ✨ Key Features

### 🔐 Uncompromising Security
*   **Military-Grade Encryption:** AES-256 encryption applied to sensitive PII such as phone numbers and 20-digit auto-generated account numbers.
*   **Cryptographic Verification:** SHA-256 transaction hashes generated for all deposits, withdrawals, and transfers to prevent tampering.
*   **Dual-Layer Authentication:** Bcrypt password hashing coupled with time-sensitive OTP verification sent directly via email.
*   **System Hardening:** CSRF protection seamlessly integrated via Flask-WTF, prepared SQL statements to thwart injection attacks, and strict role-based access control (RBAC).

### 💳 Core Banking Operations
*   **Frictionless Onboarding:** Automatic generation of unique 20-digit account numbers upon registration.
*   **Comprehensive Transactions:** Effortlessly execute Deposits, Withdrawals, and Peer-to-Peer Transfers.
*   **Smart Transfers:** Lookup recipients securely via their linked email address or encrypted account number.
*   **Live Dashboard:** Real-time visibility into account balances and a quick glimpse of recent activity.

### 🛡️ Powerful Admin Portal
*   **Holistic Monitoring:** View network-wide statistics including total assets, user volume, and high-value transactions.
*   **User & Account Control:** Execute account suspensions, activations, and closures seamlessly.
*   **Complete Audit Trail:** Deep search through all platform transactions filtering by type, status, and associated parties.

---

## 📸 System Previews

| Client Dashboard | Admin Control Center |
| :---: | :---: |
| *(Add your screenshot here)* <br> `screenshots/dashboard.png` | *(Add your screenshot here)* <br> `screenshots/admin.png` |
| **Secure Authentication** | **Transaction History** |
| *(Add your screenshot here)* <br> `screenshots/login.png` | *(Add your screenshot here)* <br> `screenshots/transactions.png` |

---

## 🛠️ Technology Stack

| Category | Technologies Used |
| :--- | :--- |
| **Backend Framework** | Python 3.10+, Flask, Flask-Mail |
| **Database & ORM** | MySQL 8.0, Flask-MySQLdb |
| **Security & Crypto** | Bcrypt, cryptography (AES-256), Flask-WTF (CSRF), SHA-256 |
| **Frontend UI** | HTML5, CSS3, JavaScript, Jinja2 Templates |

---

## 🚀 Quick Start Guide

Transform your local machine into a cloud banking server in less than 5 minutes.

### 1. Clone the Repository
```bash
git clone <repo-url>
cd Secure-Cloud-Banking-System
```

### 2. Prepare Virtual Environment
Isolate your dependencies for a clean installation.
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Database Initialization
Ensure your MySQL server is running. Create the `securebank` schema and populate essential tables.
```bash
# Ensure MySQL credentials in setup_database.py are correct before running
python setup_database.py
```
> 💡 *Note: The setup script automatically provisions a master admin account:*  
> **Email:** `admin@example.com` | **Password:** `admin123`

### 4. Environment Configuration
Create a `.env` file in the root directory. This is critical for session stability and encryption.
```env
# Critical: Keep these keys highly secure and stable across restarts!
SECRET_KEY=generate_a_strong_random_string_here
ENCRYPTION_KEY=generate_a_32_byte_base64_key_here
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=ayush123
MYSQL_DB=securebank
```

### 5. Ignite the Server
```bash
python run.py
```
> The application is now live at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 API & Endpoint Architecture

| Focus Area | Route | Methods | Auth Required | Description |
| :--- | :--- | :---: | :---: | :--- |
| **Auth** | `/auth/login` | `GET/POST` | ❌ | Credential validation & OTP trigger |
| **Auth** | `/auth/verify-otp` | `GET/POST` | ❌ | Time-sensitive email OTP verification |
| **Client** | `/dashboard` | `GET` | ✅ | Primary user balance & summary |
| **Finance** | `/transactions/transfer`| `GET/POST` | ✅ | P2P fund transfers via Email |
| **Admin** | `/admin/dashboard` | `GET` | 👑 | Exec view of network analytics |
| **Admin** | `/admin/accounts` | `GET/POST` | 👑 | Suspend/Activate/Close user accounts |

---

## 🛡️ Best Practices & Next Steps

This project is actively developed. Upcoming enhancements include:
- [ ] Transitioning hardcoded SMTP / DB credentials strictly to the `.env` pipeline.
- [ ] Integrating full OAuth2.0 authentication.
- [ ] Implementing automated CI/CD pipelines.
- [ ] Introducing Redis for rate-limiting and temporary OTP storage.

---

## 🤝 Contributing to the Future
We welcome visionary developers to improve the cloud banking ecosystem! 
1. `Fork` the repository.
2. Create a Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a **Pull Request**.

---

<div align="center">

**[ MIT License ]**  
*Built with ❤️ utilizing the Flask Web Framework.*

If this project impressed you, please leave a ⭐ on the repository!  

*Because seriously... mtlb jo bhi dekhe bole kya lagra hai! 🔥*

</div>
