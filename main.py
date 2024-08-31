import django_setup
from main.models import Genre, Game

action = Genre(
    name="Action"
)
rpg = Genre(
    name="RPG"
)
strategy = Genre(
    name="Strategy"
)

game1 = Game(
    title="Minecraft",
    release_year=2011,
    rating=9.0
)
game2 = Game(
    title="Starcraft 2",
    release_year=2010,
    rating=8.9
)

action.save()
rpg.save()
strategy.save()

game1.save()
game2.save()

game1.genres.add(rpg, action)
game2.genres.add(strategy)
