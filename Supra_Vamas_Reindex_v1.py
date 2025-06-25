# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 08:25:49 2025

btach convert

@author: David
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox

def reindex_vamas_file(input_path):
    try:
        with open(input_path, 'r') as file:
            lines = [line.rstrip('\r\n') for line in file]
    except Exception as e:
        return f"Failed to read {os.path.basename(input_path)}: {e}"

    currentIndex = 0
    blockLabel = ''
    scanIteration = ''

    for index, line in enumerate(lines):
        if line.strip() == 'XPS':
            label = lines[index - 10]

            if blockLabel == '':
                blockLabel = label

            if blockLabel == label:
                currentIndex += 2
                scanIteration = '0'
            else:
                split = label.partition(':')
                try:
                    if split[1] == ':' and int(split[0]) and split[0] != scanIteration:
                        scanIteration = split[0]
                        currentIndex += 2
                except:
                    pass
            lines[index + 1] = str(currentIndex)

    output_path = os.path.join(os.path.dirname(input_path), 'ReIndexed_' + os.path.basename(input_path))

    try:
        with open(output_path, 'w') as outputFile:
            for line in lines:
                outputFile.write(f'{line}\r\n')
        return f"Processed: {os.path.basename(input_path)}"
    except Exception as e:
        return f"Failed to write {os.path.basename(input_path)}: {e}"

def select_directory_and_convert():
    directory = filedialog.askdirectory()
    if not directory:
        return

    vms_files = [f for f in os.listdir(directory) if f.lower().endswith('.vms')]
    if not vms_files:
        messagebox.showinfo("No Files", "No .VMS files found in the selected directory.")
        return

    results = []
    for file in vms_files:
        full_path = os.path.join(directory, file)
        result = reindex_vamas_file(full_path)
        results.append(result)

    result_text = "\n".join(results)
    messagebox.showinfo("Batch Conversion Complete", result_text)

# === GUI ===
root = tk.Tk()
root.title("Batch VAMAS Block Reindexer")
root.geometry("500x250")

tk.Label(root, text="Batch VAMAS Block Reindexer 1.0", font=("Helvetica", 14), pady=10).pack()
tk.Label(root, text="By David O'Connor, Modified by DaveXPS\nFor KRATOS AXIS SUPRA Data Files\n\nNOTE: This may not work for all files\nas we look for the technique label (XPS) 10 lines into the datafile", font=("Helvetica", 10)).pack(pady=5)

tk.Button(root, text="Select Folder and Convert All .VMS Files", command=select_directory_and_convert, padx=10, pady=5).pack(pady=20)

root.mainloop()

