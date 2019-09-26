import sys, os


def send(button_request):
    command = './' + button_request
    print command
    os.system(command)
