from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Literal, Optional

from explainaboard_api_client import Configuration


@dataclass
class HostConfig:
    host: Optional[str] = None
    frontend: Optional[str] = None


ENV_HOST_MAP: defaultdict[str, HostConfig] = defaultdict(
    HostConfig,
    {
        "main": HostConfig(
            host="https://explainaboard.inspiredco.ai/api",
            frontend="https://explainaboard.inspiredco.ai",
        ),
        "staging": HostConfig(
            host="https://dev.explainaboard.inspiredco.ai/api",
            frontend="https://dev.explainaboard.inspiredco.ai",
        ),
        "local": HostConfig(
            host="http://localhost:5000/api", frontend="http://localhost:3000"
        ),
    },
)


@dataclass
class Config:
    """configurations for explainaboard CLI
    :param host: if specified, it takes precedence over environment

    """

    user_email: str
    api_key: str
    environment: Literal["main", "staging", "local"] = "main"
    host: Optional[str] = None

    def __post_init__(self):
        if self.environment not in {"main", "staging", "local"}:
            raise ValueError(f"{self.environment} is not a valid environment")

    @staticmethod
    def get_env_host_map():
        return ENV_HOST_MAP

    def to_client_config(self):
        client_config = Configuration()
        client_config.host = ENV_HOST_MAP[self.environment].host

        if self.host:
            client_config.host = self.host

        client_config.username = self.user_email
        client_config.password = self.api_key
        return client_config
