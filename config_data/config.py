from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    # If you want to change vars in .env => override=True
    env.read_env(path=path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))
