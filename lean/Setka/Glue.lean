/-! Утверждение 16 (склейки и дыры на плоскости): проверяемые в Lean части доказательства. -/
namespace Setka

/-! ### Счёт вершин над точкой p: V(p) = k(p) − s(p) + [целиком склеенный квадрат 2×2].
Вокруг точки — 4 квадрата по кругу (0,1,2,3); сторона i разделяет квадраты i и i+1 (mod 4).
Число компонент считаем независимо — честным поиском достижимости. -/

def nxt (i : Fin 4) : Fin 4 := ⟨(i.val + 1) % 4, Nat.mod_lt _ (by decide)⟩
def prv (i : Fin 4) : Fin 4 := ⟨(i.val + 3) % 4, Nat.mod_lt _ (by decide)⟩

/-- допустимая конфигурация: склеить можно только стороны между двумя квадратами объекта -/
def valid (pres glue : Fin 4 → Bool) : Bool :=
  (List.finRange 4).all fun i => !glue i || (pres i && pres (nxt i))

/-- соседство в графе Γ(p) -/
def adj (glue : Fin 4 → Bool) (i j : Fin 4) : Bool :=
  (glue i && j == nxt i) || (glue j && i == nxt j)

/-- достижимость за ≤ n шагов -/
def reach (glue : Fin 4 → Bool) : Nat → Fin 4 → Fin 4 → Bool
  | 0, i, j => i == j
  | n + 1, i, j => reach glue n i j || (List.finRange 4).any fun m => reach glue n i m && adj glue m j

/-- число компонент: квадраты, у которых нет достижимого квадрата с меньшим номером -/
def comps (pres glue : Fin 4 → Bool) : Nat :=
  ((List.finRange 4).filter fun i => pres i &&
    (List.finRange 4).all fun j => !(j.val < i.val && reach glue 4 j i)).length

def kk (pres : Fin 4 → Bool) : Nat := ((List.finRange 4).filter (fun i => pres i)).length
def ss (glue : Fin 4 → Bool) : Nat := ((List.finRange 4).filter (fun i => glue i)).length

/-- конфигурация по маске (4 бита) -/
def bits (m : Nat) (i : Fin 4) : Bool := m.testBit i.val

/-- все 16 × 16 конфигураций: формула для V(p) верна -/
theorem vertex_count : ∀ a < 16, ∀ b < 16, valid (bits a) (bits b) = true →
    comps (bits a) (bits b) = kk (bits a) - ss (bits b) +
      (if kk (bits a) = 4 ∧ ss (bits b) = 4 then 1 else 0) := by
  decide

/-- пункт (в): если три стыка квадрата 2×2 уже склеены, то клетки по обе стороны четвёртого
    уже в одном куске (новая склейка между разными кусками не создаёт целиком склеенный квадрат) -/
theorem three_seams_connect : ∀ b < 16, ∀ i : Fin 4,
    (List.finRange 4).all (fun j => j == i || bits b j) = true → reach (bits b) 4 i (nxt i) = true := by
  decide

/-! ### Подсчёт и формула (а). -/
theorem euler (O S q : Int) :
    let V := 4 * O - 2 * S + q
    let E := 4 * O - S
    let F := O
    V - E + F = O - S + q := by intro V E F; simp only [V, E, F]; omega

/-- d = b₀ − χ, где χ = |O| − |S| + q -/
def dd (b0 O S q : Int) : Int := b0 - O + S - q

/-- (б): растяжение группы из g клеток в f раз с r перпендикулярными склейками внутри группы -/
theorem stretch_keeps_d (b0 O S q g r f : Int) :
    dd b0 (O + (f - 1) * g) (S + (f - 1) * g + (f - 1) * r) (q + (f - 1) * r) = dd b0 O S q := by
  simp only [dd]; omega

/-- (в): склейка внутри куска (q растёт на δ ∈ {0,1,2}) — Δd ∈ {1, 0, −1};
    склейка двух кусков (кусков на 1 меньше, q не меняется) — Δd = 0 -/
theorem glue_inside (b0 O S q δ : Int) (h : 0 ≤ δ ∧ δ ≤ 2) :
    dd b0 O (S + 1) (q + δ) - dd b0 O S q = 1 - δ ∧ -1 ≤ 1 - δ ∧ 1 - δ ≤ 1 := by
  simp only [dd]; omega
theorem glue_join (b0 O S q : Int) : dd (b0 - 1) O (S + 1) q - dd b0 O S q = 0 := by
  simp only [dd]; omega

/-- (г): шаги построения — растяжения (Δd = 0) и склейки (Δd ≤ 1). Начав с d = 0,
    получаем d ≤ число склеек. -/
inductive Step | stretch | glue (δ : Int)

def run : Int → List Step → Int
  | d, [] => d
  | d, Step.stretch :: rest => run d rest
  | d, Step.glue δ :: rest => run (d + δ) rest

def glues : List Step → Nat
  | [] => 0
  | Step.stretch :: rest => glues rest
  | Step.glue _ :: rest => glues rest + 1

theorem d_le_glues : ∀ (steps : List Step) (d : Int),
    (∀ δ, Step.glue δ ∈ steps → δ ≤ 1) → run d steps ≤ d + glues steps
  | [], d, _ => by simp [run, glues]
  | Step.stretch :: rest, d, h => by
    simp only [run, glues]; exact d_le_glues rest d (fun δ hδ => h δ (by simp [hδ]))
  | Step.glue δ :: rest, d, h => by
    simp only [run, glues]
    have := d_le_glues rest (d + δ) (fun δ' hδ => h δ' (by simp [hδ]))
    have := h δ (by simp); omega

end Setka
