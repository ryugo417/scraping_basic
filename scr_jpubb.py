import requests
from bs4 import BeautifulSoup

ur=input("スクレイピングしたいURLを入力してください(ID番号なし)．")
max_page=input("ページ数を入力してください.")

 
def set_url(num1):
    url = requests.get(str(ur)+str(num1+1))
    soup = BeautifulSoup(url.content, "html.parser")
    all_text=soup.find(class_="corpTable").text
    all_text_list=all_text.split("\n")
    return all_text_list

def set_ur(num2):
    url = requests.get(str(ur)+str(num2+1))
    soup = BeautifulSoup(url.content, "html.parser")
    hps = soup.select('a')
    return hps

#def print_text(nam3):
#    for nam3 in range(int(max_page)):
#    all_text_list=set_url(nam3)
#    for i in range(4,len(all_text_list),6):
#        print(all_text_list[i])

print("社名を表示します")
#print_text(num)
for num in range(int(max_page)):
    all_text_list=set_url(num)
    for i in range(4,len(all_text_list),6):
        print(all_text_list[i])
print()
print("本社の場所を表示します")
for num in range(int(max_page)):
    all_text_list=set_url(num)
    for i in range(4,len(all_text_list),6):
        all_text_list2=all_text_list[i+1].split("|")
        print(all_text_list2[2])
print()
print("URLを表示します．")
for num in range(int(max_page)):
    hps=set_ur(num)
    for hp in hps:
        if "jpubb" not in hp.get('href'):
            if "list" not in hp.get('href'):
                if "JavaScript" not in hp.get('href'):
                    if "redcruise" not in hp.get('href'):
                        print('{}'.format(hp.get('href')))












  

