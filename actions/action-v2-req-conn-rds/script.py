def run(metadata):
    print("###################################")
    print(f"Hello {metadata.inputs.get('user_name')}")
    print("###################################")
    print(f"Engine: {metadata.inputs.get('aws_rds_conn__CONNECTOR__engine')}")
    print(f"Engine Version: {metadata.inputs.get('aws_rds_conn__CONNECTOR__engine_version')}")
    print(f"Name: {metadata.inputs.get('aws_rds_conn__CONNECTOR__name')}")
    print(f"Host: {metadata.inputs.get('aws_rds_conn__CONNECTOR__host')}")
    print(f"Port: {metadata.inputs.get('aws_rds_conn__CONNECTOR__port')}")
    print(f"User: {metadata.inputs.get('aws_rds_conn__CONNECTOR__user')}")
    print('Done!')