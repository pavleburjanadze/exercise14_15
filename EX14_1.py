import boto3
import argparse

client = boto3.client("iam")

def list_policy(username):
   response = client.list_attached_user_policies(
      UserName=username
   )
   return response


def parse_args():
   parser = argparse.ArgumentParser()
   parser.add_argument("-u", "--username", help="username")
   args = parser.parse_args()
   return args



def main():
   args = parse_args()
   list_policy(args.username)


if __name__ == "__main__":
   main()