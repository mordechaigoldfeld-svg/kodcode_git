from utils import find_by_id,is_valid_name
from data import solider_list_test






"""הוספת חייל"""
def add_solider(solider_id:int,solider_name:str):
    if find_by_id(solider_id):
        raise ValueError(f'id: {solider_id} exists in the system!')
    if not is_valid_name(solider_name):
        raise ValueError('invalid name')
    else:
        solider=({'id':solider_id,'name':solider_name,'duty':[{'n_duty':'','day':'','status':''}]})
        solider_list_test.append(solider)



"""מחיקת חייל"""
def remove_solider(id:int):
    solider_exist = find_by_id(id)
    if solider_exist:
        solider_list_test.remove(solider_exist)
    else:
        raise KeyError(f':{id} not exist')



def get_all_soliders():
    for solider in solider_list_test:
        print(solider)




