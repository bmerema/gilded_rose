# -*- coding: utf-8 -*-


class GildedRose(object):
    max_quality = 50
    min_quality = 0
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            elif item.name == "Aged Brie":
                self.update_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_pass(item)
            elif item.name == "Conjured Mana Cake":
                self.update_conjured(item)
            else:
                self.item_update(item)

    def item_update(self, item):
        if item.quality > self.min_quality:
            item.quality = item.quality - 1
            # if sell in days have passed, decrease quality twice
            if item.sell_in <= 0:
                item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1


    def update_brie(self, item):
        if item.quality < self.max_quality:
            item.quality = item.quality + 1
            if item.sell_in <= 0:
                item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1

    def update_backstage_pass(self, item):
        if 10 >= item.sell_in > 5:
            item.quality = item.quality + 2
        elif 5 >= item.sell_in > 0:
            item.quality = item.quality + 3
        elif item.sell_in <= 0:
            item.quality = 0
        else:
            item.quality = item.quality + 1

        if item.quality > self.max_quality:
            item.quality = self.max_quality
        item.sell_in = item.sell_in - 1

    def update_conjured(self, item):
        if item.quality > self.min_quality:
            item.quality = item.quality - 2
            if item.sell_in <= 0:
                item.quality = item.quality - 2
        if item.quality < self.min_quality:
            item.quality = self.min_quality
        item.sell_in = item.sell_in - 1
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    # def item_update(normal_item: Item):
    #     if min_quality < normal_item.quality: = 0 else normal_item.quality: -= 2
    #     normal_item.quality = max(normal_item.quality, min_quality)
    #     normal_item.sell_in -= 1
    #
    # def aged_brie_updater(aged_brie: Item):
    #     if min_quality <= aged_brie.quality: else aged_brie.quality + 2:
    #         aged_brie.quality = min(max_quality, quality)
    #     aged_brie.sell_in -= 1
