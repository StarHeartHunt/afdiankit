import shutil
from pathlib import Path
from typing import Any, Dict

import tomli
from jinja2 import Environment, PackageLoader

from .log import logger
from .config import Config
from .models import SchemaData
from .utils import sanitize, kebab_case, snake_case, pascal_case

env = Environment(
    loader=PackageLoader("codegen"),
    trim_blocks=True,
    lstrip_blocks=True,
    extensions=["jinja2.ext.loopcontrols"],
)
env.globals.update(
    {
        "sanitize": sanitize,
        "snake_case": snake_case,
        "pascal_case": pascal_case,
        "kebab_case": kebab_case,
    }
)


def load_config() -> Config:
    pyproject = tomli.loads(Path("./pyproject.toml").read_text())
    config_dict: Dict[str, Any] = pyproject.get("tool", {}).get("codegen", {})

    return Config.model_validate(config_dict)


def build_api(data: SchemaData, client_output: str):
    # build endpoints
    logger.info("Building endpoints...")

    client_path = Path(client_output)
    shutil.rmtree(client_path)
    client_path.mkdir(parents=True, exist_ok=True)

    client_template = env.get_template("client/client.py.jinja")

    for tag, endpoints in data.endpoints_by_tag.items():
        logger.info(f"Building endpoints for tag {tag}...")
        tag_path = client_path / f"{tag}.py"
        tag_path.write_text(client_template.render(tag=tag, endpoints=endpoints))
        logger.info(f"Successfully built endpoints for tag {tag}!")
    logger.info("Successfully built endpoints!")

    # build types
    logger.info("Building types...")
    types_template = env.get_template("models/types.py.jinja")
    types_path = client_path / "types.py"
    types_path.write_text(types_template.render(data=data))
    logger.info("Successfully built types!")

    # build namespace
    logger.info("Building namespace...")
    namespace_template = env.get_template("namespace/namespace.py.jinja")
    namespace_path = client_path / "__init__.py"
    namespace_path.write_text(
        namespace_template.render(tags=data.endpoints_by_tag.keys())
    )
    logger.info("Successfully built namespace!")


def build_types(data: SchemaData, client_output: str): ...


def build():
    config = load_config()
    logger.info(f"Loaded config: {config!r}")

    logger.info("Parsing schema from dumped JavaScript file...")
    raw_schema_path = Path(__file__).parent / "data" / "data.json"
    data = SchemaData.model_validate_json(raw_schema_path.read_text("utf-8"))

    build_api(data, config.client_output)
