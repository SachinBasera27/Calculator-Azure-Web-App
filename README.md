# Flask Calculator — Azure Web App

A simple arithmetic calculator built with Python + Flask, deployed on Azure Web App via GitHub Actions.

---

## Project Structure

```
calculator-app/
├── app.py                        # Flask application (backend logic)
├── requirements.txt              # Python dependencies
├── startup.txt                   # Gunicorn startup command for Azure
├── templates/
│   └── index.html                # Frontend UI
└── .github/
    └── workflows/
        └── deploy.yml            # GitHub Actions CI/CD pipeline
```

---

## Local Development

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/<your-repo>.git
cd calculator-app

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run locally
python app.py

# Visit: http://127.0.0.1:5000
```

---

## Azure Web App Setup (One-Time)

### 1. Create the Web App in Azure Portal
- Go to **Azure Portal → App Services → Create**
- Runtime stack: **Python 3.11**
- OS: **Linux**
- Region: your preferred region

### 2. Set the Startup Command
- In your Web App → **Configuration → General Settings**
- Set **Startup Command** to:
  ```
  gunicorn --bind=0.0.0.0 --timeout 600 app:app
  ```

### 3. Get the Publish Profile
- In your Web App → **Overview → Get publish profile**
- Download the `.PublishSettings` file
- Open it and copy the **entire XML content**

### 4. Add GitHub Secrets
Go to your GitHub repo → **Settings → Secrets and variables → Actions → New repository secret**

| Secret Name              | Value                                      |
|--------------------------|--------------------------------------------|
| `AZURE_WEBAPP_NAME`      | Your Azure Web App name (e.g. `my-calc-app`) |
| `AZURE_PUBLISH_PROFILE`  | The full XML content from the publish profile |

---

## Deploy

Once secrets are set, simply push to `main`:

```bash
git add .
git commit -m "Initial deployment"
git push origin main
```

GitHub Actions will automatically build and deploy to Azure. Check the **Actions** tab in your repo for live logs.

---

## API Endpoints

| Method | Endpoint      | Description           |
|--------|---------------|-----------------------|
| GET    | `/`           | Serves the calculator UI |
| POST   | `/calculate`  | Performs the calculation |

### POST `/calculate` — Request Body (JSON)

```json
{
  "num1": 10,
  "num2": 3,
  "operation": "divide"
}
```

Operations: `add`, `subtract`, `multiply`, `divide`

### Response

```json
{
  "result": 3.33333333,
  "expression": "10 ÷ 3 = 3.33333333"
}
```

---

## Notes

- `gunicorn` is used instead of Flask's dev server — Azure requires a production WSGI server.
- `debug=False` is set in `app.py` — never run debug mode in production.
- The publish profile method is the simplest auth approach; for enterprise use, consider **Azure Service Principal + OIDC** instead.
