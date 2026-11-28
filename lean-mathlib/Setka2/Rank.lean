import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Algebra.BigOperators.Finsupp.Basic

/-!
# Rank bound and tree method for R(H)

Heights `h i` (i : Fin D) are built from factors `m j` (j : Fin R): `h i = ∏ j ∈ S i, m j`.
`A i k` = exponent of the prime `P k` in `h i`.
-/

open Matrix

namespace Setka2

/-- Exponent table of the heights. -/
noncomputable def expTable {D K : ℕ} (h : Fin D → ℕ) (P : Fin K → ℕ) : Matrix (Fin D) (Fin K) ℚ :=
  Matrix.of fun i k => ((h i).factorization (P k) : ℚ)

/-- The table factors as (0/1 usage table) × (exponent table of the factors). -/
theorem expTable_eq_mul {D R K : ℕ} (h : Fin D → ℕ) (m : Fin R → ℕ) (hm : ∀ j, m j ≠ 0)
    (S : Fin D → Finset (Fin R)) (hS : ∀ i, h i = ∏ j ∈ S i, m j) (P : Fin K → ℕ) :
    expTable h P =
      (Matrix.of fun i j => if j ∈ S i then (1 : ℚ) else 0) * expTable m P := by
  ext i k
  simp only [expTable, Matrix.mul_apply, Matrix.of_apply, hS i,
    Nat.factorization_prod (fun j _ => hm j), Finset.sum_apply', Nat.cast_sum, ite_mul, one_mul,
    zero_mul]
  rw [Finset.sum_ite_mem, Finset.univ_inter]

/-- **Rank bound** (Theorem `thm:rank`): `R ≥ rank A`. -/
theorem rank_bound {D R K : ℕ} (h : Fin D → ℕ) (m : Fin R → ℕ) (hm : ∀ j, m j ≠ 0)
    (S : Fin D → Finset (Fin R)) (hS : ∀ i, h i = ∏ j ∈ S i, m j) (P : Fin K → ℕ) :
    (expTable h P).rank ≤ R := by
  rw [expTable_eq_mul h m hm S hS P]
  calc _ ≤ (Matrix.of fun i j => if j ∈ S i then (1 : ℚ) else 0).rank := rank_mul_le_left _ _
    _ ≤ Fintype.card (Fin R) := rank_le_card_width _
    _ = R := Fintype.card_fin R

/-- If the rows of the table are linearly independent, at least `D` factors are needed. -/
theorem le_of_rows_independent {D R K : ℕ} (h : Fin D → ℕ) (m : Fin R → ℕ) (hm : ∀ j, m j ≠ 0)
    (S : Fin D → Finset (Fin R)) (hS : ∀ i, h i = ∏ j ∈ S i, m j) (P : Fin K → ℕ)
    (hli : LinearIndependent ℚ (expTable h P)) : D ≤ R := by
  have h1 := rank_bound h m hm S hS P
  rw [← finrank_span_range_row, finrank_span_eq_card (b := (expTable h P).row) hli,
    Fintype.card_fin] at h1
  exact h1

/-! ## Tree method: counting part (Theorem `thm:tree`) -/

variable {α β : Type*} [DecidableEq α] [DecidableEq β]

/-- Factors of `B` used by at least two heights. -/
def shared (B : Finset α) (H : Finset β) (S : β → Finset α) : Finset α :=
  B.filter fun b => 2 ≤ (H.filter fun g => b ∈ S g).card

/-- Heights factored only by shared factors. -/
def treeGroup (B : Finset α) (H : Finset β) (S : β → Finset α) : Finset β :=
  H.filter fun g => S g ⊆ shared B H S

