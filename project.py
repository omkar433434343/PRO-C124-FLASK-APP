from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        'id':1,
        'name':'ram',
        'contact':'9888891234',
        'done':True
    },
    {
        'id':2,
        'name':'rahul',
        'contact':'1234988988',
        'done':False
    }
]
@app.route('/adddata',methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide phone datya'
        },400
        )
    task={
        "id":tasks[-1]['id']+1,
        "name":request.json['name'],
        "contact":request.json.get('contact',""),
        "done":True
        }

    tasks.append(task)
    return jsonify({
        'done':'success',
        'message':'number added'
    })

@app.route('/getdata')
def get_task():
    return jsonify({
        "data":tasks
    })  
@app.route("/")

def hello_world():
    return 'hello world'

if (__name__=='__main__'):
    app.run(debug=True)
