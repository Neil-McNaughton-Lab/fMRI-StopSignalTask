# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:21:06 2021
A simple tkinter GUI. Instead of using an object oriented approach I have 
structured the tkinter script into boxes corresponding to each frame. This 
should make it much easier to understand.

@author: hobrh17p
"""
__version__ = '2.2'

import tkinter as tk

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def pardetGUI():
    global SUB_DATA
    SUB_DATA = {}
    
    width = 500
    height = 300
    
    # root window title and dimension
    root = tk.Tk()
    root.title("Participant details")
    root.geometry(str(width)+'x'+str(height)) # widthxheight
    
    
    
    # %% LEFT BOX frame stacking (Why tkinter, why!?):
    LEFT_FRAME = tk.LabelFrame(root, padx=10, pady=2, 
                               height=height, #Force the frame to have specific dimensions
                               highlightthickness=0, borderwidth=0) #Hide border
    LEFT_FRAME.grid(sticky = tk.N, column=0, row=0)
    
    
    
    # %% Participant Number Entry Field:
    participant_frame = tk.LabelFrame(LEFT_FRAME, padx=10, pady=2)
    participant_frame.grid(sticky = tk.W, column=0, row=0)
    
    # adding a label to the frame
    participant_lbl = tk.Label(participant_frame, text="Number")
    participant_lbl.grid()
     
    # adding Entry Field
    txt = tk.Entry(participant_frame, width=20)
    txt.grid(column=1, row=0)
        
    # adding blank space to the frame because tkinter is stupid
    participan_blank = tk.Label(participant_frame, text = " "*11)
    participan_blank.grid(column=2, row=0)
    
    
    # %% Gender Select, Radio Buttons:
    '''
    gender_frame = tk.LabelFrame(LEFT_FRAME, padx=10, pady=2)
    gender_frame.grid(column=0, row=1)
    
    # adding a label to the frame
    gender_lbl = tk.Label(gender_frame, text = "Sex recorded at birth: ")
    gender_lbl.pack(side=tk.LEFT)
    
    # Creating the information corresponding to each radio button:
    GENDER_MODES = [
        ('Female', 0),
        ('Male', 1)
        ]
    
    # Creating the tk storage variable for the radiobutton choice:
    gender = tk.IntVar()
    gender.set(2)
    
    # Build an invisible radio button to be the default:
    tk.Radiobutton(gender_frame, text='', variable=gender, value=2)
    
    # Build each radio button:
    for text, mode in GENDER_MODES: #for i, text, mode in enumerate(GENDER_MODES):
        tk.Radiobutton(gender_frame, text=text, variable=gender, value=mode).pack(side=tk.LEFT)
    '''
    
    
    
    # %% Handedness Select, Radio Buttons:
    handedness_frame = tk.LabelFrame(LEFT_FRAME, padx=10, pady=2)
    handedness_frame.grid(sticky = tk.W, column=0, row=2)
    
    # adding a label to the frame
    hand_lbl = tk.Label(handedness_frame, text = "Handedness")
    hand_lbl.pack(side=tk.LEFT)
    
    # Creating the information corresponding to each radio button:
    HAND_MODES = [
        ('Left', 0),
        ('Right', 1)
        ]
    
    # Creating the tk storage variable for the radiobutton choice:
    hand = tk.IntVar()
    hand.set(1)
    
    # Build each radio button:
    for text, mode in HAND_MODES: #for i, text, mode in enumerate(GENDER_MODES):
        tk.Radiobutton(handedness_frame, text=text, variable=hand, value=mode).pack(side=tk.LEFT)
        
    # adding blank space to the frame because tkinter is stupid
    hand_blank = tk.Label(handedness_frame, text = " "*11)
    hand_blank.pack(side=tk.LEFT)
    
    # %% Error Message Region:
    # String Variable for the error message:
    error_text = tk.StringVar()
    
    # Label Widget to display the error message:
    error_lbl = tk.Label(LEFT_FRAME, anchor='w', textvariable=error_text, fg='red')
    error_lbl.grid(sticky=tk.W)
    
    #Update the error text:
    error_text.set('')
    
    
    # %% Ethnicity Selection:
    # function to carry out when the button is clicked
    ethnicity_frame = tk.LabelFrame(root, padx=10, pady=2)
    ethnicity_frame.grid(sticky = tk.E, column=1, row=0)
    
    
    # Adding a label to the frame
    ethn_lbl = tk.Label(ethnicity_frame, text = "Which ethnic group do you belong to?")
    ethn_lbl.grid(column=0, row=0)
    
    ETHNICITIES = ('New Zealand European',
                   'Maori',
                   'Samoan',
                   'Cook Island Maori',
                   'Tongan',
                   'Niuean',
                   'Chinese',
                   'Indian',
                   'Other, eg DUTCH, JAPANESE,\nTOKELAUAN. Please state:') #Must be last
                   
    ethns = []
    for i, text in enumerate(ETHNICITIES):
        var = tk.IntVar()
        text = text.replace('Maori', 'Ma'+ "\u0304" + 'ori')
        tk.Checkbutton(ethnicity_frame, text=text, variable=var).grid(sticky = tk.W, column=0, row=i+1)
        ethns.append(var)
    
      
    # Other option text input:
    other_txt = tk.Entry(ethnicity_frame, width=30)
    other_txt.grid(sticky = tk.W, column=0, row=len(ETHNICITIES)+1)
    
    
    # Get frame dimensions (won't give correct values until the frame is unpacked):
    ethnicity_frame.update()
    ethnicity_frame.x = ethnicity_frame.winfo_reqwidth()
    ethnicity_frame.y = ethnicity_frame.winfo_reqheight()
    
    
    # %% Disable sound settings:
    # tick widget 
    sound_var = tk.IntVar()
    sound = tk.Checkbutton(root, text='Enable Sound Test', variable=sound_var)
    
    # Set the sounds variable to ticked:
    sound_var.set(1)
    
    # Get button pixel width and height:
    sound.w = sound.winfo_reqwidth()
    sound.h = sound.winfo_reqheight()
    
    #Set the position of the button's top-left corner:
    x = 120 
    y = height-sound.h-(height-ethnicity_frame.y)
    sound.place(x=x, y=y) 
    
    
    
    # %% Enter Button:
    # function to carry out when the button is clicked
    def clicked():
        global SUB_DATA
        exit_condition = True
        
        # Organise ethnicities:
        chosen_ethnicities = tuple(i.get() for i in ethns)
        ethnicities = [ETHNICITIES[i] for i, ethn in enumerate(chosen_ethnicities) if ethn == 1]
        ethnicities = ', '.join(ethnicities + [other_txt.get()])
        if ethnicities[-2:] == ', ':
            ethnicities = ethnicities[:-2]
        
        # # Organise gender:
        # gender_index = gender.get()
        # if gender_index == 2:
        #     gender_index = 0
        
        # Store:
        SUB_DATA = {"participant": txt.get(),
                    #"gender": GENDER_MODES[gender_index][0],
                    "handedness": HAND_MODES[hand.get()][0],
                    "ethnicities": ethnicities,
                    "soundtest": sound_var.get()
                    }
            
        # Check there are no chosen ethnicities:
        if sum(chosen_ethnicities) == 0:
            error_text.set("Please enter at least one ethnicity.")
            exit_condition = False
            
        # Check if the subject entered numbers into the other box:
        if hasNumbers(other_txt.get()):
            error_text.set("Ethnicities aren't spelt with numbers!")
            exit_condition = False 
            
        # Check if the "other" entry box is empty:
        if chosen_ethnicities[-1] == 1 and other_txt.get() == '':
            error_text.set("Please enter an ethnicity\n into the box below \"other\".")
            exit_condition = False
        
        # # Check if the participant number entry box is empty:
        # if gender.get() == 2:
        #     error_text.set("Please input the sex recorded on your birth certificate when you were born.")
        #     exit_condition = False
            
        # Check if the participant number entry box is not a number:
        if txt.get() == '':
            error_text.set("Please enter your participant number.")
            exit_condition = False
            
        
        # Check if it's ok to close the window:
        if exit_condition:
            root.destroy() #Close the tkinter window
        
    
    # button widget 
    btn = tk.Button(root, text="Enter", fg="black", command=clicked)
    
    # Set button size:
    btn.configure(height = 1, width = 10)
    
    # Get button pixel width and height:
    btn.w = btn.winfo_reqwidth()
    btn.h = btn.winfo_reqheight()
    
    #Set the position of the button's top-left corner:
    x = 10 
    y = height-btn.h-(height-ethnicity_frame.y)
    btn.place(x=x, y=y)     
    
    
    
    # %% Define the windows red-X exit behaviour:
    def exit_function():
        global SUB_DATA
        SUB_DATA = {"participant": '',
                    "gender": None,
                    "handedness": None,
                    "ethnicities": None,
                    "soundtest": 100 #<- Used as an exit flag inside psychopy
                    }
        root.destroy()
    
    root.protocol('WM_DELETE_WINDOW', exit_function)
        
    
    
    # %% Execute Tkinter:
    root.mainloop()
    
    # Deleting the global variable now that I'm done with it:
    sub_data = SUB_DATA
    del SUB_DATA
    return sub_data


