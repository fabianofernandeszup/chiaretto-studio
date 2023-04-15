def run(metadata):
    print("###################################")
    print(f"Hello {metadata.inputs.get('user_name')}")
    print("###################################")
    print(f"Arn: {metadata.inputs.get('aws_secret_manager_conn__CONNECTOR__arn')}")
    print(f"Name: {metadata.inputs.get('aws_secret_manager_conn__CONNECTOR__name')}")
    print('Done!')