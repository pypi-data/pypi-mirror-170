# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelmantelKleur(KeuzelijstField):
    """Lijst van mogelijke kleuren voor de kabelmantel."""
    naam = 'KlKabelmantelKleur'
    label = 'Kabelmantel kleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlKabelmantelKleur'
    definition = 'Lijst van mogelijke kleuren voor de kabelmantel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelmantelKleur'
    options = {
        'blank-koper': KeuzelijstWaarde(invulwaarde='blank-koper',
                                        label='blank koper',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/blank-koper'),
        'blauw': KeuzelijstWaarde(invulwaarde='blauw',
                                  label='blauw',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/blauw'),
        'geel-grijs': KeuzelijstWaarde(invulwaarde='geel-grijs',
                                       label='geel-grijs',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-grijs'),
        'geel-groen': KeuzelijstWaarde(invulwaarde='geel-groen',
                                       label='geel-groen',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-groen'),
        'geel-of-zwart': KeuzelijstWaarde(invulwaarde='geel-of-zwart',
                                          label='geel of zwart',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-of-zwart'),
        'geel-zwart': KeuzelijstWaarde(invulwaarde='geel-zwart',
                                       label='geel-zwart',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-zwart'),
        'grijs': KeuzelijstWaarde(invulwaarde='grijs',
                                  label='grijs',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/grijs'),
        'groen-met-4-zwarte-strepen': KeuzelijstWaarde(invulwaarde='groen-met-4-zwarte-strepen',
                                                       label='groen met 4 zwarte strepen',
                                                       status='ingebruik',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/groen-met-4-zwarte-strepen'),
        'groen-zwart': KeuzelijstWaarde(invulwaarde='groen-zwart',
                                        label='groen-zwart',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/groen-zwart'),
        'onbekend': KeuzelijstWaarde(invulwaarde='onbekend',
                                     label='onbekend',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/onbekend'),
        'oranje': KeuzelijstWaarde(invulwaarde='oranje',
                                   label='oranje',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/oranje'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/rood'),
        'rood-wit': KeuzelijstWaarde(invulwaarde='rood-wit',
                                     label='rood-wit',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/rood-wit'),
        'transparant': KeuzelijstWaarde(invulwaarde='transparant',
                                        label='transparant',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/transparant'),
        'yp': KeuzelijstWaarde(invulwaarde='yp',
                               label='YP',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/yp'),
        'zwart': KeuzelijstWaarde(invulwaarde='zwart',
                                  label='zwart',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/zwart'),
        'zwart-rood': KeuzelijstWaarde(invulwaarde='zwart-rood',
                                       label='zwart-rood',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/zwart-rood')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

