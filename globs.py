import toml


#Prompt user to load config file or to select th folder/file location manually
print("""
------------------------------------------------------
|  File Monitoring Tool 0.0.1                        |
|  CreativeMinds                                     |
|  Developed by cemmetje87 & Pixdigit                |
------------------------------------------------------
""")
#load_config_query = input("Would you like to load config file?: {0}, {1}".format("(Y)es", "(N)o" ))
#try:
#    if

with open('config.toml', 'r') as conffile:
    config = toml.loads(conffile.read())
#print(config['DEFAULT']['folder'])
