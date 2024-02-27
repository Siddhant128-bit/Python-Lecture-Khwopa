'''
make a script to basically take in these informations

patient name: 
parents name: 
dr name: 
diagnosis: 
date_of_departure: 

'''
def collect_patient_information():
    patient_info_dict={}
    patient_info_dict['name']=input('Enter patient name: ')
    patient_info_dict['parents_name']=input('Enter parents name: ')
    patient_info_dict['dr_name']=input('Enter doctor name')
    patient_info_dict['diagnosis']=input('Enter diagnosis: ')
    patient_info_dict['departure']=input('Enter departure date: ')
    #print(patient_info_dict)
    return patient_info_dict

def make_it_look_good(dict_val):
    name=dict_val['name']
    print(f'name: {name}')
    #print(f'parents name: {dict_val['parents_name']}')

if __name__=='__main__':
    collect_patient_information()