from ast import Global
from flask import Flask,render_template,request
import threading
import time
import requests



inplace=[0,0,0,0,0,0,0]
RS=0
l1=0.0000
l2=0.0000
l3=0.0000
u1=0.0000
u2=0.0000
u3=0.0000
tokenpair="usdtinr"
level_1_rs=RS/3
level_2_rs=RS/3
level_3_rs=RS/3
total_tokens=0
def thread_function(name):

    while 1:

        if(RS<=0):
            print("0 Balance ")
            time.sleep(2)
            #continue
        if ((l1<=0)|(l2<=0)|(l3<=0)|(u1<=0)|(u2<=0)|(u3<=0)):
            print("Sell and Buy points not set")
            time.sleep(2)
            #continue
        data = requests.get('https://api.wazirx.com/api/v2/tickers')
        tokenvalue=float(data.json()[tokenpair]['last'])
        if tokenvalue <=l1 :
            print("Triggered Buy 1")
            total_tokens+=level_1_rs/tokenvalue
            print ("Bought "+str(total_tokens)+" Token") 

        if tokenvalue <=l2 :
            print("Triggered Buy 2")
            total_tokens+=level_2_rs/tokenvalue
            print ("Bought "+str(total_tokens)+" Token") 
        if tokenvalue <=l3 :
            print("Triggered Buy 3")
            total_tokens+=level_3_rs/tokenvalue
            print ("Bought "+str(total_tokens)+" Token") 
        if tokenvalue >=u1 :
            print("Triggered Sell 1")
            RS=tokenvalue*(total_tokens/3)
        if tokenvalue >=u2 :
            print("Triggered Sell 2")
            RS=tokenvalue*(total_tokens/3)
        if tokenvalue >=u3 :
            RS=tokenvalue*(total_tokens/3)
            print("Triggered Sell 3")
            
        print("Thread %s: starting", name)
        time.sleep(1)
        



app = Flask(__name__)
 
@app.route('/set')
def form():
    return render_template('set.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    global RS
    global l1,level_1_rs
    global l2,level_2_rs
    global l3,level_3_rs
    global u1
    global u2
    global u3
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        data = request.form

        RS+=float(data['Rs'])#adding RS to existing
        print(RS)
        l1=float(data['l1'])
        u1=float(data['u1'])
        l2=float(data['l2'])
        u2=float(data['u2'])
        l3=float(data['l3'])
        u3=float(data['u3'])
        level_1_rs+=RS/3
        level_2_rs+=RS/3
        level_3_rs+=RS/3
        return render_template('data.html',form_data = data)
 
x = threading.Thread(target=thread_function, args=(1,))
x.start()

app.run(host='localhost', port=5000)
print("End")
