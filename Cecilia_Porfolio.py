from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # Import Pillow's Image and ImageTk
import webbrowser #import module to open a URL in default web browser


#main window
window=Tk() 
window.geometry("800x800")
window.title("Cecilia's Portfolio")
window.config(background="lavender")

#creating notebook- tab system
notebook=ttk.Notebook(window)

#create the tab frames 
tab1= Frame(notebook,bg="#043927")
tab2=Frame(notebook,bg="white")
tab3=Frame(notebook,bg="white")
tab4=Frame(notebook,bg="white")

#add tabs to notebook
notebook.add(tab1,text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3,text="Tab 3")
notebook.add(tab4, text="Tab 4")

#------------------------------------------------------------------------------------------------------------------------------

# Tab 1 content - Intro
# Load and resize the image
image = Image.open("Images/picture.JPG")
image = image.resize((800, 800))
photo = ImageTk.PhotoImage(image)

# Background image (placed first)
background_label = Label(tab1, image=photo)
background_label.image = photo
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# "PORTFOLIO" title in the center, lower on the screen
title_label = Label(
    tab1,
    text="PORTFOLIO",
    font=("Century Gothic", 40, "bold"),
    bg="#705689",  
    fg="#FFFFFF"
)
title_label.place(relx=0.5, rely=0.50, anchor="center")
name_label = Label(
    tab1,
    text="Cecilia Martinez",
    font=("Century Gothic", 14, "italic"),
    bg="#EDDDFC",  
    fg="#FFFFFF"
)
name_label.place(relx=0.98, rely=0.98, anchor="se")  # Slight offset from the edge



