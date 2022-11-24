import csv

from django.test import TestCase

from utils.misc import (check_date, check_decimal, check_num, check_services,
                        get_retrieve_data)


class MiscTestCase(TestCase):
    
    def test_retrieve_data(self):
        test_file = open('utils/tests/fixtures/bills.csv')
        reader = csv.reader(test_file, delimiter=',')
        self.assertEquals(
            get_retrieve_data(list(reader)),
            [
                ['client1', 'OOO Client1Org1', 1, 10000.0, '2021-04-01', 'вызов врача на дом'],
                ['client1', 'OOO Client1Org1', 5, 10000.0, '2021-04-05', 'клинический'],
                ['client1', 'OOO Client1Org1', 6, 10000.54, '2021-04-06', 'прием терапевта гастроэнтеролога первичный'],
                ['client1', 'OOO Client1Org1', 7, 10000.64, '2021-04-07', 'прием уролога первичный', 'клинический', 'анализ крови развернутый'],
                ['client2', 'OOO Client2Org1', 1, 777.0, '2021-04-21', 'прием терапевта первичный']
            ]
        )
        test_file.close()
    
    
    def test_check_num(self):
        self.assertEquals(check_num('1'), 1)
        self.assertEquals(check_num(1), 1)
        self.assertEquals(check_num('Test'), False)
        self.assertEquals(check_num(-1), False)
        self.assertEquals(check_num(0), False)
        self.assertEquals(check_num('-1'), False)
        self.assertEquals(check_num('0'), False)
        self.assertEquals(check_num(3.5), False)


    def test_check_decimal(self):
        self.assertEquals(check_decimal('1'), 1.0)
        self.assertEquals(check_decimal(1), 1.0)
        self.assertEquals(check_decimal(0), 0.0)
        self.assertEquals(check_decimal(3.5), 3.5)
        self.assertEquals(check_decimal(3.57), 3.57)
        self.assertEquals(check_decimal(3.578), 3.58)


    def test_check_date(self):
        self.assertEquals(check_date('05.04.2021'), '2021-04-05')
        self.assertEquals(check_date('05.2021'), False)
        self.assertEquals(check_date('2021.04.05'), False)
        self.assertEquals(check_date('05,04,2021'), '2021-04-05')


    def test_check_services(self):
        self.assertEquals(
            check_services(
                [
                    'прием уролога первичный',
                    'клинический',
                    ' анализ крови развернутый'
                ]
            ), [
                'прием уролога первичный',
                'клинический',
                'анализ крови развернутый'
            ]
        )
        self.assertEquals(check_services(['',]), [False])
        self.assertEquals(check_services(['-',]), [False])
        self.assertEquals(check_services(['-', 'клинический']), ['клинический'])
