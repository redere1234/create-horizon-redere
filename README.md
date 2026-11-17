<div align="center">

# Create for Horizon — Redere Edition

**A redere1234-maintained fork of the native Rust Create port for the Horizon runtime.**

Gears, belts, kinetic power and moving machines — rebuilt for Horizon.

[![Horizon](https://img.shields.io/badge/Horizon-26.3-6d5dfc?style=for-the-badge)](https://playhorizon.dev/)
[![Rust](https://img.shields.io/badge/Rust-native-orange?style=for-the-badge&logo=rust)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## What is this?

Create for Horizon — Redere Edition is a native implementation of Create-inspired factory mechanics for Minecraft 26.3 on the Horizon runtime. It is written in Rust and built around Horizon's APIs rather than running Java JARs directly.

This fork is maintained by **redere1234**. Its original Horizon-native integration, compatibility updates, packaging, and documentation changes are the work of this fork's maintainer. The `create` mod namespace is intentionally preserved so existing worlds and registry references remain compatible.

The goal is simple: make machines feel powerful, connected and useful — with the original Create identity intact.

## What's included

- Kinetic power — hand cranks, water wheels, Creative Motors, shafts, cogs, gearboxes.
- Item transport — belts, depots, funnels, chutes.
- Processing — pressing, milling, fan processing, washing, smoking, haunting, blasting.
- Heat-aware crafting — basins, mixers, Blaze Burners.
- Moving contraptions — deployers, drills, saws, bearings, pistons, rope pulleys.
- Assembly — Super Glue, sequenced assembly, portable storage.
- Presentation — native models, textures, particles, sounds and Horizon-compatible hooks.

## Install

1. Create a Horizon instance for Minecraft 26.3.
2. Open **Mods → Add from GitHub** and enter the repository URL.
3. Build the native mod and start the instance.

For original Create models and textures, place the supported Create 6.0.10 JAR in `horizon-mods/create-resources/`. Original assets are not bundled here.

- [Installation guide](docs/installation.md)
- [Resource setup](docs/assets.md)

## Development

```bash
python3 tools/bootstrap.py
HORIZON_SOURCE=/path/to/horizon python3 tools/stage.py check
```

The project uses Rust and the pinned Horizon Mixins pipeline. The native build targets the pinned Horizon revision. Check the compatibility and roadmap documents before changing gameplay or presentation.

- [Build and test](docs/development.md)
- [Compatibility](docs/compatibility.md)
- [Roadmap](docs/roadmap.md)

## Project status

Active and experimental. Some features are still being refined. Horizon API changes may require compatibility updates as the runtime evolves.

## License

MIT for the fork's original code and modifications. Create's original code, art and audio remain credited to their authors and are subject to their original terms. See [AUTHORS.md](AUTHORS.md), [LICENSE](LICENSE), and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for details.

---

<div align="center">

*Built one machine, one belt and one bug fix at a time.*

</div>
