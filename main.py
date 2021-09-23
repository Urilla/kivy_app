from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


class Container(BoxLayout):

    def change_image(self):
            app = App.get_running_app()
            app.root.ids['my_image'].source = 'heart.png'
            self.label_widget.text = 'ОЧЕНЬ СИЛЬНО ЛЮБЛЮ!! '
class MyApp(App):
    def build(self):
        return Container()
if __name__ == "__main__":
    MyApp().run()