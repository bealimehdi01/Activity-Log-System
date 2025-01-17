# Activity Log System

A full-stack application for processing and analyzing real-time user activity logs.

## Requirements Checklist

✅ Flask Application Setup
- [x] PostgreSQL database integration
- [x] Activity log model with required fields

✅ CRUD Operations
- [x] POST /logs endpoint with validation
- [x] GET /logs/{user_id} with filtering
- [x] GET /logs/stats endpoint

✅ Complex API Query
- [x] Total activity count per user
- [x] Most frequent activity type

✅ Validation & Error Handling
- [x] Input validation
- [x] Error responses
- [x] Missing fields checking

✅ Database Tasks
- [x] Schema design
- [x] Sample data insertion
- [x] Analytics queries

✅ DevOps
- [x] Docker configuration
- [x] Docker Compose setup

✅ Frontend Integration
- [x] React frontend
- [x] Activity log display
- [x] User ID based filtering

## Setup Instructions

1. Clone the repository
2. Set up the database:
```bash
# Create PostgreSQL database
createdb activity_logs
```

3. Create virtual environment:
```bash
python -m venv new_venv
source new_venv/Scripts/activate  # Windows: new_venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
cd frontend
npm install
```

5. Start the application:
```bash
# Terminal 1 - Backend
python app.py

# Terminal 2 - Frontend
cd frontend
npm start
```

6. Insert sample data:
```bash
python sample_data.py
```

## Testing the Application

1. Backend API Tests:
```bash
# Test home endpoint
curl http://localhost:5000/

# Create new log
curl -X POST http://localhost:5000/logs \
-H "Content-Type: application/json" \
-d '{
  "user_id": "12345",
  "activity": "page_view",
  "timestamp": "2024-01-17T14:00:00",
  "metadata": {"page": "home"}
}'

# Get user logs
curl http://localhost:5000/logs/12345

# Get statistics
curl "http://localhost:5000/logs/stats?start=2024-01-01T00:00:00&end=2024-12-31T23:59:59"
```

2. Frontend Testing:
- Open http://localhost:3000
- Enter user ID (e.g., "12345")
- Click "Fetch Logs"
- View activity logs

## Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build
```

## API Documentation

- POST /logs - Create new activity log
  - Required fields: user_id, activity, timestamp, metadata

- GET /logs/{user_id} - Get user's logs
  - Optional query params: activity_type, start_date, end_date

- GET /logs/stats - Get activity statistics
  - Required query params: start, end

## Tech Stack

- Backend: Flask, PostgreSQL, SQLAlchemy
- Frontend: React, Axios
- DevOps: Docker, Docker Compose
- Testing: pytest
