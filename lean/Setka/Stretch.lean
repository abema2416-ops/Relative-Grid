import Setka.Basic
/-! Пункт 1.7: действие α. Утверждение 11 (баланс ячеек), свойство 1.7(в). -/
namespace Setka

/-- Ячейка: позиция p вдоль оси действия (измеренная по направлению s) и остальные координаты r. -/
structure Cell (β : Type) where
  p : Int
  r : β
deriving DecidableEq

set_option linter.unusedSectionVars false
variable {β : Type} [DecidableEq β]

/-- j-я ячейка образа ячейки c при растяжении в f раз от закреплённой стороны a. -/
def img (a : Int) (f : Nat) (c : Cell β) (j : Nat) : Cell β := ⟨a + f * (c.p - a) + j, c.r⟩

/-- образ ячейки: f ячеек подряд -/
def imgs (a : Int) (f : Nat) (c : Cell β) : List (Cell β) := (List.range f).map (img a f c)

/-- Растяжение: α(O) = (O \ G) ∪ {образы ячеек G}. Объект записан как rest ++ G. -/
def stretch (a : Int) (f : Nat) (rest G : List (Cell β)) : List (Cell β) := rest ++ G.flatMap (imgs a f)

/-- Главная арифметика: f·t + j = f·t' + j' при 0 ≤ j, j' < f даёт t = t' и j = j'. -/
theorem div_unique {f : Nat} {t t' : Int} {j j' : Nat} (hj : j < f) (hj' : j' < f)
    (h : (f : Int) * t + j = f * t' + j') : t = t' ∧ j = j' := by
  have key : ∀ {u v : Int} {i i' : Nat}, i < f → i' < f → u < v → (f : Int) * u + i < f * v + i' := by
    intro u v i i' hi _ huv
    have : (f : Int) * (u + 1) ≤ f * v := Int.mul_le_mul_of_nonneg_left (by omega) (by omega)
    rw [Int.mul_add] at this; omega
  rcases Int.lt_trichotomy t t' with hlt | heq | hgt
  · exact absurd h (Int.ne_of_lt (key hj hj' hlt))
  · subst heq; constructor; rfl; omega
  · exact absurd h.symm (Int.ne_of_lt (key hj' hj hgt))

/-- Образы разных ячеек группы (и разные j) различны: растяжение ничего не склеивает. -/
theorem img_inj {a : Int} {f : Nat} {c c' : Cell β} {j j' : Nat} (hj : j < f) (hj' : j' < f)
    (h : img a f c j = img a f c' j') : c = c' ∧ j = j' := by
  simp only [img, Cell.mk.injEq] at h
  obtain ⟨h1, h2⟩ := h
  have h1' : (f : Int) * (c.p - a) + j = f * (c'.p - a) + j' := by omega
  obtain ⟨ht, hjj⟩ := div_unique hj hj' h1'
  refine ⟨?_, hjj⟩
  cases c; cases c'; simp at *; constructor <;> omega

/-- 1.7(в), Утверждение 11: если действие допустимо (П3: новые ячейки не задевают O \ G),
    то повторов нет и |α(O)| = |O| + (f − 1)·|G|. -/
theorem stretch_card (a : Int) (f : Nat) (hf : 2 ≤ f) (rest G : List (Cell β))
    (hO : (rest ++ G).Nodup)
    (hP3 : ∀ x ∈ rest, ∀ y ∈ G.flatMap (imgs a f), x ≠ y) :
    (stretch a f rest G).Nodup ∧
    (stretch a f rest G).length = (rest ++ G).length + (f - 1) * G.length := by
  have hG : G.Nodup := (List.nodup_append.1 hO).2.1
  have hR : rest.Nodup := (List.nodup_append.1 hO).1
  have himg : (G.flatMap (imgs a f)).Nodup := by
    apply nodup_flatMap hG
    · intro c _
      apply nodup_map_of_inj List.nodup_range
      intro x hx y hy hxy
      exact (img_inj (List.mem_range.1 hx) (List.mem_range.1 hy) hxy).2
    · intro c _ c' _ x hx hx'
      simp only [imgs, List.mem_map, List.mem_range] at hx hx'
      obtain ⟨j, hj, rfl⟩ := hx
      obtain ⟨j', hj', he⟩ := hx'
      exact (img_inj hj' hj he).1.symm
  refine ⟨List.nodup_append.2 ⟨hR, himg, hP3⟩, ?_⟩
  have hlen : (G.flatMap (imgs a f)).length = f * G.length :=
    length_flatMap_const (fun c _ => by simp [imgs])
  simp only [stretch, List.length_append, hlen]
  obtain ⟨k, rfl⟩ : ∃ k, f = k + 1 := ⟨f - 1, by omega⟩
  simp [Nat.succ_mul]; omega

/-- 1.7(а),(б): ячейки вне зоны не меняются; у образов «остальные координаты» те же. -/
theorem stretch_keeps_rest (a : Int) (f : Nat) (rest G : List (Cell β)) :
    ∀ x ∈ rest, x ∈ stretch a f rest G := by
  intro x hx; simp [stretch, hx]

theorem img_r (a : Int) (f : Nat) (c : Cell β) (j : Nat) : (img a f c j).r = c.r := rfl

/-- Сжатие: ячейка c переходит в позицию a + ⌊(p − a)/f⌋. -/
def shrink1 (a : Int) (f : Nat) (c : Cell β) : Cell β := ⟨a + (c.p - a) / f, c.r⟩

/-- 1.7(г): две ячейки сливаются при сжатии ровно тогда, когда они в одном ряду
    и у них одинаковое ⌊t/f⌋. -/
theorem shrink_merge (a : Int) (f : Nat) (c c' : Cell β) :
    shrink1 a f c = shrink1 a f c' ↔ c.r = c'.r ∧ (c.p - a) / f = (c'.p - a) / f := by
  simp only [shrink1, Cell.mk.injEq]; constructor
  · rintro ⟨h1, h2⟩; exact ⟨h2, by omega⟩
  · rintro ⟨h1, h2⟩; exact ⟨by omega, h1⟩

end Setka
