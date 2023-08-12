from tkinter import *
import os
from datetime import datetime, timedelta
import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog

df = ''
predict_val = ''

def graph():

    def get_files():
        files = filedialog.askopenfilenames(title = "Select CSV Files", filetypes = (("CSV files", "*.csv"), ("All files", "*.*")))
        text = "\n".join(files)
        r4_l1.configure(text=text)
        return list(files)
    
    def generate_graph(files):
        data_frames = []
        for file in files:
            df = pd.read_csv(file)
            total_sales = df['sale'].sum()
            data_frames.append((os.path.splitext(os.path.basename(file))[0], total_sales))
        data_frames = sorted(data_frames, key=lambda x: x[1], reverse=True)
        products = [df[0] for df in data_frames]
        sales = [df[1] for df in data_frames]
        plt.bar(products, sales)
        plt.xticks(rotation=0)
        plt.ylabel('Total Sales')
        plt.title('Comparison of Total Sales')
        plt.show()

    # Create a GUI in tkinter
    root4 = Toplevel()
    root4.configure(bg="#daf2dc")
    root4.title('CSV Comparison Graph')
    root4.geometry('400x200')

    # Function to generate the comparison graph when the button is clicked
    def generate():
        files = get_files()
        generate_graph(files)

    # Create a button to generate the comparison graph
    button = Button(root4, text="Form Graph",font=('Arial', 12, 'bold'), bg='#DDC3A5', fg='#201E20', highlightthickness=0, borderwidth=0, activebackground='#E0A96D', activeforeground='#201E20', width=20, height=2, command=generate)
    button.pack(pady=20)

    r4_l1 = Label(root4,text="File yet not Selected....:(",bg='#daf2dc')
    r4_l1.pack(pady=10)
   

    root4.grab_set() # Make the window modal
    root4.focus_set() # Set focus to the window
    root4.wait_window()

def pur_remi():

    def write_to_csv(name, phone_num, email, days):
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone_num, email, days])

    def send_email(name, email):
    # create the message
        msg = MIMEMultipart()
        days = int(days_entry.get())
        date = datetime.today() + timedelta(days=days)
        # msg['From'] = 'your_email_address'
        # msg['To'] = email
        msg['Subject'] = 'Thanks for shoping from Apna Bazar :)'

        message = f"Dear {name},\n\nWe hope this email finds you well. We wanted to take a moment to thank you for choosing \nAPNA BAZAR for your recent purchase. We truly value your business and appreciate your \ntrust in our products and services.\n\nWe are glad to hear that you enjoyed shopping with us, and we would like to extend an \ninvitation for you to visit our shop again soon. We are constantly updating our inventory \nwith new products and promotions, so we hope you will come back at {date.date()} and see us again soon.\n\nThank you once again for choosing APNA BAZAR for your grocery needs. If you have any \nfeedback or suggestions on how we can improve your shopping experience, please do not \nhesitate to let us know. \n\nWe look forward to serving you again in the near future.\n\nBest regards,\nBhaskar Ghogale,\nApna Bazar,\nKhed."

        msg.attach(MIMEText(message, 'plain'))

        # send the message
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('apnabazarkhed@gmail.com', 'mufmffkorybqdqqw')
        text = msg.as_string()
        server.sendmail('apnabazarkhed@gmail.com', email, text)
        server.quit()

    def submit_form():
        name = name_entry.get()
        phone_num = phone_entry.get()
        email = email_entry.get()
        days = days_entry.get()

        write_to_csv(name, phone_num, email, days)

        # send email to user
        send_email(name, email)

        name_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        days_entry.delete(0, 'end')



    root3 = Tk()
    root3.configure(bg='#ced7d8')
    #root3.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root3.geometry("300x300")
    root3.title("Customer Database")


    name_label = Label(root3, text="Name :",bg='#ced7d8')
    name_entry = Entry(root3)

    phone_label = Label(root3, text="Phone Number :",bg='#ced7d8')
    phone_entry = Entry(root3)

    email_label = Label(root3, text="Email :",bg='#ced7d8')
    email_entry = Entry(root3)

    days_label = Label(root3, text="Number of Days :",bg='#ced7d8')
    days_entry = Entry(root3)

    # create a button to submit the form
    submit_button = Button(root3, text="Submit",font=('Arial', 12, 'bold'), bg='#aed6dc', fg='#00154f', highlightthickness=1, borderwidth=1, activebackground='#f4898b', activeforeground='#00154f', width=20, height=2, command=submit_form)

    # arrange the labels, entries, and button in the grid
    name_label.pack(pady=10)
    name_entry.pack()

    phone_label.pack(pady=10)
    phone_entry.pack()

    email_label.pack(pady=10)
    email_entry.pack()

    days_label.pack(pady=10)
    days_entry.pack()

    submit_button.pack(pady=15)

    root3.mainloop()


