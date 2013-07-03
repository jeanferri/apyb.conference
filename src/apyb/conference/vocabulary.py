# -*- coding: utf-8 -*-
from apyb.conference import MessageFactory as _
from apyb.conference.config import SPONSOR_LEVELS
from five import grok
from plone.i18n.locales.countries import _countrylist
from Products.CMFCore.utils import getToolByName
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class PeriodsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        levels = [('morning', _(u'Morning')),
                  ('afternon', _(u'Afternon'))]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(PeriodsVocabulary,
                    name=u"apyb.conference.periods")


class DurationVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        levels = [('half_day', _(u'Half day')),
                  ('one_day', _(u'1 day')),
                  ('two_days', _(u'2 days'))]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(DurationVocabulary,
                    name=u"apyb.conference.duration")


class LanguagesVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        levels = [('english', _(u'English')),
                  ('portuguese', _(u'Portuguese')),
                  ('spanish', _(u'Spanish'))]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(LanguagesVocabulary,
                    name=u"apyb.conference.languages")


class ThemeVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        levels = [('cloud_system_administration_networks',
                   _(u'Cloud, System Administration and Networks')),
                  ('community_education', _(u'Community and Education')),
                  ('django', _(u'Django')),
                  ('enterprise_management', _(u'Enterprise and Management')),
                  ('media_networks', _(u'Media and Networks')),
                  ('mobility_embedded_systems',
                   _(u'Mobility and Embedded Systems')),
                  ('plone', _(u'Plone')),
                  ('pyramid', _(u'Pyramid')),
                  ('scipy', _(u'Scipy')),
                  ('web_wevelopment', _(u'Web Development')),
                  ('other', _(u'Other'))]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(ThemeVocabulary,
                    name=u"apyb.conference.theme")


class LevelsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Look for an enclosing program
            list available languages in it '''
        terms = []
        levels = [('basic', _(u'Basic')),
                  ('advanced', _(u'Advanced'))]
        for code, text in levels:
            term = (code, code, text)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(LevelsVocabulary,
                    name=u"apyb.conference.levels")


class GendersVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Genders '''
        terms = []
        genders = [('m', _(u'Male')),
                   ('f', _(u'Female'))]
        for key, value in genders:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(GendersVocabulary,
                    name=u"apyb.conference.gender")


class TShirtVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' TShirt Sizes '''
        terms = []
        sizes = [('S', _(u'Small')),
                 ('M', _(u'Medium')),
                 ('L', _(u'Large')),
                 ('X', _(u'X-Large'))]
        for key, value in sizes:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(TShirtVocabulary,
                    name=u"apyb.conference.tshirt")


class RegTypesVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Registration Types'''
        terms = []
        types = [('apyb', _(u'APyB Members')),
                 ('student', _(u'Student')),
                 ('individual', _(u'Individual')),
                 ('government', _(u'Government')),
                 ('group', _(u'Group/Corporate')),
                 ('speaker', _(u'Speaker')),
                 ('speaker_c', _(u'Speaker')),
                 ('sponsor', _(u'Sponsor')),
                 ('organizer', _(u'Organization'))]
        for key, value in types:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(RegTypesVocabulary,
                    name=u"apyb.conference.types")


class TrainingsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        trainings = []
        for key, value in trainings:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(TrainingsVocabulary,
                    name=u"apyb.conference.trainings")


class PaymentMethodsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Payment Method Options '''
        terms = []
        types = [('cash', _(u'Cash / At the conference')),
                 ('paypal', _(u'PayPal')),
                 ('pagseguro', _(u'Pagseguro'))]
        for key, value in types:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(PaymentMethodsVocabulary,
                    name=u"apyb.conference.paymentservices")


class CaipirinhaSprintVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Caipirinha Sprint Options'''
        terms = []
        types = [('no', _(u'No, I will not attend')),
                 ('yes_1', _(u'Yes, I will')),
                 ('yes_2', _(u'Yes and I will bring my SO')),
                 ('yes_3', _(u'Yes, plus 2 other people'))]
        for key, value in types:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(CaipirinhaSprintVocabulary,
                    name=u"apyb.conference.caipirinha")


class WallOptionsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Wall Options '''
        terms = []
        types = [('no', _(u'No, thanks')),
                 ('100', _(u'Yes, I support with R$100,00')),
                 ('200', _(u'Yes, I support with R$200,00')),
                 ('400', _(u'Yes, I support with R$400,00'))]
        for key, value in types:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(WallOptionsVocabulary,
                    name=u"apyb.conference.wall")


class SponsorLevelsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Wall Options '''
        terms = []
        types = SPONSOR_LEVELS
        for key, value in types:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(SponsorLevelsVocabulary,
                    name=u"apyb.conference.sponsor_levels")


class CountriesVocabulary(object):
    """Vocabulary factory for a list of countries
    """
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        countries = [(v['name'], k) for k, v in _countrylist.items()]
        countries.sort()
        items = [SimpleTerm(k, k, v) for v, k in countries]
        return SimpleVocabulary(items)

grok.global_utility(CountriesVocabulary, name=u"contact.countries")


class TalksReferenceTypeVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Talk Reference Types Options '''
        terms = []
        types = [('article', _(u'Article / Post')),
                 ('presentation', _(u'Presentation')),
                 ('video', _(u'Video'))]
        for key, value in types:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(TalksReferenceTypeVocabulary,
                    name=u"apyb.conference.talk.referencetype")


class TalksTypeVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Talk Types Options '''
        terms = []
        types = [('talk', _(u'Talk')),
                 ('panel', _(u'Panel'))]
        for key, value in types:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(TalksTypeVocabulary,
                    name=u"apyb.conference.talk.type")


class TracksVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Tracks Vocabulary '''
        ct = getToolByName(context, 'portal_catalog')
        tracks = ct.searchResults(portal_type='track',
                                  sort_on='getObjPositionInParent')
        items = [SimpleTerm(b.UID, b.UID, b.Title) for b in tracks]
        return SimpleVocabulary(items)


grok.global_utility(TracksVocabulary,
                    name=u"apyb.conference.talk.tracks")


class TalksLevelVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Talk Types Options '''
        terms = []
        types = [('basic', _(u'Basic')),
                 ('intermediate', _(u'Intermediate')),
                 ('advanced', _(u'Advanced'))]
        for key, value in types:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(TalksTypeVocabulary,
                    name=u"apyb.conference.talk.level")


class RoomsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Conference rooms Options '''
        terms = []
        rooms = [
            ('dorneles-tremea', _(u'Auditório Dorneles Treméa')),
            ('cleese', _(u'Sala John Cleese')),
            ('idle', _(u'Sala Eric Idle')),
            ('gillian', _(u'Sala Terry Gilliam')),
        ]
        for key, value in rooms:
            term = (key, key, value)
            terms.append(SimpleVocabulary.createTerm(*term))

        return SimpleVocabulary(terms)


grok.global_utility(TalksTypeVocabulary,
                    name=u"apyb.conference.rooms")


class SpeakersVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        ''' Speakers Vocabulary '''
        ct = getToolByName(context, 'portal_catalog')
        speakers = ct.searchResults(portal_type='speaker',
                                    sort_on='getObjPositionInParent')
        items = [SimpleTerm(b.UID, b.UID, b.Title) for b in speakers]
        return SimpleVocabulary(items)


grok.global_utility(TracksVocabulary,
                    name=u"apyb.conference.speakers")
