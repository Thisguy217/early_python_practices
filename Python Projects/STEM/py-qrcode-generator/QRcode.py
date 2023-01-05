import qrcode

# Create the variable to store the information
data = "You are about to be rick-rolled"
print("Data Accepted")

# Generate QR Code
img=qrcode.make(data)
print(type(img))
print("QR Code Generated")

#Saves QR Code
img.save("qrcode.jpg")
print("QR Code Saved")