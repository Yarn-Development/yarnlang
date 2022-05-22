import yrn
while True:
    text = input("Yarn >> ")
    result,error = yrn.run('<stdin>',text)
    if error: print(error.as_string())
    else: print(result)