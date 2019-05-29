 experiment.html将数据保存至json文件 
list开头的html是读取report.json并以图表显示 note:txCompeltion和detailedLatency已默认8*11 
方法1：直接运行experiment.html，config.json会下载到浏览器默认的目录 
方法2：运行Django项目后，在浏览器输入localhost:8000/experiment进入， 点击提交按钮后，
config.json会下载到浏览器默认的目录和../static/json目录下，（同时可以用os库调用cmd命令行(views.py)），
 程序会判断../static/json目录下是否存在report.json,存在后台跳转到list_throughput.html，不存在则显示程序正在运行。