def data_analysis():
    
    def cl_hr():
        total = df.isnull().sum().sort_values(ascending=False)
        percent = (df.isnull().sum()/df.isnull().count()
               ).sort_values(ascending=False)
        missing_data = pd.concat(
        [total, percent], axis=1, keys=['Total', 'Percent'])
        p = missing_data.head(20)
        t2.insert(END, p)

        c = df.dtypes
        t3.insert(END, c)

        j = df.describe()
        t4.insert(END, j)

    root2 = Tk()
    root2.configure(bg='#c6d7eb')
    root2.geometry("800x700")
    root2.title("Sales Prediction")

    t2 = Text(root2, width=50, height=10,bg='#d9a5b3',fg='black')
    t2.pack()
    l1 = Label(root2, text="Checking missing value 👆 ",font=("Futura", 10, "bold"),bg='#c6d7eb')
    l1.pack(pady=10)

    t3 = Text(root2, width=50, height=10,bg='#d9a5b3',fg='black')
    t3.pack()
    l2 = Label(root2, text="Column wise data type 👆 ",font=("Futura", 10, "bold"),bg='#c6d7eb')
    l2.pack(pady=10)

    t4 = Text(root2, width=50, height=10,bg='#d9a5b3',fg='black')
    t4.pack()
    l3 = Label(root2, text="Data type information 👆 ",font=("Futura", 10, "bold"),bg='#c6d7eb')
    l3.pack(pady=10)

    btn4 = Button(root2, text="Click here for Analysing", font=('Arial', 12, 'bold'), bg='#FE7773', fg='#0E0301', highlightthickness=0, borderwidth=0, activebackground='#E81E25', activeforeground='#0E0301', width=20, height=2, command=cl_hr)
    btn4.pack(pady=10)

    root2.mainloop()

def select_option():
    selected_option = listbox.get(listbox.curselection())
    # message = f"You selected: {selected_option}"
    # messagebox.showinfo("Selection", message)
    lbl4.config(text=selected_option,fg="green", font=("Futura",10))
    #print(selected_option)

def get_val():
    val1 = float(valA.get())
    val2 = float(valB.get())

    # #Important features of data taken and output of that data..... two independent variable and one dependent variable....
    X = df[['sale_qty','sale_cost']].values
    Y = df['sale'].values

    # #Training and testing of data.......
    xtr,xte,ytr,yte=train_test_split(X,Y,test_size=0.50, random_state = 2)

    # #Using Mulitiple Linear Regression model.....
    r = linear_model.LinearRegression()
    r.fit(xtr,ytr)
    
    value = lbl4.cget("text")
    # #Predicting Value on basis of input taken from user.........
    predict_val = r.predict([[val1,val2]])
    fina.configure(text='Predicted value for '+value+' is '+str(predict_val),fg='green',font=("Verdana", 14, "bold"))

def search():
    # Clear any previous search results
    listbox.delete(0, END)
    search_term = lbl3_4.get()

    # Perform the search (in this example, just search a list of fruits)
    fruits = df['prod_name']
    search_results = [f for f in fruits if search_term.lower() in f.lower()]

    # Display the search results in the listbox
    if search_results:
        for result in search_results:
            listbox.insert(END, result)
    else:
        listbox.insert(END, "No results found.")

def browsefile():
    # For getting CSV file from user to train and test the data......
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select File", filetypes=(("CSV Files", "*.csv"), ("All", "*.*")))
    lbl2.configure(text="File Opened: "+filename,
                   fg="green", font=("Verdana", 14, "bold"))

    global df
    df = pd.read_csv(filename)
    # print(Y)
    t1.insert(END, df)


root = Tk()
root.configure(bg='#c6d7eb')
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Sales Prediction")

