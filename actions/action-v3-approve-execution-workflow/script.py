from ulid import ULID
from oscli.core.http import post_with_authorization
from oscli import __workflow_base_url__


def run(metadata):
    result = post_with_authorization(
        url=f"{__workflow_base_url__}/v1/executions/{metadata.inputs['execution_id']}/jobs/{metadata.inputs['job_id']}/accept",
    )
    if not result.ok:
        print(result.text)
        result.raise_for_status()
