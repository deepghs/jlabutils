from .dispatch import jlabutilcli

_DECORATORS = [
]

cli = jlabutilcli
for deco in _DECORATORS:
    cli = deco(cli)
