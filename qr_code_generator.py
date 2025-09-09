#Author= ARNAB BAG

import qrcode 

upi_id = input ("enter your upi id : ")

#upi://pay ?pa=upi_id & pn= name & am= amount & currency & tn=message

phone_pay = f"upi://pay ?pa={upi_id} & pn= recipient & am= amount & cu=currency & tn=message"
google_pay = f"upi://pay ?pa={upi_id} & pn= recipient & am= amount &cu=currency & tn=message"
paytm= f"upi://pay ?pa={upi_id} & pn= recipient & am= amount & cu=currency & tn=message"


# generate qrcode

phone_pay_qr= qrcode.make(upi_id)
google_pay_qr= qrcode.make(upi_id)
paytm_qr= qrcode.make(upi_id)

#if want to save qrcode in image

phone_pay_qr.save("phone_pay-qr.png")
google_pay_qr.save("google_pay_qr.png")
paytm_qr.save("paytm_qr.png")

#display qrcode

phone_pay_qr.show()
google_pay_qr.show()
paytm_qr.show()