from instagram_private_api import Client, ClientCompatPatch, errors
from colorama import init, Fore, Style
from time import strftime, sleep
from sys import exit

def get_time():
    date = strftime("%H:%M:%S")
    return (f"{Style.BRIGHT + Fore.CYAN}[{date}]{Style.RESET_ALL}")

def main():
    logo = f"""
    {Style.BRIGHT + Fore.RED}  ▄▄ ▄███▄{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}▄▀▀▀▀ ▄▄▄ ▀▀▀▀▄   {Style.BRIGHT + Fore.MAGENTA}Instagram Takipçi Arttırma Aracı{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}█    █   █    █   {Style.BRIGHT + Fore.RED}+-----------------------------------+{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}█    ▀▄▄▄▀    █             {Style.BRIGHT + Fore.YELLOW}Coded by @aralaydinn for Tesaxoa //{Style.RESET_ALL}
    {Style.BRIGHT + Fore.RED}▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀{Style.RESET_ALL}

    """
    print(logo)
    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Hoş geldin,Tesa...Hangi takip etme yöntemini kullanmak istersin:{Style.RESET_ALL}")
    tmp = (11 * " ")
    print(f"{Style.RESET_ALL}{tmp}{Style.BRIGHT + Fore.MAGENTA}1 > {Style.RESET_ALL + Fore.WHITE}Etiket kullanarak takipçi bulma.{Style.RESET_ALL}")
    print(f"{Style.RESET_ALL}{tmp}{Style.BRIGHT + Fore.MAGENTA}2 > {Style.RESET_ALL + Fore.WHITE}Kullanıcı adı ile takipçi bulma.{Style.RESET_ALL}")
    print(f"{Style.RESET_ALL}")
    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[>] {Style.BRIGHT + Fore.WHITE}Seçiminiz:{Style.RESET_ALL} ", end="")
    method = input()

    if (method != "1" and method != "2"):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Seçiminiz 1 veya 2 olmalıdır!{Style.RESET_ALL}")
        exit(0)

    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Ardaşık takipler sırasında kaç saniye beklensin: {Style.RESET_ALL}", end="")
    sleep_sec = input()

    try:
        int(sleep_sec)
    except:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Bekleme süresi bir sayı olmalıdır!{Style.RESET_ALL}")
        exit(0)

    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Kullanıcı adın: {Style.RESET_ALL}", end="")
    username = input()
    if (" " in username or username.strip() == ""):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Kullanıcı adınız boş veya boşluk içeriyor!{Style.RESET_ALL}")
        exit(0)

    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Şifren: {Style.RESET_ALL}", end="")
    password = input()

    if (password.strip() == ""):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Şifreniz boş olamaz!{Style.RESET_ALL}")
        exit(0)

    try:
        api = Client(username, password)
    except errors.ClientLoginError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Kullanıcı adınız veya şifreniz hatalı! ({e}){Style.RESET_ALL}")
        exit(0)
    except errors.ClientChallengeRequiredError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Giriş için doğrulama gerekli! ({e}){Style.RESET_ALL}")
        exit(0)
    except errors.ClientCheckpointRequiredError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Giriş için doğrulama gerekli! ({e}){Style.RESET_ALL}")
        exit(0)
    except errors.ClientSentryBlockError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Giriş yapılamadı! Hesap spam olarak işaretlenmiş! ({e}){Style.RESET_ALL}")
        exit(0)
    except errors.ClientConnectionError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Bağlantı hatası! ({e}){Style.RESET_ALL}")
        exit(0)
    except errors.ClientError as e:
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Giriş yapılamadı! ({e}){Style.RESET_ALL}")
        exit(0)

    print("")
    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}Giriş başarılı!{Style.RESET_ALL}")

    if ("KAYA" not in logo):
        print("Bu programı @aralaydinn ' dan çaldım ve o kadar aptalım ki bunu kaldırmayı unuttum'.")
        exit(0)

    if (method == "1"):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Aramak istediğiniz etiketleri giriniz ('#' işareti olmadan ve etiketler arasına virgül koyarak örnek: aydin,bmw,supraa vs.):{Style.RESET_ALL} ", end="")
        hashtags = input()
        hashtag_list = hashtags.strip().split(",")
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{len(hashtag_list)} adet etiket aranacak!{Style.RESET_ALL}")

        for hashtag in hashtag_list:
            if (hashtag.strip() == ""):
                print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Boş etiket bulundu! Geçiliyor.{Style.RESET_ALL}")
                continue

            try:
                data = api.top_search(hashtag)

                if (len(data["users"]) == 0):
                    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}{hashtag} etiketini kimse kullanmamış! Geçiliyor!{Style.RESET_ALL}")
                    continue

                tmp = len(data["users"])
                print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{tmp} adet kullanıcıya takip atılacak!{Style.RESET_ALL}")

                for users in data["users"]:
                    if ("user" not in users):
                        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Kullanıcı bulunamadı! Geçiliyor.{Style.RESET_ALL}")
                        continue

                    user_data = users["user"]
                    tmp = user_data["username"]

                    try:
                        if(api.friendships_show(user_data["pk"])["following"] == True):
                            print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{tmp} kullanıcısına zaten takip atıldı! Geçildi!{Style.RESET_ALL}")
                            continue

                        api.friendships_create(user_data["pk"])
                        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{tmp} kullanıcısına takip atıldı!{Style.RESET_ALL}")
                    except errors.ClientError as e:
                        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}{tmp} kullanıcısına takip atılamadı! ({e}){Style.RESET_ALL}")
                    except errors.ClientConnectionError as e:
                        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}{tmp} kullanıcısına takip atılamadı! Bağlantı hatası!({e}){Style.RESET_ALL}")

                    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.CYAN}[*] {Style.BRIGHT + Fore.WHITE}{sleep_sec} saniye bekleniyor!{Style.RESET_ALL}")
                    sleep(int(sleep_sec))
                    continue
            except errors.ClientError as e:
                print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}etiket bilgileri alınamadı! ({e}){Style.RESET_ALL}")
            except errors.ClientConnectionError as e:
                print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Bağlantı hatası! ({e}){Style.RESET_ALL}")
    elif (method == "2"):
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.MAGENTA}[?] {Style.BRIGHT + Fore.WHITE}Hedefin kullanıcı adını girin:{Style.RESET_ALL} ", end="")
        target_username = input()
        if (" " in target_username or target_username.strip() == ""):
            print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Hedefin kullanıcı adı boş veya boşluk içeriyor!{Style.RESET_ALL}")
            exit(0)

        try:
            data = api.username_info(target_username)
            data = api.user_followers(data["user"]["pk"], api.generate_uuid())

            tmp = data["users"]
            print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{len(tmp)} adet kullanıcıya takip atılacak!{Style.RESET_ALL}")

            for user in data["users"]:
                try:
                    tmp = user["username"]

                    if(api.friendships_show(str(user["pk"]))["following"] == True):
                        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{tmp} kullanıcısına zaten takip atıldı! Geçildi!{Style.RESET_ALL}")
                        continue

                    api.friendships_create(str(user["pk"]))
                    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.GREEN}[+] {Style.BRIGHT + Fore.WHITE}{tmp} kullanıcısına takip atıldı!{Style.RESET_ALL}")
                except errors.ClientError as e:
                    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}{tmp} kullanıcısına takip atılamadı! ({e}){Style.RESET_ALL}")
                except errors.ClientConnectionError as e:
                    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}{tmp} kullanıcısına takip atılamadı! Bağlantı hatası!({e}){Style.RESET_ALL}")

                print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.CYAN}[*] {Style.BRIGHT + Fore.WHITE}{sleep_sec} saniye bekleniyor!{Style.RESET_ALL}")
                sleep(int(sleep_sec))
                continue

        except errors.ClientError as e:
            print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}etiket bilgileri alınamadı! ({e}){Style.RESET_ALL}")
        except errors.ClientConnectionError as e:
            print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.RED}[-] {Style.BRIGHT + Fore.WHITE}Bağlantı hatası! ({e}){Style.RESET_ALL}")

    print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.CYAN}[*] {Style.BRIGHT + Fore.WHITE}Takip işlemleri bitti!{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        init()
        main()
    except KeyboardInterrupt:
        print()
        print(f"{Style.RESET_ALL}{get_time()} {Style.BRIGHT + Fore.CYAN}[*] {Style.BRIGHT + Fore.WHITE}Program kapatılıyor!{Style.RESET_ALL}")
    pass
