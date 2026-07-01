import json
import random
import string
import os
import webbrowser
from datetime import datetime
from pathlib import Path
from nicegui import ui, app

# Database Path
DB_PATH = Path(__file__).parent / "library.json"

# State variables for search filtering
state = {
    "book_search": "",
    "member_search": "",
    "selected_borrow_member_id": "",
    "selected_borrow_book_id": "",
    "selected_return_member_id": "",
    "selected_return_book_id": "",
}

# Load and Save operations
def load_data():
    if DB_PATH.exists():
        try:
            with open(DB_PATH, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
        except Exception as e:
            print(f"Error reading library.json: {e}")
    
    default_data = {"books": [], "members": []}
    save_data(default_data)
    return default_data

def save_data(data_to_save):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, indent=4, default=str)

# Load data into memory
data = load_data()

# Helper ID generator
def get_id(prefix='B'):
    random_id = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return f"{prefix}-{random_id}"

# Global UI refresher functions
def refresh_all():
    show_dashboard.refresh()
    show_books.refresh()
    show_members.refresh()
    show_transactions.refresh()

# Page logic functions
def add_book(title: str, author: str, copies: int):
    title = title.strip().lower()
    author = author.strip().lower()
    
    if not title or not author or copies <= 0:
        ui.notify("⚠️ Please enter valid Title, Author, and Positive Copies count.", type="warning", color="amber-500")
        return
    
    b = {
        "id": get_id('B'),
        "title": title,
        "author": author,
        "total_copies": copies,
        "available_copies": copies,
        "added_on": datetime.now().strftime("%d/%m/%Y,%I:%M:%S %p") 
    }
    data['books'].append(b)
    save_data(data)
    ui.notify(f"📚 Book '{title.title()}' added successfully!", type="positive", color="emerald-500")
    refresh_all()

def add_member(username: str, phone: str, email: str, borrow_immediately: bool = False):
    u_name = username.strip().lower().replace(" ", "")
    p_no = phone.strip()
    email = email.strip().lower()
    
    if not u_name or not p_no or not email:
        ui.notify("⚠️ Please enter valid Username, Phone, and Email.", type="warning", color="amber-500")
        return
    
    if any(m['username'] == u_name for m in data['members']):
        ui.notify("⚠️ Username already exists. Please choose another.", type="warning", color="rose-500")
        return
        
    m = {
        "id": get_id("M"),
        "username": u_name,
        "p_no": p_no,
        "email": email,
        "borrowed": [],
        "added_on": datetime.now().strftime("%d/%m/%Y,%I:%M:%S %p"),      
    }
    data['members'].append(m)
    save_data(data)
    ui.notify(f"👤 Member '{u_name}' added successfully!", type="positive", color="emerald-500")
    refresh_all()
    
    if borrow_immediately:
        # Switch tab to transactions and pre-select this member
        state['selected_borrow_member_id'] = m['id']
        ui.notify(f"Redirecting to borrow panel for ID: {m['id']}", color="cyan-500")
        tabs.value = 'transactions'

def borrow_book(member_id: str, book_id: str):
    member = next((m for m in data['members'] if m['id'] == member_id), None)
    if not member:
        # Prompt to add member
        ui.notify("❌ Member ID not found. Registration suggested.", color="rose-500")
        return
    
    book = next((b for b in data['books'] if b['id'] == book_id), None)
    if not book:
        ui.notify("❌ Book ID not found.", color="rose-500")
        return
        
    if book['available_copies'] <= 0:
        ui.notify("❌ Sorry, all available book copies are currently borrowed.", color="amber-500")
        return
        
    if any(b['book_id'] == book_id for b in member['borrowed']):
        ui.notify("⚠️ Member already borrowed this book.", color="amber-500")
        return
        
    be = {
        "book_id": book['id'],
        "title": book['title'],
        "borrow_on": datetime.now().strftime("%d/%m/%Y,%I:%M:%S %p")
    } 
    member['borrowed'].append(be)
    book['available_copies'] -= 1
    save_data(data)
    ui.notify(f"✅ Book '{book['title'].title()}' borrowed successfully!", color="cyan-500")
    refresh_all()

