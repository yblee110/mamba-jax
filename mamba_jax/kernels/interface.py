from typing import Optional

import jax
import jax.numpy as jnp


# TODO: populate function that arranges data as expected by kernel and calls it
# TODO: add `jax.custom_jvp` for calling correct kernel for fwd / bwd pass
def mamba_ssm(
    u: jax.Array,
    delta: jax.Array,
    A: jax.Array,
    B: jax.Array,
    C: jax.Array,
    D: Optional[jax.Array] = None,
    delta_bias: Optional[jax.Array] = None,
    delta_softplus: bool = False,
) -> jax.Array:
    pass


# TODO: add fused residual+norm layer
# TODO: add `jax.custom_jvp` for calling correct kernel for fwd / bwd pass
def add_norm():
    pass
