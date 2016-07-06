# -*- coding: utf-8 -*-
import os
import string


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
    if not os.path.exists("./.current_config.json"):
        new_user_config()
    else:
        answer = input("Previous configuration has been found.\n Would you like to use that one? (Yes)")
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


def new_user_config():
    #Let the user create a new config

    #get valid name
    invalid_name = True
    while invalid_name:
        invalid_chars = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
        name = input("Name of the configuration: ?")
        all_chars_valid = True
        for letter in name:
            all_chars_valid = all_chars_valid and letter not in invalid_chars
        invalid_name = not all_chars_valid
        if invalid_name:
            print("That name cannot be used since it contains special characters.\n Try not to use / \\ : * ? \" < > or |")

    #get root search directory
    not_correct_answer = True
    while not_correct_answer:
        root_search_directory = input("Root search directory: ?")
        if os.path.exists(root_search_directory):
            not_correct_answer = False
        else:
            print("The directory you entered does not exists.\n Make sure you made no typos and that the directory exists.")

    #bla blablablal
    monitor_mode_menu = True
    monitor_mode = ""
    while monitor_mode_menu:
        answer_monitor_mode = input("Please define monitor mode for selected files/folder: (M)odify, (D)eletion, M(O)ve")
        #check for selection in answer
        for option in ["M", "D", "O"]:
            if option in answer_monitor_mode:
                monitor_mode += option
        #No valid option chosen
        if monitor_mode == "":
            print("Your answer must at least contain either M, D or O")
        else:
            monitor_mode_menu = False


def load_conf(config_file):
    #TODO
    #Load a configuration from file
    config_file.close()

