#WAP scans the email address and forms a tuple of username of domain 
 
 
# mail = input("Enter your gmail")
# print(mail)
# dom=()
# for i in range(0,len(mail)):
#     if(mail[i]=='@'):
#         dom = mail[i:]
#         username = mail[:i]
# print("Username",username)
# print("Domain",dom)




# email=input("enter the email")

# username=email.split('@')
# print(username)


emails = input("Enter the Email addresses separated by commas: ")
elist = emails.split(',')

for email in elist:
    username, domain = email.strip().split('@')
    print("Username: ", username, "Domain: ", domain)