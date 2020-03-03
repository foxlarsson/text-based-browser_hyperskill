import sys
import os
import logging
from _collections import deque

browser_history = deque()

logging.basicConfig(level=logging.DEBUG)

args = sys.argv
saved_tabs_directory = args[1]
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''
bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def create_directory():
    if saved_tabs_directory:
        try:
            os.mkdir(saved_tabs_directory)
        except FileExistsError:
            pass


def create_web_page_files(filename, content):
    with open(f'{os.getcwd()}\\{saved_tabs_directory}\\{filename}.txt', 'w') as f:
        f.write(content)
        f.flush()


def read_web_page(filename):
    if os.path.exists(f'{os.getcwd()}\\{saved_tabs_directory}\\{filename}.txt'):
        with open(f'.\\{saved_tabs_directory}\\{filename}.txt') as f:
            print(f.read())
    else:
        print('Error: Incorrect URL')


def browser_loop():
    while True:
        command = input("Type URL: ")
        if command == 'back':
            history_loop()
        elif command == 'exit':
            return False
        elif command == 'bloomberg':
            read_web_page('bloomberg.txt')
            browser_history.append(command)
        elif command == 'nytimes':
            read_web_page('nytimes.txt')
            browser_history.append(command)
        elif '.' not in command:
            print("error")
        elif command == 'bloomberg.com':
            print(bloomberg_com)
            create_web_page_files('bloomberg.txt', bloomberg_com)
            browser_history.append(command)
        elif command == 'nytimes.com':
            print(nytimes_com)
            create_web_page_files('nytimes.txt', nytimes_com)
            browser_history.append(command)
        else:
            print('error')


def history_loop():
    if len(browser_history) != 0:
        command = browser_history.pop()
        if command == 'bloomberg' or command == 'bloomberg.com':
            read_web_page('bloomberg.txt')
        elif command == 'nytimes' or command == 'nytimes.com':
            read_web_page('nytimes.txt')


create_directory()
browser_loop()
