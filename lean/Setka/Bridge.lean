/-! Утверждение 29(а),(б): клеточное растяжение — это обычное растяжение без округлений.
    Работаем вдоль оси действия (остальные координаты не меняются), точки — рациональные числа. -/
namespace Setka

/-- непрерывное растяжение в f раз от закреплённой стороны a -/
def T (a : Int) (f : Nat) (y : Rat) : Rat := a + f * (y - a)

/-- Точка y лежит в ячейке p ровно тогда, когда T(y) лежит в блоке из f ячеек,
    в которые переходит ячейка p: [a + f(p − a), a + f(p − a) + f). -/
theorem T_cell (a p : Int) (f : Nat) (hf : 0 < f) (y : Rat) :
    ((p : Rat) ≤ y ∧ y < p + 1) ↔
    ((a : Rat) + f * (p - a) ≤ T a f y ∧ T a f y < a + f * (p - a) + f) := by
  have hf' : (0 : Rat) < f := by exact_mod_cast hf
  unfold T
  constructor
  · rintro ⟨h1, h2⟩
    have e1 : (f : Rat) * (p - a) ≤ f * (y - a) :=
      Rat.mul_le_mul_of_nonneg_left (by grind) (Rat.le_of_lt hf')
    have e2 : (f : Rat) * (y - a) < f * (p + 1 - a) := (Rat.mul_lt_mul_left hf').2 (by grind)
    constructor
    · grind
    · have : (f : Rat) * (p + 1 - a) = f * (p - a) + f := by grind
      grind
  · rintro ⟨h1, h2⟩
    constructor
    · have h3 : (f : Rat) * (p - a) ≤ f * (y - a) := by grind
      by_cases hc : y - a < p - a
      · have := (Rat.mul_lt_mul_left hf').2 hc; grind
      · grind
    · have : (f : Rat) * (y - a) < f * (p + 1 - a) := by grind
      have := (Rat.mul_lt_mul_left hf').1 this
      grind

/-- T обратимо: каждая точка блока — образ точки ячейки (поэтому T(ячейка) = весь блок). -/
theorem T_onto (a : Int) (f : Nat) (hf : 0 < f) (v : Rat) : T a f (a + (v - a) / f) = v := by
  have hf' : (f : Rat) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hf)
  unfold T
  rw [show (a : Rat) + (v - a) / f - a = (v - a) / f by grind]
  have : (f : Rat) * ((v - a) / f) = v - a := by grind
  grind

/-- Блок [q, q + f) — это ровно f ячеек q, q+1, …, q+f−1 (точка блока лежит в одной из них). -/
theorem block_eq_cells (q : Int) (f : Nat) (v : Rat) :
    ((q : Rat) ≤ v ∧ v < q + f) ↔ ∃ j : Nat, j < f ∧ ((q + j : Int) : Rat) ≤ v ∧ v < ((q + j : Int) : Rat) + 1 := by
  constructor
  · rintro ⟨h1, h2⟩
    have hq : q ≤ v.floor := by
      have := Rat.lt_floor_add_one v
      have : ((q : Int) : Rat) < ((v.floor + 1 : Int) : Rat) := by grind
      have := Rat.intCast_lt_intCast.mp this; omega
    have hfl : v.floor < q + f := by
      have a1 := Rat.floor_le v
      have : ((v.floor : Int) : Rat) < ((q + f : Int) : Rat) := by push_cast; grind
      exact Rat.intCast_lt_intCast.mp this
    refine ⟨(v.floor - q).toNat, by omega, ?_, ?_⟩
    · rw [show q + ((v.floor - q).toNat : Int) = v.floor by omega]
      exact Rat.floor_le v
    · rw [show q + ((v.floor - q).toNat : Int) = v.floor by omega]
      have := Rat.lt_floor_add_one v; push_cast at this; exact this
  · rintro ⟨j, hj, h1, h2⟩
    push_cast at h1 h2
    have : (j : Rat) + 1 ≤ f := by exact_mod_cast hj
    have : (0 : Rat) ≤ j := by exact_mod_cast Nat.zero_le j
    constructor <;> grind

/-- Утверждение 29(б): при сжатии ячейка p (t = p − a) попадает в ячейку a + ⌊t/f⌋,
    и T⁻¹ переводит её в слой, лежащий внутри этой ячейки. -/
theorem shrink_slab (a p : Int) (f : Nat) (hf : 0 < f) :
    a + (p - a) / f ≤ a + (p - a) / f ∧
    f * ((p - a) / f) ≤ p - a ∧ p - a + 1 ≤ f * ((p - a) / f + 1) := by
  refine ⟨Int.le_refl _, ?_, ?_⟩
  · have := Int.mul_ediv_add_emod (p - a) f
    have : 0 ≤ (p - a) % f := Int.emod_nonneg _ (by omega)
    omega
  · have h1 := Int.mul_ediv_add_emod (p - a) f
    have h2 : (p - a) % f < f := Int.emod_lt_of_pos _ (by omega)
    rw [Int.mul_add, Int.mul_one]; omega

end Setka
