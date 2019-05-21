from tkinter import *

master = Tk()
master.title("Vector Products")
Label(master, text="First Vector: ").grid(row=0)
Label(master, text="Second Vector: ").grid(row=1)

vector1_1 = Entry(master)
vector1_2 = Entry(master)
vector1_3 = Entry(master)

vector1_1.grid(row=0, column=1)
vector1_2.grid(row=0, column=2)
vector1_3.grid(row=0, column=3)

vector2_1 = Entry(master)
vector2_2 = Entry(master)
vector2_3 = Entry(master)

vector2_1.grid(row=1, column=1, pady=5, padx=10)
vector2_2.grid(row=1, column=2, pady=5, padx=10)
vector2_3.grid(row=1, column=3, pady=5, padx=10)


def calculate_dot_product():
    vector_1 = [int(vector1_1.get()), int(vector1_2.get()), int(vector1_3.get())]
    vector_2 = [int(vector2_1.get()), int(vector2_2.get()), int(vector2_3.get())]    
    dot_product = (vector_1[0]*vector_2[0] + vector_1[1]*vector_2[1] + vector_1[2]*vector_2[2])
    toplevel = Toplevel()
    output_label = Label(toplevel, text=dot_product)
    output_label.pack()

def calculate_cross_product():
    vector_1 = [int(vector1_1.get()), int(vector1_2.get()), int(vector1_3.get())]
    vector_2 = [int(vector2_1.get()), int(vector2_2.get()), int(vector2_3.get())]    
    
    cross_product = [(vector_1[1]*vector_2[2])-(vector_1[2]*vector_2[1]), (vector_1[2]*vector_2[0])-(vector_1[0]*vector_2[2]), (vector_1[0]*vector_2[1])-(vector_1[1]*vector_2[0])]
    final_cross_product= "(" + str(cross_product[0]) + ", " + str(cross_product[1]) + ", " + str(cross_product[2]) + ")"
    toplevel = Toplevel()
    output_label = Label(toplevel, text=final_cross_product)
    output_label.pack()    
    
Button(master, text="Calculate Dot Product", command=calculate_dot_product).grid(row=3, column=2, sticky=W, pady=5)
Button(master, text="Calculate Cross Product", command=calculate_cross_product).grid(row=3, column=3, sticky=W, pady=5)
mainloop()




