from tkinter import *

root=Tk()
root.title("Calorie Calculator")

def calories(initial_temp, final_temp, initial_mass, final_mass):
     try:
          float(initial_temp)
     except ValueError:
          initial_temp=0
     try:
          float(final_temp)
     except ValueError:
          final_temp=0
     try:
          float(initial_mass)
     except ValueError:
          initial_mass=0
     try:
          float(final_mass)
     except ValueError:
          final_mass=0
     Temp_dif=final_temp-initial_temp
     Mass_dif=initial_mass-final_mass
     try:
          Calories=(((final_temp-initial_temp)*10)/(initial_mass-final_mass))/1000
     except ZeroDivisionError:
          Calories=0
     output1.configure(text=f"Temperature Change: {Temp_dif}")
     output2.configure(text=f"Mass Change: {Mass_dif}")
     output3.configure(text=f"Calories Released: {Calories}")

it=Entry(root)
ft=Entry(root)
im=Entry(root)
fm=Entry(root)
initial_water=Label(root, text="Initial Temperature:")
final_water=Label(root, text="Final Temperature:")
initial_weight=Label(root, text="Initial Mass:")
final_weight=Label(root, text="Final Mass:")
calculate=Button(root, text="Calculate", command=lambda:calories(float(it.get()),float(ft.get()),float(im.get()),float(fm.get())))
output1=Label(root, text='Temperature Change:')
output2=Label(root, text='Mass Change:')
output3=Label(root, text='Calories Released:')

it.grid(row=0,column=1)
ft.grid(row=1,column=1)
im.grid(row=2,column=1)
fm.grid(row=3,column=1)
initial_water.grid(row=0,column=0)
final_water.grid(row=1,column=0)
initial_weight.grid(row=2,column=0)
final_weight.grid(row=3,column=0)
calculate.grid(row=4,column=0,columnspan=2)
output1.grid(row=5,column=0,columnspan=2)
output2.grid(row=6,column=0,columnspan=2)
output3.grid(row=7,column=0,columnspan=2)

root.mainloop()