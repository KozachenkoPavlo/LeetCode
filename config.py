import os
from dataclasses import dataclass

import environ


@dataclass(frozen=True)
class Config:
    root_dir: str
    leetcode_api_url: str

    @staticmethod
    def load() -> "Config":
        environ.Env.read_env()
        env = environ.Env()

        return Config(
            root_dir=os.path.dirname(os.path.abspath(__file__)),
            leetcode_api_url=env.str("LEETCODE_API_URL")
        )
