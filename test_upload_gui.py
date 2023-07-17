import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

from pathlib import Path
from datetime import datetime
import glob

import mass.mass_measurement as mass_measurement
import metrology.metrology_measurement as metrology_measurement
import metrology.output_metrology as output_metrology

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
        self.root.geometry("1100x900")

        self.root.title("Metrology Test")

        self.frame.destroy()
        self.frame = tk.Frame(self.root)
        self.frame.pack()


        self.file_selector_button = tk.Button(self.frame, text="Choose a file",font=("Arial", 16),command=self.select_file)
        self.file_selector_button.grid(row=0, column=0, padx=5, pady=30,sticky="EW")

        self.file_selector_label = tk.Label(self.frame, text="-", font=("Arial", 16))
        self.file_selector_label.grid(row=0, column=1, padx=5, pady=30, sticky="EW")


        self.Jig_file_selector_button = tk.Button(self.frame, text="Choose a Jig file",font=("Arial", 16),command=self.select_Jig_file)
        self.Jig_file_selector_button.grid(row=1, column=0, padx=5, pady=30,sticky="EW")

        self.Jig_file_selector_label = tk.Label(self.frame, text="-", font=("Arial", 16))
        self.Jig_file_selector_label.grid(row=1, column=1, padx=5, pady=30, sticky="EW")


        self.serial_label = tk.Label(self.frame, text="Serial Number", font=("Arial", 16))
        self.serial_label.grid(row=2, column=0, padx=5, pady=30, sticky="EW")

        self.serial_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.serial_entry.grid(row=2, column=1, padx=5, pady=30,sticky="EW")



        self.component_options = [
            "Bare Module",
            "Flex",
            "Assembled Module"
            ]


        self.component_type_label = tk.Label(self.frame, text="Component type", font=("Arial", 16))
        self.component_type_label.grid(row=3, column=0, padx=5, pady=30, sticky="EW")

        self.component_type = tk.StringVar()
  
        self.component_type_menu = tk.OptionMenu( self.frame , self.component_type , *self.component_options )
        self.component_type_menu.grid(row=3, column=1, padx=5, pady=30,sticky="EW")


        self.run_label = tk.Label(self.frame, text="Run Number", font=("Arial", 16))
        self.run_label.grid(row=4, column=0, padx=5, pady=30, sticky="EW")

        self.run_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.run_entry.grid(row=4, column=1, padx=5, pady=30,sticky="EW")


        self.analysis_version_label = tk.Label(self.frame, text="Analysis Version", font=("Arial", 16))
        self.analysis_version_label.grid(row=5, column=0, padx=30, pady=5, sticky="EW")

        self.analysis_version_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.analysis_version_entry.grid(row=5, column=1, padx=5, pady=20,sticky="EW")


        self.rename_file_query = tk.IntVar()
        self.checkbox_rename_file = tk.Checkbutton(self.frame, text='Rename File',variable=self.rename_file_query, onvalue=1, offvalue=0)
        self.checkbox_rename_file.grid(row=6, column=1, padx=5, pady=30, sticky="EW")


        self.save_button = tk.Button(self.frame, text="Save", font=("Arial", 16), command=self.save_metrology_test)
        self.save_button.grid(row=7,column=1,padx=10,pady=30)



    def show_message(self):
        #file = filedialog.askopenfilename(initialdir="./",title="Select a file",filetypes=(("Text files","*.txt"),("all files","*.*")))
        if self.check_state.get() == 0:
            print(self.text.get("1.0",tk.END))
        else:
            messagebox.showinfo("Message",self.text.get("1.0",tk.END))


    def save_mass_test(self):
        serial = self.serial_entry.get()
        mass = self.mass_entry.get()
        run = self.run_entry.get()
        analysis_version = self.analysis_version_entry.get()
        
        
        date = datetime.now().strftime("%m-%d-%Y")
        path = Path("./results", date)
        path = mass_measurement.add_folder(path)

        json_path = mass_measurement.add_folder(Path(path,"json_data"))
        file_name = "mass_measurement_"+datetime.now().strftime("%m_%d_%y")+".csv"
        output_file = Path(path,file_name)
        mass_measurement.create_mass_csv_file(output_file)

        scale_accuracy = 0.1

        mass_measurement.add_data_csv(output_file,serial,mass,scale_accuracy,run,analysis_version)
        mass_measurement.add_data_json(json_path,serial,mass,scale_accuracy,run,analysis_version)


    def save_metrology_test(self):
        serial = self.serial_entry.get()
        component_type = self.component_type.get()
        run = self.run_entry.get()
        analysis_version = self.analysis_version_entry.get()
        rename_file = self.rename_file_query.get()
        input_file = self.input_file
        input_Jig_file = self.input_Jig_file

        #if input_file == None:
        #    messagebox.showinfo("Message","No file selected")
        #    return
        #print(component_type)


        date = datetime.now().strftime("%m-%d-%Y")
        path = Path("./results", date)
        path = metrology_measurement.add_folder(path)

        json_path = metrology_measurement.add_folder(Path(path,"json_data"))
        file_name = "metrology_test_"+datetime.now().strftime("%m_%d_%y")+".csv"
        output_csv_file = Path(path,file_name)
        metrology_measurement.create_metrology_csv_file(output_csv_file)



        if component_type=="Flex":
            metrology_measurement.flexMeasurement(serial,input_file,input_Jig_file,output_csv_file,json_path)
        elif component_type =="Assembled Module":
            metrology_measurement.assemblyMeasurement(input_file,input_Jig_file)
        elif component_type == "Bare Module":
            metrology_measurement.BMMeasurement(serial,input_file, input_Jig_file, output_csv_file, json_path)



    def select_file(self):
        self.input_file = filedialog.askopenfilename(initialdir="./",title="Select a file",filetypes=(("Text files","*.txt"),("all files","*.*")))
        print(self.input_file)

        self.file_selector_label.destroy()
        self.file_selector_label = tk.Label(self.frame, text=self.input_file.split("/")[-1], font=("Arial", 16))
        self.file_selector_label.grid(row=0, column=1, padx=5, pady=30, sticky="EW")

    def select_Jig_file(self):
        self.input_Jig_file = filedialog.askopenfilename(initialdir="./",title="Select a file",filetypes=(("Text files","*.txt"),("all files","*.*")))
        print(self.input_file)

        self.Jig_file_selector_label.destroy()
        self.Jig_file_selector_label = tk.Label(self.frame, text=self.input_Jig_file.split("/")[-1], font=("Arial", 16))
        self.Jig_file_selector_label.grid(row=1, column=1, padx=5, pady=30, sticky="EW")

TestUploadGUI()