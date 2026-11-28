import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Finset.Powerset
import Mathlib.Algebra.BigOperators.Fin

/-!
# Exact loss of compressing a row: the counting part (Theorem `thm:exact`)

The geometric part (the result is determined by the anchor and the set of nonempty blocks)
is `shrink_same_of_blocks` / `shrinkCell_eq_iff` in `lean/Setka/Core.lean`.
Here: the number of admissible block contents is `2^(z₀-1) · ∏ (2^{z_B} - 1)`.
-/

namespace Setka2

variable {α : Type*} [DecidableEq α]

/-- Nonempty subsets of a block: `2^z - 1`. -/
theorem card_nonempty_subsets (B : Finset α) :
    (B.powerset.filter fun X => X.Nonempty).card = 2 ^ B.card - 1 := by
  have h : B.powerset.filter (fun X => X.Nonempty) = B.powerset.erase ∅ := by
    ext X; simp [← Finset.ne_empty_iff_nonempty, and_comm]
  rw [h, Finset.card_erase_of_mem (Finset.empty_mem_powerset B), Finset.card_powerset]

/-- Subsets of the anchor block containing the anchor cell: `2^(z₀-1)`. -/
theorem card_subsets_with (B : Finset α) {a : α} (ha : a ∈ B) :
    (B.powerset.filter fun X => a ∈ X).card = 2 ^ (B.card - 1) := by
  have h : (B.powerset.filter fun X => a ∈ X) = (B.erase a).powerset.image (insert a) := by
    ext X
    simp only [Finset.mem_filter, Finset.mem_powerset, Finset.mem_image]
    constructor
    · rintro ⟨hX, haX⟩
      refine ⟨X.erase a, Finset.erase_subset_erase a hX, Finset.insert_erase haX⟩
    · rintro ⟨Y, hY, rfl⟩
      refine ⟨Finset.insert_subset ha (hY.trans (Finset.erase_subset a B)), Finset.mem_insert_self a Y⟩
  rw [h, Finset.card_image_of_injOn, Finset.card_powerset, Finset.card_erase_of_mem ha]
  intro Y₁ h₁ Y₂ h₂ he
  have n₁ : a ∉ Y₁ := fun h => (Finset.notMem_erase a B) (Finset.mem_powerset.1 h₁ h)
  have n₂ : a ∉ Y₂ := fun h => (Finset.notMem_erase a B) (Finset.mem_powerset.1 h₂ h)
  rw [← Finset.erase_insert n₁, ← Finset.erase_insert n₂]
  exact congrArg (Finset.erase · a) he

/-- Independent choices in blocks: block `0` holds the anchor, the other `r` blocks are
nonempty. The number of contents with the same result is `2^(z₀-1) · ∏ (2^{z_i} - 1)`. -/
theorem card_preimages {r : ℕ} (blk : Fin (r + 1) → Finset α) {a : α} (ha : a ∈ blk 0) :
    (Fintype.piFinset fun i : Fin (r + 1) =>
        if i = 0 then (blk i).powerset.filter (fun X => a ∈ X)
        else (blk i).powerset.filter (fun X => X.Nonempty)).card =
      2 ^ ((blk 0).card - 1) * ∏ i : Fin r, (2 ^ (blk i.succ).card - 1) := by
  rw [Fintype.card_piFinset, Fin.prod_univ_succ]
  simp only [Fin.succ_ne_zero, ite_false, ite_true]
  rw [card_subsets_with _ ha]
  congr 1
  exact Finset.prod_congr rfl fun i _ => card_nonempty_subsets _

end Setka2
