from Generic.verification import verify_title
from POM import *
from POM.Ftux import *
from POM.dashboard import dashboard
from time import sleep
def test_TC1(setup):
    driver = setup
    verify_title("IMVU - #1 3D Avatar Social App, Virtual Worlds, Virtual Reality, VR, Avatars, Free 3D Chat",driver)
    f=Ftux(driver)
    f.Ftux_login_button()
    print(driver.title)
    # verify_title("IMVU - #1 3D Avatar Social App, Virtual Worlds, Virtual Reality, VR, Avatars, Free 3D Chat",driver)
    # f.Ftux_username("smuthu+1@imvu.com")
    # f.Ftux_password("Auto@123")
    # f.Ftux_signin_button()
    # sleep(10)
    # # verify_title("IMVU Next",driver)
    # d=dashboard(driver)
    # d.profile_icon()
    # d.signout()
    # # verify_title("IMVU - #1 3D Avatar Social App, Virtual Worlds, Virtual Reality, VR, Avatars, Free 3D Chat",driver)