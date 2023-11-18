from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
import numpy as np
from sklearn.linear_model import LinearRegression

from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


def main():
    global z
    csv_file_path = askopenfilename()
    print(csv_file_path)
    set(csv_file_path)
    df = pd.read_csv(csv_file_path)

    lr = LinearRegression()
    imp = IterativeImputer(
        estimator=lr,
        max_iter=30,
        tol=1e-10,
        imputation_order='roman',
    )

    df = imp.fit_transform(df)
    l = df.tolist()

    Frame = Tk()
    Frame.geometry('850x900')
    Frame.title('OUTPUT')
    Frame.config(bg='#E6E6E6')
    cf = pd.read_csv(csv_file_path)

    def display():
        Label(Frame, text=cf, font='san-serif 12 bold', bg='#E6E6E6', fg='black').place(x=50, y=150)

        Label(Frame, text=df, font='san-serif 12 bold', bg='#E6E6E6', fg='blue').place(x=500, y=165)

    Button(Frame, text='Show result', font='san-serif 12 bold', bg='black', fg='white', command=display).place(x=10,
                                                                                                               y=10)

    Button(Frame, text='close', font='san-serif 12 bold', bg='red', fg='white', command=Frame.destroy).place(x=150,
                                                                                                             y=10)

    Label(Frame, text='BEFORE IMPUTATION : ', font='san-serif 16 bold underline').place(x=50, y=100)

    Label(Frame, text='AFTER IMPUTATION : ', font='san-serif 16 bold underline').place(x=500, y=100)

    Frame.mainloop()


root = Tk()
root.geometry('400x200')
root.title('Mini Project')
root.config(bg='#E6E6E6')

Label(root, text="Model Based Imputation", font='san-serif 22 bold underline italic').pack()

Button(root, text='Browse Data Set', font='san-serif 16 bold', bg='#0D0D0D', fg='white', command=main).place(x=105,
                                                                                                             y=70)
Button(root, text='Close', font='san-serif 10 bold ', bg='red', fg='white', command=root.destroy).place(x=105, y=120)

root.mainloop()