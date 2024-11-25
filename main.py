import random , string
import tkinter as tk


def password_gen():
    global min_length_value, want_special, want_digits
    
    chars = letters
    if want_digits:
        chars += digits

    if want_special:
        chars += special

    meets_condition = True
    password = ""

    while len(password) < min_length_value or not meets_condition:
        
        password += random.choice(chars)
        
        meets_condition = True
        
        if password[-1] in digits:
            has_digits = True
            if want_digits:
                meets_condition = has_digits
        
        if password[-1] in special:
            has_special = True
            if want_special:
                meets_condition = has_special and meets_condition
    
    tk.Label(top_level ,text=password).pack()


def get_values():
    global min_length_value,top_level
    
    min_length_value = int(min_length.get())
    
    top_level = tk.Toplevel()
    top_level.title('password gen')
    
    generate = tk.Button(top_level, text='genrate password.', command=password_gen)
    generate.pack()

def digits_show_state():
    want_digits = want_digits_checkbox_state.get()
    return want_digits

letters = string.ascii_letters 
digits = string.digits 
special = string.punctuation 

root = tk.Tk()
root.title('Password Generator')

min_length_label = tk.Label(text='please enter the minimum length for your password.').pack()
min_length = tk.Entry(root)
min_length.pack()

want_digits_checkbox_state = tk.BooleanVar()
want_digits_checkbox = tk.Checkbutton(root, text='Add digits to my password!', variable=want_digits_checkbox_state)
want_digits_checkbox.pack()

want_digits = False
want_special = False
if want_digits_checkbox_state.get():
    want_digits = True
else:
    pass

print(want_digits)

submit_button = tk.Button(root, text='submit', command=get_values)
submit_button.pack()


root.mainloop()