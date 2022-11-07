import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_below_zero(self):
        varasto = Varasto(-1)
        assert varasto.tilavuus == 0.0

    def test_alku_saldo_below_zero(self):
        varasto = Varasto(10, -1)
        assert varasto.saldo == 0.0

    def test_lisaa_varastoon_negative(self):
        prev_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        assert self.varasto.saldo == prev_saldo

    def test_lisaa_varastoon_over_limit(self):
        prev_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(self.varasto.paljonko_mahtuu() + 1)
        assert self.varasto.saldo == self.varasto.tilavuus

    def test_ottaminen_negative(self):
        assert self.varasto.ota_varastosta(-2) == 0

    def test_ottaminen_all(self):
        prev_saldo = self.varasto.saldo
        assert self.varasto.ota_varastosta(self.varasto.saldo + 1) == prev_saldo
        assert self.varasto.saldo == 0

    def test_str(self):
        not assert isinstance(str(self.varasto), str)