/-! Утверждение 28: поворот на 90° вокруг точки решётки. -/
structure Cell where
  x : Int
  y : Int
deriving DecidableEq, Repr

/-- ρ(c) = (p₁ − (c₂ − p₂) − 1, p₂ + (c₁ − p₁)) -/
def rot (p : Cell) (c : Cell) : Cell := ⟨p.x - (c.y - p.y) - 1, p.y + (c.x - p.x)⟩

/-- обратный поворот -/
def rotInv (p : Cell) (c : Cell) : Cell := ⟨p.x + (c.y - p.y), p.y - (c.x - p.x) - 1⟩

theorem rotInv_rot (p c : Cell) : rotInv p (rot p c) = c := by
  cases c; simp [rot, rotInv]; constructor <;> omega
theorem rot_rotInv (p c : Cell) : rot p (rotInv p c) = c := by
  cases c; simp [rot, rotInv]; constructor <;> omega
/-- поворот обратим: разные клетки не сливаются (потеря 0, число клеток то же) -/
theorem rot_injective (p : Cell) {a b : Cell} (h : rot p a = rot p b) : a = b := by
  have := congrArg (rotInv p) h; simpa [rotInv_rot] using this
/-- четыре поворота = тождество -/
theorem rot4 (p c : Cell) : rot p (rot p (rot p (rot p c))) = c := by
  cases c; simp [rot]; constructor <;> omega
/-- соседи по стороне остаются соседями по стороне (склейки и трещины сохраняются) -/
def l1 (a b : Cell) : Int := (if a.x ≥ b.x then a.x - b.x else b.x - a.x) + (if a.y ≥ b.y then a.y - b.y else b.y - a.y)
theorem rot_l1 (p a b : Cell) : l1 (rot p a) (rot p b) = l1 a b := by
  cases a; cases b; simp only [rot, l1]; (repeat' split) <;> omega
