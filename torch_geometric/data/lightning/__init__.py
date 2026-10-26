from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .datamodule import (
        LightningDataset,
        LightningLinkData,
        LightningNodeData,
    )


def __getattr__(name):
    if name in ('LightningDataset', 'LightningNodeData', 'LightningLinkData'):
        import warnings

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            from .datamodule import (
                LightningDataset,
                LightningLinkData,
                LightningNodeData,
            )
        return {
            'LightningDataset': LightningDataset,
            'LightningNodeData': LightningNodeData,
            'LightningLinkData': LightningLinkData,
        }[name]
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')


__all__ = classes = [
    'LightningDataset',
    'LightningNodeData',
    'LightningLinkData',
]
