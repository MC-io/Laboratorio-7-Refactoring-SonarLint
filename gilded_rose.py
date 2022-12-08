# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    def lower_quality(self, i):
        if self.quality - i >= 0:
            self.quality -= i
        else:
            self.quality = 0

    def increase_quality(self, i):
        if self.quality + i <= 50:
            self.quality += i
        else:
            self.quality = 50

    def degrade_quality(self):
        if self.sell_in < 0:
            self.lower_quality(2)
        else:
            self.lower_quality(1)

    def sell_in_aproaches(self):
        if self.name != "Sulfuras, Hand of Ragnaros":
            self.sell_in -= 1

    def update_quality(self):
        if self.name == "Aged Brie":
            self.increase_quality(1)         
        elif self.name == "Backstage passes to a TAFKAL80ETC concert":
            if self.sell_in < 0:
                self.quality = 0
            elif self.sell_in <= 5:
                self.increase_quality(3)
            elif self.sell_in <= 10:
                self.increase_quality(2)
            else:
                self.increase_quality(1)         
        elif self.name != "Sulfuras, Hand of Ragnaros":
            self.degrade_quality()
        self.sell_in_aproaches()
        
class ConjuredItem(NormalItem):
    def degrade_quality(self):
        if self.sell_in < 0:
            self.lower_quality(4)
        else:
            self.lower_quality(2)


