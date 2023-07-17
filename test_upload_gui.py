import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk


class TestUploadGUI:

    def __init__(self):

        #Create window
        self.root = tk.Tk()
        self.root.title("Test Upload Tool")
        self.root.geometry("500x500")

        # Create menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.fileMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.fileMenu)

        self.fileMenu.add_command(label="Mass Test", command=self.mass_test)
        self.fileMenu.add_command(label="Metrology Test", command=self.metrology_test)

        #Run frame configuration
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.main_menu()
        #self.mass_test()

        # Run main loop
        self.root.mainloop()




    def main_menu(self):

        self.label = tk.Label(self.frame, text="Test Upload App", font=("Arial", 16))
        self.label.pack(padx=10,pady=10)





    def mass_test(self):
        self.root.geometry("900x900")

        self.root.title("Mass Test")

        self.frame.destroy()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        

        self.serial_label = tk.Label(self.frame, text="Serial Number", font=("Arial", 16))
        self.serial_label.grid(row=0, column=0, padx=5, pady=30, sticky="EW")

        self.serial_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.serial_entry.grid(row=0, column=1, padx=5, pady=30,sticky="EW")


        self.mass_label = tk.Label(self.frame, text="Mass", font=("Arial", 16))
        self.mass_label.grid(row=1, column=0, padx=5, pady=30, sticky="EW")

        self.mass_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.mass_entry.grid(row=1, column=1, padx=5, pady=30,sticky="EW")


        self.run_label = tk.Label(self.frame, text="Run Number", font=("Arial", 16))
        self.run_label.grid(row=2, column=0, padx=5, pady=30, sticky="EW")

        self.run_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.run_entry.grid(row=2, column=1, padx=5, pady=30,sticky="EW")


        self.analysis_version_label = tk.Label(self.frame, text="Analysis Version", font=("Arial", 16))
        self.analysis_version_label.grid(row=3, column=0, padx=30, pady=5, sticky="EW")

        self.analysis_version_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.analysis_version_entry.grid(row=3, column=1, padx=5, pady=20,sticky="EW")


        self.save_button = tk.Button(self.frame, text="Save", font=("Arial", 16), command=self.save_mass_test)
        self.save_button.grid(row=4,column=1,padx=10,pady=30)





    def metrology_test(self):
        self.root.geometry("900x900")

        self.root.title("Metrology Test")

        self.frame.destroy()
        self.frame = tk.Frame(self.root)
        self.frame.pack()


        self.serial_label = tk.Label(self.frame, text="Serial Number", font=("Arial", 16))
        self.serial_label.grid(row=0, column=0, padx=5, pady=30, sticky="EW")

        self.serial_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.serial_entry.grid(row=0, column=1, padx=5, pady=30,sticky="EW")



        self.component_options = [
            "Bare Module",
            "Flex",
            "Assembled Module"
            ]


        self.component_type_label = tk.Label(self.frame, text="Mass", font=("Arial", 16))
        self.component_type_label.grid(row=1, column=0, padx=5, pady=30, sticky="EW")

        self.component_type = tk.StringVar()
  
        self.component_type_menu = tk.OptionMenu( self.frame , self.component_type , *self.component_options )
        self.component_type_menu.grid(row=1, column=1, padx=5, pady=30,sticky="EW")


        self.run_label = tk.Label(self.frame, text="Run Number", font=("Arial", 16))
        self.run_label.grid(row=2, column=0, padx=5, pady=30, sticky="EW")

        self.run_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.run_entry.grid(row=2, column=1, padx=5, pady=30,sticky="EW")


        self.analysis_version_label = tk.Label(self.frame, text="Analysis Version", font=("Arial", 16))
        self.analysis_version_label.grid(row=3, column=0, padx=30, pady=5, sticky="EW")

        self.analysis_version_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.analysis_version_entry.grid(row=3, column=1, padx=5, pady=20,sticky="EW")


        self.rename_file_query = tk.IntVar()
        self.checkbox_rename_file = tk.Checkbutton(self.frame, text='Rename File',variable=self.rename_file_query, onvalue=1, offvalue=0)
        self.checkbox_rename_file.grid(row=4, column=1, padx=5, pady=30, sticky="EW")


        self.save_button = tk.Button(self.frame, text="Save", font=("Arial", 16), command=self.save_metrology_test)
        self.save_button.grid(row=5,column=1,padx=10,pady=30)



    def show_message(self):
        #file = filedialog.askopenfilename(initialdir="./",title="Select a file",filetypes=(("Text files","*.txt"),("all files","*.*")))
        if self.check_state.get() == 0:
            print(self.text.get("1.0",tk.END))
        else:
            messagebox.showinfo("Message",self.text.get("1.0",tk.END))


    def save_mass_test(self):
        pass

    def save_metrology_test(self):
        pass

TestUploadGUI()