def return_book(member_id: str, book_id: str):
    member = next((m for m in data['members'] if m['id'] == member_id), None)
    if not member:
        ui.notify("❌ Member not found.", color="rose-500")
        return
        
    borrowed_item = next((b for b in member['borrowed'] if b['book_id'] == book_id), None)
    if not borrowed_item:
        ui.notify("❌ Member has not borrowed this book.", color="rose-500")
        return
        
    member['borrowed'].remove(borrowed_item)
    book = next((bk for bk in data['books'] if bk['id'] == book_id), None)
    if book:
        book['available_copies'] += 1
        
    save_data(data)
    ui.notify(f"✅ Book '{borrowed_item['title'].title()}' returned successfully!", color="emerald-500")
    refresh_all()

def delete_book(book_id: str):
    book = next((b for b in data['books'] if b['id'] == book_id), None)
    if not book:
        ui.notify("❌ Book not found.", color="rose-500")
        return
        
    borrowed = book['total_copies'] - book['available_copies']
    if borrowed > 0:
        ui.notify(f"❌ Cannot delete book: {borrowed} copies are still borrowed.", color="rose-500")
        return
        
    data['books'].remove(book)
    save_data(data)
    ui.notify("✅ Book deleted successfully.", color="emerald-500")
    refresh_all()

def delete_member(member_id: str):
    member = next((m for m in data['members'] if m['id'] == member_id), None)
    if not member:
        ui.notify("❌ Member not found.", color="rose-500")
        return
        
    if member['borrowed']:
        ui.notify("❌ Cannot delete member: please return all books first.", color="rose-500")
        return
        
    data['members'].remove(member)
    save_data(data)
    ui.notify("✅ Member deleted successfully.", color="emerald-500")
    refresh_all()

# UI Layout configuration
ui.add_head_html("""
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
* {
    font-family: 'Outfit', sans-serif !important;
}
body {
    background: radial-gradient(circle at 10% 20%, rgba(90, 18, 142, 0.15) 0%, transparent 45%),
                radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.12) 0%, transparent 45%),
                #070412 !important;
    color: #f8fafc;
    min-height: 100vh;
}
/* Custom premium glassmorphic panels */
.glass-panel {
    background: rgba(18, 12, 38, 0.45) !important;
    backdrop-filter: blur(25px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(25px) saturate(180%) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 24px !important;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4) !important;
}
/* Premium glass hover cards */
.glass-card-hover {
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
.glass-card-hover:hover {
    transform: translateY(-5px) scale(1.02) !important;
    background: rgba(26, 17, 56, 0.6) !important;
    border-color: rgba(6, 182, 212, 0.25) !important;
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5), 0 0 20px rgba(6, 182, 212, 0.1) !important;
}
/* Glowing buttons and accents */
.neon-glow-cyan {
    box-shadow: 0 0 25px rgba(6, 182, 212, 0.15) !important;
    border-color: rgba(6, 182, 212, 0.2) !important;
}
.neon-glow-purple {
    box-shadow: 0 0 25px rgba(168, 85, 247, 0.15) !important;
    border-color: rgba(168, 85, 247, 0.2) !important;
}
.neon-glow-pink {
    box-shadow: 0 0 25px rgba(236, 72, 153, 0.15) !important;
    border-color: rgba(236, 72, 153, 0.2) !important;
}
.neon-glow-rose {
    box-shadow: 0 0 25px rgba(244, 63, 94, 0.15) !important;
    border-color: rgba(244, 63, 94, 0.2) !important;
}
/* Premium input elements */
.q-field__control {
    background: rgba(5, 3, 12, 0.4) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 12px !important;
    transition: all 0.3s ease !important;
}
.q-field--focused .q-field__control {
    border-color: rgba(6, 182, 212, 0.4) !important;
    box-shadow: 0 0 15px rgba(6, 182, 212, 0.15) !important;
}
.q-field__label {
    color: rgba(148, 163, 184, 0.7) !important;
}
/* Premium Tabs styling */
.q-tabs {
    border-radius: 20px !important;
    padding: 6px !important;
}
.q-tab {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    margin: 4px 8px !important;
    border-radius: 16px !important;
    min-height: 52px !important;
    padding: 8px 20px !important;
    color: #94a3b8 !important;
    border: 1px solid transparent !important;
}
.q-tab:hover {
    background: rgba(255, 255, 255, 0.03) !important;
    color: #ffffff !important;
}
/* Dashboard Tab Active */
.q-tab[name="dashboard"].q-tab--active {
    color: #22d3ee !important;
    background: rgba(6, 182, 212, 0.08) !important;
    border: 1px solid rgba(6, 182, 212, 0.2) !important;
    box-shadow: 0 0 15px rgba(6, 182, 212, 0.15) !important;
}
/* Books Tab Active */
.q-tab[name="books"].q-tab--active {
    color: #c084fc !important;
    background: rgba(168, 85, 247, 0.08) !important;
    border: 1px solid rgba(168, 85, 247, 0.2) !important;
    box-shadow: 0 0 15px rgba(168, 85, 247, 0.15) !important;
}
/* Members Tab Active */
.q-tab[name="members"].q-tab--active {
    color: #f472b6 !important;
    background: rgba(236, 72, 153, 0.08) !important;
    border: 1px solid rgba(236, 72, 153, 0.2) !important;
    box-shadow: 0 0 15px rgba(236, 72, 153, 0.15) !important;
}
/* Transactions Tab Active */
.q-tab[name="transactions"].q-tab--active {
    color: #34d399 !important;
    background: rgba(52, 211, 153, 0.08) !important;
    border: 1px solid rgba(52, 211, 153, 0.2) !important;
    box-shadow: 0 0 15px rgba(52, 211, 153, 0.15) !important;
}
/* Custom premium buttons */
.q-btn {
    border-radius: 12px !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.03em !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
.q-btn:hover {
    transform: translateY(-1px) !important;
}
/* Custom Scrollbars */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: rgba(0, 0, 0, 0.1);
}
::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.15);
}
/* Bulletproof line clamping and ellipsis */
.line-clamp-1 {
    display: -webkit-box !important;
    -webkit-line-clamp: 1 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}
.line-clamp-2 {
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}
/* Hide Quasar select dropdown icon text and replace with a clean CSS arrow */
.q-select__dropdown-icon {
    font-size: 0 !important;
    width: 0 !important;
    height: 0 !important;
    border-left: 6px solid transparent !important;
    border-right: 6px solid transparent !important;
    border-top: 6px solid rgba(255, 255, 255, 0.6) !important;
    margin-left: 8px !important;
    transition: transform 0.3s ease !important;
}
.q-field--focused .q-select__dropdown-icon {
    border-top-color: #22d3ee !important;
    transform: rotate(180deg) !important;
}
/* Completely hide scroll chevrons on Quasar tabs */
.q-tabs__arrow, .q-tabs__arrow * {
    font-size: 0 !important;
    width: 0 !important;
    height: 0 !important;
    display: none !important;
}
</style>
""")

