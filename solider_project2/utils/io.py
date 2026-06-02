import json
from logger_config import logger




def load_soliders_from_jason(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            logger.info("succssesfuly readed")
            return json.load(file)
    except:
        logger.warning("current file not found: open a new file")
        with open(filename,"w",encoding="utf-8") as file:
            json.dump([],file,indent=2)
            
            
            
def get_one_solider(filename,id):
    pass            
            
            
            
def save_to_jason(filename,soliders:list):
    try:
        with open(filename,"w",encoding="utf-8") as file:
            json.dump(soliders,file,indent=2)
            logger.info("succsseful saved")
    except Exception as e:
        logger.error(f'save falied error{e}')
                
                
                
def add_solider(filename,body:dict):
    logger.info("try to add a new solider")
    soliders_list=load_soliders_from_jason(filename)
    soliders_list.append(body)
    logger.info(f'solider {body} as aded')
    save_to_jason(filename,soliders_list)

