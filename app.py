from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from sqlalchemy import func
from flask_cors import CORS  # Add this import

app = Flask(__name__)
CORS(app)  # Add this line

# Load configuration from config.py
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

# Define the ActivityLog model
class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    activity = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    log_metadata = db.Column(db.JSON)  # Renamed from metadata to log_metadata

# Create the database tables within the application context
with app.app_context():
    db.create_all()

# Add home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Activity Log System API",
        "endpoints": {
            "create_log": "/logs [POST]",
            "get_user_logs": "/logs/<user_id> [GET]",
            "get_stats": "/logs/stats [GET]"
        }
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

# POST /logs endpoint to accept and validate activity logs
@app.route("/logs", methods=["POST"])
def create_log():
    data = request.get_json()
    if not data or not all(k in data for k in ("user_id", "activity", "timestamp", "metadata")):
        return jsonify({"error": "Invalid data"}), 400

    log = ActivityLog(
        user_id=data["user_id"],
        activity=data["activity"],
        timestamp=datetime.fromisoformat(data["timestamp"]),
        log_metadata=data["metadata"]  # Updated to log_metadata
    )
    db.session.add(log)
    db.session.commit()
    return jsonify({"message": "Log created"}), 201

# Update GET /logs/<user_id> to support filtering
@app.route("/logs/<user_id>", methods=["GET"])
def get_logs(user_id):
    start_date = request.args.get('start_date', (datetime.utcnow() - timedelta(days=7)).isoformat())
    end_date = request.args.get('end_date', datetime.utcnow().isoformat())
    activity_type = request.args.get('activity_type')

    query = ActivityLog.query.filter(
        ActivityLog.user_id == user_id,
        ActivityLog.timestamp.between(start_date, end_date)
    )

    if activity_type:
        query = query.filter(ActivityLog.activity == activity_type)

    logs = query.all()
    return jsonify([{
        "id": log.id,
        "user_id": log.user_id,
        "activity": log.activity,
        "timestamp": log.timestamp.isoformat(),
        "metadata": log.log_metadata
    } for log in logs])

# Add UPDATE endpoint
@app.route("/logs/<int:log_id>", methods=["PUT"])
def update_log(log_id):
    log = ActivityLog.query.get_or_404(log_id)
    data = request.get_json()
    
    if "activity" in data:
        log.activity = data["activity"]
        db.session.commit()
        return jsonify({"message": "Log updated successfully"})
    
    return jsonify({"error": "Activity field is required"}), 400

# GET /logs/stats endpoint to return total activity count per user and most frequent activity type
@app.route("/logs/stats", methods=["GET"])
def get_stats():
    start = request.args.get("start")
    end = request.args.get("end")
    start_date = datetime.fromisoformat(start)
    end_date = datetime.fromisoformat(end)

    user_activity_count = db.session.query(
        ActivityLog.user_id, func.count(ActivityLog.id)
    ).filter(
        ActivityLog.timestamp.between(start_date, end_date)
    ).group_by(ActivityLog.user_id).all()

    most_frequent_activity = db.session.query(
        ActivityLog.activity, func.count(ActivityLog.id)
    ).filter(
        ActivityLog.timestamp.between(start_date, end_date)
    ).group_by(ActivityLog.activity).order_by(func.count(ActivityLog.id).desc()).first()

    return jsonify({
        "user_activity_count": dict(user_activity_count),
        "most_frequent_activity": most_frequent_activity[0] if most_frequent_activity else None
    })

# Run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
