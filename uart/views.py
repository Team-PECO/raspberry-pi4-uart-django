from django.shortcuts import render, redirect
from django.http import HttpResponse
import serial

def index(request):
    return render(request, 'uart/index.html')

def manual_control(request):
    # Your manual control logic here
    return render(request, 'uart/manual.html')

def automatic_control(request):
    # Your automatic control logic here
    return render(request, 'uart/automatic.html')

def send_uart_command(request, command):
    try:
        # Open serial port
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.write(command.encode('utf-8'))
        ser.close()
        return HttpResponse(f"Command {command} sent successfully")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
