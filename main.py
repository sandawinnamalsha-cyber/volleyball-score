import flet as ft

def main(page: ft.Page):
    page.title = "Volleyball Pro"
    page.bgcolor = "#0F172A"
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    team_a = ft.TextField(value="TEAM A", width=130, text_align=ft.TextAlign.CENTER, text_style=ft.TextStyle(color="white"))
    team_b = ft.TextField(value="TEAM B", width=130, text_align=ft.TextAlign.CENTER, text_style=ft.TextStyle(color="white"))

    score_a = ft.Text("0", size=80, color="#22D3EE", weight=ft.FontWeight.BOLD)
    score_b = ft.Text("0", size=80, color="#F472B6", weight=ft.FontWeight.BOLD)
    sets_a = ft.Text("Sets: 0", color="white")
    sets_b = ft.Text("Sets: 0", color="white")
    info = ft.Text("First to 25, Win by 2 | Best of 3", color="grey", size=11, text_align=ft.TextAlign.CENTER)
    history = ft.Column([], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5)

    sa = 0
    sb = 0
    set_a = 0
    set_b = 0

    def win_check():
        nonlocal sa, sb, set_a, set_b
        if (sa >= 25 or sb >= 25) and abs(sa - sb) >= 2:
            # Team name empty නම් default දාන්න
            name_a = team_a.value.strip() if team_a.value.strip() else "TEAM A"
            name_b = team_b.value.strip() if team_b.value.strip() else "TEAM B"
            
            history.controls.append(ft.Text(f"{name_a} {sa}-{sb} {name_b}", color="white", size=13))
            if sa > sb:
                set_a += 1
            else:
                set_b += 1
            
            sets_a.value = f"Sets: {set_a}"
            sets_b.value = f"Sets: {set_b}"
            sa = 0
            sb = 0
            score_a.value = "0"
            score_b.value = "0"
            
            if set_a == 2 or set_b == 2:
                winner = name_a if set_a == 2 else name_b
                info.value = f"🏆 {winner} WON THE MATCH!"
                info.color = "yellow"
                info.size = 18

    def add_a(e): 
        nonlocal sa
        sa += 1
        score_a.value = str(sa)
        win_check()
        page.update()

    def sub_a(e):
        nonlocal sa
        if sa > 0:
            sa -= 1
            score_a.value = str(sa)
            page.update()

    def add_b(e):
        nonlocal sb
        sb += 1
        score_b.value = str(sb)
        win_check()
        page.update()

    def sub_b(e):
        nonlocal sb
        if sb > 0:
            sb -= 1
            score_b.value = str(sb)
            page.update()

    def reset(e):
        nonlocal sa, sb, set_a, set_b
        sa = 0; sb = 0; set_a = 0; set_b = 0
        score_a.value = "0"; score_b.value = "0"
        sets_a.value = "Sets: 0"; sets_b.value = "Sets: 0"
        history.controls.clear()
        info.value = "First to 25, Win by 2 | Best of 3"
        info.color = "grey"
        info.size = 11
        page.update()

    main_content = ft.Container(
        content=ft.Column([
            ft.Text("VOLLEYBALL PRO", color="white", weight=ft.FontWeight.BOLD, size=22),
            info,
            ft.Row([team_a, ft.Text("VS", color="white"), team_b], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.Column([sets_a, score_a, ft.Row([ft.ElevatedButton("-", on_click=sub_a), ft.ElevatedButton("+", on_click=add_a)], alignment=ft.MainAxisAlignment.CENTER)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Text(":", color="white", size=40),
                ft.Column([sets_b, score_b, ft.Row([ft.ElevatedButton("-", on_click=sub_b), ft.ElevatedButton("+", on_click=add_b)], alignment=ft.MainAxisAlignment.CENTER)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER),
            history,
            ft.ElevatedButton("NEW MATCH", bgcolor="#EF4444", color="white", on_click=reset)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=18, scroll=ft.ScrollMode.AUTO, expand=True),
        padding=20,
        bgcolor="#0F172A",
        expand=True
    )

    page.add(main_content)

ft.app(target=main)
