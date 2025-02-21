from langchain_gigachat.chat_models import GigaChat

from ..config.config import load_config


config = load_config()


model = GigaChat(
    credentials=config.giga_key.secret_key,
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    streaming=False,
    verify_ssl_certs=False,
)