# Page Header
with ui.row().classes("w-full justify-between items-center px-8 py-6 mb-4 glass-panel neon-glow-purple"):
    with ui.column():
        ui.label("LibraCore").classes("text-3xl font-extrabold tracking-wider text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-500")
        ui.label("FUTURISTIC LIBRARY MANAGEMENT NETWORK").classes("text-xs font-semibold tracking-widest text-purple-400/80")
    with ui.row().classes("items-center gap-4"):
        ui.html('<svg class="w-8 h-8 text-cyan-400 animate-pulse" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>')
        ui.label("v2.0.0").classes("text-sm text-cyan-400/70 font-mono")

# Dialog Modals
# 1. Add Book Dialog
with ui.dialog() as add_book_dialog, ui.card().classes("glass-panel neon-glow-purple p-6 w-96"):
    ui.label("ADD NEW BOOK RECORD").classes("text-lg font-bold text-purple-300 tracking-wide mb-2")
    title_input = ui.input(label="Book Title").classes("w-full mb-2").props("dark color=purple")
    author_input = ui.input(label="Book Author").classes("w-full mb-2").props("dark color=purple")
    copies_input = ui.number(label="Copies Count", value=1, min=1, precision=0).classes("w-full mb-4").props("dark color=purple")
    with ui.row().classes("w-full justify-end gap-2"):
        ui.button("Cancel", on_click=add_book_dialog.close).props("flat color=purple")
        ui.button("Add Record", on_click=lambda: [
            add_book(title_input.value, author_input.value, int(copies_input.value)),
            add_book_dialog.close(),
            title_input.set_value(""),
            author_input.set_value(""),
            copies_input.set_value(1)
        ]).classes("bg-gradient-to-r from-purple-500 to-pink-500 text-white font-bold px-4 py-2 rounded-lg")

