import numpy as np
from nicegui import ui, app

# ─────────────────────────────────────────────────────────────
#  Game Logic
# ─────────────────────────────────────────────────────────────
def winner_chk(b):
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return 'X'
    elif -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return 'O'
    elif np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return 'X'
    elif np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return 'O'
    elif 0 not in b:
        return 'Draw'
    return None

# ─────────────────────────────────────────────────────────────
#  Global State
# ─────────────────────────────────────────────────────────────
state = {
    "board":    np.zeros((3, 3), dtype=int),
    "current":  1,        # 1 = X,  -1 = O
    "p1":       "Player X",
    "p2":       "Player O",
    "p1_score": 0,
    "p2_score": 0,
    "draw_score": 0,
    "game_over": False,
    "phase":    "setup",  # "setup" | "game"
}

cell_buttons: list[list] = [[None]*3 for _ in range(3)]

# ─────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────
def current_player_name():
    return state["p1"] if state["current"] == 1 else state["p2"]

def current_symbol():
    return "X" if state["current"] == 1 else "O"

def reset_board():
    state["board"]    = np.zeros((3, 3), dtype=int)
    state["current"]  = 1
    state["game_over"] = False
    for r in range(3):
        for c in range(3):
            btn = cell_buttons[r][c]
            if btn:
                btn.text  = ""
                btn.props("flat")
                btn.classes(
                    remove="text-x-color text-o-color bg-x-glow bg-o-glow cell-won cell-filled",
                    add="",
                )
                btn.enable()

# ─────────────────────────────────────────────────────────────
#  UI Refs (filled during build)
# ─────────────────────────────────────────────────────────────
refs = {}

# ─────────────────────────────────────────────────────────────
#  Cell Click
# ─────────────────────────────────────────────────────────────
def on_cell_click(r, c):
    if state["game_over"]:
        return
    board = state["board"]
    if board[r, c] != 0:
        ui.notify("Cell already taken!", type="warning", position="top")
        return

    board[r, c] = state["current"]

    btn = cell_buttons[r][c]
    sym = current_symbol()
    btn.text = sym

    if sym == "X":
        btn.classes(add="text-x-color cell-filled")
    else:
        btn.classes(add="text-o-color cell-filled")

    result = winner_chk(board)
    if result is not None:
        state["game_over"] = True
        if result == "Draw":
            state["draw_score"] += 1
            refs["status"].set_text("It's a Draw!")
            refs["status"].classes(remove="status-x status-o", add="status-draw")
            refs["draw_score_label"].set_text(str(state["draw_score"]))
            ui.notify("It's a Draw!", type="info", position="top")
        elif result == "X":
            state["p1_score"] += 1
            refs["status"].set_text(f"{state['p1']} Wins!")
            refs["status"].classes(remove="status-o status-draw", add="status-x")
            refs["p1_score_label"].set_text(str(state["p1_score"]))
            ui.notify(f"{state['p1']} wins!", type="positive", position="top")
        else:
            state["p2_score"] += 1
            refs["status"].set_text(f"{state['p2']} Wins!")
            refs["status"].classes(remove="status-x status-draw", add="status-o")
            refs["p2_score_label"].set_text(str(state["p2_score"]))
            ui.notify(f"{state['p2']} wins!", type="positive", position="top")

        for row in cell_buttons:
            for btn in row:
                if btn:
                    btn.disable()
        refs["play_again_btn"].set_visibility(True)
        return

    state["current"] = -1 if state["current"] == 1 else 1
    sym2  = current_symbol()
    name2 = current_player_name()
    refs["status"].set_text(f"{name2}'s Turn  ({sym2})")
    refs["status"].classes(
        remove="status-x status-o status-draw",
        add="status-x" if sym2 == "X" else "status-o",
    )


