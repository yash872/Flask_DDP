from flask import Flask, render_template,stream_with_context, request, Response
from execute import execute
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('home.html')


@app.route('/etrade') 
def etrade(): 
	return render_template('script.html', console_gave =execute()) 






if __name__ == '__main__':
    app.run(debug=True)