import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import *

file = open('clinics.csv', 'w', encoding='utf-8_sig', newline='\n')
f_obj = csv.writer(file)
f_obj.writerow(['Clinic Name', 'Address', 'Rating ?/5'])


page = 1
while page < 6:
    url = 'https://tsamali.ge/clinics/' + str(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    sub_soup = soup.find('div', class_= 'doctor_items')
    clinics = sub_soup.find_all('div', class_= 'doctor_item doctor_item_inside')
    for each in clinics:
        title =  each.find('div', class_='doctor_item_r').a.text.strip()
        address_l = each.find('div', class_='doctor_clinics')
        address = address_l.find('div', class_='doctor_clinic_location').text.strip()
        rating_l= each.find('div', class_= 'doctor_item_l')
        rating = rating_l.find('div', class_= 'item_rank_text left').text.strip()
        f_obj.writerow(([title, address, rating]))

    page += 1

    sleep(randint(10,20))