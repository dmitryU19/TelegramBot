from enum import Enum

token = "801826757:AAExGDlSSB7rK_3bUV3byWKEg1euB7acacg"
db_file = "database.vdb"


class States(Enum):
    S_START = "0"
    S_PERSONAL_DATA_REQUEST = "1"
    S_USER_SEARCH = "2"
    S_MAIN_MENU = "3"
    S_GEO_LOCATION_TYPE = "4"
    S_TROUBLE_LOCATION = "5"
    S_TROUBLE_LOCATION_ANSWER = "6"
    S_TROUBLE_LOCATION_INDOOR = "7"
    S_TROUBLE_TYPE = "8"
    S_TROUBLE_TYPE_ANSWER = "9"
    S_NETWORK_TYPE = "10"
    S_TICKET_NUMBER = "11"


message_library = {
    "start_message": "Вітаємо! Ви звернулися до системи обслуговування абонентів.",
    "reset_message": "Заявка відмінена користувачем. Інформація поточної заявки очищена.",
    "personal_data_permission": "Чи даєте Ви згоду на обробку персональних даних?",
    "personal_data_declined": "Без згоди на обробку персональних даних продовжити неможливо",
    "user_found": "Вітаємо, %s!",
    "main_menu": "Чим Вам допомогти (вкажіть номер розділу меню):\n"
                 "1 - Оформити заявку\n"
                 "2 - Статус заявки\n"
                 "3 - Тарифний план\n"
                 "4 - Баланс\n",
    "unknown_command": "Некоректний розділ меню. Повторіть введення номеру меню.",
    "geo_location_type": "Надішліть будь-ласка Вашу геолокацію або адресу",
    "unknown_type": "Некоректна інформація. Надішліть будь-ласка геолокацію або Вашу адресу",
    "trouble_place": "Вкажіть будь-ласка місце розташування, де спостерігається проблема:",
    "location_floor": "Вкажіть будь-ласка номер поверху, на якому Ви знаходитесь:",
    "unknown_floor": "Некоректна інформація. вкажіть будь-ласка номер поверху:",
    "trouble_type": "Оберіть будь-ласка тип проблеми:",
    "network_type": "Вкажіть стандарт мережі стільникового зв'язку:",
    "ticket_number": "Ваша заявка № %s прийнята. Статус - в обробці."
}