from app import app, db, ActivityLog
from datetime import datetime, timedelta

sample_logs = [
    {
        "user_id": "12345",
        "activity": "page_view",
        "timestamp": datetime.utcnow(),
        "log_metadata": {"page": "home"}
    },
    {
        "user_id": "12345",
        "activity": "click",
        "timestamp": datetime.utcnow() - timedelta(hours=2),
        "log_metadata": {"element": "submit_button"}
    },
    {
        "user_id": "67890",
        "activity": "page_view",
        "timestamp": datetime.utcnow(),
        "log_metadata": {"page": "profile"}
    },
    {
        "user_id": "67890",
        "activity": "form_submit",
        "timestamp": datetime.utcnow() - timedelta(hours=3),
        "log_metadata": {"form": "contact"}
    },
    {
        "user_id": "12345",
        "activity": "login",
        "timestamp": datetime.utcnow() - timedelta(days=1),
        "log_metadata": {"status": "success"}
    },
    {
        "user_id": "67890",
        "activity": "page_view",
        "timestamp": datetime.utcnow() - timedelta(days=2),
        "log_metadata": {"page": "settings"}
    },
    {
        "user_id": "12345",
        "activity": "button_click",
        "timestamp": datetime.utcnow() - timedelta(days=3),
        "log_metadata": {"button": "save"}
    },
    {
        "user_id": "67890",
        "activity": "logout",
        "timestamp": datetime.utcnow() - timedelta(days=4),
        "log_metadata": {"status": "success"}
    },
    {
        "user_id": "12345",
        "activity": "form_submit",
        "timestamp": datetime.utcnow() - timedelta(days=5),
        "log_metadata": {"form": "signup"}
    },
    {
        "user_id": "67890",
        "activity": "page_view",
        "timestamp": datetime.utcnow() - timedelta(days=6),
        "log_metadata": {"page": "dashboard"}
    }
]

def insert_sample_data():
    with app.app_context():
        for log_data in sample_logs:
            log = ActivityLog(**log_data)
            db.session.add(log)
        db.session.commit()
        print("Sample data inserted successfully!")

if __name__ == "__main__":
    insert_sample_data()
