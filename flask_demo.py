from app   import app
from flask import render_template
from flask import jsonify

@app.route('/')
@app.route('/GetFileInfo1', defaults = {'repo': 'missing'})
@app.route('/GetFileInfo1/<repo>')
def index(repo):
    return jsonify({'repo': repo})
#    return render_template('index.html', title = 'home', repository = repo)

@app.route('/GetFileInfo')
def GetFileInfo():
    block_info = {'blockId': '123',
                  'user': 'parasan',
                  'fileInfo': [{'file1': 'i_am_file1'},
                               {'file2': 'i_am_file2'},
                               {'file3': 'i_am_file3'}]}
#    return jsonify(block_info)
    return 'test'

@app.route('/default', defaults = {'name' : 'Missing'})
@app.route('/default/<name>')
def default(name):
	return 'The Value is: ' + name

@app.route('/stringroute/<string:name>')
def stringroute(name):
	return 'The Value is: ' + name

@app.route('/introute/<int:srno>')
def introute(srno):
	return 'The Number is: ' + str(srno)

@app.route('/floatroute/<float:srno>')
def floatroute(srno):
	return 'The Floating point number is: ' + str(srno)

@app.route('/pathroute/<path:mypath>')
def pathroute(mypath):
	return 'The path is: ' + mypath

@app.route('/combinedroute/<string:mystring>/<int:myint>')
def combinedroute(mystring, myint):
	return 'The string value is ' + mystring + ' and the int value is ' + str(myint)
