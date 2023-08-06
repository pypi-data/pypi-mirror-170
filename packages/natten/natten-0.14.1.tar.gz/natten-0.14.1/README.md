# Neighborhood Attention CUDA Extension (NATTEN)
NATTEN, a PyTorch extension.

## About NATTEN

### Why use NATTEN?
Sliding window self attention mechanisms have been relatively overlooked, in part due to implementation difficulties.
In a paper proposing one the earliest examples of such methods, [SASA](https://arxiv.org/abs/1906.05909), it was noted that
although such methods are theoretically efficient, they're relatively slow in practice, compared to convolutions, 
which have been implemented in most well-known deep learning libraries.

That is why we started developing NATTEN, an extension to existing libraries with efficient implementations of sliding window
attention mechanisms.

We introduced [Neighborhood Attention](https://github.com/SHI-Labs/Neighborhood-Attention-Transformer), a localized self
attention module, which becomes equivalent to self attention when the window size matches input size.

For more information, we highly recommend reading our preprints [NAT](https://arxiv.org/abs/2204.07143) and
[DiNAT](https://arxiv.org/abs/2209.15001), and check out their [repository](https://github.com/SHI-Labs/Neighborhood-Attention-Transformer).

### How fast is NATTEN?
The latest version of NATTEN runs pretty fast on Ampere with the latest torch and CUDA versions.
For more details on recommended settings for speed, please refer to the [usage guide](USAGE.md).

![V012](assets/natten/v012dark.png#gh-dark-mode-only) ![V012](assets/natten/v012light.png#gh-light-mode-only)
![V012](assets/natten/kernelmemory_dark.png#gh-dark-mode-only) ![V012](assets/natten/kernelmemory_light.png#gh-light-mode-only)


## Requirements
We highly recommend using Python 3.8 and PyTorch 1.12 + CUDA 11.6 for the best performance.
However, NATTEN supports `torch>=1.8` and Python versions 3.7, 3.8, and 3.9.

**NOTE:** The current version of NATTEN comes with Linux-only wheels, and supports Pascal and above (`SM >= 6.0`).
You may try and build from source on Windows, but do so at your own risk.
For contributing Windows support, please see [contributing guide](CONTRIBUTE.md).
