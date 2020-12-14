# PyScripts
These are general python scripts I made to benefit my computing experience.

--ConnectWifi.py--     {Requires Root}
Connects you to wifi using wireless NIC.
Rewrites wpa_supplicant.conf every time it is ran.
Kills other wpa_supplicant services and NetworkManager.
  Only kills NetworkManager because it seems to end the connection some times.
Outputs your new IPv4.

--LinColor.py--
Function 'Color()'-
  Colors a certain string using bash color codes. It can do bright or background colors.
Function 'DeColor()'-
  MUST ALSO HAVE COLOR FUNCTION
  it finds the default bash color codes and prints them as the colors.
    May add extra '\\', function is best used to just print outputs. 
  Great for .bashrc translation. 

--Mount&Open.py--     {Requires Root}
General purpose starting script for me.
Mounts a drive, specifically a USB for me.
  Can use Crtl+C to skip this part.
Asks you what programs you would like to open, you can type all of the numbers of the programs if you like.
  Executes all programs as the logged-in user.
  If you type multiple, make sure the 'Exit' program is the last number you type.
  You can add programs by adding them to the programs list and creating the function.
