import json
from logger_config import logger
from utils import helper




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
    try:
        soliders_list=load_soliders_from_jason(filename)
        for solider in soliders_list:
            if solider["id"]==id:
                logger.info("get solider sucssesfuly")
                return solider
        logger.warning("id not found")           
    except Exception as e:
        logger.error(f"keyError:{e}")        
                
            
            
            
def save_to_jason(filename,soliders:list):
    try:
        with open(filename,"w",encoding="utf-8") as file:
            json.dump(soliders,file,indent=2)
            logger.info("succsseful saved")
    except Exception as e:
        logger.error(f'save falied error{e}')
                
                
                
def add_solider(filename,body:dict):
    logger.info("try to add a new solider")
    
    if helper.validation_of_solider(body):
        soliders_list=load_soliders_from_jason(filename)
        soliders_list.append(body)
        logger.info(f'solider {body} as aded')
        save_to_jason(filename,soliders_list)
      
def update_role(filename,id:int,data:str):
    logger.info("try to update a solider")
    try:
        soliders_list=load_soliders_from_jason(filename)
        for solider in soliders_list:
            if solider["id"]==id:
                solider["role"]=data
                save_to_jason(filename,soliders_list)
                logger.info(f"soldier updated succssesfuly:{solider}")
                return True     
        logger.warning("id not found")
        return False           
    except Exception as e:
        logger.error(f"keyError:{e}") 



def remove_solider(filename,id:int):
    try:
        logger.info("trying to remone a solider")
        soliders_list=load_soliders_from_jason(filename)
        updated_list=[]
        for solider in soliders_list:
            if solider["id"]==id:
                logger.info(f"{solider} has succssesfuly removed")
                continue
            updated_list.append(solider)
            save_to_jason(filename,updated_list)
            
        # logger.warning("id not found")
    except Exception as e:
        logger.error(f"error by remove {id}: {e}")          