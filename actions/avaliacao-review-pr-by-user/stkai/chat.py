import json
from typing import Dict, List
from oscli.core.http import post_with_authorization
from oscli import __codebuddy_base_url__


def call_code_buddy_chat(
        prompt: str
) -> Dict:
    """
    Chama o chat do Code Buddy com streaming

    Args:
        prompt: Prompt do usuário

    Returns:
        Dict com resposta completa
    """
    url = f"{__codebuddy_base_url__}/v3/chat"
    payload = {
        "context": {
            "upload_ids": [],
            "agent_built_in": True,
        },
        "user_prompt": prompt
    }

    result = post_with_authorization(
        url=url,
        body=payload,
        headers={"Accept": "text/event-stream"},
        stream=True
    )

    if result.status_code != 200:
        error_msg = f"Erro ao chamar Code Buddy: {result.status_code} - {result.text}"
        raise Exception(error_msg)

    resposta_completa = []

    for raw_line in result.iter_lines():
        if not raw_line:
            continue

        line = raw_line.decode("utf-8").strip()

        if line.startswith("data:"):
            try:
                data_content = json.loads(line[5:].strip())
                if "answer" in data_content and isinstance(data_content["answer"], str):
                    resposta_completa.append(data_content["answer"])
            except json.JSONDecodeError:
                continue
        elif line.startswith("event: end_event"):
            break

    return {"answer": "".join(resposta_completa).strip()}