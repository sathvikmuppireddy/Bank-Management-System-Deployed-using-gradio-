

import gradio as gr

# Bank Management System
class BankManagementSystem:
    def __init__(self):
        self.customer = {}  # Creating a dictionary to store customer details

    # Adding Customer
    def add_cus(self, cus_acc_no, name, acc_bal, acc_type):
        if cus_acc_no in self.customer:
            return "Customer Account Already Exists"
        else:
            self.customer[cus_acc_no] = {"name": name, "acc_bal": acc_bal, "acc_type": acc_type}
            return "Customer Added Successfully"

    # To Update Details of a Customer
    def update_cus(self, cus_acc_no, name=None, acc_bal=None, acc_type=None):
        if cus_acc_no in self.customer:
            if name:
                self.customer[cus_acc_no]["name"] = name
            if acc_bal:
                self.customer[cus_acc_no]["acc_bal"] = acc_bal
            if acc_type:
                self.customer[cus_acc_no]["acc_type"] = acc_type
            return "Customer Details Updated Successfully"
        else:
            return "Customer Account Not Found"

    # To Delete Customer Details
    def del_cus(self, cus_acc_no):
        if cus_acc_no in self.customer:
            del self.customer[cus_acc_no]
            return f"{cus_acc_no} Has Been Deleted Successfully"
        else:
            return f"Customer Account No {cus_acc_no} Not Found"

    # To View a Particular Customer's Details
    def view_cus(self, cus_acc_no):
        if cus_acc_no in self.customer:
            customer_info = self.customer[cus_acc_no]
            return f"Customer Account No: {cus_acc_no}\n" + \
                   f"Name: {customer_info['name']}\n" + \
                   f"Account Balance: {customer_info['acc_bal']}\n" + \
                   f"Account Type: {customer_info['acc_type']}"
        else:
            return "Customer Account No Not Found"

    # To View All Customers' Details
    def view_all_cus(self):
        if self.customer:
            details = ""
            for cus_acc_no, info in self.customer.items():
                details += f"Customer Account No: {cus_acc_no}\n" + \
                           f"Name: {info['name']}\n" + \
                           f"Account Balance: {info['acc_bal']}\n" + \
                           f"Account Type: {info['acc_type']}\n" + \
                           "-" * 40 + "\n"
            return details
        else:
            return "No Customers Found"

mng_sys = BankManagementSystem()

def add_customer(cus_acc_no, name, acc_bal, acc_type):
    return mng_sys.add_cus(cus_acc_no, name, acc_bal, acc_type)

def update_customer(cus_acc_no, name, acc_bal, acc_type):
    return mng_sys.update_cus(cus_acc_no, name, acc_bal, acc_type)

def delete_customer(cus_acc_no):
    return mng_sys.del_cus(cus_acc_no)

def view_customer(cus_acc_no):
    return mng_sys.view_cus(cus_acc_no)

def view_all_customers():
    return mng_sys.view_all_cus()

with gr.Blocks() as demo:
    with gr.Tab("Add Customer"):
        cus_acc_no = gr.Textbox(label="Customer Account No")
        name = gr.Textbox(label="Name")
        acc_bal = gr.Textbox(label="Account Balance")
        acc_type = gr.Textbox(label="Account Type")
        add_button = gr.Button("Add Customer")
        add_output = gr.Textbox(label="Output")
        add_button.click(add_customer, inputs=[cus_acc_no, name, acc_bal, acc_type], outputs=add_output)

    with gr.Tab("Update Customer"):
        cus_acc_no = gr.Textbox(label="Customer Account No")
        name = gr.Textbox(label="Name (Leave blank if no change)")
        acc_bal = gr.Textbox(label="Account Balance (Leave blank if no change)")
        acc_type = gr.Textbox(label="Account Type (Leave blank if no change)")
        update_button = gr.Button("Update Customer")
        update_output = gr.Textbox(label="Output")
        update_button.click(update_customer, inputs=[cus_acc_no, name, acc_bal, acc_type], outputs=update_output)

    with gr.Tab("Delete Customer"):
        cus_acc_no = gr.Textbox(label="Customer Account No")
        delete_button = gr.Button("Delete Customer")
        delete_output = gr.Textbox(label="Output")
        delete_button.click(delete_customer, inputs=cus_acc_no, outputs=delete_output)

    with gr.Tab("View Customer"):
        cus_acc_no = gr.Textbox(label="Customer Account No")
        view_button = gr.Button("View Customer")
        view_output = gr.Textbox(label="Output")
        view_button.click(view_customer, inputs=cus_acc_no, outputs=view_output)

    with gr.Tab("View All Customers"):
        view_all_button = gr.Button("View All Customers")
        view_all_output = gr.Textbox(label="Output")
        view_all_button.click(view_all_customers, outputs=view_all_output)

demo.launch()