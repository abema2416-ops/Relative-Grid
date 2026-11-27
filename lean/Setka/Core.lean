import Setka.Basic
import Setka.Stretch
/-!
# Ядро системы «Относительная сетка»: строгая модель

Пространство — ℤⁿ, точка — функция `Fin n → Int`. Объект (как набор клеток) — предикат
`Pt n → Prop` («клетка x занята»). Склейки на набор клеток не влияют, поэтому в этой модели
β₊, β₋ и γ — тождественные по клеткам шаги (они учитываются отдельно в Glue.lean).

Действия ядра: растяжение и сжатие α (одна зона, одна ось, одно направление s = ±1,
коэффициент f ≥ 2, закреплённая сторона a), уничтожение σ, склейка/расклейка β.
-/
namespace Setka.Core

abbrev Pt (n : Nat) := Fin n → Int
abbrev Obj (n : Nat) := Pt n → Prop

variable {n : Nat}

/-- Точка x, у которой i-я координата заменена на v. -/
def upd (x : Pt n) (i : Fin n) (v : Int) : Pt n := fun k => if k = i then v else x k

@[simp] theorem upd_same (x : Pt n) (i : Fin n) (v : Int) : upd x i v i = v := by simp [upd]
@[simp] theorem upd_other (x : Pt n) {i k : Fin n} (v : Int) (h : k ≠ i) : upd x i v k = x k := by
  simp [upd, h]
theorem upd_self (x : Pt n) (i : Fin n) : upd x i (x i) = x := by
  funext k; by_cases h : k = i <;> simp [upd, h]

/-- Направление: s = 1 или s = −1. -/
def Dir (s : Int) : Prop := s = 1 ∨ s = -1

/-- Закреплённая сторона (1.7): a = min { s·c_i : c ∈ G }, G = O ∩ Z. -/
def Anchor (O Z : Obj n) (i : Fin n) (s a : Int) : Prop :=
  (∃ e, O e ∧ Z e ∧ s * e i = a) ∧ ∀ c, O c → Z c → a ≤ s * c i

/-- Растяжение (1.7): α(O) = (O \ G) ∪ { c[a + f·t(c) + j] : c ∈ G, 0 ≤ j < f },
    где позиция p задаёт i-ю координату s·p. -/
def stretch (O Z : Obj n) (i : Fin n) (s : Int) (f : Nat) (a : Int) : Obj n := fun x =>
  (O x ∧ ¬ Z x) ∨ ∃ c, O c ∧ Z c ∧ ∃ j, j < f ∧ x = upd c i (s * (a + f * (s * c i - a) + j))

/-- Сжатие (1.7): c ↦ c[a + ⌊t(c)/f⌋]. -/
def shrinkCell (i : Fin n) (s : Int) (f : Nat) (a : Int) (c : Pt n) : Pt n :=
  upd c i (s * (a + (s * c i - a) / f))

def shrink (O Z : Obj n) (i : Fin n) (s : Int) (f : Nat) (a : Int) : Obj n := fun x =>
  (O x ∧ ¬ Z x) ∨ ∃ c, O c ∧ Z c ∧ x = shrinkCell i s f a c

/-- Уничтожение σ (1.8). -/
def sigma (O Z : Obj n) : Obj n := fun x => O x ∧ ¬ Z x

/-- П3 для растяжения: новые клетки не задевают O \ G. -/
def P3 (O Z : Obj n) (i : Fin n) (s : Int) (f : Nat) (a : Int) : Prop :=
  ∀ x, O x → ¬ Z x → ¬ ∃ c, O c ∧ Z c ∧ ∃ j, j < f ∧ x = upd c i (s * (a + f * (s * c i - a) + j))

/-- П3 для сжатия: новые клетки не задевают O \ G. -/
def P3s (O Z : Obj n) (i : Fin n) (s : Int) (f : Nat) (a : Int) : Prop :=
  ∀ x, O x → ¬ Z x → ¬ ∃ c, O c ∧ Z c ∧ x = shrinkCell i s f a c

