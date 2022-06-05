import boto3
import argparse
import json

iam_client = boto3.client("iam")

def generate_random_password(length=12):
   alphabet = string.ascii_letters + string.digits
   password = ''.join(secrets.choice(alphabet) for _ in range(length))
   return password

def create_user(username):
   iam_client.create_user(
       UserName=username,
   )
   password = generate_random_password(15)
   iam_client.create_login_profile(
       UserName=username,
       Password=password,
       PasswordResetRequired=False
   )
   Info = {"Username":username, "Password":password}
   with open('creds.json', 'w') as jsonFile:
      json.dump(Info, jsonFile)
      jsonFile.close()


def create_group(group_name):
   response = client.create_group(GroupName=group_name)
   print(response)
   return group_name


def attach_policy_to_group(group_name, policy_arn):
   response = client.attach_group_policy(GroupName=group_name, PolicyArn=policy_arn)
   print(response)

def add_user_to_group(username, group_name):
   response = iam_client.add_user_to_group(GroupName=group_name, UserName=username)
   print(response)


def parse_args():
   parser = argparse.ArgumentParser()
   parser.add_argument("-u", "--username", help="username")
   args = parser.parse_args()
   return args



def main():
   args = parse_args()
   create_user(args.username)
   group_name = "Admins"
   create_group(group_name)
   attach_policy_to_group(group_name, "arn:aws:iam::aws:policy/AdministratorAccess")
   add_user_to_group(args.username, "Admins")


if __name__ == "__main__":
   main()