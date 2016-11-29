#!/bin/bash
rustup default nightly
cargo clean
RUSTFLAGS="-Z print-type-sizes" cargo build >type_sizes_nightly.txt
cargo clean
rustup default univariant_optimization
RUSTFLAGS="-Z print-type-sizes" cargo build >type_sizes_optimized.txt
python3 load_sizes.py >out.txt