/-- Один шаг ядра. Метка `some i` — действие α вдоль оси i; `none` — σ или β (клетки по осям не растут). -/
inductive Step : Obj n → Obj n → Option (Fin n) → Prop
  | stretch (O Z : Obj n) (i : Fin n) (s : Int) (f : Nat) (a : Int) :
      Dir s → 2 ≤ f → Anchor O Z i s a → P3 O Z i s f a → Step O (stretch O Z i s f a) (some i)
  | shrink (O Z : Obj n) (i : Fin n) (s : Int) (f : Nat) (a : Int) :
      Dir s → 2 ≤ f → Anchor O Z i s a → P3s O Z i s f a → Step O (shrink O Z i s f a) (some i)
  | sigma (O Z : Obj n) : Step O (sigma O Z) none
  | glue (O : Obj n) : Step O O none

/-- Цепочка шагов; список меток — по одной на действие, его длина — число действий. -/
inductive Chain : Obj n → Obj n → List (Option (Fin n)) → Prop
  | nil (O : Obj n) : Chain O O []
  | cons {O O₁ O₂ : Obj n} {ax : Option (Fin n)} {l : List (Option (Fin n))} :
      Step O O₁ ax → Chain O₁ O₂ l → Chain O O₂ (ax :: l)

/-- Объект «развёрнут» вдоль оси k: у его клеток есть два разных значения k-й координаты. -/
def Spreads (O : Obj n) (k : Fin n) : Prop := ∃ x y, O x ∧ O y ∧ x k ≠ y k

/-- Одна клетка. -/
def single (c : Pt n) : Obj n := fun x => x = c

/-! ## Утверждение 19(а), нижняя оценка: m(O) ≤ ℓ(O) -/

