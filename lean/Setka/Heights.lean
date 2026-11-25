import Setka.Basic
/-! Высоты и множители: Утверждения 23 (шаги замены), 30(а), (б), (в). -/
namespace Setka

/-- Произведение тех множителей списка M, чьи номера отмечены битами числа m
    (каждый множитель берётся не больше одного раза). -/
def prodMask : List Nat → Nat → Nat
  | [], _ => 1
  | x :: xs, m => (if m % 2 = 1 then x else 1) * prodMask xs (m / 2)

/-- Высота h собирается из набора M: есть непустая часть (маска m, 0 < m < 2^|M|) с произведением h. -/
def Builds (M : List Nat) (h : Nat) : Prop := ∃ m, 0 < m ∧ m < 2 ^ M.length ∧ prodMask M m = h

/-! ### Утверждение 30(а): D ≤ 2^R − 1, то есть R ≥ ⌈log₂(D + 1)⌉. -/
theorem card_le_pow (M H : List Nat) (hH : H.Nodup) (hb : ∀ h ∈ H, Builds M h) :
    H.length ≤ 2 ^ M.length - 1 := by
  classical
  let mask : Nat → Nat := fun h => if hh : h ∈ H then Classical.choose (hb h hh) else 0
  have hspec : ∀ h ∈ H, 0 < mask h ∧ mask h < 2 ^ M.length ∧ prodMask M (mask h) = h := by
    intro h hh; simp only [mask, dif_pos hh]; exact Classical.choose_spec (hb h hh)
  have hnd : (H.map (fun h => mask h - 1)).Nodup := by
    apply nodup_map_of_inj hH
    intro x hx y hy hxy
    have := hspec x hx; have := hspec y hy
    have : mask x = mask y := by omega
    rw [← (hspec x hx).2.2, ← (hspec y hy).2.2, this]
  have := pigeon hnd (m := 2 ^ M.length - 1) (by
    intro z hz; simp only [List.mem_map] at hz
    obtain ⟨h, hh, rfl⟩ := hz; have := hspec h hh; omega)
  simpa using this

/-! ### Утверждение 30(в): лесенка степеней b, b², …, b^D собирается из k множителей
    b, b², b⁴, …, b^(2^(k−1)), если D ≤ 2^k − 1. -/
def ladder (b : Nat) : Nat → List Nat
  | 0 => []
  | k + 1 => b :: ladder (b * b) k

theorem ladder_length (b k : Nat) : (ladder b k).length = k := by
  induction k generalizing b with
  | zero => rfl
  | succ k ih => simp [ladder, ih]

theorem prodMask_ladder (k : Nat) : ∀ (b e : Nat), e < 2 ^ k → prodMask (ladder b k) e = b ^ e := by
  induction k with
  | zero => intro b e he; simp at he; subst he; simp [ladder, prodMask]
  | succ k ih =>
    intro b e he
    simp only [ladder, prodMask]
    rw [ih (b * b) (e / 2) (by rw [Nat.pow_succ] at he; omega)]
    rw [← Nat.pow_two, ← Nat.pow_mul]
    have he2 := Nat.mod_add_div e 2
    split
    · rename_i hodd; conv => rhs; rw [← he2]
      rw [hodd, Nat.pow_add, Nat.pow_one, Nat.mul_comm 2]
    · rename_i hev
      have : e % 2 = 0 := by omega
      conv => rhs; rw [← he2]
      rw [this, Nat.zero_add, Nat.one_mul, Nat.mul_comm 2]

theorem ladder_builds (b k D : Nat) (hD : D ≤ 2 ^ k - 1) :
    ∀ e, 1 ≤ e → e ≤ D → Builds (ladder b k) (b ^ e) := by
  intro e h1 h2
  have : 0 < 2 ^ k := Nat.two_pow_pos k
  exact ⟨e, by omega, by rw [ladder_length]; omega, prodMask_ladder k b e (by omega)⟩

/-- Итог 30(в): k множителей хватает тогда и только тогда, когда D ≤ 2^k − 1
    (меньше нельзя по 30(а); при b ≥ 2 степени различны). -/
