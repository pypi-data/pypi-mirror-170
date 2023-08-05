# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDatakabelAdersEnSectie(KeuzelijstField):
    """Lijst van mogelijke waarden volgens de catalogusposten van het standaardbestek voor de samenstelling van een datakabel volgens het aantal aders en in voorkomende gevallen, hun dikte in vierkante millimeter."""
    naam = 'KlDatakabelAdersEnSectie'
    label = 'Datakabel aders en sectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDatakabelAdersEnSectie'
    definition = 'Lijst van mogelijke waarden volgens de catalogusposten van het standaardbestek voor de samenstelling van een datakabel volgens het aantal aders en in voorkomende gevallen, hun dikte in vierkante millimeter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDatakabelAdersEnSectie'
    options = {
        '100-x-2-x-1-mm2': KeuzelijstWaarde(invulwaarde='100-x-2-x-1-mm2',
                                            label='100 x 2 X 1 mm²',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/100-x-2-x-1-mm2'),
        '20-x-2-x-1-mm2': KeuzelijstWaarde(invulwaarde='20-x-2-x-1-mm2',
                                           label='20 x 2 X 1 mm²',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/20-x-2-x-1-mm2'),
        '21-x-2-x-1-mm2': KeuzelijstWaarde(invulwaarde='21-x-2-x-1-mm2',
                                           label='21 x 2 X 1 mm²',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/21-x-2-x-1-mm2'),
        '48-vezels': KeuzelijstWaarde(invulwaarde='48-vezels',
                                      label='48 vezels',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/48-vezels'),
        '96-vezels': KeuzelijstWaarde(invulwaarde='96-vezels',
                                      label='96 vezels',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/96-vezels'),
        'zonder-verdere-specificatie': KeuzelijstWaarde(invulwaarde='zonder-verdere-specificatie',
                                                        label='zonder verdere specificatie',
                                                        status='ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/zonder-verdere-specificatie')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

