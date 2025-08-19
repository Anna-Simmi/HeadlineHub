

# 📰 HeadlineHub

<p align="center">
  <img src="screenshot.png" alt="HeadlineHub Screenshot" width="800"/>
</p>  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-2.3-black?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/NewsAPI-powered-orange?style=for-the-badge&logo=rss&logoColor=white" />
</p>  

---

## ✨ Features

✅ Fetches **top news headlines** (default: India 🇮🇳)
✅ REST endpoint `/api/news` for JSON access
✅ Clean & minimal **Flask + Jinja2** frontend
✅ Handles API errors gracefully

---

## ⚙️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML + Jinja2 templates
* **API:** [NewsAPI.org](https://newsapi.org)

---

## 🚀 Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/headlinehub.git
cd headlinehub
```

### 2️⃣ Create & activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set your API key

Get your free key from [NewsAPI](https://newsapi.org/register).

Create a `.env` file in your project root:

```ini
NEWSAPI_KEY=your_api_key_here
```

Or set it in your shell:

```bash
export NEWSAPI_KEY=your_api_key_here
```

### 5️⃣ Run the app

```bash
python app.py
```

👉 Open **[http://127.0.0.1:10000/](http://127.0.0.1:10000/)** in your browser

---

## 📡 API Endpoint

* `GET /api/news` → returns JSON with latest headlines

Example:

```json
{
  "status": "ok",
  "articles": [
    {
      "title": "Sample News",
      "description": "This is a test headline.",
      "url": "https://example.com"
    }
  ]
}
```

---

## 🔮 Future Enhancements

* Category-based filtering (Tech, Sports, Politics, etc.)
* Multi-country news support 🌍
* Styled UI with Tailwind or Bootstrap
* Caching for faster responses

---

## 🤝 Contributing

Contributions are welcome!

* Fork the repo
* Create your branch (`git checkout -b feature-xyz`)
* Commit changes (`git commit -m 'Add new feature'`)
* Push & create a PR 🚀

---

## 🌐 Connect With Me

<p align="center">
  <a href="https://github.com/Anna-Simmi"><img src="https://img.shields.io/badge/GitHub-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/anna-simmi-m-d-797ba8339"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:annasimmim@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
</p>  
