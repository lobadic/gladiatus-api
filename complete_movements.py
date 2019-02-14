import msg

def goto_city(driver):
    msg.info("Goint to city tab...")
    try:
        driver.execute_script("switchMenu(1)")
        msg.info("done")
    except:
        msg.warning("failed")

def goto_country(driver):
    msg.info("Goint to country tab...")
    try:
        driver.execute_script("switchMenu(2)")
        msg.info("done")
    except:
        msg.warning("failed")

def goto(clickable_object):
    try:
        clickable_object.click()
        msg.info("done")
    except:
        msg.warning("failed")
