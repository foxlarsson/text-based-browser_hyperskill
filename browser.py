import sys
import os

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
target_directory = f'{os.getcwd()}\\{saved_tabs_directory}'


def create_directory():
    if saved_tabs_directory:
        try:
            os.mkdir(saved_tabs_directory)
        except FileExistsError:
            pass


def create_web_page_files(filename, content):
    if os.getcwd() != target_directory:
        os.chdir(f'{os.getcwd()}\\{saved_tabs_directory}')
    with open(filename, 'w') as f:
        f.write(content)
        os.chdir('..')


def read_web_page(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            print(f.read())
    else:
        print('Error: Incorrect URL')


def browser_loop():
    while True:
        command = input("Type URL: ")
        if command == 'exit':
            return False
        elif command == 'bloomberg':
            read_web_page('bloomberg.txt')
        elif command == 'nytimes':
            read_web_page('nytimes.txt')
        elif '.' not in command:
            print("error")
        elif command == 'bloomberg.com':
            print(bloomberg_com)
            create_web_page_files('bloomberg.txt', bloomberg_com)
        elif command == 'nytimes.com':
            print(nytimes_com)
            create_web_page_files('nytimes.txt', nytimes_com)
        else:
            print('error')


create_directory()
browser_loop()
