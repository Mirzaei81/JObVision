import requests 
from bs4 import BeautifulSoup
import json

job = {}
def ponisha():
    for i in range(1,22):
        ponishaUrl = f"https://ponisha.ir/search/projects/skill-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%AA%D8%AD%D8%AA-%D9%88%D8%A8/status-open/page/{i}"
        res = requests.get(ponishaUrl)
        data= res.content.decode('utf-8')
        soup = BeautifulSoup(data,"html.parser")
        labelbar=soup.find_all(lambda tag:tag.get('class')==['labels','clearfix'])
        strings = ""
        for label in labelbar:
            labelString = label.get_text().split()
            for tags in labelString:
                strings +=(tags+'\n')
                match tags:
                    case "ASP.Net": 
                        if "ASP.Net" in job:
                            job["ASP.Net"]+=1;
                        else:
                            job["ASP.Net"]=0;
                    case "(Cloud": 
                        if "CloudComputing" in job:
                            job["CloudComputing"]+=1;
                        else:
                            job["CloudComputing"]=1;

                    case "Microsoft": 
                        if "MicrosoftSQLServer" in job:
                            job["MicrosoftSQLServer"]+=1;
                        else:
                            job["MicrosoftSQLServer"]=1;
                    case "(React)": 
                        if "React" in job:
                            job["React"]+=1;
                        else:
                            job["React"]=1;

                    case "(Node.js)": 
                        if "Node.js" in job:
                            job["Node.js"]+=1;
                        else:
                            job["Node.js"]=1;

                    case "(Larvel)": 
                        if "Larvel" in job:
                            job["Larvel"]+=1;
                        else:
                            job["Larvel"]=1;

                    case "(MySQL)": 
                        if "MySql" in job:
                            job["MySql"]+=1;
                        else:
                            job["MySql"]=1;

                    case "(Css)": 
                        if "Css" in job:
                            job["Css"]+=1;
                        else:
                            job["Css"]=1;
                    case "(php)": 
                        if "php"in job:
                            job["php"]+=1;
                        else:
                            job["php"]=1;

                    case "(Telegram)": 
                        if "Telegram"in job:
                            job["Telegram"]+=1;
                        else:
                            job["Telegram"]=1;

                    case "(Django)": 
                        if "Django"in job:
                            job["Django"]+=1;
                        else:
                            job["Django"]=1;

                    case "(WordPress)": 
                        if "WordPress"in job:
                            job["WordPress"]+=1;
                        else:
                            job["WordPress"]=1;
                    case "(Prestashop)": 
                        if "Prestashop"in job:
                            job["Prestashop"]+=1;
                        else:
                            job["Prestashop"]=1;
    with open("tags.txt",'w') as fs:
        fs.writelines(strings)

ponisha()
print(job)
