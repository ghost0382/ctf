
import os
import time

from colorama import Fore, Style, init
from crawler import WebCrawler

init(autoreset=True)

TARGET = 'http://web-16.challs.olicyber.it/'

crawler = WebCrawler(TARGET)


def progress_bar(visited, discovered, width=35):
    if discovered == 0:
        percentage = 0
    else:
        percentage = visited / discovered

    percentage = min(percentage, 1)

    filled = int(width * percentage)
    empty = width - filled

    bar = (
        Fore.GREEN + "█" * filled +
        Fore.WHITE + "░" * empty
    )

    return f"[{bar}] {percentage * 100:5.1f}%"


def activity_animation():
    frames = ["|", "/", "-", "\\"]
    return frames[int(time.time() * 4) % len(frames)]


def clear_terminal():
    print("\033[H", end="")


def dashboard():

    while crawler.end_time is None:

        clear_terminal()

        print(Fore.CYAN + """
╔══════════════════════════════════════════════╗
║              MINI SPIDER MONITOR             ║
║                  WEB CRAWLER                 ║
╚══════════════════════════════════════════════╝
""")

        print(Fore.WHITE + f" TARGET: {TARGET}")

 
        print(Fore.GREEN + "\n [ CRAWLING PROGRESS ]")

        print()
        print("  " + progress_bar(
            len(crawler.visited),
            len(crawler.discovered)
        ))

        print(
             f"\n  {activity_animation()} Spider is exploring..."
        )

        print(Fore.YELLOW + "\n [ LIVE STATISTICS ]")

        print(f"""
          Visited pages:       {len(crawler.visited)}
          Discovered pages:    {len(crawler.discovered)}
          Queue size:          {len(crawler.to_visit)}
          
          HTTP requests:       {crawler.total_requests}
          Total links:         {crawler.total_links}
          Duplicate links:     {crawler.duplicates}
          Failed requests:     {crawler.errors}
         """)

        print(Fore.MAGENTA + " [ RECENTLY VISITED ]")

        for url in crawler.last_urls[-10:]:
            print(f"  > {url}")

        print("\n" + Fore.CYAN + " Crawling in progress...")

        time.sleep(0.5)

    clear_terminal()


if __name__ == '__main__':


    print("\033[2J\033[H", end="")
    print("\033[?25l", end="")

    import threading

    worker = threading.Thread(
        target=crawler.crawl
    )

    worker.start()

    dashboard()

    worker.join()

    print(Fore.GREEN + """
╔══════════════════════════════════════════════╗
║                 CRAWLING DONE                ║
╚══════════════════════════════════════════════╝
""")

    print(f" Visited:       {len(crawler.visited)}")
    print(f" Discovered:    {len(crawler.discovered)}")
    print(f" Requests:      {crawler.total_requests}")
    print(f" Duration:      {crawler.elapsed:.2f} seconds")

    if crawler.flag:
        print(Fore.GREEN + f"\n FLAG FOUND: {crawler.flag}")
    else:
        print(Fore.RED + "\n Flag not found.")

    print("\033[?25h", end="")
