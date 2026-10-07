from abc import ABC, abstractmethod
from app_logging import logger
import smtplib
from twilio.rest import Client
from validation import (
    validate_email,
    validate_receiver_email
)
import tkinter
from tkinter import messagebox
import pywhatkit as kit

class notification:

    @abstractmethod
    def send(self,message):
        pass

class email_notification(notification):
    def send(self):
        email = validate_email()
        receiver_email = validate_receiver_email()
        subject = input("SUBJECT: ")
        message = input("MESSAGE: ")
        text = f"Subject: {subject}\n\n{message}"
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,"asxb ubfw pydn iqsp")
        server.sendmail(email, receiver_email, text)
        print("Email send successfully...")
        logger.info("Email send successfully...")

class sms_notification(notification):
    def send(self):
        try:
            number = '+911111111111'
            kit.sendwhatmsg(
                number,
                'Happy Birthday!',11,10
            )
        except:
            print("Error")
        

class app_notification(notification):
    def send(self,message):
        root = tkinter.Tk()
        root.withdraw()

        messagebox.showerror("Error","This is error message")
        messagebox.showwarning("warning","This is warning message")
        messagebox.showinfo("Info","This is info message")
        messagebox.askquestion("Question","Do you want to run this program")
        messagebox.askokcancel("askokcancel","Do you want to run this code")
        messagebox.askyesno("askyesno","Do you want to run this code")
        messagebox.askretrycancel("retry","Do you want to retry or cancel")

        root.destroy()
        logger.info("App notification send successfully...")
