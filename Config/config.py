class TestData:
    CHROME_EXECUTABLE_PATH = "C:\\chromedriver\\chromedriver.exe"
    BASE_URL = "https://www.optibet.lv"
    LOGIN_URL = "https://www.optibet.lv/login"
    LOGIN_LABEL = "Lietotājvārds vai epasts *"
    LOGIN_SUBMIT_BUTTON_TEXT = "Ienākt"
    LOGIN_ERROR_MESSAGE = "E-pasts un lietotājvārds ir obligāti"
    LOGIN_SHORT_ERROR_MESSAGE = "Lietotājvārds nevar būt īsāks par 6 zīmēm."
    LOGIN_LONG_ERROR_MESSAGE = "Lietotājvārds nedrīkst būt garāks par 32 zīmēm"
    LOGIN_SYMBOLS_ERROR_MESSAGE = "Izmanto latīņu alfabēta burtus, ciparus un pasvītrojumus, bez atstarpēm."

    PASSWORD_ERROR_MESSAGE = "Parole ir obligāta"
    PASSWORD_LABEL = "Parole *"
    FALSE_LOGIN = "Lietotājvārds vai parole nav pareiza"

    ID_LABEL = "Personas kods *"
    ID_FIELD_SYMBOLS_ERROR_MESSAGE = "Nepareizs personas koda formāts"
    ID_FIELD_ERROR_MESSAGE = "Personas kods ir obligāts"
    ID_FIELD_FALSE_ERROR_MESSAGE = "Smart-ID sesijas uzsākšanas kļūda"

    WELCOME_URL = 'https://www.optibet.lv/?dialogType=welcome'
    LIMITS_URL = 'https://www.optibet.lv/account/limits'
    DEPOSIT_URL = 'https://www.optibet.lv/account/deposit'
    CASINO_URL = 'https://www.optibet.lv/casino'
    SPORTS_URL = 'https://www.optibet.lv/sport'
    LIVECASINO_URL = 'https://www.optibet.lv/live-casino'
    BONUS_URL = 'https://www.optibet.lv/account/bonus?subTab=available'

    RESTRICTED_ENG = 'Restricted'
    CONTENT_ENG = 'Player personal ID is not verified.'

    RESTRICTED_LV = 'Nav pieejams'
    CONTENT_LV = 'Personas kods nav verificēts.'

    RESTRICTED_RU = 'Запрещено'
    CONTENT_RU = 'Персональный код не верифицирован.'