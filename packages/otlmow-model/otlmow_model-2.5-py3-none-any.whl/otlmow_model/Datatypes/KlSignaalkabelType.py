# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignaalkabelType(KeuzelijstField):
    """Lijst met types voor signalisatiekabels volgens de gebruikte materialen zoals opgenomen in het Standaarbestek 270."""
    naam = 'KlSignaalkabelType'
    label = 'Signalisatiekabel types'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignaalkabelType'
    definition = 'Lijst met types voor signalisatiekabels volgens de gebruikte materialen zoals opgenomen in het Standaarbestek 270.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignaalkabelType'
    options = {
        'koperkabel': KeuzelijstWaarde(invulwaarde='koperkabel',
                                       label='koperkabel',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/koperkabel'),
        'profibuskabel': KeuzelijstWaarde(invulwaarde='profibuskabel',
                                          label='profibuskabel',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/profibuskabel'),
        'svavb-f2': KeuzelijstWaarde(invulwaarde='svavb-f2',
                                     label='SVAVB-F2',
                                     status='ingebruik',
                                     definitie='Gewapende signaalkabel voor ondergronds gebruik.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/svavb-f2'),
        'svv-f2': KeuzelijstWaarde(invulwaarde='svv-f2',
                                   label='SVV-F2',
                                   status='ingebruik',
                                   definitie='Niet-gewapende signaalkabel voor binnen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/svv-f2'),
        'sxag-f2': KeuzelijstWaarde(invulwaarde='sxag-f2',
                                    label='SXAG-F2',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/sxag-f2'),
        'sxavb': KeuzelijstWaarde(invulwaarde='sxavb',
                                  label='SXAVB',
                                  status='ingebruik',
                                  definitie='Gewapende signaalkabel voor ondergronds gebruik.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/sxavb')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

