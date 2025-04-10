 # File: modify_file_gui.py

import tkinter as tk
from tkinter import filedialog
import os

def modify_file():
    # Create a hidden Tkinter window
    root = tk.Tk()
    root.withdraw()

    # Ask user to select input file
    input_path = filedialog.askopenfilename(
        title="Select a text file to modify",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if not input_path:
        print("No file selected. Exiting.")
        return

    # Suggest output file path
    directory = os.path.dirname(input_path)
    base_name = os.path.basename(input_path)
    output_path = os.path.join(directory, f"MODIFIED_{base_name}")

    try:
        # Read the file
        with open(input_path, 'r') as infile:
            content = infile.read()

        # Modify content: e.g., make it uppercase
        modified_content = content.upper()

        # Write to the new file
        with open(output_path, 'w') as outfile:
            outfile.write(modified_content)

        print(f"\n✅ Modified file saved as: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")


# Run the function
if __name__ == "__main__":
    modify_file()
