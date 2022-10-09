def get_absolute_phone_number(phone_number):
    new_phone = phone_number.split('@')
    absolute_phone_number = new_phone[0]
    return absolute_phone_number
