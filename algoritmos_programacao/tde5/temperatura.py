from xml.dom import InuseAttributeErr


celsius = float(input("Insira a temperatura em celsius :"))
celsius_para_fahrenheit = 9/5*celsius +32
fahrenheit_para_kelvin = 5/9*celsius_para_fahrenheit +273,15

print("A temperatura em Celsius é de: ",celsius,)
print("A temperatura em Fahrenheit é de: ",celsius_para_fahrenheit,)
print("A temperatura em Kelvin é de: ",fahrenheit_para_kelvin,)