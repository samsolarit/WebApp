from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the ATEN Box Informational Page. The Aten Box is a project by Samuel Scott, Jr. for Photovoltaic and Datascience purposes."

@app.route('/index', methods=['GET', 'POST'])
def pictures():
    return app.send_static_file('webappindex.html')

if __name__== "__main__":
        app.run(debug=True)