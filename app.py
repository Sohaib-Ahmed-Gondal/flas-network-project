from flask import Flask, render_template, request
import socket
import platform
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    ip_address = request.remote_addr
    hostname = socket.gethostname()
    os_info = platform.system() + " " + platform.release()
    browser = request.user_agent.browser
    time_accessed = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("index.html", ip=ip_address, hostname=hostname,
                           os_info=os_info, browser=browser, time=time_accessed)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
