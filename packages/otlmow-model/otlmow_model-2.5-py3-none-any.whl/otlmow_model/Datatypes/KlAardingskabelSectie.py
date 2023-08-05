# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAardingskabelSectie(KeuzelijstField):
    """Lijst met mogelijke waarden voor de sectie van een aardingskabel."""
    naam = 'KlAardingskabelSectie'
    label = 'Aardingskabel sectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlAardingskabelSectie'
    definition = 'Lijst met mogelijke waarden voor de sectie van een aardingskabel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAardingskabelSectie'
    options = {
        '10-mm2': KeuzelijstWaarde(invulwaarde='10-mm2',
                                   label='10 mm²',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/10-mm2'),
        '16-mm2': KeuzelijstWaarde(invulwaarde='16-mm2',
                                   label='16 mm²',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/16-mm2'),
        '2.5-mm2': KeuzelijstWaarde(invulwaarde='2.5-mm2',
                                    label='2.5 mm²',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/2.5-mm2'),
        '25-mm2': KeuzelijstWaarde(invulwaarde='25-mm2',
                                   label='25 mm²',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/25-mm2'),
        '35-mm2': KeuzelijstWaarde(invulwaarde='35-mm2',
                                   label='35 mm²',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/35-mm2'),
        '4-mm2': KeuzelijstWaarde(invulwaarde='4-mm2',
                                  label='4 mm²',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/4-mm2'),
        '50-mm2': KeuzelijstWaarde(invulwaarde='50-mm2',
                                   label='50 mm²',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/50-mm2'),
        '6-mm2': KeuzelijstWaarde(invulwaarde='6-mm2',
                                  label='6 mm²',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/6-mm2')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

