#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
import sqlite3
GPIO.setwarnings(False)

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

#GPIO Pins zuweisen
GPIO_LED = 16
GPIO_TASTER = 18

#Richtung festlegen (IN / OUT)
GPIO.setup(GPIO_LED, GPIO.OUT)
GPIO.setup(GPIO_TASTER, GPIO.IN)

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#db_path = os.path.join(BASE_DIR, "worker.db")
#print(db_path)

class Taster():

    def switch(self, LED_Status):

        LED_Status = False

        while True:
            if GPIO.input(GPIO_TASTER) == GPIO.HIGH and LED_Status == False:
        
                LED.On(1)
                LED_Status = True
                print("an")
                time.sleep(0.2)
        
                # Taster gedrückt und LED aus == LED aus 
            elif GPIO.input(GPIO_TASTER) == GPIO.HIGH and LED_Status == True:
                
                LED.Off(1)
                LED_Status = False
                print("aus")
                time.sleep(0.2)

class LED():

    def On(self):
        GPIO.output(GPIO_LED, GPIO.HIGH)

    def Off(self):
        GPIO.output(GPIO_LED, GPIO.LOW)

            
if __name__ == "__main__":
	Taster.switch(1, False)
