from time import sleep

from Generic.verification import *
from POM.Ftux import Ftux
from POM.dashboard import dashboard


def test_TC2(setup):
    driver = setup
    verify_title("IMVU - #1 3D Avatar Social App, Virtual Worlds, Virtual Reality, VR, Avatars, Free 3D Chat", driver)
    f = Ftux(driver)
    f.Ftux_login_button()
    f.Ftux_username("smuthu+1@imvu.com")
    f.Ftux_password("Auto@123")
    f.Ftux_signin_button()
    d = dashboard(driver)
    d.profile_icon()
    d.edit_profile()
    d.edit_yourname("swethasree")
    d.edit_bio("Hi Hello How are you I am swetha")
    d.edit_hashtag()
    d.hashtag_search_music("music")
    sleep(10)
    mouse_hover(driver, d.music())
    d.edit_hashtag_cancel()
    d.show_gender()
    # d.select_gender()
    sleep(10)