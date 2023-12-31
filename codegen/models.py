from collections import defaultdict
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, RootModel


class Endpoint(BaseModel):
    name: str
    url: str
    method: str
    data: Optional[Dict[str, Any]]

    def get_endpoint_tag(self) -> str:
        return self.url.split("/")[2]

    @property
    def params(self):
        return self.data if self.method == "get" else None

    @property
    def body(self):
        return self.data if self.method == "post" else None

    def get_type(self, value: Any):
        return type(value).__name__


class SchemaData(RootModel):
    root: List[Endpoint]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]

    @property
    def endpoints_by_tag(self):
        tags_endpoints = defaultdict(list)
        for endpoint in self:
            tags_endpoints[endpoint.get_endpoint_tag()].append(endpoint)

        return tags_endpoints