#------------------------------------------------------------------------------------------------------------------------------------
# Tab 2
# Functions for each project (they can be expanded later)
def project_car_game():
    for widget in tab2.winfo_children():
        widget.destroy()
    
    #  background color for the car game project
    tab2.config(bg="#E1C7FA")
    
    Label(tab2, text="3D Car Game in Unity – Rocky Road", font=("Arial", 20, "bold"), bg="#E1C7FA").pack(pady=20)
    Label(tab2, text="Project Overview: A Unity-based car game featuring a rocky road track with obstacles and increasing difficulty.",
          font=("Arial", 14), wraplength=700, justify="center", bg="#E1C7FA").pack(pady=10)
    Label(tab2, text="Features:\n- Dynamic car movement\n- Real-time collision detection\n- Increasing difficulty with each level",
          font=("Arial", 14), wraplength=700, justify="left", bg="#E1C7FA").pack(pady=10)
    Button(tab2, text="Back to Projects", command=show_main_content, font=("Arial", 12), width=20, fg="#F4A300").pack(pady=10)
    # --- Image 1 (Bottom-left) ---
    img1 = Image.open("Images/MainMenu.png")
    img1 = img1.resize((430, 400))  
    img1_photo = ImageTk.PhotoImage(img1)

    img1_label = Label(tab2, image=img1_photo, bg="#E1C7FA")
    img1_label.image = img1_photo
    img1_label.place(x=0, rely=1.0, anchor='sw')  # bottom-left corner
    
    
    # --- Image 2 (Bottom-right) ---
    img3 = Image.open("Images/codesnippet2.png")
    img3 = img3.resize((300, 280)) 
    img3_photo = ImageTk.PhotoImage(img3)

    img3_label = Label(tab2, image=img3_photo, bg="#E1C7FA")
    img3_label.image = img3_photo
    img3_label.place(x=tab2.winfo_width() * 2 // 3 - 50, rely=1.0, anchor='sw')  # bottom-center-right
def project_python_portfolio():
    for widget in tab2.winfo_children():
        widget.destroy()
    
    # background color for the Python portfolio project to lighter yellow
    tab2.config(bg="#F7D380")
    
    Label(tab2, text="Python Portfolio", font=("Arial", 20, "bold"), bg="#F7D380").pack(pady=20)
    Label(tab2, text="Project Overview: A collection of Python projects demonstrating different programming concepts, "
                     "including algorithms, data structures, and applications.",
          font=("Arial", 14), wraplength=700, justify="center", bg="#F7D380").pack(pady=10)
    Label(tab2, text="Features:\n- Data manipulation\n- Algorithm design\n- Application development using Python",
          font=("Arial", 14), wraplength=700, justify="left", bg="#F7D380").pack(pady=10)
    Button(tab2, text="Back to Projects", command=show_main_content, font=("Arial", 12), width=20, fg="#F4A300").pack(pady=20)


def project_real_estate():
    for widget in tab2.winfo_children():
        widget.destroy()
    
    # background color for the Real Estate Web App project
    tab2.config(bg="#A2D5F2")
    
    Label(tab2, text="Real Estate Web App (Zillow-style)", font=("Arial", 20, "bold"), bg="#A2D5F2").pack(pady=20)
    Label(tab2, text="Project Overview: A web application inspired by Zillow, made with a group of software developers. "
                     "Allows users to search for properties, view listings, and get real estate market data.",
          font=("Arial", 14), wraplength=700, justify="center", bg="#A2D5F2").pack(pady=10)
    Label(tab2, text="Features:\n- Property search\n- Interactive maps\n- Market data analysis",
          font=("Arial", 14), wraplength=700, justify="left", bg="#A2D5F2").pack(pady=10)
    Button(tab2, text="Back to Projects", command=show_main_content, font=("Arial", 12), width=20, fg="#F4A300").pack(pady=20)
  
    real_state_img = Image.open("Images/RealState.png") 
    real_state_img = real_state_img.resize((240, 220))   
    real_state_photo = ImageTk.PhotoImage(real_state_img)

    real_state_label = Label(tab2, image=real_state_photo, bg="#A2D5F2")
    real_state_label.image = real_state_photo  # Prevent garbage collection
    real_state_label.place(x=10, rely=1.0, anchor='sw')  # Bottom-left corner
    # --- CodeSnippet Image (Big & Bottom-right) ---
    code_snippet_img = Image.open("Images/CodeSnippet.png")
    code_snippet_img = code_snippet_img.resize((500, 300)) 
    code_snippet_photo = ImageTk.PhotoImage(code_snippet_img)

    code_snippet_label = Label(tab2, image=code_snippet_photo, bg="#A2D5F2")
    code_snippet_label.image = code_snippet_photo
    code_snippet_label.place(x=tab2.winfo_width() +30, rely=.90, anchor='se')  # bottom-right corner
# Function to display main project list
def show_main_content():
    for widget in tab2.winfo_children():
        widget.destroy()
    
    # Reload the background image
    image_path = "Images/ComputerInfo.JPG"
    photo = Image.open(image_path)
    photo = photo.resize((800, 800))
    photo = ImageTk.PhotoImage(photo)
    
    photo_label = Label(tab2, image=photo, bg="white")
    photo_label.image = photo
    photo_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(tab2, text="My Projects", font=("Arial", 22, "bold"), bg="black").pack(pady=20)
    
    
    # Project title buttons
    Button(tab2, text="3D Car Game in Unity – Rocky Road", command=project_car_game, font=("Arial", 15), width=35).pack(pady=10)
    Button(tab2, text="Python Portfolio", command=project_python_portfolio, font=("Arial", 15), width=35).pack(pady=10)
    Button(tab2, text="Real Estate Web App (Zillow-style)", command=project_real_estate, font=("Arial", 15), width=35).pack(pady=10)

# Initialize Tab 2
show_main_content()


#------------------------------------------------------------------------------------------------------------------------------------
# Tab 3 - Resume content


def project_resume():
    # Clear existing widgets in tab3
    for widget in tab3.winfo_children():
        widget.destroy()
    
   
    resume_img = Image.open("Images/Resume.png")
    resume_img = resume_img.resize((800, 800))  
    resume_photo = ImageTk.PhotoImage(resume_img)

    # Set the background image on the tab
    background_label = Label(tab3, image=resume_photo)
    background_label.image = resume_photo  
    background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch the image to cover the whole tab
    
   
# Call the function to display the resume image when you need
project_resume()


#------------------------------------------------------------------------------------------------------------------------------------
# Tab 4 - Contact Info content

def open_link(url):
    webbrowser.open(url) # Opens the URL in the default web browser
    
Label(tab4).pack(pady=20)


#picture for tab4
contactpic="Images/Contactpic.png"
background_image = Image.open(contactpic)
background_image = background_image.resize((800, 800))  
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(tab4, image=background_photo)
background_label.image = background_photo # Retain reference to prevent garbage collection
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire tab

# Frame for contact info (overlay on the background)
contact_frame = Frame(tab4, bg="#B5CEB4", bd=10,)  # Semi-transparent background
contact_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.5)  # Center with relative size

# Add contact information
Button(contact_frame, text="Email: Cecyy917@gmail.com", font=("Consola", 14), bg="pink").pack(pady=15)
Button(contact_frame, text="Phone Number: (424)391-9001", font=("Consola", 14), bg="pink").pack(pady=15)
Button(contact_frame,text="Linkedin: https://linkedin.com/in/username",font=("Consola", 14), bg="pink",
    command=lambda: open_link("https://linkedin.com/in/username"),).pack(pady=15)
Button( contact_frame,text="GitHub: https://github.com/cecyy1",font=("Consola", 14),bg="pink",
    command=lambda: open_link("https://github.com/cecyy1"),).pack(pady=15)


# Notebook pack in window
notebook.pack(expand=True, fill="both")

window.mainloop()