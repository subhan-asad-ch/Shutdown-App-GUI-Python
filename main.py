import os
from tkinter import *
from tkinter import messagebox


def confirm_action(action_name, action_func):
    response = messagebox.askyesno("Confirmation", f"Are you sure you want to perform {action_name}?")
    if response:
        action_func()


def restart():
    os.system("shutdown /r /t 1")


def restart_with_time():
    global time_entry, time_frame, time_instruction_label

    # Create a frame to hold the entry and label
    time_frame = Frame(st, bg="light grey", width=180, height=40)
    time_frame.place(x=110, y=160)

    time_instruction_label = Label(time_frame, text="Enter time in seconds:", font=("Times New Roman", 10),
                                   bg="light grey")
    time_instruction_label.pack()

    time_entry = Entry(time_frame, font=("Times New Roman", 20))
    time_entry.pack()

    time_confirm_button = Button(time_frame, text="Confirm", font=("Times New Roman", 10),
                                 command=confirm_restart_with_time)
    time_confirm_button.pack()


def confirm_restart_with_time():
    try:
        time_in_seconds = int(time_entry.get())
        confirm_action(f"Restart with {time_in_seconds} seconds delay",
                       lambda: os.system(f"shutdown /r /t {time_in_seconds}"))
    except Exception as e:
        print(e)


def log_out():
    confirm_action("Log Out", lambda: os.system("shutdown -l"))


def shutdown():
    confirm_action("Shut Down", lambda: os.system("shutdown /s /t 1"))


def hibernate():
    confirm_action("Hibernate", lambda: os.system("shutdown /h"))


def close_app():
    st.destroy()


st = Tk()

st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="Blue")

r_button = Button(st, text="Restart", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus",
                  command=lambda: confirm_action("Restart", restart))
r_button.place(x=150, y=60, height=50, width=200)

rt_button = Button(st, text="Restart With Time", font=("Times New Roman", 15, "bold"), relief=RAISED, cursor="plus",
                   command=restart_with_time)
rt_button.place(x=150, y=110, height=50, width=200)

lg_button = Button(st, text="LOG-OUT", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus",
                   command=log_out)
lg_button.place(x=150, y=240, height=50, width=200)

Sh_button = Button(st, text="ShutDown", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus",
                   command=shutdown)
Sh_button.place(x=150, y=290, height=50, width=200)

Hib_button = Button(st, text="Hibernate", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus",
                    command=hibernate)
Hib_button.place(x=150, y=340, height=50, width=200)

close_button = Button(st, text="Close", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus",
                      command=close_app)
close_button.place(x=380, y=450, height=40, width=120)

st.mainloop()
