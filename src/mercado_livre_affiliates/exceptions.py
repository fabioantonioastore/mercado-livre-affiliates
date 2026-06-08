class MercadoLivreAffiliatesException(Exception):
    pass


class IsLoggedError(MercadoLivreAffiliatesException):
    pass


class LoginError(MercadoLivreAffiliatesException):
    pass


class ManualLoginError(MercadoLivreAffiliatesException):
    pass


class GenerateAffiliateLinkError(MercadoLivreAffiliatesException):
    pass


class EventFunctionTaskError(MercadoLivreAffiliatesException):
    pass


class EventNotStartedError(MercadoLivreAffiliatesException):
    pass


class EventLogicError(MercadoLivreAffiliatesException):
    pass