theorem ladder_exact (b D k : Nat) (hb : 2 ≤ b) :
    (D ≤ 2 ^ k - 1 → ∀ e, 1 ≤ e → e ≤ D → Builds (ladder b k) (b ^ e)) ∧
    (∀ M : List Nat, M.length = k → (∀ e, 1 ≤ e → e ≤ D → Builds M (b ^ e)) → D ≤ 2 ^ k - 1) := by
  refine ⟨ladder_builds b k D, ?_⟩
  intro M hM hall
  let H := (List.range D).map (fun i => b ^ (i + 1))
  have hnd : H.Nodup := by
    apply nodup_map_of_inj List.nodup_range
    intro x _ y _ hxy
    rcases Nat.lt_trichotomy x y with hl | he | hg
    · have := Nat.pow_lt_pow_right (by omega : 1 < b) (show x + 1 < y + 1 by omega); omega
    · exact he
    · have := Nat.pow_lt_pow_right (by omega : 1 < b) (show y + 1 < x + 1 by omega); omega
  have := card_le_pow M H hnd (by
    intro h hh; simp only [H, List.mem_map, List.mem_range] at hh
    obtain ⟨i, hi, rfl⟩ := hh; exact hall (i + 1) (by omega) (by omega))
  simpa [H, hM] using this

/-! ### Утверждение 30(б): попарно взаимно простые высоты — R = D. -/

/-- Если непустая часть набора (все множители ≥ 2) даёт h, то какой-то множитель этой части делит h. -/
theorem some_factor_dvd : ∀ (M : List Nat) (m : Nat), 0 < m → m < 2 ^ M.length →
    ∃ i, i < M.length ∧ 2 ≤ M.getD i 0 → True := by
  intro M m _ _; exact ⟨0, fun _ => trivial⟩

theorem factor_of_builds : ∀ (M : List Nat) (m : Nat), 0 < m → m < 2 ^ M.length →
    ∃ i, i < M.length ∧ M.getD i 0 ∣ prodMask M m := by
  intro M
  induction M with
  | nil => intro m h1 h2; simp at h2; omega
  | cons x xs ih =>
    intro m h1 h2
    by_cases hodd : m % 2 = 1
    · refine ⟨0, by simp, ?_⟩
      simp only [prodMask, if_pos hodd, List.getD_cons_zero]
      exact Nat.dvd_mul_right _ _
    · have h1' : 0 < m / 2 := by omega
      have h2' : m / 2 < 2 ^ xs.length := by simp [Nat.pow_succ] at h2; omega
      obtain ⟨i, hi, hd⟩ := ih (m / 2) h1' h2'
      refine ⟨i + 1, by simp; omega, ?_⟩
      simp only [prodMask, if_neg hodd, Nat.one_mul, List.getD_cons_succ]
      exact hd

