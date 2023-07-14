from dotenv import load_dotenv
from flask import Flask,jsonify,request
from google.cloud import run_v2
import os

load_dotenv()  # take environment variables from .env

project_id = os.environ["PROJECT_ID"]
region = os.environ["REGION"]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "i just wanted to get the gang together early in my tenure to say....yo."

'''
@app.route('/jobs',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        client = run_v2.JobsClient()
        parent = f"projects/{project_id}/locations/{region}"
        req = run_v2.ListJobsRequest(
            parent = parent
        )
        page_result = client.list_jobs(request=req)
        jobs = []
        for response in page_result:
            #print(response.__dict__)
            jobs.append(response.__dict__)
        return jobs
'''

@app.route('/executions',methods= ['POST', 'GET'])
def executions():
    if request.method == 'POST':
        pass
    else:
        client = run_v2.ExecutionsClient()
        parent = f"projects/{project_id}/locations/{region}/jobs/worker"
        print(parent)
        req = run_v2.ListExecutionsRequest(
            parent="parent_value",
        )
        page_result = client.list_executions(request=req)
        for response in page_result:
            print(response)
        return "hi"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)),
        threaded=True)