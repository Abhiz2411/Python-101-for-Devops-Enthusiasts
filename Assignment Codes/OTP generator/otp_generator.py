import random, string
otp = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
print("Your OTP is:", otp)