import os
import pyfiglet
import fade
import requests
import re
import pyshorteners

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_logo():
    logo_text = """

██████╗  ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██╔═══██╗╚██╗██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║  ██║██║   ██║ ╚███╔╝        ██║   ██║   ██║██║   ██║██║     
██║  ██║██║   ██║ ██╔██╗        ██║   ██║   ██║██║   ██║██║     
██████╔╝╚██████╔╝██╔╝ ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                                

    """
    
    faded_text = fade.purpleblue(logo_text)
    print(faded_text)

def get_ip_info(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            data = response.json()
            return f"   IP Address: {ip_address}\nCity: {data.get('city')}\nRegion: {data.get('region')}\nCountry: {data.get('country')}\nVPN: {data.get('vpn')}"
        else:
            return f"Could not fetch information for {ip_address}."
    except Exception as e:
        return str(e)

def display_doxxing_tutorial():
    clear_screen()


    
    doxxing_tutorial = """
   Link here
   https://mega.nz/file/oiNDmYjJ#dxNG27MZW3AaVyBpEyentGwzMPnzQKLs9m8QGTCaHBM
    """
    
    faded_numbers = fade.purpleblue(doxxing_tutorial)
    
    print(faded_numbers)
    input("Press Enter to return to the main menu...")

    
    tools_tutorial = """
  ?leaksearch?
═══════════════════════════════════════
https://intelx.io
https://leakpeek.com
https://leak-lookup.com
https://snusbase.com/search
https://haveibeenpwned.com
https://www.dehashed.com/
https://cybernews.com/personal-data-leak-check
https://breachdirectory.com/search
https://breachdirectory.org
https://leakcheck.net
https://breachdbsztfykg2fdaq2gnqnxfsbj5d....onion.pet
https://aleph.occrp.org
https://checkleaked.cc
https://namescan.io/freeemailcompromisedcheck
https://monitor.firefox.com
https://www.fasterbroadband.co.uk/tools/...ach-search
https://www.hotsheet.com/inoitsu
https://checkashleymadison.com
https://surfshark.com
https://tragercop.1password.com
https://ghostproject.fr
https://saverudata.online/ (RussinLeak DB search)
 ?PhoneSearch?
═══════════════════════════════════════
https://www.spydialer.com
https://www.numlookup.com
https://www.truecaller.com
https://www.searchyellowdirectory.com
https://demo.phoneinfoga.crvx.fr
https://onlinesim.io
https://www.411.com
https://411.info
https://www.calleridtest.com
https://thatsthem.com/reverse-phone-lookup
http://www.fonefinder.net
https://www.callersmart.com
https://www.phonevalidator.com
https://freecarrierlookup.com
https://www.usphonebook.com
https://pccare99.com
https://www.numberguru.com
https://www.calltruth.com/
https://www.allareacodes.com
https://www.peoplebyphone.com
https://www.confidentialphonelookup.com
 ?People Search?
═══════════════════════════════════════
https://www.familytreenow.com/
https://hunter.io
https://thatsthem.com
https://www.zabasearch.com
http://usa-people-search-live.us-west-1....nstalk.com
https://www.cyberbackgroundchecks.com
https://www.advancedbackgroundchecks.com
https://radaris.com/
https://webmii.com
https://www.xlek.com
https://www.freepeopledirectory.com/
https://www.locatefamily.com/index.html
https://www.truepeoplesearch.com
https://www.fastpeoplesearch.com/
https://publicrecords.directory
https://www.open-public-records.com
https://www.spyfly.com
https://nuwber.com
https://clustrmaps.com/
https://www.peekyou.com
https://backgroundcheck.run/
https://johndoe.com/
https://allpeople.com/
https://www.spokeo.com
https://pipl.com/
https://persopo.com/
https://secure.publicrecords.com
https://www.ussearch.com/
https://www.peeplookup.com
https://www.truthfinder.com/
http://snoopstation.com/index.html
https://kiwisearches.com/
https://www.checkthem.com/
https://www.intelius.com
https://www.mylife.com
https://www.anywho.com/
https://www.addresses.com/
https://www.beenverified.com
https://www.spytox.com
https://www.checkpeople.com
https://www.dobsearch.com/
https://infotracer.com/
https://members.infotracer.com/tspec/sha...t_form.pdf
https://www.instantcheckmate.com/
https://www.idtrue.com/
https://www.backgroundalert.com/
https://golookup.com/
https://www.peoplefinders.com
https://kiwisearches.com/
https://www.findpeoplesearch.com/

?Public Records?
═══════════════════════════════════════
https://publicrecords.searchsystems.net/
https://publicrecords.netronline.com/state/WA
https://www.melissa.com/v2/lookups/prope...r/zipcode/
https://hauziz.com/
https://www.arivify.com/
https://neighbor.report/
https://govdataca.com/
https://books.google.com/advanced_patent_search
https://voterrecords.com/
https://www.blackbookonline.info/USA-Voter-Records.aspx
https://www.findagrave.com/
https://www.familywatchdog.us/
http://www.theinmatelocator.com
https://www.bop.gov/inmateloc/
https://mugshots.com
https://arrests.org
  Username
═══════════════════════════════════════
https://whatsmyname.app/
https://intelx.io/tools?tab=username
https://www.idcrawl.com/username
https://analyzeid.com/username/
https://namechk.com/
https://checkusernames.com/
https://namecheckup.com/
https://instantusername.com
https://www.gotinder.com/@%3Cusername%3E

 Darkweb
═══════════════════════════════════════
https://www.reddit.com/r/deepweb/
https://www.reddit.com/r/onions/
https://www.reddit.com/r/darknet/


 ? Archives ?
═══════════════════════════════════════
https://archive.org/web/
https://archive.is/
http://cachedview.com/


 ? Email search ?
═══════════════════════════════════════
https://epieos.com/
https://identificator.space/
https://pypi.org/project/holehe/
https://github.com/m4ll0k/Infoga
https://github.com/martinvigo/email2phonenumber
https://emailable.com/api/?redirect_source=trumail
https://hunter.io/email-verifier
https://osint.sh/reversewhois/
https://centralops.net/co/emaildossier.aspx
    """
    
    faded_text = fade.purpleblue(tools_tutorial)
    print(" Lookup Tools")
    print(faded_text)
    input("Press Enter to return to the main menu...")


    


def display_roblox_tutorial():
    clear_screen()


    roblox_tutorial = """
   IP METHOD...
  ____________
   Roblox ip method...

   Make a new roblox account add 2step to it now tell your target

   to login to the account so give him the username and password

   when he is trying to log in to your account you will get a code on your mail.

   Now send him the code so he can login.

   Once he logged in you will get a new mail message and in the message his ip will be right there also city...
    """
    
    faded_text = fade.purpleblue(roblox_tutorial)
    print("ROBLOX IP METHOD:")
    print(faded_text)
    input("Press Enter to return to the main menu...")

def display_ip_tutorial():
    clear_screen()


    ip_tutorial = """
   IP METHOD...
  ____________
    Ip Logger method...

   Are you that bad at getting somones ip? Ahahaha well its okay i will tell you

   If you want to get somones ip address using a ip logger its easy but its a bad method but here

   Here is websites for it

   https://iplogger.org/
   https://grabify.link/
   
   So once you are in the website copy a random link it can be any lets just say youtube.
   Paste it in And then it will take you to another menu and you can change the name of the link.
   And then just copy the new link send it to your target and if they open it refesh the website page go down.
   And then their ip will be right there
    """
    
    faded_text = fade.purpleblue(ip_tutorial)
    print("IP LOGGER METHOD:")
    print(faded_text)
    input("Press Enter to return to the main menu...")

def display_website_tutorial():
    clear_screen()


    website_tutorial = """
   IP METHOD...
  ____________
   Website Ip Method...

   Okay so this works most times and its very very easy to use 

   here is how you use it.

   First be on a call it can be discord or facetime or anything that you can screenshare on.


   And then when your target is screensharing tell him to go to this website

   https://ipinfo.io/

   Once he enterd the website his ip will show up on the screen make sure you record or take a pic .
   Of the ip bc when he see its his ip he might close the website so be fast with it...
    """
    
    faded_text = fade.purpleblue(website_tutorial)
    print("WEBSITE IP METHOD:")
    print(faded_text)
    input("Press Enter to return to the main menu...")




def get_ip_info(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            data = response.json()
            return data  
        else:
            return f"Could not fetch information for {ip_address}."
    except Exception as e:
        return str(e)

def display_ip_lookup():
    clear_screen()
    print("iplook")
    ip_address = input("Enter an IP address: ")
    
    ip_info = get_ip_info(ip_address)
    
    if ip_info:
        faded_info = fade.purpleblue(f"""
          \u001b[36m  ╔══════════════════════════════════════╗\u001b[0m
          \u001b[36m  ║          IP Information              \u001b[36m║\u001b[0m

        \u001b[33m            IP Address: {ip_address}\u001b[0m
        \u001b[33m            City: {ip_info.get('city')}\u001b[0m
        \u001b[33m            Region: {ip_info.get('region')}\u001b[0m
        \u001b[33m            Country: {ip_info.get('country')}\u001b[0m

          \u001b[36m  ╔══════════════════════════════════════╗\u001b[0m
          \u001b[36m  ║                                      \u001b[36m║\u001b[0m
          \u001b[36m  ╚══════════════════════════════════════╝\u001b[0m
        """)
        print(faded_info)
    else:
        print("Could not fetch information for the entered IP address.")
    
    input("Press Enter to return to the main menu...")

def main():
    while True:
        clear_screen()
        display_ascii_logo()
        print()
        print("              Made by zora   ")
        print()
        print()
        print(f"  01  {fade.purpleblue('    [<>] Dox tut ')}")              
        print()
        print()
        print(f"  02  {fade.purpleblue(   '    [<>] Osint ')}")      
        print()
        print()
        print()
        print(f" 03  {fade.purpleblue('    [<>] Roblox method')}")
        print()
        print()
        print(f" 04   {fade.purpleblue('   [<>] iplogger method (Bad)')}")
        print()
        print()
        print(f" 05  {fade.purpleblue('    [<>] Website method)')}")
        print()
        print()
        print()
        print(f" 06  {fade.purpleblue('  [<>] ip info')}")
        print()
        print()



        
        choice = input("[< ")

        
        if choice == '01':
            display_doxxing_tutorial()
        if choice == '02':
            display_tools_tutorial()
        if choice == '03':
            display_roblox_tutorial()
        if choice == '04':
            display_ip_tutorial()
        if choice == '05':
            display_website_tutorial()
        if choice == '06':
            display_ip_lookup()
        
        
if __name__ == "__main__":
    main()
