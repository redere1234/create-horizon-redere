"""Build the generated native bundle manifest from source compatibility metadata."""
import json
import tomllib
from common import ROOT, NATIVE, PINS


def native_manifest():
    mixin = tomllib.loads((NATIVE / "horizon-mixin.toml").read_text())
    mod = mixin["mod"]
    return {
        "schema": 1,
        "id": mod["id"],
        "version": mod["version"],
        "game": "26.3",
        "horizon": PINS["horizon_revision"],
        "mixins": PINS["horizon_mixins_revision"],
    }


def native_manifest_bytes():
    return (json.dumps(native_manifest(), indent=2) + "\n").encode()
