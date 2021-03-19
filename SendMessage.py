from Messages import WhatsApp  as _whatsApp
from ReadFile import Excel as _exl, Text as _txt
                      

message = _txt.ReadText("Message.txt")
contacts = _exl.readContacts("MobileContacts.xlsx")
for contact in contacts:
    p1 = _whatsApp.WhatsApp()
    p1.send_message_to_unsavaed_contact("91"+ str(contact), message, 1)



##username = ["Deepika", "Sonu Dubey Dubey", "Vijay 1"]
##for user in username:
##    p1.send_message(user, "Hello", 1)






