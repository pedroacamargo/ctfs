import base64

msg = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

bytess = bytes.fromhex(msg)

print(bytess)

base64value = base64.b64encode(bytess)

print(base64value)

# In Python, after importing the base64 module with import base64, you can use the base64.b64encode() function. Remember to decode the hex first as the challenge description states.
