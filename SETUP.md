# Setup Instructions

This project has two parts that run together:
- **Backend** — Django 3.0.7 (runs on port `8000`)
- **Frontend** — React 19 + Vite (runs on port `5173`, proxies API calls to Django)

---

## Prerequisites

Make sure you have the following installed:

| Tool | Version |
|------|---------|
| Python | 3.8+ |
| pip | latest |
| Node.js | 18+ |
| npm | 9+ |
| Git | any |

---

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/workshop_booking.git
cd workshop_booking
```

---

## 2. Backend Setup (Django)

### 2a. Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 2b. Install dependencies

```bash
pip install -r requirements.txt
```

### 2c. Configure environment variables

Copy the sample env file and fill in your values:

```bash
cp .sampleenv .env
```

Open `.env` and set the following (SQLite is the default — no DB setup needed for local dev):

```env
DB_ENGINE=sqlite3
DB_NAME=db.sqlite3
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=
EMAIL_HOST=localhost
EMAIL_PORT=25
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=False
SENDER_EMAIL=admin@localhost
```

> For production with PostgreSQL/MySQL, update `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT` accordingly.

### 2d. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2e. Seed workshop types

Populate the booking dropdown with default workshop types:

```bash
python manage.py shell < seed_workshop_types.py
```

### 2f. Create a superuser

```bash
python manage.py createsuperuser
```

### 2g. Start the Django server

```bash
python manage.py runserver
```

Django is now running at **http://127.0.0.1:8000**

### 2h. Configure user roles (via Admin panel)

1. Go to **http://localhost:8000/admin** and log in with your superuser credentials.
2. Navigate to **Groups** → create a group named `instructor` and assign it all permissions.
3. By default, registered users get the `coordinator` role. To promote a user to instructor:
   - Go to **Profiles** → select the user → set position to `instructor`
   - Add them to the `instructor` group

---

## 3. Frontend Setup (React + Vite)

Open a **new terminal** (keep Django running in the first one).

```bash
cd frontend
npm install
npm run dev
```

The React app is now running at **http://localhost:5173**

> Vite automatically proxies all API calls (`/workshop/`, `/admin/`, `/statistics/`, `/page/`, `/reset/`, `/data/`) to Django on port `8000` — no CORS configuration needed in development.

---

## 4. Running the Full App

You need **both servers running simultaneously**:

| Terminal | Command | URL |
|----------|---------|-----|
| Terminal 1 | `python manage.py runserver` | http://127.0.0.1:8000 |
| Terminal 2 | `cd frontend && npm run dev` | http://localhost:5173 |

Open **http://localhost:5173** in your browser to use the app.

---

## 5. Production Build (Optional)

To build the React frontend into Django's static folder:

```bash
cd frontend
npm run build
```

This outputs the compiled files into `workshop_app/static/workshop_app/`, after which Django can serve the entire app on its own at port `8000`.

---

## Project Structure

```
workshop_booking/
├── cms/                        # CMS Django app
├── docs/                       # Original documentation
├── frontend/                   # React + Vite frontend
│   ├── src/
│   │   ├── components/         # Navbar, Footer, WorkshopCard, BookingForm
│   │   ├── pages/              # Home, BookWorkshop, Dashboard, Statistics, Profile, Login, Register
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js          # Dev proxy config (port 5173 → 8000)
├── statistics_app/             # Statistics Django app
├── teams/                      # Teams Django app
├── .env                        # Your local environment variables (not committed)
├── .sampleenv                  # Template for .env
├── manage.py
├── requirements.txt
├── seed_workshop_types.py      # One-time script to populate workshop types
└── README.md
```

---

## Troubleshooting

**`ModuleNotFoundError` on `python manage.py runserver`**
→ Make sure your virtual environment is activated and `pip install -r requirements.txt` completed without errors.

**Booking dropdown is empty**
→ Run the seed script: `python manage.py shell < seed_workshop_types.py`

**Frontend shows blank page or API errors**
→ Make sure Django is running on port `8000` before starting Vite. The proxy in `vite.config.js` requires Django to be up.

**`npm install` fails**
→ Ensure Node.js ≥ 18 is installed. Run `node -v` to check.
