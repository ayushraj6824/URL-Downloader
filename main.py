import tkinter as tk
import requests

# Function to download the file
def download_file():
    url = url_entry.get()  # Get the URL from the entry field
    file_name = file_name_entry.get()  # Get the file name from the entry field

    if url and file_name:
        try:
            # Send a GET request to the provided URL
            response = requests.get(url, timeout=10)

            # Check if the request was successful
            if response.status_code == 200:
                # Save the content to the specified file
                with open(file_name, 'wb') as file:
                    file.write(response.content)
                result_label.config(text=f"File '{file_name}' downloaded successfully.", fg="green")
            else:
                result_label.config(text=f"Failed to download. Status code: {response.status_code}", fg="red")
        except requests.exceptions.RequestException as e:
            result_label.config(text=f"Error: {e}", fg="red")
    else:
        result_label.config(text="Please enter both a URL and a file name.", fg="red")

# Create the main window
root = tk.Tk()
root.title("File Downloader")
root.geometry("800x400")  # Set the window size

# Label and Entry for URL
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Label and Entry for file name
file_name_label = tk.Label(root, text="Enter File Name (with extension):")
file_name_label.pack(pady=5)
file_name_entry = tk.Entry(root, width=50)
file_name_entry.pack(pady=5)

# Button to trigger the download_file function
download_button = tk.Button(root, text="Download", command=download_file)
download_button.pack(pady=10)

# Label to display result or error message
result_label = tk.Label(root, text="", wraplength=700, justify="left", fg="blue")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()



