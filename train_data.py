TRAIN_DATA = [
    # Releases
    ("The customer wants to monitor releases closely", 
     {"entities": [(30, 38, "releases")]}),
    ("How can we set up release tracking?", 
     {"entities": [(18, 25, "releases")]}),
    ("They are interested in the latest releases details", 
     {"entities": [(34, 42, "releases")]}),
    ("Ensure the releases are properly configured", 
     {"entities": [(11, 19, "releases")]}),

     #Alert Rules
    ("Please provide detailed alerts configuration", 
    {"entities": [(24, 44, "alert_rules")]}),
    ("We need to review our alert rules", 
    {"entities": [(22, 33, "alert_rules")]}),
    ("Are the alert rules set up correctly?", 
    {"entities": [(8, 19, "alert_rules")]}),
    ("Check the alert for this project", 
    {"entities": [(10, 15, "alert_rules")]}),

    # Environments
    ("How can we configure different environments?", 
    {"entities": [(31, 43, "environments")]}),
    ("We need separate environments for production and staging", 
    {"entities": [(17, 29, "environments")]}),
    ("Are the environments set up for testing?", 
    {"entities": [(8, 20, "environments")]}),
    ("Make sure the environments are configured correctly", 
    {"entities": [(14, 26, "environments")]}),
]


'''


# Teams
("Ensure the teams are correctly set up", 
    {"entities": [(12, 17, "teams")]}),
("We need to review our teams assignments", 
    {"entities": [(21, 26, "teams")]}),
("Are the teams updated for this project?", 
    {"entities": [(8, 13, "teams")]}),
("Verify that teams have the right permissions", 
    {"entities": [(11, 16, "teams")]}),

# Members
("Make sure all members are added", 
    {"entities": [(15, 22, "members")]}),
("We need to update the list of members", 
    {"entities": [(28, 35, "members")]}),
("Are the members properly assigned to teams?", 
    {"entities": [(8, 15, "members")]}),
("Check if all members have access", 
    {"entities": [(9, 16, "members")]}),

# Notification Settings
("Ensure notification settings are configured correctly", 
    {"entities": [(7, 27, "notification_settings")]}),
("How can we update the notification settings?", 
    {"entities": [(22, 42, "notification_settings")]}),
("Are the notification settings set up for alerts?", 
    {"entities": [(8, 28, "notification_settings")]}),
("We need to review our notification settings", 
{"entities": [(21, 41, "notification_settings")]}),
'''