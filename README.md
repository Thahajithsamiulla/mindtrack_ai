# 🧠 MindTrack AI — Adaptive Mental Health Chatbot

A production-ready full-stack mental health companion app with AI chat, mood tracking, analytics dashboard, daily check-ins, and curated wellness suggestions.

---

## 📁 Folder Structure

```
mindtrack/
├── index.html       ← Full frontend (single-file, Tailwind + Chart.js + Vanilla JS)
├── server.js        ← Node.js + Express backend with NLP engine
├── package.json     ← Project metadata & dependencies
└── README.md        ← This file
```

---

## 🚀 Quick Start

### Prerequisites
- **Node.js** v16 or higher — [Download here](https://nodejs.org)

### Step 1 — Install dependencies
```bash
cd mindtrack
npm install
```

### Step 2 — Start the backend server
```bash
npm start
```
You'll see:
```
🧠 MindTrack AI Backend running at http://localhost:3001
```

### Step 3 — Open the app
Open your browser and go to:
```
http://localhost:3001
```

That's it! The Express server serves the frontend automatically.

---

## 🔌 API Endpoints

| Method | Endpoint          | Description                        |
|--------|-------------------|------------------------------------|
| POST   | `/chat`           | Analyze message, detect emotion, return response + suggestions |
| GET    | `/history`        | Retrieve all chat records          |
| POST   | `/checkin`        | Save daily mood check-in           |
| GET    | `/mood-trend`     | 7-day wellbeing score trend        |
| GET    | `/progress-score` | Overall wellbeing progress %       |
| GET    | `/health`         | Server health check                |

### POST /chat — Request body
```json
{ "message": "I'm feeling really anxious about my exam" }
```

### POST /chat — Response
```json
{
  "response": "I understand how overwhelming anxiety can feel...",
  "emotion": "anxious",
  "suggestions": [
    "Try box breathing: inhale 4s, hold 4s, exhale 4s, hold 4s",
    "Ground yourself: name 5 things you can see right now",
    ...
  ]
}
```

---

## 🧩 Features

### 💬 Chat
- Real-time AI chatbot interface
- Emotion detection (8 emotions: happy, sad, anxious, angry, stressed, grateful, lonely, neutral)
- Personalized suggestions per emotion (5 tips)
- Typing animation indicator
- Chat history persisted in LocalStorage
- Graceful fallback if backend is unavailable

### 📊 Dashboard
- Wellbeing progress ring + bar
- Emotion distribution bar chart (Chart.js)
- Weekly mood trend line chart
- Total sessions, streak, dominant mood stats

### ❤️ Daily Check-in
- 8-mood selector buttons
- 1–10 wellbeing slider
- Optional notes input
- Data saved to backend + LocalStorage

### 🕘 History
- All past chat sessions displayed
- Emotion badge per message
- Clear all option

### 💡 Suggestions
- 6 mental health tip cards
- 3 embedded YouTube guided videos
- Crisis helpline resources

---

## 🗄️ Adding MongoDB (Optional Upgrade)

Install the MongoDB driver:
```bash
npm install mongoose
```

Add to `server.js` at the top:
```javascript
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/mindtrack');

const ChatSchema = new mongoose.Schema({
  message: String, emotion: String, response: String,
  suggestions: [String], timestamp: Date
});
const Chat = mongoose.model('Chat', ChatSchema);
```

Then replace in-memory `chatRecords.push(record)` with:
```javascript
await Chat.create(record);
```

---

## 🎨 Tech Stack

| Layer     | Technology                     |
|-----------|-------------------------------|
| Frontend  | HTML5, Tailwind CSS (CDN), Vanilla JS |
| Charts    | Chart.js                       |
| Fonts     | Google Fonts (Sora + DM Serif Display) |
| Backend   | Node.js, Express               |
| Storage   | In-memory (default) / MongoDB  |
| AI Logic  | Keyword-based NLP engine       |

---

## 🛡️ Error Handling

- If the backend is unreachable, the frontend falls back to a built-in NLP engine
- Empty message inputs are rejected gracefully
- All API errors return meaningful JSON responses
- No console errors in production mode

---

## 📱 Responsive Design

- Full mobile support with hamburger menu
- Sidebar collapses on small screens
- Grid adapts to single column on mobile

---

*Built with 💜 — MindTrack AI is not a substitute for professional mental health care.*