/-- Шаг вдоль оси i не создаёт новых значений координаты k ≠ i; σ и β — никаких. -/
theorem step_spreads {O O' : Obj n} {ax : Option (Fin n)} (h : Step O O' ax) (k : Fin n)
    (hs : Spreads O' k) : Spreads O k ∨ ax = some k := by
  -- у каждой клетки результата k-я координата — как у некоторой клетки O (если ось ≠ k)
  have keyα : ∀ (P : Obj n) (i : Fin n), (∀ x, P x → ∃ c, O c ∧ (k ≠ i → x k = c k)) →
      Spreads P k → Spreads O k ∨ some i = some k := by
    intro P i hP ⟨x, y, hx, hy, hxy⟩
    by_cases hik : k = i
    · exact Or.inr (by rw [hik])
    · left
      obtain ⟨c, hc, hcx⟩ := hP x hx
      obtain ⟨d, hd, hdy⟩ := hP y hy
      exact ⟨c, d, hc, hd, by rw [← hcx hik, ← hdy hik]; exact hxy⟩
  cases h with
  | stretch Z i s f a _ _ _ _ =>
    apply keyα _ i _ hs
    intro x hx
    rcases hx with ⟨hO, _⟩ | ⟨c, hc, _, j, _, rfl⟩
    · exact ⟨x, hO, fun _ => rfl⟩
    · exact ⟨c, hc, fun hne => upd_other c _ hne⟩
  | shrink Z i s f a _ _ _ _ =>
    apply keyα _ i _ hs
    intro x hx
    rcases hx with ⟨hO, _⟩ | ⟨c, hc, _, rfl⟩
    · exact ⟨x, hO, fun _ => rfl⟩
    · exact ⟨c, hc, fun hne => upd_other c _ hne⟩
  | sigma Z =>
    left
    obtain ⟨x, y, hx, hy, hxy⟩ := hs
    exact ⟨x, y, hx.1, hy.1, hxy⟩
  | glue => exact Or.inl hs

theorem chain_spreads {O O' : Obj n} {l : List (Option (Fin n))} (h : Chain O O' l) (k : Fin n)
    (hs : Spreads O' k) : Spreads O k ∨ some k ∈ l := by
  induction h with
  | nil => exact Or.inl hs
  | cons hstep _ ih =>
    rcases ih hs with h1 | h1
    · rcases step_spreads hstep k h1 with h2 | h2
      · exact Or.inl h2
      · exact Or.inr (by rw [h2]; simp)
    · exact Or.inr (List.mem_cons_of_mem _ h1)

theorem single_not_spreads (c : Pt n) (k : Fin n) : ¬ Spreads (single c) k := by
  rintro ⟨x, y, hx, hy, hxy⟩
  simp only [single] at hx hy; subst hx; subst hy; exact hxy rfl

/-- **Утверждение 19(а), нижняя оценка.** Если цепочка из ℓ действий строит O из одной клетки,
    то любые различные оси, вдоль которых O развёрнут, — их не больше ℓ. -/
theorem axes_le_length {c : Pt n} {O : Obj n} {l : List (Option (Fin n))}
    (h : Chain (single c) O l) (L : List (Fin n)) (hL : L.Nodup) (hsp : ∀ k ∈ L, Spreads O k) :
    L.length ≤ l.length := by
  have hsub : ∀ x ∈ L.map some, x ∈ l := by
    intro x hx
    obtain ⟨k, hk, rfl⟩ := List.mem_map.1 hx
    rcases chain_spreads h k (hsp k hk) with h1 | h1
    · exact absurd h1 (single_not_spreads c k)
    · exact h1
  have hnd : (L.map some).Nodup :=
    nodup_map_of_inj hL (fun a _ b _ hab => Option.some.inj hab)
  have := nodup_length_le_of_subset hnd hsub
  simpa using this

/-! ## σ: прообразы (потеря σ ровно |Z| бит; Утверждения 15(а), 35) -/

/-- σ_Z(O') = σ_Z(O) тогда и только тогда, когда O' совпадает с O вне зоны:
    содержимое зоны может быть любым. -/
theorem sigma_preimage (O O' Z : Obj n) :
    (∀ x, sigma O' Z x ↔ sigma O Z x) ↔ (∀ x, ¬ Z x → (O' x ↔ O x)) := by
  constructor
  · intro h x hz
    have := h x; simp only [sigma] at this
    constructor
    · intro h1; exact (this.1 ⟨h1, hz⟩).1
    · intro h1; exact (this.2 ⟨h1, hz⟩).1
  · intro h x
    simp only [sigma]
    constructor
    · rintro ⟨h1, hz⟩; exact ⟨(h x hz).1 h1, hz⟩
    · rintro ⟨h1, hz⟩; exact ⟨(h x hz).2 h1, hz⟩

/-! ## Лемма к Утверждению 14 (структурная часть): сжатию всё равно, сколько клеток в блоке -/

/-- Если O' получен из O удалением части клеток группы (вне зоны всё то же),
    и каждый непустой блок остался непустым, то сжатие даёт тот же результат. -/
theorem shrink_same_of_blocks (O O' Z : Obj n) (i : Fin n) (s : Int) (f : Nat) (a : Int)
    (hout : ∀ x, ¬ Z x → (O' x ↔ O x)) (hsub : ∀ x, O' x → O x)
    (hblk : ∀ c, O c → Z c → ∃ c', O' c' ∧ Z c' ∧ shrinkCell i s f a c' = shrinkCell i s f a c) :
    ∀ x, shrink O' Z i s f a x ↔ shrink O Z i s f a x := by
  intro x; simp only [shrink]
  constructor
  · rintro (⟨h1, hz⟩ | ⟨c, hc, hz, rfl⟩)
    · exact Or.inl ⟨(hout x hz).1 h1, hz⟩
    · exact Or.inr ⟨c, hsub c hc, hz, rfl⟩
  · rintro (⟨h1, hz⟩ | ⟨c, hc, hz, rfl⟩)
    · exact Or.inl ⟨(hout x hz).2 h1, hz⟩
    · obtain ⟨c', hc', hz', he⟩ := hblk c hc hz
      exact Or.inr ⟨c', hc', hz', he.symm⟩

/-- Закреплённая сторона сохраняется, если оставить клетку e, на которой достигается минимум. -/
theorem anchor_of_subset (O O' Z : Obj n) (i : Fin n) (s a : Int) (h : Anchor O Z i s a)
    (hsub : ∀ x, O' x → O x) (e : Pt n) (he : O' e) (hez : Z e) (hea : s * e i = a) :
    Anchor O' Z i s a :=
  ⟨⟨e, he, hez, hea⟩, fun c hc hz => h.2 c (hsub c hc) hz⟩

/-- Слияние при сжатии происходит ровно внутри блока (тот же ряд и то же ⌊t/f⌋). -/
theorem shrinkCell_eq_iff (i : Fin n) (s : Int) (hs : Dir s) (f : Nat) (a : Int) (c d : Pt n) :
    shrinkCell i s f a c = shrinkCell i s f a d ↔
      (∀ k, k ≠ i → c k = d k) ∧ (s * c i - a) / f = (s * d i - a) / f := by
  constructor
  · intro h
    refine ⟨fun k hk => ?_, ?_⟩
    · have := congrFun h k; simpa [shrinkCell, upd, hk] using this
    · have := congrFun h i
      simp only [shrinkCell, upd_same] at this
      rcases hs with rfl | rfl <;> omega
  · rintro ⟨h1, h2⟩
    funext k
    by_cases hk : k = i
    · subst hk; simp [shrinkCell, h2]
    · simp [shrinkCell, upd, hk, h1 k hk]

/-! ## Утверждения 13, 15(б): рост на одну клетку без потерь -/

/-- Позиция при растяжении одной клетки вдвое от неё самой. -/
theorem pos_two (s : Int) (hs : Dir s) (v : Int) (j : Nat) :
    s * (s * v + ((2 : Nat) : Int) * (s * v - s * v) + (j : Int)) = v + s * j := by
  rcases hs with rfl | rfl <;> omega

/-- Растяжение одной клетки c вдвое в сторону s: появляется ровно соседняя клетка c + s·e_i. -/
theorem grow_one (O : Obj n) (c : Pt n) (i : Fin n) (s : Int) (hs : Dir s) (hc : O c) :
    ∀ x, stretch O (single c) i s 2 (s * c i) x ↔ (O x ∨ x = upd c i (c i + s)) := by
  intro x
  simp only [stretch, single]
  constructor
  · rintro (⟨h1, _⟩ | ⟨c', _, rfl, j, hj, rfl⟩)
    · exact Or.inl h1
    · rw [pos_two s hs]
      have : j = 0 ∨ j = 1 := by omega
      rcases this with rfl | rfl
      · left; simpa [upd_self] using hc
      · right; simp
  · rintro (h1 | rfl)
    · by_cases hx : x = c
      · refine Or.inr ⟨c, hc, rfl, 0, by omega, ?_⟩
        rw [pos_two s hs]; simpa [upd_self] using hx
      · exact Or.inl ⟨h1, hx⟩
    · refine Or.inr ⟨c, hc, rfl, 1, by omega, ?_⟩
      rw [pos_two s hs]; simp

/-! ## Точность переборов на коробке: растяжение не сужает рамку объекта -/

/-- Каждая клетка O по каждой оси лежит между двумя клетками результата растяжения:
    рамка (наименьший брусок) при растяжении не уменьшается. Поэтому если итоговая фигура
    лежит в коробке, в той же коробке лежат все промежуточные фигуры цепочки растяжений. -/
theorem stretch_frame (O Z : Obj n) (i : Fin n) (s : Int) (hs : Dir s) (f : Nat) (hf : 2 ≤ f)
    (a : Int) (ha : Anchor O Z i s a) :
    ∀ y, O y → ∀ k, ∃ x x', stretch O Z i s f a x ∧ stretch O Z i s f a x' ∧ x k ≤ y k ∧ y k ≤ x' k := by
  intro y hy k
  by_cases hz : Z y
  · -- образ клетки y при j = 0
    have himg : stretch O Z i s f a (upd y i (s * (a + f * (s * y i - a) + 0))) :=
      Or.inr ⟨y, hy, hz, 0, by omega, rfl⟩
    by_cases hk : k = i
    · subst hk
      obtain ⟨⟨e, he, hez, hea⟩, hmin⟩ := ha
      have hey : a ≤ s * y k := hmin y hy hz
      have himge : stretch O Z k s f a (upd e k (s * (a + f * (s * e k - a) + ((0 : Nat) : Int)))) :=
        Or.inr ⟨e, he, hez, 0, by omega, rfl⟩
      have h0 : s * e k - a = 0 := by omega
      rw [h0, Int.mul_zero] at himge
      have ht : 0 ≤ s * y k - a := by omega
      have hft : s * y k - a ≤ (f : Int) * (s * y k - a) := by
        have h1 : (1 : Int) * (s * y k - a) ≤ (f : Int) * (s * y k - a) :=
          Int.mul_le_mul_of_nonneg_right (by omega) ht
        simpa using h1
      rcases hs with rfl | rfl
      · refine ⟨_, _, himge, himg, ?_, ?_⟩ <;> simp only [upd_same] <;> omega
      · refine ⟨_, _, himg, himge, ?_, ?_⟩ <;> simp only [upd_same] <;> omega
    · exact ⟨_, _, himg, himg, by simp [upd_other y _ hk], by simp [upd_other y _ hk]⟩
  · exact ⟨y, y, Or.inl ⟨hy, hz⟩, Or.inl ⟨hy, hz⟩, Int.le_refl _, Int.le_refl _⟩

/-! ## Утверждение 24 (ключевой шаг сведения): множители бесквадратной высоты взаимно просты -/

/-- n свободно от квадратов: ни один квадрат d², d > 1, его не делит. -/
def SqFree (h : Nat) : Prop := ∀ d, d * d ∣ h → d = 1

theorem sqfree_dvd {h m : Nat} (hs : SqFree h) (hm : m ∣ h) : SqFree m :=
  fun d hd => hs d (Nat.dvd_trans hd hm)

/-- Если m₁·m₂ свободно от квадратов, у m₁ и m₂ нет общего делителя больше 1:
    множества простых делителей частей разложения не пересекаются (нормальный базис). -/
theorem sqfree_parts_disjoint {m₁ m₂ : Nat} (hs : SqFree (m₁ * m₂)) :
    ∀ p, p ∣ m₁ → p ∣ m₂ → p = 1 :=
  fun p h1 h2 => hs p (Nat.mul_dvd_mul h1 h2)

/-! ## 1.7(в), 1.13: растяжение не теряет информации -/

theorem pos_cancel {s : Int} (hs : Dir s) {u v : Int} (h : s * u = s * v) : u = v := by
  rcases hs with rfl | rfl <;> omega

/-- Половина «без потерь»: каждая клетка группы O восстанавливается по результату. -/
theorem stretch_lossless_half (O O' Z : Obj n) (i : Fin n) (s : Int) (hs : Dir s) (f : Nat)
    (hf : 2 ≤ f) (a : Int)
    (hout : ∀ x, ¬ Z x → (O' x ↔ O x)) (hP3 : P3 O Z i s f a)
    (heq : ∀ x, stretch O Z i s f a x ↔ stretch O' Z i s f a x) :
    ∀ c, O c → Z c → O' c := by
  intro c hc hz
  have hx : stretch O Z i s f a (upd c i (s * (a + f * (s * c i - a) + ((0 : Nat) : Int)))) :=
    Or.inr ⟨c, hc, hz, 0, by omega, rfl⟩
  rcases (heq _).1 hx with ⟨h1, h2⟩ | ⟨c', hc', hz', j', hj', he⟩
  · exact absurd ⟨c, hc, hz, 0, by omega, rfl⟩ (hP3 _ ((hout _ h2).1 h1) h2)
  · -- те же остальные координаты и f·t + 0 = f·t' + j' ⇒ c = c'
    have hpos := congrFun he i
    simp only [upd_same] at hpos
    have hpos' := pos_cancel hs hpos
    have hlin : (f : Int) * (s * c i - a) + ((0 : Nat) : Int) = f * (s * c' i - a) + (j' : Int) := by
      omega
    obtain ⟨ht, _⟩ := Setka.div_unique (by omega) hj' hlin
    have hci : c i = c' i := pos_cancel hs (by omega)
    have hcc : c = c' := by
      funext k
      by_cases hk : k = i
      · subst hk; exact hci
      · have := congrFun he k; simpa [upd_other _ _ hk] using this
    exact hcc ▸ hc'

/-- **Растяжение без потерь.** Если два содержимых зоны (вне зоны всё одинаково) при одних и тех же
    параметрах и П3 дают один и тот же результат, то они совпадают: прообраз один, потеря 0 бит. -/
theorem stretch_lossless (O O' Z : Obj n) (i : Fin n) (s : Int) (hs : Dir s) (f : Nat) (hf : 2 ≤ f)
    (a : Int) (hout : ∀ x, ¬ Z x → (O' x ↔ O x)) (hP3 : P3 O Z i s f a) (hP3' : P3 O' Z i s f a)
    (heq : ∀ x, stretch O Z i s f a x ↔ stretch O' Z i s f a x) :
    ∀ x, O x ↔ O' x := by
  intro x
  by_cases hz : Z x
  · exact ⟨fun h => stretch_lossless_half O O' Z i s hs f hf a hout hP3 heq x h hz,
      fun h => stretch_lossless_half O' O Z i s hs f hf a (fun y hy => (hout y hy).symm) hP3'
        (fun y => (heq y).symm) x h hz⟩
  · exact (hout x hz).symm

end Setka.Core