# ─────────────────────────────────────────────────────────────
#  Page
# ─────────────────────────────────────────────────────────────
@ui.page("/")
def index():
    ui.add_head_html("""
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
        background: #050816;
        font-family: 'Outfit', sans-serif;
        min-height: 100vh;
        overflow-x: hidden;
    }
    body::before {
        content: '';
        position: fixed;
        inset: 0;
        background:
            radial-gradient(ellipse 80% 50% at 20% 20%, rgba(99,102,241,.18) 0%, transparent 60%),
            radial-gradient(ellipse 60% 60% at 80% 80%, rgba(236,72,153,.14) 0%, transparent 60%),
            radial-gradient(ellipse 50% 40% at 50% 50%, rgba(16,185,129,.08) 0%, transparent 70%);
        pointer-events: none;
        z-index: 0;
    }
    body::after {
        content: '';
        position: fixed;
        inset: 0;
        background-image: radial-gradient(rgba(255,255,255,.04) 1px, transparent 1px);
        background-size: 32px 32px;
        pointer-events: none;
        z-index: 0;
    }
    .q-page { background: transparent !important; }

    .glass-card {
        background: rgba(255,255,255,0.04);
        backdrop-filter: blur(24px) saturate(180%);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 24px;
        box-shadow: 0 8px 32px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.06);
    }
    .hero-title {
        font-size: clamp(2.2rem, 5vw, 3.6rem);
        font-weight: 900;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #818cf8 0%, #c084fc 40%, #f472b6 80%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.1;
        text-align: center;
    }
    .hero-sub {
        color: rgba(255,255,255,.45);
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 4px;
        text-transform: uppercase;
        text-align: center;
    }
    .setup-label {
        color: rgba(255,255,255,.6);
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    .q-field__control {
        background: rgba(255,255,255,.05) !important;
        border-radius: 12px !important;
    }
    .q-field__native { color: white !important; font-family: 'Outfit', sans-serif !important; }
    .start-btn {
        width: 100%;
        height: 56px;
        border-radius: 14px !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%) !important;
        border: none !important;
        box-shadow: 0 0 32px rgba(139,92,246,.45), 0 4px 16px rgba(0,0,0,.4) !important;
        transition: transform .15s, box-shadow .15s !important;
        color: white !important;
    }
    .start-btn:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 0 48px rgba(139,92,246,.65), 0 8px 24px rgba(0,0,0,.5) !important;
    }
    .score-card {
        border-radius: 18px;
        padding: 18px 28px;
        text-align: center;
        min-width: 130px;
    }
    .score-card-x   { background: linear-gradient(135deg,rgba(99,102,241,.25),rgba(99,102,241,.08)); border: 1px solid rgba(99,102,241,.4); }
    .score-card-o   { background: linear-gradient(135deg,rgba(236,72,153,.25),rgba(236,72,153,.08)); border: 1px solid rgba(236,72,153,.4); }
    .score-card-draw{ background: linear-gradient(135deg,rgba(16,185,129,.2),rgba(16,185,129,.06));  border: 1px solid rgba(16,185,129,.35);}
    .score-number   { font-size: 2.6rem; font-weight: 900; line-height: 1; }
    .score-number-x { color: #818cf8; }
    .score-number-o { color: #f472b6; }
    .score-number-draw { color: #34d399; }
    .score-name     { font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-top: 4px; }
    .score-name-x   { color: #818cf8; opacity:.7; }
    .score-name-o   { color: #f472b6; opacity:.7; }
    .score-name-draw{ color: #34d399; opacity:.7; }

    .status-bar {
        font-size: 1.15rem;
        font-weight: 700;
        padding: 14px 32px;
        border-radius: 999px;
        text-align: center;
        letter-spacing: .5px;
        transition: all .35s ease;
        width: 100%;
    }
    .status-x {
        background: linear-gradient(90deg,rgba(99,102,241,.3),rgba(139,92,246,.2));
        border: 1.5px solid rgba(99,102,241,.5);
        color: #a5b4fc;
        box-shadow: 0 0 28px rgba(99,102,241,.3);
    }
    .status-o {
        background: linear-gradient(90deg,rgba(236,72,153,.3),rgba(244,63,94,.2));
        border: 1.5px solid rgba(236,72,153,.5);
        color: #f9a8d4;
        box-shadow: 0 0 28px rgba(236,72,153,.3);
    }
    .status-draw {
        background: linear-gradient(90deg,rgba(16,185,129,.25),rgba(6,182,212,.2));
        border: 1.5px solid rgba(16,185,129,.5);
        color: #6ee7b7;
        box-shadow: 0 0 28px rgba(16,185,129,.25);
    }

    .board-wrapper {
        padding: 20px;
        background: rgba(255,255,255,.03);
        border: 1px solid rgba(255,255,255,.07);
        border-radius: 24px;
        box-shadow: 0 0 60px rgba(139,92,246,.12), 0 16px 48px rgba(0,0,0,.5);
    }
    .cell-btn {
        width: 108px !important;
        height: 108px !important;
        border-radius: 18px !important;
        font-size: 2.8rem !important;
        font-weight: 900 !important;
        font-family: 'Outfit', sans-serif !important;
        background: rgba(255,255,255,.04) !important;
        border: 1.5px solid rgba(255,255,255,.1) !important;
        transition: all .18s cubic-bezier(.34,1.56,.64,1) !important;
        color: white !important;
        line-height: 1 !important;
    }
    .cell-btn:hover:not(:disabled) {
        background: rgba(255,255,255,.09) !important;
        border-color: rgba(139,92,246,.5) !important;
        transform: scale(1.07) !important;
        box-shadow: 0 0 24px rgba(139,92,246,.35) !important;
    }
    .cell-btn:disabled { cursor: not-allowed; opacity: 0.65 !important; }
    .text-x-color { color: #818cf8 !important; text-shadow: 0 0 24px rgba(99,102,241,.9); }
    .text-o-color { color: #f472b6 !important; text-shadow: 0 0 24px rgba(236,72,153,.9); }

    @keyframes pop {
        0%   { transform: scale(.4) rotate(-12deg); opacity:0; }
        70%  { transform: scale(1.18) rotate(4deg); }
        100% { transform: scale(1) rotate(0deg);   opacity:1; }
    }
    .cell-filled { animation: pop .28s cubic-bezier(.34,1.56,.64,1) forwards; }

    .action-btn {
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-family: 'Outfit', sans-serif !important;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 0.8rem !important;
        height: 48px;
        transition: transform .15s, box-shadow .15s !important;
    }
    .action-btn:hover { transform: translateY(-2px) !important; }
    .btn-play-again {
        background: linear-gradient(135deg,#6366f1,#a855f7) !important;
        color: white !important;
        box-shadow: 0 4px 20px rgba(99,102,241,.4) !important;
    }
    .btn-reset {
        background: rgba(255,255,255,.06) !important;
        color: rgba(255,255,255,.7) !important;
        border: 1px solid rgba(255,255,255,.15) !important;
    }
    .btn-home {
        background: linear-gradient(135deg,#ec4899,#f43f5e) !important;
        color: white !important;
        box-shadow: 0 4px 20px rgba(236,72,153,.35) !important;
    }
    .rule-item {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 10px 0;
        border-bottom: 1px solid rgba(255,255,255,.05);
        font-size: 0.87rem;
        color: rgba(255,255,255,.58);
    }
    .rule-num {
        background: linear-gradient(135deg,#6366f1,#a855f7);
        color: white;
        font-weight: 800;
        font-size: 0.7rem;
        width: 22px; height: 22px;
        border-radius: 6px;
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0;
        margin-top: 1px;
    }
    .vs-badge { font-size: 1rem; font-weight: 900; color: rgba(255,255,255,.18); }
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-thumb { background: rgba(255,255,255,.1); border-radius: 99px; }
    </style>
    """)

    with ui.column().classes("items-center justify-center min-h-screen w-full").style("z-index:1; padding:32px 16px; position:relative;"):

        # ── SETUP PANEL ─────────────────────────────────────────
        with ui.column().classes("glass-card w-full items-center").style("max-width:460px; padding:44px 36px; gap:0;") as setup_panel:
            refs["setup_panel"] = setup_panel

            ui.label("TIC  TAC  TOE").classes("hero-sub").style("margin-bottom:6px;")
            ui.label("Battle Zone").classes("hero-title").style("margin-bottom:8px;")
            ui.label("Enter player names to begin the match").style(
                "color:rgba(255,255,255,.38); font-size:0.88rem; margin-bottom:32px; text-align:center;"
            )

            with ui.column().classes("w-full").style("gap:18px;"):
                with ui.column().classes("w-full").style("gap:4px;"):
                    ui.label("PLAYER X").classes("setup-label").style("color:#818cf8;")
                    p1_input = ui.input(placeholder="Enter name for X…").classes("w-full").props(
                        'outlined dense color="indigo-4"'
                    )

                with ui.column().classes("w-full").style("gap:4px;"):
                    ui.label("PLAYER O").classes("setup-label").style("color:#f472b6;")
                    p2_input = ui.input(placeholder="Enter name for O…").classes("w-full").props(
                        'outlined dense color="pink-4"'
                    )

            ui.separator().style("margin:26px 0; border-color:rgba(255,255,255,.07); width:100%;")

            rules = [
                "A two-player game on a 3x3 board.",
                "Player X goes first, then players alternate.",
                "Place your symbol in any empty cell.",
                "3 in a row — horizontal, vertical, or diagonal — wins.",
                "All 9 cells filled with no winner = Draw.",
            ]
            for i, rule in enumerate(rules, 1):
                with ui.row().classes("rule-item w-full"):
                    ui.label(str(i)).classes("rule-num")
                    ui.label(rule)

            ui.separator().style("margin:26px 0; border-color:rgba(255,255,255,.07); width:100%;")

            def start_game():
                name1 = p1_input.value.strip() or "Player X"
                name2 = p2_input.value.strip() or "Player O"
                state["p1"] = name1
                state["p2"] = name2
                state["p1_score"] = 0
                state["p2_score"] = 0
                state["draw_score"] = 0
                state["phase"] = "game"
                reset_board()
                refs["p1_name_label"].set_text(name1)
                refs["p2_name_label"].set_text(name2)
                refs["p1_score_label"].set_text("0")
                refs["p2_score_label"].set_text("0")
                refs["draw_score_label"].set_text("0")
                refs["status"].set_text(f"  {name1}'s Turn  (X)")
                refs["status"].classes(remove="status-o status-draw", add="status-x")
                refs["play_again_btn"].set_visibility(False)
                setup_panel.set_visibility(False)
                game_panel.set_visibility(True)

            ui.button("START MATCH", on_click=start_game).classes("start-btn").style("margin-top:4px;")

        # ── GAME PANEL ──────────────────────────────────────────
        with ui.column().classes("w-full items-center").style("max-width:640px; gap:20px;") as game_panel:
            refs["game_panel"] = game_panel
            game_panel.set_visibility(False)

            # Header
            with ui.column().classes("w-full items-center").style("gap:2px;"):
                ui.label("TIC  TAC  TOE").classes("hero-sub").style("font-size:0.7rem;")
                ui.label("Battle Zone").classes("hero-title").style("font-size:2rem;")

            # Scoreboard
            with ui.row().classes("w-full items-center justify-center").style("gap:10px; flex-wrap:wrap;"):
                with ui.column().classes("score-card score-card-x items-center"):
                    refs["p1_score_label"] = ui.label("0").classes("score-number score-number-x")
                    refs["p1_name_label"]  = ui.label(state["p1"]).classes("score-name score-name-x")

                ui.label("VS").classes("vs-badge")

                with ui.column().classes("score-card score-card-draw items-center"):
                    refs["draw_score_label"] = ui.label("0").classes("score-number score-number-draw")
                    ui.label("Draws").classes("score-name score-name-draw")

                ui.label("VS").classes("vs-badge")

                with ui.column().classes("score-card score-card-o items-center"):
                    refs["p2_score_label"] = ui.label("0").classes("score-number score-number-o")
                    refs["p2_name_label"]  = ui.label(state["p2"]).classes("score-name score-name-o")

            # Status bar
            refs["status"] = ui.label(f"  {state['p1']}'s Turn  (X)").classes("status-bar status-x")

            # Game board
            with ui.column().classes("board-wrapper items-center").style("gap:12px; width:fit-content; margin:0 auto;"):
                for r in range(3):
                    with ui.row().style("gap:12px;"):
                        for c in range(3):
                            btn = ui.button("", on_click=lambda r=r, c=c: on_cell_click(r, c))
                            btn.classes("cell-btn")
                            btn.props("flat")
                            cell_buttons[r][c] = btn

            # Actions
            with ui.row().classes("w-full items-center justify-center").style("gap:12px; flex-wrap:wrap;"):
                refs["play_again_btn"] = ui.button(
                    "Play Again",
                    on_click=lambda: [
                        reset_board(),
                        refs["status"].set_text(f"  {state['p1']}'s Turn  (X)"),
                        refs["status"].classes(remove="status-o status-draw", add="status-x"),
                        refs["play_again_btn"].set_visibility(False),
                    ]
                ).classes("action-btn btn-play-again").style("padding:0 28px;")
                refs["play_again_btn"].set_visibility(False)

                def reset_scores():
                    state["p1_score"]   = 0
                    state["p2_score"]   = 0
                    state["draw_score"] = 0
                    refs["p1_score_label"].set_text("0")
                    refs["p2_score_label"].set_text("0")
                    refs["draw_score_label"].set_text("0")
                    reset_board()
                    refs["status"].set_text(f"  {state['p1']}'s Turn  (X)")
                    refs["status"].classes(remove="status-o status-draw", add="status-x")
                    refs["play_again_btn"].set_visibility(False)
                    ui.notify("Scores reset!", type="info", position="top")

                ui.button("Reset Scores", on_click=reset_scores).classes("action-btn btn-reset").style("padding:0 24px;")

                def go_home():
                    state["p1_score"]   = 0
                    state["p2_score"]   = 0
                    state["draw_score"] = 0
                    reset_board()
                    refs["play_again_btn"].set_visibility(False)
                    game_panel.set_visibility(False)
                    setup_panel.set_visibility(True)

                ui.button("Home", on_click=go_home).classes("action-btn btn-home").style("padding:0 28px;")


# ─────────────────────────────────────────────────────────────
ui.run(
    title="Tic Tac Toe — Battle Zone",
    favicon="",
    port=8080,
    reload=False,
    dark=True,
)
