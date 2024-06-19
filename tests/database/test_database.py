import pytest
from sqlite3 import  Error, DatabaseError, IntegrityError, OperationalError
from modules.common.database import Database
import datetime


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print (users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    name = 'Sergii'
    user = db.get_users_address_by_name(name)

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db= Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():

    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detalied_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] =='Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

#Тести для виконання індивідуальної частини проєктного завдання. 
#Мітка database_prj використана для фільтрації індивідуальних тестів

@pytest.mark.database
def test_add_new_user_without_some_inform():
    db = Database()
    new_user1 = db.insert_new_users(4, "Ivan", 'Kyivska str, 2', None, None, "Poland")
    new_user1 = db.get_users_address_by_name('Ivan')
    #Коментарем позначено частину коду який використовувався для перевірки правильності виконання запиту 
    #all_users = db.get_all_users()
    #print(all_users)
    #print(new_user)
    assert new_user1[0][0] == 'Kyivska str, 2'
    assert new_user1[0][1] == 'None'
    assert new_user1[0][2] == 'None'
    assert new_user1[0][3] == "Poland"

@pytest.mark.database
def test_add_new_user_with_incorrect_type_of_id():
    db = Database()
    with pytest.raises(OperationalError):
        new_user2 = db.insert_new_users('q', 'Oleh', "Symonenka str, 5", 555, 5555, 55555)
    

@pytest.mark.database
def test_add_new_product_with_incorrect_type_of_qnt():
    db = Database()
    with pytest.raises(OperationalError):
        new_product = db.insert_product(5, 'Chery', "Fruit", "10kg")

@pytest.mark.database_prj
def test_add_new_order_with_correct_type_of_datetime():
    db = Database()
    date = datetime.datetime.now()
    new_order = db.insert_new_order(6, 2, 1,(date.strftime('%X')))
    orders = db.get_detailed_orders()
    #Перевіряємо чи нове замовлення додано
    print(db.get_detailed_orders())
    assert orders[5][0] == 6
    assert orders[5][1] == "Stepan"
    assert orders[5][2] == "солодка вода"
    assert orders[5][3] == "з цукром"
    assert orders[5][4] == date.strftime('%X')
    


@pytest.mark.database
def test_get_all_us():
    db = Database()
    users = db.get_all_users()
    order = db.get_detailed_orders()
    print(order)
    print(users)


    

