from data import solider_list_test

"""חיפוש חייל לפי id"""
def find_by_id(solider_id):

    for solider in solider_list_test:
        if solider['id']==solider_id:
            return solider
    return None

""""ולידציה של השם"""
def is_valid_name(solider_name):
    if not solider_name:
        return False
    elif solider_name.isdigit():
        return False
    else:
        return True

if __name__=='__main__':
 print(is_valid_name(input('name')))








# m=find_by_id(123)
# print(m)