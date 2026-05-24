from utils import find_by_id,is_valid_name
from data import solider_list_test







def add_solider(solider_id:int,solider_name:str):
    if find_by_id(solider_id):
        raise ValueError(f'id: {solider_id} exists in the system!')
    if not is_valid_name(solider_name):
        raise ValueError(f'invalid name')
    else:
        solider=({'id':solider_id,'name':solider_name,'duty':[{'n_duty':'','day':'','status':''}]})
        solider_list_test.append(solider)












# add_solider(333,'moty')
# print(solider_list_test)
