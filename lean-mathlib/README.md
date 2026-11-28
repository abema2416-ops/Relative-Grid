# lean-mathlib — theorems that need Mathlib

Lean 4 v4.37.0-rc1 + Mathlib v4.37.0-rc1. 9 theorems, only standard axioms (propext, Classical.choice, Quot.sound), no sorry.

- `Setka2/Rank.lean` — rank bound `R(H) ≥ rank A` (`rank_bound`, `expTable_eq_mul`, `le_of_rows_independent`); tree method, counting part (`card_ge_shared_add`, `shared_in_two`, `saving_in_group`).
- `Setka2/Exact.lean` — preimage count `2^(z₀-1)·∏(2^{z_B}-1)` in the exact loss of compressing a row (`card_preimages`).

Build: `lake exe cache get && lake build`, then `lake env lean Check.lean`.
