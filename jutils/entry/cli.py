from .dispatch import jutilcli

_DECORATORS = [
]

cli = jutilcli
for deco in _DECORATORS:
    cli = deco(cli)
