import tkinter as tk
from tkinter import ttk, messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x400")
        self.root.config(bg="#FFFFFF")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Contact Book", font=("Helvetica", 20, "bold"), fg="#D4A017", bg="#FFFFFF")
        self.title_label.pack(pady=10)

        self.form_frame = tk.Frame(self.root, bg="#FFFFFF")
        self.form_frame.pack(pady=10)

        self.name_label = tk.Label(self.form_frame, text="Name:", font=("Helvetica", 12), fg="#333333", bg="#FFFFFF")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self.form_frame, font=("Helvetica", 12))
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.form_frame, text="Phone:", font=("Helvetica", 12), fg="#333333", bg="#FFFFFF")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.phone_entry = ttk.Entry(self.form_frame, font=("Helvetica", 12))
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.form_frame, text="Email:", font=("Helvetica", 12), fg="#333333", bg="#FFFFFF")
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = ttk.Entry(self.form_frame, font=("Helvetica", 12))
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(self.form_frame, text="Address:", font=("Helvetica", 12), fg="#333333", bg="#FFFFFF")
        self.address_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.address_entry = ttk.Entry(self.form_frame, font=("Helvetica", 12))
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = ttk.Button(self.root, text="Add Contact", command=self.add_contact, style="TButton")
        self.add_button.pack(pady=10)

        self.search_label = tk.Label(self.root, text="Search by Name or Phone:", font=("Helvetica", 12), fg="#333333", bg="#FFFFFF")
        self.search_label.pack(pady=5)
        self.search_entry = ttk.Entry(self.root, font=("Helvetica", 12))
        self.search_entry.pack(pady=5)
        self.search_button = ttk.Button(self.root, text="Search", command=self.search_contact, style="TButton")
        self.search_button.pack(pady=5)

        self.contact_list_frame = tk.Frame(self.root, bg="#FFFFFF")
        self.contact_list_frame.pack(pady=10)

        self.contact_listbox = tk.Listbox(self.contact_list_frame, font=("Helvetica", 12), width=50, height=10)
        self.contact_listbox.pack(side="left", fill="both", expand=True)
        self.contact_listbox.bind('<<ListboxSelect>>', self.select_contact)

        self.scrollbar = ttk.Scrollbar(self.contact_list_frame, orient="vertical")
        self.scrollbar.config(command=self.contact_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)

        self.update_button = ttk.Button(self.root, text="Update Selected", command=self.update_contact, style="TButton")
        self.update_button.pack(pady=5)

        self.delete_button = ttk.Button(self.root, text="Delete Selected", command=self.delete_contact, style="TButton")
        self.delete_button.pack(pady=5)

        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#D4A017", foreground="#333333", font=('Helvetica', 12))

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
            self.update_contact_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def search_contact(self):
        search_term = self.search_entry.get()
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def select_contact(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, selected_contact['name'])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, selected_contact['phone'])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, selected_contact['email'])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, selected_contact['address'])

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            if name and phone:
                self.contacts[selected_index[0]] = {'name': name, 'phone': phone, 'email': email, 'address': address}
                self.update_contact_listbox()
                self.clear_entries()
            else:
                messagebox.showwarning("Warning", "Name and Phone are required fields.")
        else:
            messagebox.showwarning("Warning", "No contact selected for update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]
            self.update_contact_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "No contact selected for deletion.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
