from selenium.webdriver.common.by import By

class Locators():
    # navigation bar section
    CURRENCY_MENU_NAVBAR = (By.XPATH, '//span[contains(text(),"Currency")]')

    CURRENCY_SUBMENU_NAVBAR = (By.XPATH, '//ul[@class="dropdown-menu show"]')

    EURO_SUBMENU_NAVBAR = (By.XPATH, '//div[@class="list-group mb-3"]')

    POUNDSTERLING_SUBMENU_NAVBAR = (By.XPATH, '//div[@class="list-group mb-3"]')

    USDOLLAR_SUBMENU_NAVBAR = (By.XPATH, '//div[@class="list-group mb-3"]')

    CONTACT_MENU_NAVBAR = (By.XPATH, '//i[@class="fa-solid fa-phone"]')

    MY_ACCOUNT_MENU_NAVBAR = (By.XPATH, '//span[contains(text(), "My Account")]')

    REGISTER_SUBMENU_NAVBAR = (By.XPATH, '//a[contains(text(), "Register")]')

    LOGIN_SUBMENU_NAVBAR = (By.XPATH, '//a[contains(text(), "Login")]')

    SUBMENU_DROPDOWN = (By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]')

    MY_ACCOUNT_SUBMENU_NAVBAR = (By.XPATH, '//a[@class="dropdown-item"][contains(text(),"My Account")]')

    ORDER_HISTORY_SUBMENU_NAVBAR = (By.XPATH, '//a[@class="dropdown-item"][contains(text(),"Order History")]')

    TRANSACTIONS_SUBMENU_NAVBAR = (By.XPATH, '//a[@class="dropdown-item"][contains(text(),"Transactions")]')

    DOWNLOADS_SUBMENU_NAVBAR = (By.XPATH, '//a[@class="dropdown-item"][contains(text(),"Downloads")]')

    LOGOUT_SUBMENU_NAVBAR = (By.XPATH, '//a[@class="dropdown-item"][contains(text(),"Logout")]')

    WISHLIST_MENU_NAVBAR = (By.XPATH, '//span[contains(text(),"Wish List (0)")]')

    SHOPPING_CART_MENU_NAVBAR = (By.XPATH, '//span[contains(text(),"Shopping Cart")]')

    CHECKOUT_MENU_NAVBAR = (By.XPATH, '//span[contains(text(),"Checkout")]')

    #header section
    LOGO = (By.XPATH, '//img[@class="img-fluid"]')

    SEARCH_BAR = (By.XPATH, '//div[@id="search"]//input[@type="text"]')

    SEARCH_BUTTON = (By.XPATH, '//div[@id="search"]//button[@type="button"]')

    SHOPPING_CHART_BUTTON = (By.XPATH, '//div[@class="dropdown d-grid"]')

    #categories section


    #breadcrumb section


    # page title section

    PAGE_TITLE_TEXT = (By.TAG_NAME, 'h1')





    # main section

    FIRST_NAME_TEXT_FIELD = (By.ID, 'input-firstname')

    LAST_NAME_TEXT_FIELD = (By.ID, 'input-lastname')

    EMAIL_TEXT_FIELD = (By.ID, 'input-email')

    PASSWORD_TEXT_FIELD = (By.ID, 'input-password')

    NEWSLETTER_SUBSCRIBE_YES_RADIO_BUTTON = (By.ID, 'input-newsletter-yes')

    AGREEMENT_CHECK_BOX = (By.XPATH, '//input[@type = "checkbox"]')

    CONTINUE_BUTTON = (By.XPATH, '//button[@type = "submit"]')

    GENERAL_CONTINUE_BUTTON = (By.XPATH, '//a[@class="btn btn-primary"]')


    # Warning and Error Message

    FIRST_NAME_ERROR_TEXT = (By.ID, "error-firstname")
    LAST_NAME_ERROR_TEXT = (By.ID, "error-lastname")
    EMAIL_ERROR_TEXT = (By.ID, "error-email")
    PASSWORD_ERROR_TEXT = (By.ID, "error-password")
    RIGHT_CORNER_ERROR_TEXT = (By.ID, "alert")


    # right navigation section
    MENU_RIGHT_NAV = '//div[@class="list-group mb-3"]'

    REGISTER_MENU_RIGHT_NAV = (By.XPATH, '//a[@class="list-group-item"][contains(text(),"Register")]')

    LOGIN_MENU_RIGHT_NAV = (By.XPATH, '//a[@class="list-group-item"][contains(text(),"Login")]')
    
    MY_ACCOUNT_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"My Account")]'

    EDIT_ACCOUNT_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Edit Account")]'

    PASSWORD_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Pasword")]'

    ADDRESS_BOOK_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Address Book")]'

    WISHLIST_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Wishlist")]'

    ORDER_HISTORY_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Order History")]'

    DOWNLOADS_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Downloads")]'

    SUBSCRIPTIONS_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Subscriptions")]'

    REWARD_POINTS_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Reward Points")]'

    RETURNS_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Returns")]'

    TRANSACTIONS_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Transactions")]'

    NEWSLETTER_MENU_RIGHT_NAV = (By.XPATH, '//a[@class="list-group-item"][contains(text(),"Newsletter")]')

    LOGOUT_MENU_RIGHT_NAV = '//a[@class="list-group-item"][contains(text(),"Logout")]'


    #footer section