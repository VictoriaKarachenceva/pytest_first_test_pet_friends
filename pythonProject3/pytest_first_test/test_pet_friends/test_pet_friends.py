from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

#Проверяем валидность пользователя
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

#Проверяем вход пользователя c неверным логином
def test_get_api_key_for_invalid_user_login(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' in result

#Проверяем вход пользователя c неверным паролем
def test_get_api_key_for_invalid_user_password(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' in result

#Проверяем возврат не пустого списка при запросе моих валидных питомцев
def test_get_api_all_pets_with_valid_key(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

#Проверяем возможность добавления питомца с корректными данными и фото
def test_post_api_pets_set_photo_with_valid_data(name='Буся', animal_type='Пудель',
                                     age='3', pet_photo='images/dog.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_set_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

#Проверяем возможность добавления питомца с отрицательным возрастом
def test_post_api_pets_set_photo_with_negative_age(name='Стрелка', animal_type='Колли',
                                     age='-10', pet_photo='images/dog.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_set_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result['age'] == age

#Проверяем возможность добавления другого питомца с корректными данными и фото
def test_post_api_pets_set_photo_next_pet_with_valid_data(name='Мурзик', animal_type='Кошка',
                                     age='5', pet_photo='images/cat.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_set_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

#Проверяем возможность добавления питомца с несуществующим возрастом
def test_post_api_pets_set_photo_pet_with_old_age(name='Мурзик', animal_type='Кошка',
                                     age='2021', pet_photo='images/cat.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_set_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result['age'] == age

#Проверяем возможность добавления питомца без указания имени
def test_post_api_pets_set_photo_pet_without_name(name='', animal_type='Кошка',
                                     age='5', pet_photo='images/cat.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_set_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result['name'] == name

#Проверяем возможность добавления питомца без указания возраста
def test_post_api_pets_set_photo_pet_without_age(name='Мурзик', animal_type='Кошка',
                                     age='', pet_photo='images/cat.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_set_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result['age'] == age

#Проверяем возможность добавления питомца без указания вида животного
def test_post_api_pets_set_photo_pet_without_type(name='Мурзик', animal_type='',
                                     age='5', pet_photo='images/cat.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_set_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result['animal_type'] == animal_type

#Проверяем возможность добавления питомца c числовым значением имени и вида
def test_post_api_pets_set_photo_pet_with_numerical_value(name='3569021', animal_type='1209653',
                                     age='3', pet_photo='images/dog.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_set_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result['name'] == name

#Проверяем возможность добавления питомца c нулевым значением имени, вида и возраста
def test_post_api_pets_set_photo_pet_with_zero_value(name='0', animal_type='0',
                                     age='0', pet_photo='images/cat.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_set_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result['name'] == name

#Проверяем возможность добавления питомца c указанием возраста нечисловым значением
def test_post_api_pets_set_photo_pet_without_int(name='Стрелка', animal_type='Колли',
                                     age='lоgarithm', pet_photo='images/dog.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_set_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result['age'] == age

#Проверяем возможность удаления питомца
def test_delete_api_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_api_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.post_api_pets_set_photo(auth_key, 'Пушочек', 'Dog', '2', "format(_.jpg)")
        _, my_pets = pf.get_api_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_api_pet(auth_key, pet_id)
    _, my_pets = pf.get_api_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()

#Проверяем возможность обновления данных питомца
def test_put_api_pet_info(name='Ласка', animal_type='Кошка', age='4'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_api_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.put_api_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

#Проверяем возможность добавления питомца с корректными данными без фото
def test_post_api_pet_info_without_photo(name='Рекс', animal_type='Боксер', age='4'):
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.post_api_pet_info(auth_key, name, animal_type, age)
        assert status == 200
        assert result['name'] == name

#Проверяем возможность добавления фото питомца
def test_post_api_add_photo_of_pet(pet_photo='images/dog.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_api_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.post_api_add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    assert result['images/dog.jpg'] == pet_photo