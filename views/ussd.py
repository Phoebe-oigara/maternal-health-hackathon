import os
from flask import Flask, request
import africastalking
username = "Oigara98"
api_key = "cc528257e0e577f18fd43d884357532d36ba166c83fee644a11704d9572fb99f"

        # Initialize the SDK
africastalking.initialize(username, api_key)

# Get the SMS service
sms = africastalking.SMS
app = Flask(__name__)

def send(phoneNumber, msg):
    print("sender ", phoneNumber)
    # Set the numbers you want to send to in international format
    recipients = [phoneNumber]

    # Set your message
    message = msg

    # Set your shortCode or senderId
    # sender = "shortCode or senderId"
    try:
        # Thats it, hit send and we'll take care of the rest.
        response = sms.send(message, recipients)
        print (response)
    except Exception as e:
        print ('Encountered an error while sending: %s' % str(e))


@app.route("/ussd", methods = ['POST'])
def ussd():
  # Read the variables sent via POST from our API
  session_id   = request.values.get("sessionId", None)
  serviceCode  = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  print("am phone ", phone_number)
  text         = request.values.get("text", "default")

  if text      == '':
      # This is the first request. Note how we start the response with CON
      response  = "CON Welcome to CareCorner postnatal health services \n"
      response += "1. Postnatal health information and tips \n"
      response += "2. Schedule postnatal checkup \n"
      response += "3. Emotional wellbeing \n"
      response += "4. Nutrition \n"
      response += "5. EXit \n"


  elif text    == '1':
      # Business logic for first level response
      response  = "CON choose postnal health service \n"
      response += "1 Newborn care\n"
      response += "2 postpartum recovery \n"
      response += "3 Breastfeeding \n"
      response += "4 Hygiene and sexual health \n"
      #response += "5 Back to main menu \n"
      


  elif text   == '2':
      # This is a terminal request. Note how we start the response with END
      response  = "CON Schedule checkup \n"
      response += "1 Book a checkup \n"
      response += "2 View upcoming appointment \n"
      response += "3 Cancel apporintment \n"
      #response += "4 Back to main menu \n"
      #response = "END Your phone number is " + phone_number

  elif text   == '3':
      # This is a terminal request. Note how we start the response with END
      response  = "CON Emotional wellbeing\n"
      response += "1 Learn about postpartum depression \n"
      response += "2 Self-assessment \n"
      response += "3 Connect with a cousellor\n"
      #response += "4 Back to main menu \n"

  elif text == '1*1':

      # This is a second level response where the user selected 1 in the first instance
      # This is a terminal request. Note how we start the response with END
      msg="Tip 1:Essential newborn care immediately after birth includes delayed cord clamping, thorough drying, assessment of breathing, skin to skin contact and early initiation of breatsfeeding. \n Tip 2: During newborn period give nurturing care and assess for any health problems. \nTip 3: Support for breast milk feeding. \n Tip 4:Recognise and respond to danger signs"
      send(phone_number, msg)
      response       = "END Thank you for visiting, we have sent you an sms with all the tips you need " 

  elif text == '1*2':

      # This is a second level response where the user selected 1 in the first instance
      # This is a terminal request. Note how we start the response with END
      msg="Postpartum recovery requires taking care of your mental health, hygiene and any wounds from childbirth. Encourage your partner to be involved so you can rest"
      send(phone_number, msg)
      response       = "END Thank you for visiting, we have sent you an sms with all the tips you need "

  elif text == '1*3':

      # This is a second level response where the user selected 1 in the first instance
      # This is a terminal request. Note how we start the response with END
      msg="For best breatfeeding results support your baby's neck, shoulders and back to allow them to tilt their head back and swallow easily. Avoid leaning your breast forward into your baby's mouth as this can lead to poor attachment"
      send(phone_number, msg)
      response       = "END Thank you for visiting, we have sent you an sms with all the tips you need "

  elif text == '1*4':

      # This is a second level response where the user selected 1 in the first instance
      # This is a terminal request. Note how we start the response with END
      msg="Handwash wounds to prevent infections. Do not insert anything into vagina after childbirth. Use maternal pads to control bleeding. Sexual intercourse should be avoided until perineal wound heals"
      send(phone_number, msg)
      response       = "END Thank you for visiting "
  elif text == '1*5':

      # This is a second level response where the user selected 1 in the first instance
      # This is a terminal request. Note how we start the response with END
      msg="thanks"
      send(phone_number, msg)
      response       = "CON 1"

  elif text == '3*4':

      # This is a second level response where the user selected 1 in the first instance
      # This is a terminal request. Note how we start the response with END
      msg="thanks"
      send(phone_number, msg)
      response       = "END Thank you for visiting, we have sent you an sms with all the tips you need "

  else :
      response = "END Invalid choice"

  # Send the response back to the API
  return response



if __name__ == '__main__':
    app.run(debug=True)

# sms