# 2. Add Member Dialog
with ui.dialog() as add_member_dialog, ui.card().classes("glass-panel neon-glow-cyan p-6 w-96"):
    ui.label("REGISTER NEW MEMBER").classes("text-lg font-bold text-cyan-300 tracking-wide mb-2")
    username_input = ui.input(label="Username").classes("w-full mb-2").props("dark color=cyan")
    phone_input = ui.input(label="Phone Number").classes("w-full mb-2").props("dark color=cyan")
    email_input = ui.input(label="Email ID").classes("w-full mb-4").props("dark color=cyan")
    borrow_immediately_checkbox = ui.checkbox("Borrow book immediately?").classes("mb-4 text-sm text-cyan-400")
    with ui.row().classes("w-full justify-end gap-2"):
        ui.button("Cancel", on_click=add_member_dialog.close).props("flat color=cyan")
        ui.button("Register", on_click=lambda: [
            add_member(username_input.value, phone_input.value, email_input.value, borrow_immediately_checkbox.value),
            add_member_dialog.close(),
            username_input.set_value(""),
            phone_input.set_value(""),
            email_input.set_value(""),
            borrow_immediately_checkbox.set_value(False)
        ]).classes("bg-gradient-to-r from-cyan-500 to-blue-500 text-white font-bold px-4 py-2 rounded-lg")

# Navigation Tabs
with ui.tabs().classes("w-full justify-center p-2 mb-6 glass-panel neon-glow-cyan max-w-4xl mx-auto") as tabs:
    dashboard_tab = ui.tab("dashboard", label="📊 Dashboard").classes("text-cyan-400 font-bold")
    books_tab = ui.tab("books", label="📚 Books Archive").classes("text-purple-400 font-bold")
    members_tab = ui.tab("members", label="👥 Members Portal").classes("text-pink-400 font-bold")
    transactions_tab = ui.tab("transactions", label="⚡ Transactions").classes("text-emerald-400 font-bold")

