'''
import welcome_file as welcome
import data_wrangling


name_of_person=welcome.welcome_everyone()
welcome.greet(name_of_person)
data_patient=data_wrangling.collect_patient_information()
data_wrangling.make_it_look_good(data_patient)
'''
'''
from welcome_file import greet
greet('siddhant')

'''

from welcome_file import *
name_of_person=welcome_everyone()

greet(name_of_person)
