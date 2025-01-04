import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pyswip import Prolog

# Initialize Prolog
prolog = Prolog()
prolog.consult("project.pl")  # Ensure that the file `project.pl` is in the same directory

# Function to check travel
def check_travel():
    start = start_place.get()
    end = end_place.get()
    transport = selected_transport.get()

    if not start or not end:
        messagebox.showwarning("Warning", "Please enter both start and end places!")
        return

    # Prolog queries
    result_text = ""
    text_color = ""

    if transport == "any":
        # Direct travel query
        direct_query = f"path_available_direct('{start}', '{end}', Mode)"
        result_direct = list(prolog.query(direct_query))

        # Indirect travel query
        indirect_query = f"path_available_indirect('{start}', '{end}', Paths)"
        result_indirect = list(prolog.query(indirect_query))

        if result_direct:
            result_text = f"🚗 Direct travel available via:\n{', '.join([str(r['Mode']) for r in result_direct])}"
            text_color = "#58D68D"  # Green
        elif result_indirect:
            result_text = f"🛤️ Indirect travel available via:\n" \
                          f"{', '.join([str(r['Paths']) for r in result_indirect])}"
            text_color = "#5DADE2"  # Blue
        else:
            result_text = "❌ No travel connection available."
            text_color = "#E74C3C"  # Red
    else:
        # Query for a specific mode of transport
        direct_query = f"path_available_direct('{start}', '{end}', '{transport}')"
        result_direct = list(prolog.query(direct_query))

        if result_direct:
            result_text = f"🚗 Direct travel available via {transport}!"
            text_color = "#58D68D"  # Green
        else:
            result_text = f"❌ No direct travel available via {transport}."
            text_color = "#E74C3C"  # Red
            
    # Create a new window for the results
    output_window = tk.Toplevel(root)
    output_window.title("Travel Results")
    output_window.geometry("600x400")
    output_window.configure(bg="#1C2833")  # Dark background for the window

    # Header for the results window
    title_label = tk.Label(
        output_window, text="🌟 Travel Results 🌟",
        font=("Helvetica", 24, "bold"), bg="#2E4053", fg="#F4D03F", pady=10
    )
    title_label.pack(fill="x")

    # Display the result
    result_frame = tk.Frame(output_window, bg="#17202A", bd=10, relief="ridge")
    result_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=250)

    result_label = tk.Label(
        result_frame,
        text=result_text,
        font=("Courier", 16, "bold"),
        bg="#17202A",  # Background for the frame
        fg=text_color,  # Text color
        wraplength=480,
        justify="center"
    )
    result_label.pack(padx=10, pady=10)

# Set up the main window
root = tk.Tk()
root.title("Ultimate Travel Checker")
root.geometry("1000x700")
root.resizable(False, False)

# Add background
background_image = Image.open("calm.jpg")
background_image = background_image.resize((1000, 700), Image.Resampling.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add header
title_label = tk.Label(
    root, text="🌍 Ultimate Travel Checker 🌍",
    font=("Helvetica", 32, "bold"), bg="#222831", fg="#FFD369", pady=10
)
title_label.pack(fill="x")

# Central main frame
main_frame = tk.Frame(root, bg="#EEEEEE", bd=10, relief="ridge")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=800, height=500)

# Input fields
tk.Label(main_frame, text="Start Place:", font=("Arial", 18), bg="#EEEEEE").grid(row=0, column=0, padx=20, pady=20, sticky="w")
start_place = tk.Entry(main_frame, font=("Arial", 16), width=30, relief="solid", bd=2)
start_place.grid(row=0, column=1, padx=20, pady=20)

tk.Label(main_frame, text="End Place:", font=("Arial", 18), bg="#EEEEEE").grid(row=1, column=0, padx=20, pady=20, sticky="w")
end_place = tk.Entry(main_frame, font=("Arial", 16), width=30, relief="solid", bd=2)
end_place.grid(row=1, column=1, padx=20, pady=20)

# Dropdown menu to select transport method
selected_transport = tk.StringVar(value="any")
tk.Label(main_frame, text="Transport:", font=("Arial", 18), bg="#EEEEEE").grid(row=2, column=0, padx=20, pady=20, sticky="w")
transport_menu = tk.OptionMenu(main_frame, selected_transport, "any", "car", "train", "plane")
transport_menu.config(font=("Arial", 14), width=15, bg="#FFD369")
transport_menu.grid(row=2, column=1, padx=20, pady=20)

# Check travel button
check_button = tk.Button(
    main_frame, text="Check Travel 🚀", command=check_travel,
    font=("Arial", 16, "bold"), bg="#FFD369", fg="#222831", width=20, height=2, relief="raised", bd=5
)
check_button.grid(row=3, column=0, columnspan=2, pady=20)

# Add instructions below the Check Travel button
instructions_frame = tk.Frame(main_frame, bg="#DDDDDD", bd=2, relief="solid", width=600, height=150)
instructions_frame.grid(row=4, column=0, columnspan=2, pady=15, padx=10)
instructions_frame.grid_propagate(False)  # Prevent the frame from resizing to fit content

instructions_label = tk.Label(
    instructions_frame,
    text=(
        "💡 *Instructions*:\n"
        "1- Start place and End place should start with a capital letter.\n"
        "2- Enter both places in the text boxes.\n"
        "3- Select a transport method or choose 'any'.\n"
        "4- Press the **Check Travel** button to get your result."
    ),
    font=("Verdana", 12, "bold"),
    bg="#FFFFFF",
    fg="#333333",
    wraplength=580,  # Wrap the text within the frame
    justify="left",
    anchor="nw",
    padx=10,
    pady=10
)
instructions_label.pack(fill="both", expand=True)

# Run the application
root.mainloop()