# Tab Panels Container
with ui.tab_panels(tabs, value="dashboard").classes("w-full bg-transparent px-4 max-w-6xl mx-auto") as panels:
    
    # ==================== DASHBOARD PANEL ====================
    with ui.tab_panel("dashboard"):
        @ui.refreshable
        def show_dashboard():
            total_books = len(data['books'])
            total_copies = sum(b['total_copies'] for b in data['books'])
            borrowed_copies = sum(b['total_copies'] - b['available_copies'] for b in data['books'])
            total_members = len(data['members'])
            
            # Statistics Cards
            with ui.row().classes("w-full gap-6 justify-center mb-8"):
                # Total Books
                with ui.column().classes("glass-panel neon-glow-cyan p-6 items-center w-60"):
                    ui.label("📚").classes("text-4xl mb-2")
                    ui.label("TOTAL TITLES").classes("text-xs tracking-wider text-cyan-400/80 font-bold")
                    ui.label(str(total_books)).classes("text-4xl font-extrabold text-white mt-1")
                    ui.label(f"{total_copies} total volumes").classes("text-xs text-slate-400/70 mt-1")
                
                # Borrowed Books
                with ui.column().classes("glass-panel neon-glow-purple p-6 items-center w-60"):
                    ui.label("📤").classes("text-4xl mb-2")
                    ui.label("BORROWED COPIES").classes("text-xs tracking-wider text-purple-400/80 font-bold")
                    ui.label(str(borrowed_copies)).classes("text-4xl font-extrabold text-white mt-1")
                    ui.label(f"{total_copies - borrowed_copies} volumes on shelf").classes("text-xs text-slate-400/70 mt-1")
                
                # Active Members
                with ui.column().classes("glass-panel neon-glow-pink p-6 items-center w-60"):
                    ui.label("🪪").classes("text-4xl mb-2")
                    ui.label("REGISTERED MEMBERS").classes("text-xs tracking-wider text-pink-400/80 font-bold")
                    ui.label(str(total_members)).classes("text-4xl font-extrabold text-white mt-1")
                    ui.label("Active digital IDs").classes("text-xs text-slate-400/70 mt-1")
                    
                # Available Books percentage
                available_pct = round((total_copies - borrowed_copies) / total_copies * 100, 1) if total_copies > 0 else 100
                with ui.column().classes("glass-panel neon-glow-purple p-6 items-center w-60"):
                    ui.label("📊").classes("text-4xl mb-2")
                    ui.label("SHELF CAPACITY").classes("text-xs tracking-wider text-purple-400/80 font-bold")
                    ui.label(f"{available_pct}%").classes("text-4xl font-extrabold text-white mt-1")
                    ui.label("Available for loan").classes("text-xs text-slate-400/70 mt-1")
            
            # Sub-sections
            with ui.row().classes("w-full gap-6 justify-center"):
                # Left side: Recent Activity Log
                with ui.column().classes("glass-panel neon-glow-cyan p-6 flex-1 min-w-[320px]"):
                    ui.label("🌐 SYSTEM TRANSACTION MONITOR").classes("text-sm font-bold text-cyan-400 mb-4 tracking-wider")
                    
                    active_loans = []
                    for member in data['members']:
                        for item in member['borrowed']:
                            active_loans.append({
                                "member": member['username'],
                                "title": item['title'],
                                "book_id": item['book_id'],
                                "date": item['borrow_on']
                            })
                    
                    if not active_loans:
                        ui.label("No active loans tracked in the matrix.").classes("text-slate-400 text-sm italic my-4")
                    else:
                        with ui.column().classes("w-full gap-3 max-h-80 overflow-y-auto"):
                            for loan in reversed(active_loans):
                                with ui.row().classes("w-full justify-between items-center p-3 rounded-lg bg-black/30 border border-cyan-500/10 hover:border-cyan-500/30 transition-all overflow-hidden"):
                                    with ui.column().classes("flex-grow flex-shrink min-w-0 gap-0"):
                                        ui.label(f"@{loan['member']}").classes("text-xs font-mono text-cyan-300 font-bold truncate w-full")
                                        ui.label(loan['title'].title()).classes("text-sm font-bold text-white truncate w-full")
                                    with ui.column().classes("items-end flex-shrink-0 ml-4"):
                                        ui.label(loan['book_id']).classes("text-xs text-slate-500 font-mono")
                                        ui.label(loan['date'].split(',')[0]).classes("text-xs text-slate-400")
                
                # Right side: Quick Launch / Action Hub
                with ui.column().classes("glass-panel neon-glow-purple p-6 w-96"):
                    ui.label("⚡ COMMAND HUB").classes("text-sm font-bold text-purple-400 mb-4 tracking-wider")
                    ui.button("ADD BOOK RECORD", on_click=add_book_dialog.open).classes("w-full mb-3 bg-gradient-to-r from-purple-500 to-indigo-600 hover:shadow-[0_0_15px_rgba(168,85,247,0.5)] font-bold text-white py-3 rounded-xl transition-all")
                    ui.button("REGISTER NEW MEMBER", on_click=add_member_dialog.open).classes("w-full mb-3 bg-gradient-to-r from-cyan-500 to-blue-600 hover:shadow-[0_0_15px_rgba(6,182,212,0.5)] font-bold text-white py-3 rounded-xl transition-all")
                    ui.button("GO TO TRANSACTION WIZARD", on_click=lambda: tabs.set_value("transactions")).classes("w-full bg-gradient-to-r from-pink-500 to-rose-600 hover:shadow-[0_0_15px_rgba(236,72,153,0.5)] font-bold text-white py-3 rounded-xl transition-all")
        
        show_dashboard()

    # ==================== BOOKS PANEL ====================
    with ui.tab_panel("books"):
        @ui.refreshable
        def show_books():
            # Search and Actions Bar
            with ui.row().classes("w-full justify-between items-center mb-6 gap-4"):
                ui.input(
                    label="Search Book Title, Author or ID...",
                    value=state['book_search'],
                    on_change=lambda e: [state.update({"book_search": e.value}), show_books.refresh()]
                ).classes("w-80").props("dark color=purple input-class=text-white")
                
                ui.button("➕ ADD NEW BOOK", on_click=add_book_dialog.open).classes("bg-gradient-to-r from-purple-500 to-indigo-600 font-bold hover:shadow-[0_0_15px_rgba(168,85,247,0.4)] px-5 py-2.5 rounded-xl")
            
            # Filter books
            query = state['book_search'].strip().lower()
            filtered_books = data['books']
            if query:
                filtered_books = [
                    b for b in data['books']
                    if query in b['title'].lower() or query in b['author'].lower() or query in b['id'].lower()
                ]
            
            if not filtered_books:
                with ui.column().classes("w-full items-center py-12 glass-panel neon-glow-purple"):
                    ui.label("🔍❌").classes("text-4xl mb-2")
                    ui.label("No books found matching the matrix filter.").classes("text-slate-400 text-base font-semibold")
            else:
                # Grid of Cards
                with ui.row().classes("w-full gap-6 justify-start"):
                    for book in filtered_books:
                        total = book['total_copies']
                        avail = book['available_copies']
                        borrowed = total - avail
                        
                        # Glass book card
                        with ui.card().classes("glass-panel glass-card-hover neon-glow-purple p-5 w-72 flex flex-col justify-between overflow-hidden"):
                            with ui.column().classes("w-full min-w-0 overflow-hidden"):
                                # Header ID
                                with ui.row().classes("w-full justify-between items-center mb-2"):
                                    ui.label(book['id']).classes("text-xs font-mono text-purple-400 font-bold bg-purple-500/10 px-2 py-0.5 rounded")
                                    with ui.row().classes("items-center gap-2"):
                                        ui.label(book['added_on'].split(',')[0]).classes("text-[10px] text-slate-500")
                                        ui.button(
                                            "🗑️",
                                            on_click=lambda b_id=book['id']: delete_book(b_id)
                                        ).props("dense flat").classes("text-rose-500 hover:bg-rose-500/10 rounded-lg p-1 min-h-0 min-w-0").tooltip("Delete book")
                                
                                # Title & Author
                                ui.label(book['title'].title()).classes("text-base font-extrabold text-white leading-tight mb-0.5 line-clamp-2 w-full")
                                ui.label(f"by {book['author'].title()}").classes("text-xs text-purple-300/80 mb-4 truncate w-full")
                                
                                # Copy Statistics
                                with ui.row().classes("w-full items-center justify-between text-xs mb-1"):
                                    ui.label("Available Copies").classes("text-slate-400")
                                    ui.label(f"{avail} / {total}").classes("font-mono font-bold text-white")
                                    
                                # Linear progress bar for copies
                                progress_val = avail / total if total > 0 else 0
                                progress_color = "purple" if progress_val > 0 else "red"
                                ui.linear_progress(value=progress_val).props(f"color={progress_color}").classes("w-full mb-4 rounded-full h-1.5")
                                
                            with ui.row().classes("w-full mt-2"):
                                # Borrow button shortcut spans full width
                                if avail > 0:
                                    ui.button(
                                        "AUTHORIZE LOAN",
                                        on_click=lambda b_id=book['id']: [
                                            state.update({"selected_borrow_book_id": b_id, "selected_borrow_member_id": ""}),
                                            tabs.set_value("transactions"),
                                            ui.notify(f"Selected book: {b_id} for transaction.")
                                        ]
                                    ).classes("bg-gradient-to-r from-cyan-500 to-blue-500 text-white w-full font-bold py-2.5 rounded-xl hover:shadow-[0_0_15px_rgba(6,182,212,0.3)] transition-all")
                                else:
                                    ui.button("OUT OF STOCK").props("disabled").classes("bg-slate-700/50 text-slate-500 w-full font-bold py-2.5 rounded-xl")
        
        show_books()

    # ==================== MEMBERS PANEL ====================
    with ui.tab_panel("members"):
        @ui.refreshable
        def show_members():
            # Search and Actions Bar
            with ui.row().classes("w-full justify-between items-center mb-6 gap-4"):
                ui.input(
                    label="Search Member Username, Email or ID...",
                    value=state['member_search'],
                    on_change=lambda e: [state.update({"member_search": e.value}), show_members.refresh()]
                ).classes("w-80").props("dark color=pink input-class=text-white")
                
                ui.button("👤 REGISTER MEMBER", on_click=add_member_dialog.open).classes("bg-gradient-to-r from-pink-500 to-rose-600 font-bold hover:shadow-[0_0_15px_rgba(236,72,153,0.4)] px-5 py-2.5 rounded-xl")
            
            # Filter members
            query = state['member_search'].strip().lower()
            filtered_members = data['members']
            if query:
                filtered_members = [
                    m for m in data['members']
                    if query in m['username'].lower() or query in m['email'].lower() or query in m['id'].lower()
                ]
            
            if not filtered_members:
                with ui.column().classes("w-full items-center py-12 glass-panel neon-glow-pink"):
                    ui.label("🔍❌").classes("text-4xl mb-2")
                    ui.label("No member digital IDs match the search filter.").classes("text-slate-400 text-base font-semibold")
            else:
                # Grid of Cards
                with ui.row().classes("w-full gap-6 justify-start"):
                    for m in filtered_members:
                        # Glass member card
                        with ui.card().classes("glass-panel glass-card-hover neon-glow-pink p-5 w-80 overflow-hidden"):
                            with ui.row().classes("w-full justify-between items-center mb-3"):
                                ui.label(m['id']).classes("text-xs font-mono text-pink-400 font-bold bg-pink-500/10 px-2 py-0.5 rounded")
                                with ui.row().classes("items-center gap-2"):
                                    ui.label(m['added_on'].split(',')[0]).classes("text-[10px] text-slate-500")
                                    ui.button(
                                        "🗑️",
                                        on_click=lambda m_id=m['id']: delete_member(m_id)
                                    ).props("dense flat").classes("text-rose-500 hover:bg-rose-500/10 rounded-lg p-1 min-h-0 min-w-0").tooltip("Delete profile")
                            
                            # Profile Identity
                            with ui.row().classes("items-center gap-3 mb-4 w-full overflow-hidden"):
                                ui.label("👤").classes("text-3xl flex-shrink-0")
                                with ui.column().classes("gap-0 flex-1 min-w-0 overflow-hidden"):
                                    ui.label(f"@{m['username']}").classes("text-base font-extrabold text-white font-mono truncate w-full")
                                    ui.label(m['email']).classes("text-xs text-slate-400 line-clamp-1 w-full")
                                    ui.label(f"📞 {m['p_no']}").classes("text-xs text-slate-500 truncate w-full")
                            
                            ui.label("BORROWED VOLUMES").classes("text-[10px] font-bold text-pink-400/80 tracking-wider mb-2")
                            
                            # Borrowed list inside member card
                            if not m['borrowed']:
                                ui.label("No active borrowed records.").classes("text-xs text-slate-500 italic mb-4")
                            else:
                                with ui.column().classes("w-full gap-2 mb-4 max-h-36 overflow-y-auto pr-1"):
                                    for borrowed_book in m['borrowed']:
                                        with ui.row().classes("w-full justify-between items-center p-2 rounded bg-black/20 border border-white/5 hover:border-pink-500/20 transition-all overflow-hidden"):
                                            with ui.column().classes("gap-0 flex-grow flex-shrink min-w-0 overflow-hidden"):
                                                ui.label(borrowed_book['title'].title()).classes("text-xs font-bold text-white truncate w-full")
                                                ui.label(borrowed_book['book_id']).classes("text-[9px] font-mono text-slate-500")
                                            ui.button(
                                                "Return",
                                                on_click=lambda m_id=m['id'], b_id=borrowed_book['book_id']: return_book(m_id, b_id)
                                            ).props("dense size=xs color=green").classes("font-bold px-2 rounded flex-shrink-0 ml-2")
                            
                            # Card Footer Actions
                            with ui.row().classes("w-full border-t border-white/5 pt-3 mt-auto"):
                                ui.button(
                                    "NEW TRANSACTION",
                                    on_click=lambda m_id=m['id']: [
                                        state.update({"selected_borrow_member_id": m_id, "selected_borrow_book_id": ""}),
                                        tabs.set_value("transactions")
                                    ]
                                ).classes("bg-gradient-to-r from-cyan-500 to-blue-500 text-white w-full font-bold py-2.5 rounded-xl hover:shadow-[0_0_15px_rgba(6,182,212,0.3)] transition-all")
        
        show_members()

    # ==================== TRANSACTIONS PANEL ====================
    with ui.tab_panel("transactions"):
        @ui.refreshable
        def show_transactions():
            # Dropdown choices generator
            member_options = {m['id']: f"@{m['username']} ({m['id']})" for m in data['members']}
            book_options_borrow = {b['id']: f"{b['title'].title()} ({b['available_copies']}/{b['total_copies']} avail)" for b in data['books'] if b['available_copies'] > 0}
            
            with ui.row().classes("w-full gap-6 justify-center"):
                # Left side: Loan / Borrow Wizard
                with ui.card().classes("glass-panel neon-glow-cyan p-6 w-full max-w-md flex flex-col justify-between"):
                    with ui.column().classes("w-full"):
                        ui.label("⚡ NEW LOAN AUTHORIZATION").classes("text-base font-bold text-cyan-400 tracking-wider mb-4")
                        
                        if not data['members']:
                            ui.label("No members found. Please register members first.").classes("text-slate-400 text-sm mb-4")
                        elif not book_options_borrow:
                            ui.label("No books available for borrow (out of stock or archive empty).").classes("text-slate-400 text-sm mb-4")
                        else:
                            # Selection boxes
                            member_select = ui.select(
                                options=member_options,
                                label="Select Member Profile",
                                value=state['selected_borrow_member_id'] or None,
                                on_change=lambda e: state.update({"selected_borrow_member_id": e.value})
                            ).classes("w-full mb-4").props("dark color=cyan options-dark")
                            
                            book_select = ui.select(
                                options=book_options_borrow,
                                label="Select Book Title",
                                value=state['selected_borrow_book_id'] or None,
                                on_change=lambda e: state.update({"selected_borrow_book_id": e.value})
                            ).classes("w-full mb-6").props("dark color=cyan options-dark")
                            
                            ui.button(
                                "AUTHORIZE BORROW TRANSACTION",
                                on_click=lambda: [
                                    borrow_book(member_select.value, book_select.value),
                                    state.update({"selected_borrow_book_id": ""}),
                                    show_transactions.refresh()
                                ]
                            ).classes("w-full bg-gradient-to-r from-cyan-500 to-blue-600 font-bold py-3 rounded-xl hover:shadow-[0_0_15px_rgba(6,182,212,0.4)] transition-all")
                            
                # Right side: Return Wizard
                with ui.card().classes("glass-panel neon-glow-emerald p-6 w-full max-w-md flex flex-col justify-between"):
                    with ui.column().classes("w-full"):
                        ui.label("♻️ BOOK RETURN WIZARD").classes("text-base font-bold text-emerald-400 tracking-wider mb-4")
                        
                        members_with_loans = {
                            m['id']: f"@{m['username']} ({len(m['borrowed'])} books)"
                            for m in data['members'] if m['borrowed']
                        }
                        
                        if not members_with_loans:
                            ui.label("No active borrowed records exist in the database.").classes("text-slate-400 text-sm mb-4")
                        else:
                            # Selection boxes
                            return_member_select = ui.select(
                                options=members_with_loans,
                                label="Select Member Profile",
                                value=state['selected_return_member_id'] or None,
                                on_change=lambda e: [
                                    state.update({"selected_return_member_id": e.value, "selected_return_book_id": ""}),
                                    show_transactions.refresh()
                                ]
                            ).classes("w-full mb-4").props("dark color=emerald options-dark")
                            
                            selected_mem = next((m for m in data['members'] if m['id'] == return_member_select.value), None)
                            
                            if selected_mem and selected_mem['borrowed']:
                                borrowed_options = {b['book_id']: b['title'].title() for b in selected_mem['borrowed']}
                                
                                return_book_select = ui.select(
                                    options=borrowed_options,
                                    label="Select Book to Return",
                                    value=state['selected_return_book_id'] or None,
                                    on_change=lambda e: state.update({"selected_return_book_id": e.value})
                                ).classes("w-full mb-6").props("dark color=emerald options-dark")
                                
                                ui.button(
                                    "CONFIRM RETURN TRANSACTION",
                                    on_click=lambda: [
                                        return_book(return_member_select.value, return_book_select.value),
                                        state.update({"selected_return_member_id": "", "selected_return_book_id": ""}),
                                        show_transactions.refresh()
                                    ]
                                ).classes("w-full bg-gradient-to-r from-emerald-500 to-green-600 font-bold py-3 rounded-xl hover:shadow-[0_0_15px_rgba(16,185,129,0.4)] transition-all")
                            else:
                                ui.label("Select a member with active loans to continue.").classes("text-slate-500 text-xs italic")
                                
        show_transactions()

# Footer
with ui.row().classes("w-full justify-center py-6 mt-12 text-slate-500 text-xs tracking-wider border-t border-white/5"):
    ui.label("© 2026 LibraCore MANAGEMENT. ENCRYPTED DATABASE PERSISTENCE.")

# Auto-open browser on startup
@app.on_startup
def on_startup():
    webbrowser.open("http://127.0.0.1:8080")

# Run Application
ui.run(title="Library Management Console", port=8080, reload=True)
