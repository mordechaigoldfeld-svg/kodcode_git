import json




def load_soliders_from_jason(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            return json.load(file)
    except:
        with open(filename,"w",encoding="utf-8") as file:
            json.dump([],file,indent=2)
