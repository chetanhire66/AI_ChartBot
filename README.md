# 🤖 AI ChartBot – Flask Based AI Chatbot

AI ChartBot is a Flask-based AI chatbot that allows users to ask questions and receive AI-generated responses.  
All chat conversations are stored in a SQLite database, making it easy to view previous questions and answers.

This project is suitable for **college projects, hackathons, and portfolio showcases**.

---

## 🌐 Live Demo

👉 **Deployed Application:**  
https://ai-chartbot-dgn5.onrender.com

👉 **GitHub Repository:**  
https://github.com/chetanhire66/AI_ChartBot

---

## 🚀 Features

- 💬 AI-powered chatbot responses  
- 🧠 AI logic handled in `Chatbot.py`  
- 🗂 Stores chat history using SQLite database  
- 🌐 REST API endpoint for chatbot interaction  
- 📄 Clean Flask project structure  
- ☁️ Deployed on Render  

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Database:** SQLite, SQLAlchemy  
- **AI:** Gemini API (via `geminiF()` function)  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Render  

---

## 📁 Project Structure

```

AI_ChartBot/
│
├── app.py
├── Chatbot.py
├── requirements.txt
├── Procfile
├── templates/
├── static/
├── instance/
└── **pycache**/

````

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/chetanhire66/AI_ChartBot.git
cd AI_ChartBot
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔁 API Usage

### Ask a Question

**POST** `/ask`

**Request (JSON):**

```json
{
  "question": "What is Artificial Intelligence?"
}
```

**Response (JSON):**

```json
{
  "question": "What is Artificial Intelligence?",
  "answer": "Artificial Intelligence is the simulation of human intelligence in machines."
}
```

---

## 🗃 Database

* Uses SQLite database
* Automatically creates database and tables on first run
* Stores all questions and AI responses

---

## 📌 Future Enhancements

* User authentication
* Clear chat history option
* Improved UI/UX
* Voice-based chatbot
* Admin dashboard

---

## 👨‍💻 Author

**Chetan Hire**
GitHub: [https://github.com/chetanhire66](https://github.com/chetanhire66)
