# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose




class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_quality_does_not_increase_above_50(self):
        items = [Item("Aged Brie", 4, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected = {'sell_in': 3, 'quality': 50}
        item = items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.sell_in, expected['sell_in'])

    def test_quality_does_not_increase_above_50(self):
        items = [Item("Aged Brie", 4, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected = {'sell_in': 3, 'quality': 50}
        item = items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.sell_in, expected['sell_in'])
    def test_sulfuras(self):
        item = Item("Sulfuras, Hand of Ragnaros", 20, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", item.name)
        self.assertNotEqual(item.sell_in, 15)
        self.assertEqual(item.sell_in, 20)  # does not change
        self.assertEqual(item.quality, 80)  # never alters

# def test_quality
# def test_aged_brie
# def test_aged_brie_50
# def test_below_0

if __name__ == '__main__':
    unittest.main()
