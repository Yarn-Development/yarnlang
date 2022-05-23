import yrn
import signal
import sys
def sigint_handler(signal, frame):
    print ('KeyboardInterrupt')
    sys.exit(0)

while True:
    signal.signal(signal.SIGINT, sigint_handler)
    text = input("Yarn >> ")
    result,error = yrn.run('<stdin>',text)
    if error: print(error.as_string())
    else: print(result)
    
 

