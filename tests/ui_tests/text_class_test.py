from launch import GameRunner
from visual.UI.base.text import Text
from visual.UI.base.style import Style
from global_obj.main import Global


class Body:
    def __init__(self):
        self.texts = []
        self.i = 0
        text = 'AHAHHAH'
        for i in range(1, 11):
            t = "\t" * (i - 1)
            text = text + f'\n {t} {i} line'
            # print(text)

            self.texts.append(
                Text(f'test_text_{i}', text,
                     x_k=i / 10 - 0.1, y_k=i / 20,
                     style=Style(surface_color=(255 / i, 255 / i, 255 / i)),
                     h_size_k=0.1,
                     v_size_k=0.1,
                     color=(20 * i, 155, 20 * i),
                     )
            )
        self.texts.append(Text('test_text',
                               "\tThis is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
                               "in the sentence, but that's because the text is too long to fit the screen.\nIt can look strange sometimes.\n" \
                               "\t\t\tThis function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
                               "text will disappear underneath the surface",
                               x_k=0.0001, y_k=0.5,
                               style=Style(surface_color=(25, 25, 25),
                               from_left=True),
                               # scale_font=True,
                               # from_bot=False,
                               # from_top=False,
                               unlimited_h_size=False,
                               unlimited_v_size=False,

                               h_size_k=0.7,
                               v_size_k=0.1,
                               color=(100, 155, 100),
                               surface_color=(50, 50, 50)
                               ))

        self.texts.append(Text('test_text',
                               "\tThis is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
                               "in the sentence, but that's because the text is too long to fit the screen. It can look strange sometimes." \
                               "\t\t\tThis function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
                               "text will disappear underneath the surface.SSSSSSSSSSSSSSSSSSSSSAAAAAAAAAAAAAAAABEND",
                               x_k=0.3, y_k=0.75,
                               style=Style(surface_color=(25, 25, 25),
                                           from_left=True,
                                           from_top=True),
                               # scale_font=True,
                               # from_bot=False,
                               from_top=True,
                               unlimited_h_size=False,
                               unlimited_v_size=False,
                               h_size_k=0.3,
                               v_size_k=0.5,
                               color=(100, 155, 100),
                               surface_color=(50, 50, 50)
                               ))

        self.texts.append(
            Text('test_text', 'AHAHHA\n \t 1 line',
                 x_k=0, y_k=0.7,
                 #  from_left=True, from_bot=True, from_top=True,
                 h_size_k=0.1,
                 v_size_k=0.1,
                 style=Style(surface_color=(50, 50, 50),
                             color=(255, 155, 255),
                             ),

                 # color=(255, 155, 255),
                 )

        )

    def game_loop(self):
        for t in self.texts:
            t.draw()

        if Global.keyboard.ENTER:
            self.i += 1
            self.texts[3].change_text(f'test_{self.i}')


if __name__ == '__main__':
    GameRunner(Body()).run()
