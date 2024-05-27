from tkinter import *
import contactlist_gui
import contactlist_func


class AppWindow(Frame):
    def __init__(self, app, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.app = app

        self.app.option_add("*font", "Helvetica 10")
        self.app.resizable(width=False, height=False)

        self.app.geometry('{}x{}'.format(500, 300))

        self.app.title('Contact App')
        self.app.iconbitmap(self.app, default="assets/contactlist.ico")

        self.container = Frame(self.app)
        self.container.grid(row=0, column=0, padx=25, pady=10)

      
        self.text_id = StringVar()
        self.text_first_name = StringVar()
        self.text_last_name = StringVar()
        self.text_email = StringVar()
        self.text_phone_number = StringVar()
        self.text_address = StringVar()
        se
       
        self.contactlist_fields = []
        self.contactlist_fields.append(self.text_id)
        self.contactlist_fields.append(self.text_first_name)
        self.contactlist_fields.append(self.text_last_name)
        self.contactlist_fields.append(self.text_email)
        self.contactlist_fields.append(self.text_phone_number)
        self.contactlist_fields.append(self.text_address)

       
        self.contactlist_list = []
       
        self.active_contactbox_index = -1

     
        contactlist_gui.load_gui(self)

     
        contactlist_func.create_db()
        contactlist_func.load_contactlist(self)


if __name__ == "__main__":
    root = Tk()
    App = AppWindow(root)
    root.mainloop()
