import scratchattach as scratch3,time,random,requests
import configparser

#ConfigParserオブジェクトを生成
config = configparser.ConfigParser()

#設定ファイル読み込み
config.read('Gobo.ini')


session = scratch3.login(config["server"]["account"], config["server"]["pass"]) # 自分のパスワード
conn = session.connect_cloud(config["server"]["id"]) # project_id
act=config["server"]["account"]
# https://scratch.mit.edu/projects/767766792/
variables = scratch3.get_cloud(config["server"]["id"]) # Returns a dict with all cloud var values
while True:
    variables = scratch3.get_cloud(config["server"]["id"])
    print(variables)
    name=variables.keys()
    #print(dict(variables)["follow"])
    value = name
    time.sleep(5)
    getdata1=requests.get(f"https://api.scratch.mit.edu/users/{act}/messages/count/").json()
    conn.set_var("messeage",str(getdata1["count"]))
    getdata2=scratch3.get_user(act).following_count()
    conn.set_var("follow",str(getdata2))
    getdata3=scratch3.get_user(act).follower_count()
    conn.set_var("follower",str(getdata3))

conn.disconnect()
print("hello")
