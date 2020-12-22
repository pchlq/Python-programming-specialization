from abc import ABC, abstractmethod

class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass   

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Berserk(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["HP"] += 50
        stats["Strength"] += 7
        stats["Endurance"] += 7
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["Perception"] -= 3
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Berserk"]


class Blessing(AbstractPositive):
    def get_stats(self):
        effect_points = ["HP", "MP", "SP"]
        stats = self.base.get_stats()
        stats.update(
            {k: v+2 for (k,v) in stats.items() if k not in effect_points}
        )
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Blessing"]    


class Weakness(AbstractNegative):
    def get_stats(self):
        effects = ["Strength", "Endurance", "Agility"]
        stats = self.base.get_stats()
        stats.update({k: v-4 for (k,v) in stats.items() if k in effects})
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Weakness"]
    

class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats.update(
            {k: v-10 for (k,v) in stats.items() if k == "Luck"}
        )
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["EvilEye"]


class Curse(AbstractNegative):
    def get_stats(self):
        effect_points = ["HP", "MP", "SP"]
        stats = self.base.get_stats()
        stats.update(
            {k: v-2 for (k,v) in stats.items() if k not in effect_points}
        )
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Curse"]