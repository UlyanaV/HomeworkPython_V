# 2

def ident_f(fistname, lastname, year, city, email, phone):
    print(f"фамилия: {lastname}; имя: {fistname}; год рождения: {year}; "
          f"город проживания:{city}, email: {email}, телефон: {phone} ")


user_fistname = input('Введите имя ')
user_lastname = input('Введите фамилия ')
user_year = input('Введите год рождения ')
user_city = input('Введите город проживания ')
user_email = input('Введите email ')
user_phone = input('Введите телефон ')

ident_f(fistname=user_fistname, lastname=user_lastname, year=user_year,
        city=user_city, email=user_email, phone=user_phone)
