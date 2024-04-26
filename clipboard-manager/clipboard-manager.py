import pyperclip
import sqlite3
from datetime import datetime
import os
import sys

# Function to initialize the SQLite database
def init_database():
    conn = sqlite3.connect('clipboard_history.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clipboard (
            id INTEGER PRIMARY KEY,
            content TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to add clipboard content to the database
def add_to_database(content):
    conn = sqlite3.connect('clipboard_history.db')
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO clipboard (content, timestamp) VALUES (?, ?)', (content, timestamp))
    conn.commit()
    conn.close()

# Function to retrieve clipboard history from the database
def get_clipboard_history():
    conn = sqlite3.connect('clipboard_history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clipboard ORDER BY id DESC')
    clipboard_history = cursor.fetchall()
    conn.close()
    return clipboard_history

# Function to clear clipboard history
def clear_clipboard_history():
    conn = sqlite3.connect('clipboard_history.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clipboard')
    conn.commit()
    conn.close()

# Function to search clipboard history by content
def search_clipboard_history(search_query):
    conn = sqlite3.connect('clipboard_history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clipboard WHERE content LIKE ? ORDER BY id DESC', ('%' + search_query + '%',))
    search_results = cursor.fetchall()
    conn.close()
    return search_results

# Function to print clipboard history
def print_clipboard_history(history):
    if not history:
        print("Clipboard history is empty.")
    else:
        print("Clipboard History:")
        for entry in history:
            print(f"{entry[0]} | {entry[2]} | {entry[1]}")

# Main function to monitor clipboard changes and interact with the user
def main():
    # Initialize the database
    init_database()
    
    while True:
        try:
            # Monitor clipboard changes
            current_clipboard_content = pyperclip.paste()
            
            # Check if clipboard content has changed
            if current_clipboard_content != previous_clipboard_content:
                # Add new clipboard content to the database
                add_to_database(current_clipboard_content)
                print("Clipboard content added to history:", current_clipboard_content)
                previous_clipboard_content = current_clipboard_content
            
            # Get user input for actions
            print("\nOptions:")
            print("1. Print clipboard history")
            print("2. Search clipboard history")
            print("3. Clear clipboard history")
            print("4. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                clipboard_history = get_clipboard_history()
                print_clipboard_history(clipboard_history)
            elif choice == "2":
                search_query = input("Enter search query: ")
                search_results = search_clipboard_history(search_query)
                print_clipboard_history(search_results)
            elif choice == "3":
                clear_clipboard_history()
                print("Clipboard history cleared.")
            elif choice == "4":
                print("Exiting Clipboard Manager.")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("KeyboardInterrupt: Exiting Clipboard Manager.")
            sys.exit()
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
