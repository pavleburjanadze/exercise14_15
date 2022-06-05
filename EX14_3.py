import boto3
import datetime

client = boto3.client('ec2')
snapshots = client.describe_snapshots(OwnerIds=['self'])
for snapshot in snapshots['Snapshots']:
    a = snapshot['StartTime']
    b = a.date()
    c = datetime.datetime.now().date()
    d = c - b
    try:
        if d.days > 3:
            id = snapshot['SnapshotId']
            client.delete_snapshot(SnapshotId=id)
    except:
        print("There is not snaps during this days")
