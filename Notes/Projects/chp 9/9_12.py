#from us_us import User
from ad_ad import Admin


first_user = Admin('James','Allen','smiley face',23,3)
first_user.privileges.show_privileges()
first_user.privileges.upgrade_privileges()

