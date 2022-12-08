# -*- coding: utf-8 -*-
import unittest

from gilded_rose import NormalItem, ConjuredItem , GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras1(self):
        items = []
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items.append(NormalItem(sulfuras, 5, 80))
        items.append(NormalItem(sulfuras, 10, 80))
        items.append(NormalItem(sulfuras, 100, 80))

        gilded_rose = GildedRose(items)

        for _ in range(100):
            gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(80, items[1].quality)
        self.assertEqual(100, items[2].sell_in)


    def test_brie1(self):
        items = []
        aged_brie = "Aged Brie"
        items.append(NormalItem(aged_brie, 12, 20))
        items.append(NormalItem(aged_brie, 10, 0))
        items.append(NormalItem(aged_brie, 80, 40))

        gilded_rose = GildedRose(items)

        for _ in range(13):
            gilded_rose.update_quality()
        self.assertEqual(33, items[0].quality)
        self.assertEqual(13, items[1].quality)
        self.assertEqual(50, items[2].quality)

    def test_backstage1(self):
        items = []
        backstage = "Backstage passes to a TAFKAL80ETC concert"
        items.append(NormalItem(backstage, 12, 20))
        items.append(NormalItem(backstage, 8, 4))
        items.append(NormalItem(backstage, 16, 40))

        gilded_rose = GildedRose(items)

        for _ in range(10):
            gilded_rose.update_quality()

        self.assertEqual(41, items[0].quality)
        self.assertEqual(0, items[1].quality)
        self.assertEqual(50, items[2].quality)

    def test_normal(self):
        items = []
        items.append(NormalItem("The most normal item", 15, 20))
        items.append(NormalItem("Little Rock, Arkansas", 23, 30))
        items.append(NormalItem("Juicy juice", 10, 50))

        gilded_rose = GildedRose(items)

        for _ in range(20):
            gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(10, items[1].quality)
        self.assertEqual(21, items[2].quality)

    def test_conjured(self):
        items = []
        items.append(ConjuredItem("Dummy item", -1, 20))
        items.append(ConjuredItem("Normally normal", 4, 30))
        items.append(ConjuredItem("Cup of iced tea", 50, 40))

        gilded_rose = GildedRose(items)

        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(20, items[1].quality)
        self.assertEqual(30, items[2].quality)


if __name__ == '__main__':
    unittest.main()
