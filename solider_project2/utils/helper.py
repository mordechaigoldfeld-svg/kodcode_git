from logger_config import logger








# def validation_of_solider(body:dict):
#     try:
#         if len(body)==3:
#             if isinstance(body["full_name"],str) and isinstance(body["role"],str) and isinstance(body["id"],int) and body["full_name"]!="" and body["role"]!="" and body["id"]!="":
#                 return True
#         logger.warning("error, invalid input")    
#         return False
#     except Exception as e:
#         logger.error(f"invalid key error:{e}")    




def validation_of_solider(body:dict):
    try:
        if len(body)==3:
            if isinstance(body["full_name"],str) and isinstance(body["role"],str) and isinstance(body["id"],int) and body["full_name"]!="" and body["role"]!="" and body["id"]!="":
                return True
        logger.warning("error, invalid input")    
        return False
    except Exception as e:
        logger.error(f"invalid key error:{e}")  