from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("StudentNo:5237892992887")
root.geometry("600x500")


class Sick:
    def __init__(self):

        sickness_code = Label(root, text="Sickness Code:")
        sickness_code.place(x=25, y=150, anchor="w")

        treatment_duration = Label(root, text="Duration of Treatment:")
        treatment_duration.place(x=25, y=200, anchor="w")

        duration_unit = Label(root, text="Weeks/Months")
        duration_unit.place(x=390, y=188)

        doc_rac_num = Label(root, text="Doctor's Practice Number:")
        doc_rac_num.place(x=25, y=250, anchor="w")

        fee = Label(root, text="Scan/Consultation Fee:")
        fee.place(x=25, y=300, anchor="w")

        amount_paid_label = Label(root, text="Amount paid for treatment:")
        amount_paid_label.place(x=25, y=400)

        self.sick_id = Entry(root)
        self.duration = Entry(root, width=10)
        self.doc_id = Entry(root)
        self.scan_or_consult = Entry(root)

        self.sick_id.place(x=300, y=135)
        self.duration.place(x=300, y=185)
        self.doc_id.place(x=300, y=235)
        self.scan_or_consult.place(x=300, y=285)
        self.v = IntVar()
        cancer_radio = Radiobutton(root, text="Cancer", variable=self.v, value=1)
        influenza_radio = Radiobutton(root, text="Influenza", variable=self.v, value=2)

        cancer_radio.place(x=20, y=330)
        influenza_radio.place(x=20, y=360)

        def calculate():
            radio = self.v.get()
            if radio == 1:
                can = Cancer(self.scan_or_consult.get())

            elif radio == 2:
                flu = Influenza(self.scan_or_consult.get())

        calc_btn = Button(root, text="Calculate", command=calculate, bg="green")
        calc_btn.place(x=25, y=450)

        def clear():
            self.sick_id.delete(0, 'end')
            self.duration.delete(0, 'end')
            self.doc_id.delete(0, 'end')
            self.scan_or_consult.delete(0, 'end')

        clear_btn = Button(root, text="Clear", command=clear, bg="orange")
        clear_btn.place(x=225, y=450)


class Cancer(Sick):

    def __init__(self, scan):
        super().__init__()
        amount_paid_display = Label(root, text="")
        amount_paid_display.place(x=225, y=400)
        medication = 400
        self.scan = scan

        if float(scan) > 600:
            messagebox.showinfo("", "Sorry we cannot treat you")
        else:
            amount_paid = float(scan) + medication
            amount_paid_display.config(text="R"+str(round(amount_paid, 4)))


class Influenza(Sick):

    def __init__(self, consult):
        super().__init__()
        x = StringVar()
        amount_paid_display = Label(root, textvariable=x)
        amount_paid_display.place(x=225, y=400)
        medication = 350.50
        self.consult = consult
        consult = float(consult)

        if consult > 600:
            consult = 0.98*consult
            amount_paid = float(consult) + medication
            x.set("R"+str(round(amount_paid, 2))+"")
        else:
            amount_paid = float(consult) + medication
            x.set("R"+str(round(amount_paid, 2))+"")

    exit_btn = Button(root, text="Exit", command=root.destroy, bg="red").place(x=425, y=450)


app = Sick()

root.mainloop()
