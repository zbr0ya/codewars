def cakes(recipe, available):
    total_box = []
    for _ in recipe.items():
        if _[0] in available:
            total_box.append(available[_[0]] // _[1])
        else:
            return 0
    return min(total_box)