import serial
import time

# Set up the serial connection with the Raspberry Pi Pico (replace with correct port)
pico_ser = serial.Serial('COM3', 115200)  # Change to your device's path
#printer_ser = serial.Serial('/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0', 250000) 

while True:
    # Read a line of serial data from the Pico
    data = pico_ser.readline().decode('utf-8').strip()
    print(f"Received: {data}")

    # Check for the "SWITCH_TRIGGERED" message from the Pico
    if data == "1":
        print("Switch triggered : send gcode")
        print("G1 X30")
        #pico_ser.write(b'G1 X30\n')
        print("")

        # Send a command to Klipper via serial (e.g., to start a print)
        # Here, we're just sending a simple command to home the 3D printer

    elif data == "0":
        print("Switch off")
        print("")
    
    time.sleep(0.1)  # Delay to avoid busy-waiting too much
