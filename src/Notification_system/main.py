from app_logging import logger
import notification as notify

class Main:
    def main(self):
        logger.info("Application is started...")
        while True:
            print("select option to send notification...")
            print("1.Email")
            print("2.SMS")
            print("3.App")
            print("4.Exit")
            try:
                case = int(input("Enter Option :- "))
                if case == 1:
                    email = notify.email_notification()
                    email.send()
                elif case == 2:
                    sms = notify.sms_notification()
                    sms.send()
                elif case == 3:
                    app = notify.app_notification()
                    app.send("This is app_notification.")
                elif case == 4:
                    print("Exit")
                    logger.info("Application is stopped...")
                    break
                else:
                    print("Choose a valid option")
            except ValueError:
                print("Please select valid number")

obj = Main()
obj.main()