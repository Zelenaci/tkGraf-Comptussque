#!/usr/bin/env python3

import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
import matplotlib.pyplot as mp
import matplotlib.colors as mcolors


class Application(tk.Tk):
    name = "TkGraf"
    title_ = "TkGraf"

    def __init__(self):
        super().__init__(className=self.name)
        self.geometry("480x480")
        self.title(self.title_)
        self.bind("<Escape>", self.quit)


        self.fileNameVar = tk.StringVar()
        self.dataOrientVar = tk.StringVar(value="row")
        self.labelVar = tk.StringVar()
        self.axisXVar = tk.StringVar()
        self.axisYVar = tk.StringVar()
        self.colorVar = tk.StringVar()



        self.master_frame = tk.LabelFrame(self, text=self.name, padx=5, pady=5)
        self.file_frame = tk.LabelFrame(self.master_frame, text="Soubor")
        self.option_frame = tk.LabelFrame(self.master_frame, text="Možnosti")



# FIXME master_frame doesn't cover entire app
        self.master_frame.grid(padx=5, pady=5)
        self.file_frame.grid(row=0, sticky="we")
        self.option_frame.grid(row=1, sticky="we")


# FILE FRAME
        self.file_name = tk.Entry(self.file_frame, textvariable=self.fileNameVar, width=40)
        self.file_button = tk.Button(self.file_frame, text="...", command=self.get_file)
        self.file_data_row = tk.Radiobutton(self.file_frame, text="Data v řádcích", variable=self.dataOrientVar, value="row")
        self.file_data_col = tk.Radiobutton(self.file_frame, text="Data ve sloupcích", variable=self.dataOrientVar, value="col")


        self.file_name.grid(row=0,column=0, sticky="e")
        self.file_button.grid(row=0,column=1, sticky="w")
        self.file_data_col.grid(row=1, column=0, sticky="w")
        self.file_data_row.grid(row=2, column=0, sticky="w")
# OPTION FRMAE

        self.option_label = tk.Entry( self.option_frame, textvariable=self.labelVar)
        self.option_axis_x = tk.Entry(self.option_frame, textvariable=self.axisXVar)
        self.option_axis_y = tk.Entry(self.option_frame, textvariable=self.axisYVar)        
        self.label_label = tk.Label(self.option_frame, text="Nadpis: ")
        self.axis_x_label = tk.Label(self.option_frame, text="Popis osy x: ")
        self.axis_y_label = tk.Label(self.option_frame, text="Popis osy y: ") 
        self.line_Cbox = Combobox(self.option_frame)
        self.color_Cbox = Combobox(self.option_frame, textvariable=self.colorVar)
        
        self.interpolation_Cbox = Combobox(self.option_frame)
        self.interpolation_label = tk.Label(self.option_frame, text="Druh interpolace: ") 

        self.color_Cbox.bind("<<ComboboxSelected>>", self.set_canvas_color)

        self.color_canvas = tk.Canvas(self.option_frame, height=20, bg="red", bd=0)

        self.line_Cbox['values'] = [
            "solid (___)",
            "dotted (...)",
            "dashed (---)",
            "dashdot (-.-)"
        ]

        self.color_Cbox['values']= list(mcolors.CSS4_COLORS.keys())


        self.option_label.grid(row=0 , column=1, sticky="e", pady=5)
        self.option_axis_x.grid(row=1, column=1, sticky="e", pady=5)
        self.option_axis_y.grid(row=2, column=1, sticky="e", pady=5)
        self.label_label.grid(row=0 , column=0, sticky="w")
        self.axis_x_label.grid(row=1, column=0, sticky="w")
        self.axis_y_label.grid(row=2, column=0, sticky="w")
        self.interpolation_label.grid(row=3, column=0, sticky="w")
        self.interpolation_Cbox.grid(row=3, column=1, sticky="e", pady=5)
        self.line_Cbox.grid(row=4, column=0, padx=2)
        self.color_Cbox.grid(row=4, column=1, pady=5)
        self.color_canvas.grid(row=5, columnspan=2, pady=5)
        

        #self.dataFormatVar = tk.StringVar(value="row")
#
        #self.fileframe = tk.LabelFrame(self, text="Soubor")
        #self.fileframe.pack()
#
        #self.fileEntry = tk.Entry(self.fileframe)
        #self.fileEntry.pack()
#
        #self.row_radioButton = tk.Radiobutton(
        #    self.fileframe, text="Data in rows", variable=self.dataFormatVar, value="row")
        #self.column_radioButton = tk.Radiobutton(
        #    self.fileframe, text="Data in columns", variable=self.dataFormatVar, value="column")
#
        #self.row_radioButton.pack(anchor="w")
        #self.column_radioButton.pack(anchor="w")

    def get_file(self, event=None):
        self.fileNameVar.set(filedialog.askopenfilename())

    def set_canvas_color(self, event=None):
        self.color_canvas.configure(bg=mcolors.CSS4_COLORS[self.colorVar.get()])

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
