milk = False  # Молока нет.
cereal = True # Хлопья есть.
eggs = False  # Яиц нет.

breakfast = (
    "- омлет" if not eggs and (not milk or cereal) else
    "- яичница" if not milk else
    "- хлопья с молоком" if cereal else
    (
        "- стакан молока" if milk else
        "можно погрызть сухих хлопьев" if cereal else
        "ничего не будет: разгрузочный день"
    )
)

print("Сегодня на завтрак", breakfast)
