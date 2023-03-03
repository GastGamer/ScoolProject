from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd import images_path


KV = '''

<ContentNavigationDrawer>

    MDList:

        OneLineIconListItem:
            text: "Домашняя страница"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "main scr"
            
            IconLeftWidgetWithoutTouch:
                icon: "home"
        
        OneLineListItem:
            text: "Категории"

        OneLineIconListItem:
            text: "Логические"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"

            IconLeftWidgetWithoutTouch:
                icon: "cube"

        OneLineIconListItem:
            text: "На внимание"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"
            
            IconLeftWidgetWithoutTouch:
                icon: "eye"
        
        OneLineIconListItem:
            text: "На концентрацию"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3"
            
            IconLeftWidgetWithoutTouch:
                icon: "pencil"

        OneLineIconListItem:
            text: "Стратегическое мышление"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 4"
            
            IconLeftWidgetWithoutTouch:
                icon: "chess-knight"
    
MDScreen:

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "main scr"

                MDCard:
                    orientation: "vertical"
                    padding: 50, 50, 50, 50
                    size_hint: .9, .8
                    pos_hint: {"center_x": .5, "center_y": .45}
                    elevation: 4
                    shadow_offset: 0, 2
                
                    MDLabel:
                        text: "Приветствую! Это простое приложение в котором представлены мобильные игры помогающие развить тот или иной навык/качество, например: внимание, концентрация и логика."
                        halign: "center"

            MDScreen:
                name: "scr 1"

                MDCard:
                    orientation: "vertical"
                    padding: 0, 0, 0, 0
                    size_hint: .9, .8
                    pos_hint: {"center_x": .5, "center_y": .45}
                    elevation: 4
                    shadow_offset: 0, 2
                
                    MDScrollView
                        MDList:
                            OneLineIconListItem:
                                text: "NeuroNation"
                            OneLineIconListItem:
                                text: "Судоку"
                            OneLineIconListItem:
                                text: "CogniFit — Логические игры и задачи"
                            OneLineIconListItem:
                                text: "Мех. Коробка — Каверзные загадки"
                            OneLineIconListItem:
                                text: "1010! color"

            MDScreen:
                name: "scr 2"

                MDCard:
                    orientation: "vertical"
                    padding: 0, 0, 0, 0
                    size_hint: .9, .8
                    pos_hint: {"center_x": .5, "center_y": .45}
                    elevation: 4
                    shadow_offset: 0, 2

                    MDScrollView
                        MDList:
                            OneLineIconListItem:
                                text: "Судоку"
                            OneLineIconListItem:
                                text: "Lumosity"
                            OneLineIconListItem:
                                text: "NeuroNation"
                            OneLineIconListItem:
                                text: "CogniFit"
                            OneLineIconListItem:
                                text: " Brain Out"
            
            MDScreen:
                name: "scr 3"

                MDCard:
                    orientation: "vertical"
                    padding: 0, 0, 0, 0
                    size_hint: .9, .8
                    pos_hint: {"center_x": .5, "center_y": .45}
                    elevation: 4
                    shadow_offset: 0, 2

                    MDScrollView
                        MDList:
                            OneLineIconListItem:
                                text: "Cut The Rope: Experiments"
                            OneLineIconListItem:
                                text: "Найди отличия"
                            OneLineIconListItem:
                                text: "Lumosity"
                            OneLineIconListItem:
                                text: "Neuronation"
                            OneLineIconListItem:
                                text: "Викиум"

            MDScreen:
                name: "scr 4"

                MDCard:
                    orientation: "vertical"
                    padding: 0, 0, 0, 0
                    size_hint: .9, .8
                    pos_hint: {"center_x": .5, "center_y": .45}
                    elevation: 4
                    shadow_offset: 0, 2

                    MDScrollView
                        MDList:
                            OneLineIconListItem:
                                text: "For the King"
                                Image:
                                    source: "Icon\cover_29659.jpg"
                                    size: self.texture_size
                                    pos: 310, 205
                            OneLineIconListItem:
                                text: "Darkest Dungeon"
                            OneLineIconListItem:
                                text: "XCOM 2"
                            OneLineIconListItem:
                                text: "Divinity: Original Sin 2"
                            OneLineIconListItem:
                                text: "Pillars of Eternity"
        
        MDTopAppBar:
            title: "Полезные игры"
            elevation: 4
            pos_hint: {"top": 1}
            md_bg_color: "#131313"
            left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
    
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Project(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
    
Project().run()