lbl1 = Label(root, text="Please Upload CSV file Only :)",
             font=("Aharoni", 10, "bold"),bg='#c6d7eb')
lbl1.place(relx=0.25, rely=0.22, anchor='center')

lbl2 = Label(root, text="File yet not selected:(", fg="red",bg='#c6d7eb')
lbl2.place(relx=0.5, rely=0.46, anchor='center')

t1 = Text(root, width=80, height=20,bg='#d9a5b3',fg='black',borderwidth=2)
t1.place(relx=0.6, rely=0.24, anchor='center')

photo = PhotoImage(file="csvupload.png")
photo = photo.subsample(2)

btn1 = Button(root,image=photo, borderwidth=0, command=browsefile,bg='#c6d7eb')
btn1.place(relx=0.25, rely=0.28, anchor='center')

val_a = Label(root,text='Enter sale quantity: ',font=("Futura", 10, "bold"),bg='#c6d7eb')
val_a.place(relx=0.69,rely=0.6,anchor='center')
valA = Entry(root,width=20,justify='center',bg='#d9a5b3',fg='black')
valA.place(relx=0.85,rely=0.6,anchor='center')

val_b = Label(root,text='Enter sale cost: ',font=("Futura", 10, "bold"),bg='#c6d7eb')
val_b.place(relx=0.70,rely=0.7,anchor='center')
valB = Entry(root,width=20,justify='center',bg='#d9a5b3',fg='black')
valB.place(relx=0.85,rely=0.7,anchor='center')

lbl3 = Label(root,text="Search Product: ",font=("Futura", 10, "bold"),bg='#c6d7eb')
lbl3.place(relx=0.2,rely=0.6,anchor='center')
lbl3_4 = Entry(root,bg='#d9a5b3',fg='black')
lbl3_4.place(relx=0.3,rely=0.6,anchor='center')
photo5 = PhotoImage(file="search1.png")
photo5 = photo5.subsample(2)
btn7 = Button(root,image=photo5, borderwidth=0,command=search,bg='#c6d7eb')
btn7.place(relx=0.18,rely=0.65,anchor='center')
listbox = Listbox(root,width=40,height=8,bg='#d9a5b3',fg='black')
listbox.place(relx=0.45,rely=0.66,anchor='center')
photo6 = PhotoImage(file="select.png")
photo6 = photo6.subsample(2)
btn8 =  Button(root,image=photo6, borderwidth=0, state= DISABLED,command=select_option,bg='#c6d7eb')
btn8.place(relx=0.3,rely=0.65,anchor='center')
# Define the function to enable the select button when an option is selected
def on_select(event):
    btn8.config(state=NORMAL)
# Bind the listbox to the on_select function
listbox.bind("<<ListboxSelect>>", on_select)

lbl4 = Label(root, text='Product is not Selected', fg="red",bg='#c6d7eb')
lbl4.place(relx=0.25,rely=0.7,anchor='center')

lbl5 = Label(root,bg='#c6d7eb',text='-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
lbl5.place(relx=0.5,rely=0.5,anchor='center')

photo1 = PhotoImage(file="predict.png")
photo1 = photo1.subsample(2)

btn3 = Button(root,image=photo1, borderwidth=0, command=get_val,bg='#c6d7eb')
btn3.place(relx=0.5, rely=0.8, anchor='center')

photo2 = PhotoImage(file="data_analysis.png")
photo2 = photo2.subsample(2)

btn4 = Button(root,image=photo2, borderwidth=0, command=data_analysis,bg='#c6d7eb')
btn4.place(relx=0.5, rely=0.53, anchor='center')

photo4 = PhotoImage(file="graph.png")
photo4 = photo4.subsample(2)
 
btn5 = Button(root,image=photo4, borderwidth=0, command=graph,bg='#c6d7eb')
btn5.place(relx=0.83, rely=0.53, anchor='center')

photo3 = PhotoImage(file="database.png")
photo3 = photo3.subsample(2)

btn6 = Button(root,image=photo3, borderwidth=0,command=pur_remi,bg='#c6d7eb')
btn6.place(relx=0.2, rely=0.53, anchor='center')

fina = Label(root, text='Value is not Predicted', fg='red',bg='#c6d7eb')
fina.place(relx=0.5, rely=0.85, anchor='center')


root.mainloop()
