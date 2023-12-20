T=float(input("Enter the value of T:"))
H=float(input("Enter the value of H:"))
w=float(input("Enter the value of w:"))
W=(0.5*T**2-0.2*H+0.1*w-15)
print("W=",W)
if(W>300):
    print("The weather is Sunny")
elif(200<W<=300):
    print("The weather i Cloudy")
elif(100<W<=200):
    print("The weather is Rainy")
else:
    print("The weather is Stormy")
