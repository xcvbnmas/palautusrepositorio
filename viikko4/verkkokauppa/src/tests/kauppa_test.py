import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
        
        
    def test_metodia_tilisiirto_kutsutaan_oikein(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
        
    def test_kaksi_erilaista_tuotetta(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "leipä", 3)
                
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
                
                
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
                
        kauppa.aloita_asiointi() 
        
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        
        kauppa.tilimaksu("pekka", "12345")
        
        ostoskorin_summa = Tuote(1, "maito", 5).hinta + Tuote(2, "leipä", 3).hinta
        
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", ostoskorin_summa)
        

    def test_kaksi_samaa_tuotetta(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "leipä", 3)
                
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
                
                
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
                
        kauppa.aloita_asiointi() 
        
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        
        kauppa.tilimaksu("pekka", "12345")
        
        ostoskorin_summa = Tuote(1, "maito", 5).hinta + Tuote(1, "maito", 5).hinta
        
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", ostoskorin_summa)    
        
    def test_kaksi_eri_tuotetta_toinen_loppu(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "leipä", 3)
                
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
                                
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
                
        kauppa.aloita_asiointi() 
        
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        
        kauppa.tilimaksu("pekka", "12345")
        
        ostoskorin_summa = Tuote(1, "maito", 5).hinta
        
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", ostoskorin_summa)    
        
        
        #
        
