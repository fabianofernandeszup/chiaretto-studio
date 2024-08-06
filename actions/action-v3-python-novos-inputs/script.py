

def run(metadata):
    print(f"Hello {metadata.inputs.get('user_name')}!")
    print(f"All inputs: ", metadata.inputs)
