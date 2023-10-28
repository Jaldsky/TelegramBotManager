from random import choice


def send_greeting_personal(name: str) -> str:
    greeting_phrases = (
        f'Эй, {name}, Кибер Чирик на связи! Чё по новостям в кибермире?',
        f'Привет-привет, {name}! Кибер Чирик тут, чтобы поговорить о киберштучках. Чё скажешь?',
        f'Эй, кибердруг, {name}! Кибер Чирик в эфире, готов к чату!',
        f'Здарова, {name}! Кибер Чирик готов помочь в киберпутешествии. Чё надо?',
        f'Эй, {name}, Кибер Чирик здесь, чтобы поговорить о киберделах. Готов к чату?',
        f'Привет, кибергеймер {name}! Кибер Чирик пришел в мир реальности, чтобы обсудить кибертемы. Чё там?',
        f'Здрасте, {name}! Кибер Чирик в эфире. Чё намечено на сегодня?',
        f'Эй, {name}! Че каво, мой человек?',
        f'Салют, {name}! Как дела по киберфронту?',
        f'Хэлло, {name}! Че по планам, киберкот?',
        f'Хой, {name}! Кто тут главный кибермастер?',
        f'Приветствую, {name}! Ты готов чирикать нашими кибертрендами?',
        f'Привет, {name}, готов заражать сеть новыми идеями?',
        f'Эй, {name}, как жизнь в мире бинарных приключений?',
        f'О, {name}, чем могу помочь в этом кибер-джангле?',
    )
    return choice(greeting_phrases)
