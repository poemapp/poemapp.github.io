import flet as ft

def main(page: ft.Page):
    page.title = "Poem Collection"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700

    poems = [
        {"title": "ဖရဲသီး", "content": "‌အစိမ်းရောင် အခွံကြိုက်\n သိပ်မိုက်တဲ့နွား\n\n အေးချိုချို အနီးချစ်မှ\n စဉ်စစ်လူသား", "category": "နိုင်ငံရေး"},
        {"title": "တွေးဖို့", "content": "‌နွားသိုးက နန်းတော်ဝင်\n ဘုရင်မှ မဖြစ်ဘဲ\n\n နန်းတော်သာ နွားတင်းကုတ်လို\n ဆုပ်ယုတ်ရမြဲ", "category": "နိုင်ငံရေး"},
        {"title": "လရောင်အောက်", "content": "လရောင်အောက်မှာ အိပ်မက်တွေ ပွင့်လန်းတယ်။", "category": "သဘာဝ"},
    ]

    # Container ထဲမှာ padding ကို တိုက်ရိုက် ဂဏန်းနဲ့ ပေးလိုက်ပါမယ် (Error မတက်တော့ပါ)
    main_container = ft.Container(
        expand=True,
        padding=20, 
    )

    def show_poem(poem):
        main_container.content = ft.Column([
            ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: show_home()),
            ft.Text(poem["title"], size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text(poem["content"], size=18),
        ])
        page.update()

    def show_home():
        poem_list = ft.ListView(expand=True, spacing=10)
        for p in poems:
            poem_list.controls.append(
                ft.Card(
                    content=ft.ListTile(
                        title=ft.Text(p["title"]),
                        subtitle=ft.Text(p["category"]),
                        on_click=lambda e, poem=p: show_poem(poem),
                    )
                )
            )
        
        main_container.content = ft.Column([
            ft.Text("My Poetry", size=32, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            poem_list
        ])
        page.update()

    page.add(main_container)
    show_home()

if __name__ == "__main__":
    ft.app(target=main)