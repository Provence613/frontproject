from django.shortcuts import render
from django.shortcuts import  HttpResponse
import os
import json
# Create your views here.


# 将请求定位到index.html文件中
def experiment(request):
    return render(request, 'experiment_py.html')
def deal(request):
    difficulty = [];
    blockgaslimit =[];
    start_type ="";
    client_type ="";
    nodeCount =0;
    if request.method=="POST":
        difficultystr = request.POST.get("Difficulty", None)
        difficulty=difficultystr.split(" ")
        blockgaslimitstr = request.POST.get("gaslimit", None)
        blockgaslimit=blockgaslimitstr.split(" ")
        start_type= request.POST.get("start_type", None)
        client_type=request.POST.get("client_type", None)
        nodeCount=int(request.POST.get("node_count", None))
    data={}
    data['difficulty'] = difficulty;
    data['gaslimit'] = blockgaslimit;
    data['nodeCount'] =nodeCount;
    data['startUpType'] =start_type;
    data['clientType'] =client_type;
    file = open('static/json/config.json', 'w', encoding='utf-8')
    json.dump(data, file, ensure_ascii=False)
    file.close()
    # 可运行cmd命令
    # a=os.system(r"python d:\helloworld.py")
    if os.path.exists("static/json/report.json"):
        return render(request,'list_throughput.html')
    else:
        return render(request, 'load.html')

