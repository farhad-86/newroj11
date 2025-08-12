# my_task.py
import time
import datetime

def do_the_work():
    """
    This is the main function containing the logic you want to run 24/7.
    It can be anything: a bot, a scraper, an API poller, etc.
    """
    print("🚀 Starting the perpetual background task...")
    count = 0
    while True:
        try:
            # --- YOUR ACTUAL CODE GOES HERE ---
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{current_time}] Heartbeat: Task is alive. Iteration {count}.")
            count += 1
            # ------------------------------------

            # Sleep for 10 seconds before the next iteration
            time.sleep(10)

        except Exception as e:
            print(f"An error occurred in the main task loop: {e}")
            # Wait for a minute before retrying to avoid spamming errors
            time.sleep(60)

if __name__ == '__main__':
    # This block allows you to run the script directly for testing
    print("Testing my_task.py directly...")
    do_the_work()
