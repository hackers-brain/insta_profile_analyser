# Author : Gaurav Raj (HackersBrain)
# website : https://gauavraj.gq/
# Note : Don't Forget to Give Credits before committing any changes...

from colorama import Fore, Style
import pyfiglet
from igramscraper.instagram import Instagram
from discord_webhooks import DiscordWebhooks

username = ''
password = ''
webhook_url = ""


def banner():
    bn = pyfiglet.figlet_format(" Insta Analyser", font='slant')
    print(f"{Fore.GREEN}{bn}{Style.RESET_ALL}")
    print(f"\t\t\t\t\t\t Author : [{Fore.GREEN}HackersBrain{Style.RESET_ALL}]\n")


def insta_usr():
    instagram = Instagram()

    # authentication supported
    instagram.with_credentials(username, password)
    instagram.login()

    account = instagram.get_account(usr)
    print(f"\t{account}")

    server = DiscordWebhooks(webhook_url)
    try:
        server.set_image(url=account.profile_pic_url)
        server.add_field(name="UserName : ", value=account.username)
        server.set_content(description="Hacking is not a trick. It's an state of mind :)")
        server.set_author(name="HackersBrain Instagram Analyser Bot", url="http://gauravraj.gq/", icon_url="https://source.unsplash.com/35x35/?man")
        server.add_field(name="Full Name : ", value=account.full_name)
        server.add_field(name="Bio : ", value=account.biography)
        server.add_field(name="No. of Posts : ", value=account.media_count)
        server.add_field(name="No. of Followers : ", value=account.followed_by_count)
        server.add_field(name="No. of Follows : ", value=account.follows_count)
        server.add_field(name="Is Private : ", value=account.is_private)
        server.add_field(name="Is Verified : ", value=account.is_verified)
        server.send()
        print(Fore.GREEN + "\t Message Sent Successfully...\n" + Style.RESET_ALL)
    except KeyboardInterrupt as key_err:
        print(" Exiting Program... \tProject by : HackersBrain\n")
    except Exception as err:
        print(f"\n {err}\n Exiting Program... \tProject by : HackersBrain\n")


try:
    banner()
    usr = input(" Enter UserName : ")
    insta_usr()
except KeyboardInterrupt as key_err:
    print(f" Exiting Program... \tProject by : {Fore.GREEN}HackersBrain{Style.RESET_ALL}\n")
