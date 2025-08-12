# app.py
from flask import Flask
from threading import Thread
import os

# Import the function that contains your main script's logic
from my_task import do_the_work

# --- Flask App Initialization ---
app = Flask(__name__)

# --- Background Task Definition ---
def run_main_script():
    """
    This function will run in a separate thread.
    It simply calls the main function from your other script.
    """
    print("Starting background thread for the main task.")
    do_the_work()

# --- Web Server Routes ---
@app.route('/')
def home():
    """
    This is the main endpoint for the web server.
    It provides a simple response to confirm the server is running.
    This is the URL that our UptimeRobot will ping.
    """
    # HTML with some basic styling for a clean look
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Deployment Status</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #121212; color: #e0e0e0; }
            .container { text-align: center; padding: 40px; border-radius: 12px; background-color: #1e1e1e; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5); }
            h1 { color: #4CAF50; font-size: 2.5em; }
            p { font-size: 1.2em; }
            code { background-color: #2c2c2c; padding: 3px 6px; border-radius: 4px; font-family: "Courier New", Courier, monospace; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✅ Online</h1>
            <p>The web server shim is active.</p>
            <p>The background task is running. Check the service logs for output.</p>
        </div>
    </body>
    </html>
    """

# --- Main Execution Block ---
if __name__ == "__main__":
    # Create and start the background thread
    # We use a daemon thread so it exits when the main thread (Flask app) exits.
    # On a real server, the Flask app never exits, so the background task runs forever.
    background_thread = Thread(target=run_main_script, daemon=True)
    background_thread.start()

    # Get the port from the environment variable Render sets
    port = int(os.environ.get("PORT", 5000))
    
    # Run the Flask web server
    # Use host='0.0.0.0' to make it accessible from outside the container
    app.run(host='0.0.0.0', port=port)
