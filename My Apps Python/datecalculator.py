
# import tkinter as tk
# from tkinter import messagebox
# from datetime import date

# def calculate_days():
#     try:
#         # Get and convert inputs for the first date
#         day1 = int(entry_day1.get())
#         month1 = int(entry_month1.get())
#         year1 = int(entry_year1.get())
#         first_date = date(year1, month1, day1)
        
#         # Get and convert inputs for the second date
#         day2 = int(entry_day2.get())
#         month2 = int(entry_month2.get())
#         year2 = int(entry_year2.get())
#         second_date = date(year2, month2, day2)
        
#         # Calculate the difference in days between the two dates
#         delta = second_date - first_date
#         label_result.config(text=f"Difference: {delta.days} day(s)")
#     except ValueError as e:
#         messagebox.showerror("Invalid Input", f"Error: {e}")

# # Set up the main application window
# root = tk.Tk()
# root.title("Days Calculator")

# # Create a frame for the first date input
# frame_first = tk.LabelFrame(root, text="First Date (YYYY-MM-DD)")
# frame_first.pack(padx=10, pady=5, fill="x")

# tk.Label(frame_first, text="Day:").grid(row=0, column=0, padx=5, pady=5)
# entry_day1 = tk.Entry(frame_first, width=5)
# entry_day1.grid(row=0, column=1, padx=5, pady=5)

# tk.Label(frame_first, text="Month:").grid(row=0, column=2, padx=5, pady=5)
# entry_month1 = tk.Entry(frame_first, width=5)
# entry_month1.grid(row=0, column=3, padx=5, pady=5)

# tk.Label(frame_first, text="Year:").grid(row=0, column=4, padx=5, pady=5)
# entry_year1 = tk.Entry(frame_first, width=7)
# entry_year1.grid(row=0, column=5, padx=5, pady=5)

# # Create a frame for the second date input
# frame_second = tk.LabelFrame(root, text="Second Date (YYYY-MM-DD)")
# frame_second.pack(padx=10, pady=5, fill="x")

# tk.Label(frame_second, text="Day:").grid(row=0, column=0, padx=5, pady=5)
# entry_day2 = tk.Entry(frame_second, width=5)
# entry_day2.grid(row=0, column=1, padx=5, pady=5)

# tk.Label(frame_second, text="Month:").grid(row=0, column=2, padx=5, pady=5)
# entry_month2 = tk.Entry(frame_second, width=5)
# entry_month2.grid(row=0, column=3, padx=5, pady=5)

# tk.Label(frame_second, text="Year:").grid(row=0, column=4, padx=5, pady=5)
# entry_year2 = tk.Entry(frame_second, width=7)
# entry_year2.grid(row=0, column=5, padx=5, pady=5)

# # Button to trigger the calculation
# button_calculate = tk.Button(root, text="Calculate Days", command=calculate_days)
# button_calculate.pack(padx=10, pady=10)

# # Label to display the result
# label_result = tk.Label(root, text="Difference: ")
# label_result.pack(padx=10, pady=10)

# root.mainloop()
