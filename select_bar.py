import msg
from selenium.webdriver.common.action_chains import ActionChains

class select_bar:
    ############################ LOGIN ##############################
    def username(driver):
        try:
            return driver.find_element_by_id("login_username")
        except:
            return False

    def password(driver):
        try:
            return driver.find_element_by_id("login_password")
        except:
            return False

    ############################# MAIN ##############################

    def subtab(driver, subtab_number):
        try:
            msg.info(f"Going to subtab {subtab_number}...")
            return driver.find_element_by_css_selector(f"ul#mainnav > li > table > tbody > tr > td:nth-child({subtab_number}) > a")
        except:
            msg.warning("Couldn't find subtab {subtab_number}")
            return False

    #****************************overview*****************************
    def overview(driver):
        try:
            msg.info("Goint to overview tab...")
            return driver.find_element_by_css_selector("#mainmenu > a:nth-child(1)")
        except:
            msg.warning("couldn't find overview tab")
            return False

    #*****************************pantheon***************************
    def pantheon(driver):
        try:
            msg.info("Goint to pantheon tab...")
            return driver.find_element_by_css_selector("#mainmenu > a:nth-child(2)")
        except:
            msg.warning("couldn't find pantheon tab")
            return False

    #*****************************guild******************************
    def guild(driver):
        try:
            msg.info("Goint to guild tab...")
            return driver.find_element_by_css_selector("#mainmenu > a:nth-child(3)")
        except:
            msg.warning("couldn't find guild tab")
            return False

    #****************************highscore***************************
    def highscore(driver):
        try:
            msg.info("Goint to highscore tab...")
            return driver.find_element_by_css_selector("#mainmenu > a:nth-child(4)")
        except:
            msg.warning("couldn't find highscore tab")
            return False

    #***************************recruiting***************************
    def recruiting(driver):
        try:
            msg.info("Goint to recruiting tab...")
            return driver.find_element_by_css_selector("#mainmenu > a:nth-child(5)")
        except:
            msg.warning("couldn't find recruiting tab")
            return False

    #*****************************premium****************************
    def premium(driver):
        try:
            msg.info("Goint to premium tab...")
            return driver.find_element_by_css_selector("#mainmenu > a:nth-child(6)")
        except:
            msg.warning("couldn't find premium tab")
            return False


    ############################# CITY ##############################
    def work(driver):
        try:
            msg.info("Goint to work tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(1)")
        except:
            msg.warning("couldn't find work tab")
            return False

    def arena(driver):
        try:
            msg.info("Goint to arena tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(2)")
        except:
            msg.warning("couldn't find arena tab")
            return False

    def training(driver):
        try:
            msg.info("Goint to training tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(3)")
        except:
            msg.warning("couldn't find training tab")
            return False

    def weapon_smith(driver):
        try:
            msg.info("Goint to weapon smith tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(4)")
        except:
            msg.warning("couldn't find weapon smith tab")
            return False

    def armour_smith(driver):
        try:
            msg.info("Goint to armour smith tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(5)")
        except:
            msg.warning("couldn't find armour smith tab")
            return False

    def general_goods(driver):
        try:
            msg.info("Goint to general goods tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(6)")
        except:
            msg.warning("couldn't find general goods tab")
            return False

    def alchemist(driver):
        try:
            msg.info("Goint to alchemist tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(7)")
        except:
            msg.warning("couldn't find alchemist tab")
            return False

    def mercenary(driver):
        try:
            msg.info("Goint to mercenary tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(8)")
        except:
            msg.warning("couldn't find mercenary tab")
            return False

    def maleficia(driver):
        try:
            msg.info("Goint to maleficia tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(9)")
        except:
            msg.warning("couldn't find maleficia tab")
            return False

    def forge(driver):
        try:
            msg.info("Goint to forge tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(10)")
        except:
            msg.warning("couldn't find forge tab")
            return False

    def smelter(driver):
        try:
            msg.info("Goint to smelter tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(11)")
        except:
            msg.warning("couldn't find smelter tab")
            return False

    def workbench(driver):
        try:
            msg.info("Goint to workbench tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(12)")
        except:
            msg.warning("couldn't find workbench tab")
            return False

    def horreum(driver):
        try:
            msg.info("Goint to horreum tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(13)")
        except:
            msg.warning("couldn't find horreum tab")
            return False

    def magnus_hermeticus(driver):
        try:
            msg.info("Goint to magnus hermeticus tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(14)")
        except:
            msg.warning("couldn't find magnus hermeticus tab")
            return False

    def auction_house(driver):
        try:
            msg.info("Goint to auction house tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(15)")
        except:
            msg.warning("couldn't find auction house tab")
            return False

    def market(driver):
        try:
            msg.info("Goint to market tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(16)")
        except:
            msg.warning("couldn't find market tab")
            return False

    def city_gate(driver):
        try:
            msg.info("Goint to city gate tab...")
            return driver.find_element_by_css_selector("#submenu1 > a:nth-child(17)")
        except:
            msg.warning("couldn't find city gate tab")
            return False

    ############################ COUNTRY ############################
    def country_zone(driver, zone_number):
        try:
            msg.info(f"Goint to country zone {zone_number}...")
            return driver.find_element_by_css_selector(f"#submenu2 > a:nth-child({zone_number})")
        except:
            msg.warning(f"couldn't find country zone {zone_number}")
            return False

    def event_zone(driver):
        try:
            msg.info("Goint to event zone...")
            return driver.find_element_by_css_selector(f"#submenu2 > a:last-child")
        except:
            msg.warning("couldn't find event zone")
            return False





