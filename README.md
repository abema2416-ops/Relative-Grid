# Relative Grid

**English summary.** A system of actions on shapes made of lattice cells: stretch or compress part of a shape along one axis by an integer factor (α), delete cells (σ), glue or unglue touching cells (β). Each action has an information loss in bits; each shape has a number of actions needed to build it from one cell. Proven: every vanished cell costs at least 1 bit; cellular stretching equals the affine stretch exactly; in the plane stretching keeps the number of holes and one gluing changes it by at most 1; counting actions for reliefs is NP-hard. Conjecture (the *segment rule*) checked by exhaustive search on 4,835,965 shapes in 2D and 3D. Core formalized in Lean 4 (42 machine-checked theorems, no sorry).

**Main text (Russian, 11 pp.):** [основной-текст/osnova.pdf](основной-текст/osnova.pdf). **Read the paper:** [English](статья/setka-en.pdf) · [中文](статья/setka-zh.pdf) · [Русский](статья/setka.pdf). Author: Muhammad Zafarov. License: CC BY 4.0 (text), MIT (code). Questions, criticism and counterexamples are welcome — open an Issue.

---

# Относительная сетка

**Система операций над формами любой размерности.** Черновик, версия 1.18 (28 ноября 2026).

**Автор идеи и определений:** Зафаров Мухаммад.
Доказательства записаны с помощью ИИ-помощника (Claude).

## О чём это

Единый язык действий над объектами, разбитыми на ячейки сетки: растянуть или сжать (α), повернуть (α°),
уничтожить (σ), найти касания (γ), склеить и расклеить (β). Для каждого действия считается, сколько
информации (бит) оно теряет, и сколько действий нужно, чтобы построить форму.

## Что в репозитории

| Файл / папка | Что это |
|---|---|
| **`основной-текст/osnova.pdf`** | **Основной текст 2.1 (12 страниц): ядро, все доказанные теоремы, гипотезы, надстройки в приложении. Начинать с него.** |
| `Относительная сетка — черновик 1.18.txt` | Рабочий журнал: полный черновик со всеми проверками и историей версий |
| `Относительная сетка — ядро и аудит.txt` | Строгое определение ядра; таблица: чем подтверждено каждое утверждение (Lean, текст, известный факт, перебор); строгие доказательства |
| `статья/setka.pdf`, `статья/setka.tex` | Короткая статья в классическом виде (8 страниц): определения, теоремы с доказательствами, гипотезы, литература |
| `статья/setka-en.pdf` | Та же статья на английском |
| `статья/setka-zh.pdf` | Та же статья на китайском |
| `Относительная сетка — результаты счёта.txt` | Приложение: счёт на малых сетках |
| `рисунки/` | Рисунки 1–22 |
| `программы/` | Программы проверок (как запускать — раздел 12 теории) |
| `lean/` | Формальная запись ядра на Lean 4: 42 теоремы, без sorry, только стандартные аксиомы (файл `Setka/Core.lean` — строгая модель ядра; сборка: `lake build`, проверка аксиом: `lake env lean Check.lean`) |

## Специальная и общая система

- **Специальная** — только собственные правила и теоремы системы.
- **Общая** — специальная плюс подключённые формулы геометрии, топологии, теории узлов и других разделов
  (с указанием источников). Словарь понятий и список подключённых разделов — раздел 15 теории.

## Как дополнить

Система открыта для дополнений — см. [CONTRIBUTING.md](CONTRIBUTING.md).

## Лицензия

- Текст и рисунки — [CC BY 4.0](LICENSE): можно свободно копировать, изменять и использовать для любых целей,
  **обязательно указывая автора (Зафаров Мухаммад) и ссылку на этот репозиторий**.
- Программы и файлы Lean — [MIT](LICENSE-CODE).

## Как ссылаться

Зафаров Мухаммад. «Относительная сетка: система операций над формами любой размерности».
Черновик, версия 1.18, 28 ноября 2026. https://github.com/abema2416-ops/Relative-Grid
