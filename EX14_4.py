import boto3

ec2 = boto3.resource('ec2')
snapshot = ec2.Snapshot('id')

for vol in ec2.volumes.all():
    if vol.state=='available':
        string=vol.id
        ec2.create_snapshot(VolumeId=vol.id,Description=string)
        print(vol.id),
        print('Snapshot has been created')
    else:
        print('There is not any volumes')