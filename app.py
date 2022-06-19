from flask import Flask, redirect, url_for, render_template, request
import time
import RPi.GPIO as GPIO

app = Flask(__name__)


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

A = 7
B = 11
C = 13
D = 15

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)


@app.route("/slider", methods=["POST", "GET"])
def slider():
    if request.method == "POST":
         slidervalue = request.form["slider"]
         return redirect(url_for("value", val=slidervalue))
    else:
         return render_template("slider.html")



@app.route("/<val>")
def value(val):
    return render_template("value.html")



def GPIO_SETUP(a,b,c,d):
 GPIO.output(A, a)
 GPIO.output(B, b)
 GPIO.output(C, c)
 GPIO.output(D, d)
 time.sleep(0.001)

def RIGHT_TURN(deg):

 full_circle = 510.0
 degree = full_circle/360*deg
 GPIO_SETUP(0,0,0,0)

 while degree > 0.0:
  GPIO_SETUP(1,0,0,0)
  GPIO_SETUP(1,1,0,0)
  GPIO_SETUP(0,1,0,0)
  GPIO_SETUP(0,1,1,0)
  GPIO_SETUP(0,0,1,0)
  GPIO_SETUP(0,0,1,1)
  GPIO_SETUP(0,0,0,1)
  GPIO_SETUP(1,0,0,1)
  degree -= 1

def LEFT_TURN(deg):

 full_circle = 510.0
 degree = full_circle/360*deg
 GPIO_SETUP(0,0,0,0)

 while degree > 0.0:
  GPIO_SETUP(1,0,0,1)
  GPIO_SETUP(0,0,0,1)
  GPIO_SETUP(0,0,1,1)
  GPIO_SETUP(0,0,1,0)
  GPIO_SETUP(0,1,1,0)
  GPIO_SETUP(0,1,0,0)
  GPIO_SETUP(1,1,0,0)
  GPIO_SETUP(1,0,0,0)
  degree -= 1


deg = {val}
if 0<deg<=360:
  RIGHT_TURN(deg)

GPIO_SETUP(0,0,0,0)
    

@app.route("/")
def webapp():
    return render_template("webapp.html")
    

if __name__ == "__main__":
    app.run(debug=True)