#зад1
duration = int(input("Введите время в секундах: "))
days = duration // (60 * 60 * 24)
hours = (duration - days * (60 * 60 * 24)) // 3600
minutes = (duration - days * (60 * 60 * 24) - hours * 3600) // 60
seconds = duration - days * (60 * 60 * 24) - hours * 3600 - minutes * 60
if days <= 0:
    pass #это я пытался сделать чтобы 0 не печатался ...
print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')


#зад2
