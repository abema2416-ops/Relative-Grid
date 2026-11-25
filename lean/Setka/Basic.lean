/-! Вспомогательные факты о списках без повторов (вместо Mathlib). -/
namespace Setka

/-- Если список без повторов целиком лежит в k, он не длиннее k. -/
theorem nodup_length_le_of_subset [DecidableEq α] :
    ∀ {l k : List α}, l.Nodup → (∀ x ∈ l, x ∈ k) → l.length ≤ k.length
  | [], _, _, _ => by simp
  | a :: l, k, hn, hs => by
    rw [List.nodup_cons] at hn
    have ha : a ∈ k := hs a (by simp)
    have hsub : ∀ x ∈ l, x ∈ k.erase a := by
      intro x hx
      have hxa : x ≠ a := fun h => hn.1 (h ▸ hx)
      exact (List.mem_erase_of_ne hxa).2 (hs x (by simp [hx]))
    have ih := nodup_length_le_of_subset hn.2 hsub
    rw [List.length_erase_of_mem ha] at ih
    have : 0 < k.length := List.length_pos_of_mem ha
    simp; omega

/-- Принцип ящиков: различные натуральные числа меньше m — их не больше m. -/
theorem pigeon {l : List Nat} {m : Nat} (hn : l.Nodup) (hl : ∀ x ∈ l, x < m) : l.length ≤ m := by
  have := nodup_length_le_of_subset (k := List.range m) hn (by intro x hx; simpa using hl x hx)
  simpa using this

/-- Образ списка без повторов при отображении, различающем его элементы, — без повторов. -/
theorem nodup_map_of_inj {f : α → β} :
    ∀ {l : List α}, l.Nodup → (∀ a ∈ l, ∀ b ∈ l, f a = f b → a = b) → (l.map f).Nodup
  | [], _, _ => by simp
  | a :: l, hn, hi => by
    rw [List.nodup_cons] at hn
    simp only [List.map_cons, List.nodup_cons, List.mem_map]
    refine ⟨?_, nodup_map_of_inj hn.2 (fun x hx y hy h => hi x (by simp [hx]) y (by simp [hy]) h)⟩
    rintro ⟨b, hb, hfb⟩
    have := hi b (by simp [hb]) a (by simp) hfb
    exact hn.1 (this ▸ hb)

/-- flatMap без повторов: каждый кусок без повторов, а куски разных элементов не пересекаются. -/
theorem nodup_flatMap {g : α → List β} :
    ∀ {l : List α}, l.Nodup → (∀ a ∈ l, (g a).Nodup) →
      (∀ a ∈ l, ∀ b ∈ l, ∀ x, x ∈ g a → x ∈ g b → a = b) → (l.flatMap g).Nodup
  | [], _, _, _ => by simp
  | a :: l, hn, hg, hd => by
    rw [List.nodup_cons] at hn
    rw [List.flatMap_cons, List.nodup_append]
    refine ⟨hg a (by simp), nodup_flatMap hn.2 (fun x hx => hg x (by simp [hx]))
      (fun x hx y hy z h1 h2 => hd x (by simp [hx]) y (by simp [hy]) z h1 h2), ?_⟩
    intro x hx y hy hxy
    subst hxy
    obtain ⟨b, hb, hxb⟩ := List.mem_flatMap.1 hy
    have := hd a (by simp) b (by simp [hb]) x hx hxb
    exact hn.1 (this ▸ hb)

theorem length_flatMap_const {g : α → List β} {c : Nat} :
    ∀ {l : List α}, (∀ a ∈ l, (g a).length = c) → (l.flatMap g).length = c * l.length
  | [], _ => by simp
  | a :: l, h => by
    rw [List.flatMap_cons, List.length_append, h a (by simp),
      length_flatMap_const (fun x hx => h x (by simp [hx]))]
    simp [Nat.mul_succ]; omega

end Setka
