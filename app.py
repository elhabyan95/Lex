from flask import Flask, request, render_template,jsonify
import time
import importlib
import final
import pandas as pd
app = Flask(__name__)

def do_something(text1):
   try:
       file2=pd.read_excel(text1)
       text12,a,b,c=[],[],[],[]
       tweetdic={}
       for tweet in file2[file2.columns[0]]:
           text11, a1 , b1, c1 = final.dunc(tweet)
           text12.append(text11)
           a.append(a1)
           b.append(b1)
           c.append(c1)
           tweetdic[tweet]=[text11,a1,b1,c1]

       return tweetdic,text12,a,b,c

           


   except:
       text12, a , b, c = final.dunc(text1)
       return text12,a,b,c
   #text1=xcode.hi()
#    print(text1,a,b,c,'SERVER')
#    return {'text1':text1,'a':a , 'b':b, 'c':c}
   
@app.route('/')
def home():
    return render_template('same_page.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    # word = request.args.get('text1')
    # text2 = request.form['text2']
    combine,a,b,c= do_something(text1)
    # print('lll'.combine,a,b,c)
    combine=['The Effectiveness score is : '+str(combine),'The Efficiency score is : '+str(a),'The Satsfication score is : '+str(b),c]
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/fileUpload', methods=['GET','POST'])
def upload_file():
    file = request.files['file']
    # word = request.args.get('text1')
    # text2 = request.form['text2']
    tweetdic,combine,a,b,c= do_something(file)
    # combine=['The Effectiveness score is : '+str(combine),'The Efficiency score is : '+str(a),'The Satsfication score is : '+str(b),c]
    res=[]
    dic={}
    print(tweetdic,'tweetdic')
    for key,val in tweetdic.items():
        res.append(["tweet: "+key,' The Effectiveness score is : '+str(val[0]) ,' The Efficiency score is : '+str(val[1]),' The Satsfication score is : '+str(val[2]),val[3]])
        # res.append(["tweet: "+key,' The Effectiveness score is : '+str(val[0]) ,' The Efficiency score is : '+str(val[1]),' The Satsfication score is : '+str(val[2]),val[3]])
    # for i in range(len(combine)):
    #     res.append(['The Effectiveness score is : '+str(combine[i]) ,'The Efficiency score is : '+str(a[i]),'The Satsfication score is : '+str(b[i]),c[i]])
    result = {
        "output": res
    }
    result = {str(key): value for key, value in result.items()}
    # Satsfication=[cc.split(',').replace('(','') for cc in c]
    # Satsfication=[cc.split(',')[0].replace('(','') for cc in c]
    dd=pd.DataFrame({'tweet':tweetdic.keys(),'Effectiveness':combine,'Efficiency':a,'Satsfication':b,'overall Usability':c})
    dd.to_excel('results.xlsx')
    print(result,908)

    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
