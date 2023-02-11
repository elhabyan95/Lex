from flask import Flask, request, render_template,jsonify
import time
import importlib
import final
app = Flask(__name__)
def do_something(text1):
   print(text1)
   text1, a , b, c = final.dunc(text1)
   #text1=xcode.hi()
   print(text1,a,b,c,'SERVER')
#    return {'text1':text1,'a':a , 'b':b, 'c':c}
   return text1,a,b,c
@app.route('/')
    def home():
        return render_template('same_page.html')
@app.route('/fileUpload',  methods=['POST', 'GET'])
    def upload_file():
        file = request.files['file']
        print(file)
        # word = request.args.get('text1')
        # text2 = request.form['text2']
        combine,a,b,c= do_something(file)
        combine=['The Effectiveness score is : '+str(combine),'The Efficiency score is : '+str(a),'The Satsfication score is : '+str(b),c]
        result = {
            "output": combine
        }
        result = {str(key): value for key, value in result.items()}
        return jsonify(result=result)
@app.route('/join', methods=['GET','POST'])
    def my_form_post():
        text1 = request.form['text1']
        # word = request.args.get('text1')
        # text2 = request.form['text2']
        combine,a,b,c= do_something(text1)
        combine=['The Effectiveness score is : '+str(combine),'The Efficiency score is : '+str(a),'The Satsfication score is : '+str(b),c]
        result = {
            "output": combine
        }
        result = {str(key): value for key, value in result.items()}
        return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
