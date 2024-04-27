import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Style  # Import the missing modules
import subprocess
import sys
import schedule  # Import the schedule module here
import time

# Function to check for required dependencies and install them if not found
def check_dependencies():
    print("Checking for required dependencies...")
    try:
        # Check if colorama module is installed
        import colorama
        print("colorama module found.")
    except ImportError:
        print("colorama module not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "colorama"])

# Set up logging
logging.basicConfig(filename='task_scheduler.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to send email notification
def send_email(subject, message):
    sender_email = "your_email@example.com"  # Add your email address
    receiver_email = "recipient_email@example.com"  # Add recipient email address
    password = "your_email_password"  # Add your email password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)

# Define tasks to be scheduled
def backup_task():
    logging.info("Running backup task...")
    print(f"{Fore.GREEN}Running backup task...{Style.RESET_ALL}")  # Use Fore and Style to format console output
    # Add your backup logic here
    # Example: Backup files to a specified location

def transfer_task():
    logging.info("Running transfer task...")
    print(f"{Fore.GREEN}Running transfer task...{Style.RESET_ALL}")  # Use Fore and Style to format console output
    # Add your file transfer logic here
    # Example: Transfer files between devices or cloud services

def sync_task():
    logging.info("Running synchronization task...")
    print(f"{Fore.GREEN}Running synchronization task...{Style.RESET_ALL}")  # Use Fore and Style to format console output
    # Add your data synchronization logic here
    # Example: Sync data between different devices or cloud services

# Schedule tasks to run at specified intervals
def schedule_tasks():
    # Schedule backup task to run every day at 2:00 AM
    schedule.every().day.at("02:00").do(backup_task)

    # Schedule transfer task to run every week on Sunday at 6:00 PM
    schedule.every().sunday.at("18:00").do(transfer_task)

    # Schedule synchronization task to run every month on the 1st at 12:00 PM
    schedule.every().day.at("12:00").do(sync_task)  # Corrected to run every day at 12:00 PM

# Main loop to run the task scheduler continuously
def main():
    check_dependencies()
    schedule_tasks()
    logging.info("Task scheduler started.")
    print(f"{Fore.CYAN}Task scheduler started. Press Ctrl+C to exit.{Style.RESET_ALL}")  # Use Fore and Style to format console output
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Task scheduler stopped.")
        print(f"{Fore.RED}\nTask scheduler stopped.{Style.RESET_ALL}")  # Use Fore and Style to format console output

if __name__ == "__main__":
    main()
