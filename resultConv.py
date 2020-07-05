import tkinter as tk
from tkinter import filedialog
import pandas as pd
import PyPDF2
from tkinter  import PhotoImage

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        tk.Tk.iconbitmap(self, default='jpis.ico')
        tk.Tk.state(self, 'zoomed')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FirstPage,):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

font="Calibri 20"


class FirstPage(tk.Frame):
    def generate(self,filesave,filename):
        df = pd.DataFrame()
        code = ""
        name = []
        dob = []
        cn = []
        eco, addmath, lit, lang, fren, bs, hin, evm, math = [], [], [], [], [], [], [], [], []
        read_pdf = PyPDF2.PdfFileReader(
            filename)
        number_of_pages = read_pdf.getNumPages()
        for i in range(0, number_of_pages):
            eco.append(" ")
            addmath.append(" ")
            math.append(" ")
            lit.append(" ")
            lang.append(" ")
            fren.append(" ")
            hin.append(" ")
            bs.append(" ")
            evm.append(" ")

        # making the array 'name' with all the names of the candidate
        for i in range(0, number_of_pages):
            page = read_pdf.getPage(i)
            page_content = page.extractText()
            b = 181
            while b < 650:
                if page_content[b] == "0" or page_content[b] == "1" or page_content[b] == "2" or page_content[b] == "3" \
                        or page_content[b] == "4" or page_content[b] == "5" or page_content[b] == "6" \
                        or page_content[b] == "7" or page_content[b] == "8" or page_content[b] == "9":
                    break
                b = b + 1
            name.append(page_content[181:b])
            name[i] = str(name[i]).replace('\n', '')
            c = b
            while b < 650:
                if page_content[b] == "I":
                    break
                b = b + 1
            dob.append(page_content[c:b])
            dob[i] = str(dob[i]).replace('\n', '')
            while b < 1000:
                if page_content[b] == "/":
                    break
                b = b + 1
            c = b
            while b < 1000:
                if page_content[b] == "C":
                    break
                b = b + 1
            cn.append(page_content[c:b])
            cn[i] = str(cn[i]).replace('\n', '').replace('/', '')
            while b < 1000:
                if page_content[b] == "0" or page_content[b] == "1" or page_content[b] == "2" or page_content[b] == "3" \
                        or page_content[b] == "4" or page_content[b] == "5" or page_content[b] == "6" \
                        or page_content[b] == "7" or page_content[b] == "8" or page_content[b] == "9":
                    break
                b = b + 1
            while b < 1000:
                if page_content[b] == "I":
                    break
                b = b + 1
            try:
                for k in range(0, 30):
                    while b < 1000:
                        if page_content[b] == "0" or page_content[b] == "1" or page_content[b] == "2" or page_content[
                            b] == "3" \
                                or page_content[b] == "4" or page_content[b] == "5" or page_content[b] == "6" \
                                or page_content[b] == "7" or page_content[b] == "8" or page_content[b] == "9":
                            break
                        b = b + 1
                    code = page_content[b:b + 4]
                    b += 4
                    while b < 1500:
                        if page_content[b] == "0" or page_content[b] == "1" or page_content[b] == "2" or page_content[
                            b] == "3" \
                                or page_content[b] == "4" or page_content[b] == "5" or page_content[b] == "6" \
                                or page_content[b] == "7" or page_content[b] == "8" or page_content[b] == "9" \
                                or page_content[b:b + 9] == "NO RESULT" or page_content[b:b + 8] == "UNGRADED":
                            break
                        b = b + 1
                    marks = page_content[b:b + 2]
                    if code == "0455":
                        eco[i] = marks
                        if lit[i] != " ":
                            continue
                        else:
                            lit[i] = " "
                        if hin[i] != " ":
                            continue
                        else:
                            hin[i] = " "
                        if addmath[i] != " ":
                            continue
                        else:
                            addmath[i] = " "
                        if bs[i] != " ":
                            continue
                        else:
                            bs[i] = " "
                        if evm[i] != " ":
                            continue
                        else:
                            evm[i] = " "
                        if fren[i] != " ":
                            continue
                        else:
                            fren[i] = " "
                        if lang[i] != " ":
                            continue
                        else:
                            lang[i] = " "
                        if math[i] != " ":
                            continue
                        else:
                            math[i] = " "
                    elif code == "0486":
                        lit[i] = marks
                        if eco[i] != " ":
                            continue
                        else:
                            eco[i] = " "
                        if hin[i] != " ":
                            continue
                        else:
                            hin[i] = " "
                        if addmath[i] != " ":
                            continue
                        else:
                            addmath[i] = " "
                        if bs[i] != " ":
                            continue
                        else:
                            bs[i] = " "
                        if evm[i] != " ":
                            continue
                        else:
                            evm[i] = " "
                        if fren[i] != " ":
                            continue
                        else:
                            fren[i] = " "
                        if lang[i] != " ":
                            continue
                        else:
                            lang[i] = " "
                        if math[i] != " ":
                            continue
                        else:
                            math[i] = " "
                    elif code == "0549":
                        hin[i] = marks
                        if lit[i] != " ":
                            continue
                        else:
                            lit[i] = " "
                        if eco[i] != " ":
                            continue
                        else:
                            eco[i] = " "
                        if addmath[i] != " ":
                            continue
                        else:
                            addmath[i] = " "
                        if bs[i] != " ":
                            continue
                        else:
                            bs[i] = " "
                        if evm[i] != " ":
                            continue
                        else:
                            evm[i] = " "
                        if fren[i] != " ":
                            continue
                        else:
                            fren[i] = " "
                        if lang[i] != " ":
                            continue
                        else:
                            lang[i] = " "
                        if math[i] != " ":
                            continue
                        else:
                            math[i] = " "
                    elif code == "0606":
                        addmath[i] = marks
                        if lit[i] != " ":
                            continue
                        else:
                            lit[i] = " "
                        if hin[i] != " ":
                            continue
                        else:
                            hin[i] = " "
                        if eco[i] != " ":
                            continue
                        else:
                            eco[i] = " "
                        if bs[i] != " ":
                            continue
                        else:
                            bs[i] = " "
                        if evm[i] != " ":
                            continue
                        else:
                            evm[i] = " "
                        if fren[i] != " ":
                            continue
                        else:
                            fren[i] = " "
                        if lang[i] != " ":
                            continue
                        else:
                            lang[i] = " "
                        if math[i] != " ":
                            continue
                        else:
                            math[i] = " "
                    elif code == "0450":
                        bs[i] = marks
                        if lit[i] != " ":
                            continue
                        else:
                            lit[i] = " "
                        if hin[i] != " ":
                            continue
                        else:
                            hin[i] = " "
                        if addmath[i] != " ":
                            continue
                        else:
                            addmath[i] = " "
                        if eco[i] != " ":
                            continue
                        else:
                            eco[i] = " "
                        if evm[i] != " ":
                            continue
                        else:
                            evm[i] = " "
                        if fren[i] != " ":
                            continue
                        else:
                            fren[i] = " "
                        if lang[i] != " ":
                            continue
                        else:
                            lang[i] = " "
                        if math[i] != " ":
                            continue
                        else:
                            math[i] = " "
                    elif code == "0680":
                        evm[i] = marks
                        if lit[i] != " ":
                            continue
                        else:
                            lit[i] = " "
                        if hin[i] != " ":
                            continue
                        else:
                            hin[i] = " "
                        if addmath[i] != " ":
                            continue
                        else:
                            addmath[i] = " "
                        if bs[i] != " ":
                            continue
                        else:
                            bs[i] = " "
                        if eco[i] != " ":
                            continue
                        else:
                            eco[i] = " "
                        if fren[i] != " ":
                            continue
                        else:
                            fren[i] = " "
                        if lang[i] != " ":
                            continue
                        else:
                            lang[i] = " "
                        if math[i] != " ":
                            continue
                        else:
                            math[i] = " "
                    elif code == "0520":
                        fren[i] = marks
                        if lit[i] != " ":
                            continue
                        else:
                            lit[i] = " "
                        if hin[i] != " ":
                            continue
                        else:
                            hin[i] = " "
                        if addmath[i] != " ":
                            continue
                        else:
                            addmath[i] = " "
                        if bs[i] != " ":
                            continue
                        else:
                            bs[i] = " "
                        if evm[i] != " ":
                            continue
                        else:
                            evm[i] = " "
                        if eco[i] != " ":
                            continue
                        else:
                            eco[i] = " "
                        if lang[i] != " ":
                            continue
                        else:
                            lang[i] = " "
                        if math[i] != " ":
                            continue
                        else:
                            math[i] = " "
                    elif code == "0500":
                        lang[i] = marks
                        if lit[i] != " ":
                            continue
                        else:
                            lit[i] = " "
                        if hin[i] != " ":
                            continue
                        else:
                            hin[i] = " "
                        if addmath[i] != " ":
                            continue
                        else:
                            addmath[i] = " "
                        if bs[i] != " ":
                            continue
                        else:
                            bs[i] = " "
                        if evm[i] != " ":
                            continue
                        else:
                            evm[i] = " "
                        if fren[i] != " ":
                            continue
                        else:
                            fren[i] = " "
                        if eco[i] != " ":
                            continue
                        else:
                            eco[i] = " "
                        if math[i] != " ":
                            continue
                        else:
                            math[i] = " "
                    elif code == "0580":
                        math[i] = marks
                        if lit[i] != " ":
                            continue
                        else:
                            lit[i] = " "
                        if hin[i] != " ":
                            continue
                        else:
                            hin[i] = " "
                        if addmath[i] != " ":
                            continue
                        else:
                            addmath[i] = " "
                        if bs[i] != " ":
                            continue
                        else:
                            bs[i] = " "
                        if evm[i] != " ":
                            continue
                        else:
                            evm[i] = " "
                        if fren[i] != " ":
                            continue
                        else:
                            fren[i] = " "
                        if lang[i] != " ":
                            continue
                        else:
                            lang[i] = " "
                        if eco[i] != " ":
                            continue
                        else:
                            eco[i] = " "
            except:
                continue

        df['Candidate Name'] = name
        df['Date of Birth'] = dob
        df['Candidate No.'] = cn
        df['Economics'] = eco
        df['French'] = fren
        df['Add Math'] = addmath
        df['Hindi'] = hin
        df['Business Studies'] = bs
        df['English Language'] = lang
        df['English Literature'] = lit
        df['EVM'] = evm
        df['Mathematics (W/O Coursework)'] = math

        # print(df)
        df.to_excel(filesave+'.xlsx', index=None, header=True)


    def saveto(self,filename):
        self.filesave = filedialog.asksaveasfilename(initialdir = "/",title = "Save to",filetypes = (("xlsx","*.xlsx"),("all files","*.*")))
        print(self.filesave)
        self.generate(self.filesave,filename)
        self.label.configure(text="GENERATED", fg="red")
    def browse(self):
        self.filename = filedialog.askopenfilename(defaultextension=".pdf", initialdir="D://workspace",
                       filetypes=[('pdf file', '*.pdf')])
        self.label.configure(text = self.filename)
        self.openbtn = tk.Button(self,text="Generate",bg="white",command=lambda: self.saveto(self.filename), font="Calibri 50")
        self.openbtn.pack(side="bottom")


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        # self.configure(image=PhotoImage(file='download.jpg'))
        tk.Label(self,text="Result Generator (PROTOTYPE)", font="Calibri 60 bold", bg="white").pack(side="top", pady=20)
        tk.Label(self,text="Choose a PDF file", font="Calibri 50",bg="white").pack(pady=50)
        self.bbtn = tk.Button(self,text="Browse", font="Calibri 50",bg="white",command=self.browse)
        self.bbtn.pack(pady=0)
        self.label = tk.Label(self,text="",bg="white",font="Calibri 25")
        self.label.pack(side="bottom")

app = Main()
app.title('Prototype')
app.mainloop()