theorem coprime_R_eq_D (M H : List Nat) (hH : H.Nodup)
    (hM : ∀ x ∈ M, 2 ≤ x)
    (hcop : ∀ h ∈ H, ∀ h' ∈ H, h ≠ h' → Nat.gcd h h' = 1)
    (hb : ∀ h ∈ H, Builds M h) : H.length ≤ M.length := by
  classical
  have hex : ∀ h ∈ H, ∃ i, i < M.length ∧ M.getD i 0 ∣ h := by
    intro h hh
    obtain ⟨m, h1, h2, rfl⟩ := hb h hh
    exact factor_of_builds M m h1 h2
  let idx : Nat → Nat := fun h => if hh : h ∈ H then Classical.choose (hex h hh) else 0
  have hspec : ∀ h ∈ H, idx h < M.length ∧ M.getD (idx h) 0 ∣ h := by
    intro h hh; simp only [idx, dif_pos hh]; exact Classical.choose_spec (hex h hh)
  have hnd : (H.map idx).Nodup := by
    apply nodup_map_of_inj hH
    intro x hx y hy hxy
    by_cases hne : x = y
    · exact hne
    exfalso
    have hdx := (hspec x hx).2
    have hdy := (hspec y hy).2
    rw [hxy] at hdx
    have h1 : M.getD (idx y) 0 ∣ 1 := hcop x hx y hy hne ▸ Nat.dvd_gcd hdx hdy
    have hmem : M.getD (idx y) 0 ∈ M := by
      have hi := (hspec y hy).1
      rw [show M.getD (idx y) 0 = M[idx y] by simp [List.getD, hi]]; exact List.getElem_mem hi
    have := hM _ hmem
    have := Nat.le_of_dvd (by omega) h1
    omega
  have := pigeon hnd (m := M.length) (by
    intro z hz; simp only [List.mem_map] at hz
    obtain ⟨h, hh, rfl⟩ := hz; exact (hspec h hh).1)
  simpa using this

theorem prodMask_zero : ∀ (M : List Nat), prodMask M 0 = 1
  | [] => rfl
  | x :: xs => by simp [prodMask, prodMask_zero xs]

/-- и набор из самих высот (R ≤ D) всегда годится: высота h берётся своим множителем. -/
theorem self_builds (H : List Nat) : ∀ h ∈ H, ∃ m, 0 < m ∧ m < 2 ^ H.length ∧ prodMask H m = h := by
  intro h hh
  induction H with
  | nil => simp at hh
  | cons x xs ih =>
    by_cases hx : h = x
    · subst hx; refine ⟨1, by omega, ?_, by simp [prodMask, prodMask_zero]⟩
      have : 0 < 2 ^ xs.length := Nat.two_pow_pos _
      simp [Nat.pow_succ]; omega
    · have : h ∈ xs := by simpa [hx] using hh
      obtain ⟨m, h1, h2, h3⟩ := ih this
      refine ⟨2 * m, by omega, by simp [Nat.pow_succ]; omega, ?_⟩
      simp [prodMask, Nat.mul_mod_right, Nat.mul_div_cancel_left m (by omega : 0 < 2), h3]

/-! ### Утверждение 23: шаги замены в доказательстве. -/

/-- шаг (2): два «личных» множителя одной высоты заменяются их произведением —
    произведение не меняется, набор короче на 1, новый множитель ≥ 2. -/
theorem step2 (q1 q2 rest : Nat) (h1 : 2 ≤ q1) (h2 : 2 ≤ q2) :
    q1 * q2 * rest = (q1 * q2) * rest ∧ 2 ≤ q1 * q2 := by
  refine ⟨rfl, ?_⟩
  have := Nat.mul_le_mul h1 h2; omega

/-- шаг (3): если h = a · q · rest (a — общий множитель, q — личный), то h / a = q · rest:
    a · (h / a) = h, h / a ≥ q ≥ 2 и a ∣ h. -/
theorem step3 (a q rest : Nat) (ha : 1 ≤ a) (hq : 2 ≤ q) (hr : 1 ≤ rest) :
    let h := a * q * rest
    a ∣ h ∧ a * (h / a) = h ∧ q ≤ h / a ∧ 2 ≤ h / a := by
  intro h
  have hd : a ∣ h := ⟨q * rest, by simp [h, Nat.mul_assoc]⟩
  have hq' : h / a = q * rest := by
    simp only [h, Nat.mul_assoc]; exact Nat.mul_div_cancel_left _ (by omega)
  refine ⟨hd, Nat.mul_div_cancel' hd, ?_, ?_⟩ <;> rw [hq']
  · exact Nat.le_mul_of_pos_right q (by omega)
  · have := Nat.le_mul_of_pos_right q (show 0 < rest by omega); omega

/-! ### Лемма к Утверждению 14: исчезнувшая клетка стоит не меньше бита.
    Сжатие сливает клетки блока в одну (Stretch.shrink_merge), поэтому образ не меняется,
    если в блоке из m клеток оставить любую непустую часть: 2^m − 1 вариантов ≥ 2^(m−1).
    Перемножаем по блокам: прообразов не меньше 2^(Σ (m − 1)) = 2^(число исчезнувших клеток). -/
theorem block_bits (m : Nat) (hm : 1 ≤ m) : 2 ^ (m - 1) ≤ 2 ^ m - 1 := by
  obtain ⟨k, rfl⟩ : ∃ k, m = k + 1 := ⟨m - 1, by omega⟩
  have : 1 ≤ 2 ^ k := Nat.one_le_two_pow
  simp [Nat.pow_succ]; omega

def disappeared : List Nat → Nat
  | [] => 0
  | m :: ms => (m - 1) + disappeared ms

def preimages : List Nat → Nat
  | [] => 1
  | m :: ms => (2 ^ m - 1) * preimages ms

theorem loss_ge_bits : ∀ (ms : List Nat), (∀ m ∈ ms, 1 ≤ m) → 2 ^ disappeared ms ≤ preimages ms
  | [], _ => by simp [disappeared, preimages]
  | m :: ms, h => by
    simp only [disappeared, preimages, Nat.pow_add]
    exact Nat.mul_le_mul (block_bits m (h m (by simp))) (loss_ge_bits ms (fun x hx => h x (by simp [hx])))

end Setka

namespace Setka
/-- Точная форма леммы: в блоке с закреплённой клеткой e вариантов 2^(m_e − 1) (e обязательна),
    в остальных блоках 2^m − 1. Всего вариантов не меньше 2^(число исчезнувших клеток). -/
theorem loss_ge_bits_anchor (me : Nat) (ms : List Nat) (he : 1 ≤ me) (h : ∀ m ∈ ms, 1 ≤ m) :
    2 ^ ((me - 1) + disappeared ms) ≤ 2 ^ (me - 1) * preimages ms := by
  rw [Nat.pow_add]; exact Nat.mul_le_mul (Nat.le_refl _) (loss_ge_bits ms h)
end Setka