/-- `|B| ≥ (number of shared) + (number of heights outside T)`. -/
theorem card_ge_shared_add (B : Finset α) (H : Finset β) (S : β → Finset α)
    (hSB : ∀ g ∈ H, S g ⊆ B) :
    (shared B H S).card + (H \ treeGroup B H S).card ≤ B.card := by
  classical
  -- each height outside T has a factor that is not shared; pick one
  have hex : ∀ g ∈ H \ treeGroup B H S, ∃ b ∈ S g, b ∉ shared B H S := by
    intro g hg
    simp only [Finset.mem_sdiff, treeGroup, Finset.mem_filter, not_and] at hg
    have := hg.2 hg.1
    rw [Finset.not_subset] at this
    exact this
  have h2 : shared B H S ⊆ B := Finset.filter_subset _ _
  rcases (H \ treeGroup B H S).eq_empty_or_nonempty with hE | ⟨g₀, hg₀⟩
  · rw [hE, Finset.card_empty, Nat.add_zero]; exact Finset.card_le_card h2
  have : Nonempty α := ⟨(hex g₀ hg₀).choose⟩
  choose! pick hpick hpick' using hex
  -- a non-shared factor used by g is used by g only
  have hinj : Set.InjOn pick (↑(H \ treeGroup B H S) : Set β) := by
    intro g₁ hg₁ g₂ hg₂ heq
    by_contra hne
    have hb := hpick' g₁ hg₁
    have hg₁H : g₁ ∈ H := (Finset.mem_sdiff.1 hg₁).1
    have hg₂H : g₂ ∈ H := (Finset.mem_sdiff.1 hg₂).1
    apply hb
    simp only [shared, Finset.mem_filter]
    refine ⟨hSB g₁ hg₁H (hpick g₁ hg₁), ?_⟩
    have hsub : ({g₁, g₂} : Finset β) ⊆ H.filter fun g => pick g₁ ∈ S g := by
      intro x hx
      simp only [Finset.mem_insert, Finset.mem_singleton] at hx
      rcases hx with rfl | rfl
      · exact Finset.mem_filter.2 ⟨hg₁H, hpick x hg₁⟩
      · exact Finset.mem_filter.2 ⟨hg₂H, heq ▸ hpick x hg₂⟩
    calc 2 = ({g₁, g₂} : Finset β).card := (Finset.card_pair hne).symm
      _ ≤ _ := Finset.card_le_card hsub
  have himg : (H \ treeGroup B H S).image pick ⊆ B \ shared B H S := by
    intro b hb
    obtain ⟨g, hg, rfl⟩ := Finset.mem_image.1 hb
    exact Finset.mem_sdiff.2 ⟨hSB g (Finset.mem_sdiff.1 hg).1 (hpick g hg), hpick' g hg⟩
  have h1 : (H \ treeGroup B H S).card ≤ (B \ shared B H S).card := by
    rw [← Finset.card_image_of_injOn hinj]; exact Finset.card_le_card himg
  have e : (B \ shared B H S).card + (shared B H S).card = B.card := Finset.card_sdiff_add_card_eq_card h2
  omega

/-- Every factor of a height in `T` also occurs in another height. -/
theorem shared_in_two (B : Finset α) (H : Finset β) (S : β → Finset α) {g : β}
    (hg : g ∈ treeGroup B H S) {b : α} (hb : b ∈ S g) :
    ∃ g' ∈ H, g' ≠ g ∧ b ∈ S g' := by
  classical
  simp only [treeGroup, Finset.mem_filter] at hg
  have hs := hg.2 hb
  simp only [shared, Finset.mem_filter] at hs
  by_contra hno
  push Not at hno
  have : (H.filter fun g' => b ∈ S g') ⊆ {g} := by
    intro x hx
    rw [Finset.mem_filter] at hx
    by_cases hxg : x = g
    · simp [hxg]
    · exact absurd hx.2 (hno x hx.1 hxg)
  have := Finset.card_le_card this
  simp at this
  omega

/-- **Where savings hide.** If fewer factors than heights are used, then the group `T`
is built by fewer factors than it has heights (namely by the shared ones). -/
theorem saving_in_group (B : Finset α) (H : Finset β) (S : β → Finset α)
    (hSB : ∀ g ∈ H, S g ⊆ B) (hlt : B.card < H.card) :
    (shared B H S).card < (treeGroup B H S).card ∧
      ∀ g ∈ treeGroup B H S, S g ⊆ shared B H S := by
  refine ⟨?_, fun g hg => (Finset.mem_filter.1 hg).2⟩
  have h1 := card_ge_shared_add B H S hSB
  have h2 : treeGroup B H S ⊆ H := Finset.filter_subset _ _
  have h3 : (H \ treeGroup B H S).card + (treeGroup B H S).card = H.card :=
    Finset.card_sdiff_add_card_eq_card h2
  omega

end Setka2
