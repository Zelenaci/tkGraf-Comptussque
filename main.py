#!/usr/bin/env python3

import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
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
        self.labelVar = tk.StringVar(value="")
        self.axisXVar = tk.StringVar(value="")
        self.axisYVar = tk.StringVar(value="")
        self.lineVar = tk.StringVar(value="-")
        self.markerVar = tk.StringVar(value=None)
        self.colorVar = tk.StringVar(value="red")

        self.master_frame = tk.LabelFrame(self, text=self.name, padx=5, pady=5)
        self.file_frame = tk.LabelFrame(self.master_frame, text="Soubor")
        self.option_frame = tk.LabelFrame(self.master_frame, text="Možnosti")


# FIXME master_frame doesn't cover entire app
        self.master_frame.grid(padx=5, pady=5)
        self.file_frame.grid(row=0, sticky="we")
        self.option_frame.grid(row=1, sticky="we")


# FILE FRAME
        self.file_name_entry = tk.Entry(
            self.file_frame, textvariable=self.fileNameVar, width=40)
        self.file_button = tk.Button(
            self.file_frame, text="...", command=self.set_file)
        self.file_data_row = tk.Radiobutton(
            self.file_frame, text="Data v řádcích", variable=self.dataOrientVar, value="row")
        self.file_data_col = tk.Radiobutton(
            self.file_frame, text="Data ve sloupcích", variable=self.dataOrientVar, value="col")
        self.plot_button = tk.Button(self.option_frame, text="PLOT", command=self.plot)

        self.file_name_entry.grid(row=0, column=0, sticky="e")
        self.file_button.grid(row=0, column=1, sticky="w")
        self.file_data_col.grid(row=1, column=0, sticky="w")
        self.file_data_row.grid(row=2, column=0, sticky="w")
        self.plot_button.grid(row=8)
# OPTION FRAME

        self.option_label = tk.Entry(
            self.option_frame, textvariable=self.labelVar)
        self.label_label = tk.Label(self.option_frame, text="Nadpis: ")
        self.axis_x_label = tk.Label(self.option_frame, text="Popis osy x: ")
        self.axis_y_label = tk.Label(self.option_frame, text="Popis osy y: ")
        self.line_label = tk.Label(self.option_frame, text="Druh čáry: ")
        self.color_label = tk.Label(self.option_frame, text="Barva čáry: ")
        self.marker_label = tk.Label(self.option_frame, text="Druh bodu: ")

        self.option_axis_x = tk.Entry(
            self.option_frame, textvariable=self.axisXVar)
        self.option_axis_y = tk.Entry(
            self.option_frame, textvariable=self.axisYVar)
        self.line_Cbox = Combobox(self.option_frame, textvariable=self.lineVar)
        self.color_Cbox = Combobox(
            self.option_frame, textvariable=self.colorVar)

        self.interpolation_Cbox = Combobox(self.option_frame)
        self.interpolation_label = tk.Label(
            self.option_frame, text="Druh interpolace: ")

        self.color_Cbox.bind("<<ComboboxSelected>>", self.set_canvas_color)

        self.color_canvas = tk.Canvas(
            self.option_frame, height=20, bg="red", bd=0)

        self.line_Cbox['values'] = list(plt.Line2D.lineStyles.keys())[:4]

        self.color_Cbox['values'] = list(mcolors.CSS4_COLORS.keys())

        self.marker_Cbox = Combobox(self.option_frame, textvariable=self.markerVar)
        self.marker_Cbox['values'] = list(plt.Line2D.markers.keys())[:-7]

        self.option_label.grid(row=0, column=1, sticky="e", pady=5)
        self.label_label.grid(row=0, column=0, sticky="w")

        self.axis_x_label.grid(row=1, column=0, sticky="w")
        self.axis_y_label.grid(row=2, column=0, sticky="w")
        self.interpolation_label.grid(row=3, column=0, sticky="w")
        self.line_label.grid(row=4, column=0, sticky="w")
        self.marker_label.grid(row=5, column=0, sticky="w")
        self.color_label.grid(row=6, column=0, sticky="w")

        self.option_axis_x.grid(row=1, column=1, sticky="e", pady=2)
        self.option_axis_y.grid(row=2, column=1, sticky="e", pady=2)
        self.interpolation_Cbox.grid(row=3, column=1, sticky="e", pady=2)
        self.line_Cbox.grid(row=4, column=1, sticky="e", pady=2)
        self.marker_Cbox.grid(row=5, column=1, sticky="e", pady=2)
        self.color_Cbox.grid(row=6, column=1, sticky="e", pady=2)

        self.color_canvas.grid(row=7, columnspan=2,
                               sticky="we", padx=20, pady=5)

    def set_file(self, event=None):
        file = filedialog.askopenfilename()
        self.fileNameVar.set(file)
        
    def get_file(self, event=None):    
        file = self.fileNameVar.get()
        return file

    def set_canvas_color(self, event=None):
        self.color_canvas.configure(
            bg=mcolors.CSS4_COLORS[self.colorVar.get()])

    def read_data_row(self, file, event=None):
        x_vals = []
        y_vals = []
        with open(file) as f:
            for row in f:
                x, y = map(int,row.split(','))
                x_vals.append(x)
                y_vals.append(y)
        return x_vals, y_vals

    def read_data_col(self, file, event=None):
        x_vals = []
        y_vals = []
        vals = [x_vals, y_vals]
        f.readlines(1).split(',')
        return x_vals, y_vals


    def plot(self, event=None):

        file = self.get_file()
        print(file)
        if os.path.exists(file):

            if self.dataOrientVar.get() == "row":
                x_vals, y_vals = self.read_data_row(file)
            else:
                x_vals, y_vals = self.read_data_col(file)

            plt.plot(x_vals, y_vals, linestyle=self.lineVar.get(), marker=self.markerVar.get(), color=self.colorVar.get())
            plt.title(self.labelVar.get())
            plt.xlabel(self.axisXVar.get())
            plt.ylabel(self.axisYVar.get())

            plt.show()

        else:
            print("SOUBOR NEBYL NALEZEN")

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
