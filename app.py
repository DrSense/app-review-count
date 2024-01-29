from flask import Flask, render_template, request, jsonify
import mysql.connector
from datetime import datetime, timedelta

app = Flask(__name__)

# MySQL database configuration
db = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="your_database_name"
)
cursor = db.cursor()

# Route to render the HTML page
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle the AJAX request
@app.route("/get_reviews", methods=["POST"])
def get_reviews():
    app_name = request.form.get("app_name")
    platform = request.form.get("platform")
    time_filter = request.form.get("time_filter")

    # Replace this with your logic to retrieve reviews based on filters
    # For now, I'll assume a placeholder list of reviews
    reviews = [
        {"review_name": "Review 1", "review_date": "2024-01-01", "review_content": "Lorem ipsum...", "import_date": "2024-01-05", "platform": platform},
        {"review_name": "Review 2", "review_date": "2024-01-10", "review_content": "Dolor sit amet...", "import_date": "2024-01-15", "platform": platform},
        # Add more reviews as needed
    ]

    # Save the reviews in the database (assuming the table structure)
    for review in reviews:
        insert_query = "INSERT INTO app_reviews (app_name, review_name, review_date, review_content, import_date, platform) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (app_name, review["review_name"], review["review_date"], review["review_content"], review["import_date"], review["platform"]))
        db.commit()

    # Apply time filter if needed
    if time_filter != "all_time":
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7) if time_filter == "last_week" else end_date - timedelta(days=30)

        reviews = [review for review in reviews if start_date <= datetime.strptime(review["review_date"], "%Y-%m-%d") <= end_date]

    return jsonify({"reviews": reviews})

if __name__ == "__main__":
    app.run(debug=True)
