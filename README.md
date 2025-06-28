# python_projects
Python Projects for practice
# 🌦️ Python Weather App (CLI + GUI)

This project shows how to build a weather application in Python using both command-line and GUI (Tkinter).

## 🧰 Tech Stack
- Python
- OpenWeatherMap API
- Tkinter (GUI)

## 📋 Features
- Real-time weather info
- CLI interface
- GUI using Tkinter
- Shows temperature, humidity, and conditions

## 🔧 Setup

1. Clone the repo
2. Install `requests`:  
   `pip install requests`
3. Replace the API key in the `.py` files with your own from [OpenWeatherMap](https://openweathermap.org/)
4. Run:

```bash
python weather_gui.py
## How to get the API key from openweathermap.org for fetching real time data.


## 🧾 Step-by-Step: How to Get Your API Key from OpenWeather

---

### 1️⃣ Go to the Website

👉 Visit: [https://home.openweathermap.org/](https://home.openweathermap.org/)

---

### 2️⃣ Sign Up / Log In

* **If new:** Click **Sign Up**

  * Fill in email, username, and password
  * Confirm via email (check spam just in case)
* **If already have an account:** Just **Log In**

---

### 3️⃣ Go to API Keys Section

* Once logged in, go to:
  📍 [My API Keys](https://home.openweathermap.org/api_keys)
  \*(Or click your username top-right → **My API Keys**)

---

### 4️⃣ Get Your Default Key

* You’ll see a default key like:

  ```
  741e9014fd4350307cc00f2a48bac900
  ```
* That’s your **active API key** — copy that 

---

### 5️⃣ (Optional) Create a Custom-Named Key

* Click **“Create Key”**
* Give it a name (like `weather_app_python_demo`)
* Click **Generate**
* new key is added to your list!

---

### 6️⃣ Start Using It in Code!

Example URL:

```python
https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=YOUR_API_KEY&units=metric
```

Or plug it in your script:

```python
API_KEY = "YOUR_API_KEY"
```

---

### 🛡️ Pro Tips

* Don’t share this key publicly in GitHub projects — or use a `.env` file to keep it safe
* You can regenerate or delete the key any time from your dashboard
* Free tier allows \~60 requests/minute — perfect for classroom or demos

---


