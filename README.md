#  Remind-Me-Later

A simple FastAPI backend to store reminder messages with a date, time, and preferred notification method (SMS or Email).

---

## Features

- Add a new reminder with a message, datetime, and method (`sms` or `email`)
- Retrieve all saved reminders
- Validates all input (date, time, remind_by)
- Async MongoDB integration using Motor
- Handles edge cases like invalid values and past times

---

## Tech Stack

- **FastAPI** (Backend framework)
- **MongoDB** (Database)
- **Motor** (Async MongoDB driver)
- **Pydantic** (Validation)
- **Uvicorn** (ASGI server)

---

##  Project Structure

```
remind-me-later/
├── main.py          # FastAPI routes and logic
├── models.py        # Pydantic schemas
├── database.py      # MongoDB connection
├── .env             # Environment variables (Mongo URL)
├── requirements.txt # Python dependencies
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Harshad712/Remind-me-later.git
cd remind-me-later
```

### 2. Create `.env` file

```bash
MONGO_URL=mongodb://your_url
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
uvicorn main:app --reload
```

---

## API Endpoints

### POST `/reminders/`

Create a new reminder.

**Request Body:**

```json
{
  "date": "2025-05-10",
  "time": "06:30:00",
  "message": "Wake up early",
  "remind_by": "sms"
}
```

**Response:**

```json
{
  "id": "608c8ff...e5",
  "status": "Reminder saved!",
  "created_at": "2025-05-10T06:30:00Z"
}
```

---

### GET `/reminders/`

Fetch all saved reminders.

**Response:**

```json
[
  {
    "id": "608c8ff...e5",
    "date": "2025-05-10",
    "time": "06:30:00",
    "message": "Wake up early",
    "remind_by": "sms",
    "created_at": "2025-05-10T06:30:00Z"
  }
]
```

---

## Validation & Errors

- `remind_by` must be either `"sms"` or `"email"`
- Reminder date/time **must not be in the past**
- Returns 422 or 400 errors for invalid input

---

## Author

**Harshad Kokkinti**  
[GitHub: Harshad712](https://github.com/Harshad712)  
Email: harshadkokkinti@gmail.com