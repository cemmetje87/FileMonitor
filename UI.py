# -*- coding: utf-8 -*-
import os


def init():
    #nothing to init
    pass


def check_yes_no(answer):
    #check if answer is yes or no
    if answer in ["yes", "y", "Yes", "Y", "YES"]:
        return True
    elif answer in ["no", "n", "No", "N", "NO"]:
        return False
    #Answer not detectable
    else:
        return None


def welcome():
    #implicitly joined strings
    banner = ("------------------------------------------------------\n"
             "|  File Monitoring Tool 0.0.1                        |\n"
             "|  CreativeMinds                                     |\n"
             "|  Developed by cemmetje87 & Pixdigit                |\n"
             "------------------------------------------------------")
    print(banner)


def startup_menu():
    #Check for previous configuration
    #If not start configuration
    if not os.path.exists("./.config.json"):
        user_config()
    else:
        answer = input("Previous configuration has been found.\n Would you like to use that one? (Y/n) ")
        use_conf = check_yes_no(answer)
        if use_conf is None:
            #User either did not enter an answer
            if use_conf == "":
                #If no answer is supplied "yes" is assumed
                use_conf = True
            #user did not use a valid answer
            else:
                print("Your answer could not be understand.\n Please use Y/N to indicate your decision.")
                #GOTO statements could be helpful here
                #TODO: Start question again
       #User entered yes
        elif use_conf:
            #TODO make function load_conf
            load_conf(open("./.config.json", "r"))
        #Only a no can be the case now
        else:
            #TODO
            pass
        print(use_conf)


def user_config():
    #TODO
    #Let the user create a new config
    pass


def load_conf(config_file):
    #TODO
    #Load a configuration from file
    config_file.close()
