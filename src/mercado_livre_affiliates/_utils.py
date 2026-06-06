import re


def extract_mercado_livre_verification_code_from_mail(mail_content: str) -> str | None:
    match = re.search(pattern=r"\b\d{6}\b", string=mail_content)
    if match is not None:
        return match.group(0)
    return None
