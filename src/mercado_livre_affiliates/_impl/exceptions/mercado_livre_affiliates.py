class MercadoLivreAffiliatesException(Exception):
    pass


class StartError(MercadoLivreAffiliatesException):
    pass


class BrowserNotStartedError(MercadoLivreAffiliatesException):
    pass


class CreateSessionError(MercadoLivreAffiliatesException):
    pass


class CloseSessionError(MercadoLivreAffiliatesException):
    pass


class IsSessionLoggedError(MercadoLivreAffiliatesException):
    pass


class LoginError(MercadoLivreAffiliatesException):
    pass


class GenerateAffiliateLinkError(MercadoLivreAffiliatesException):
    pass


class BackgroundSessionError(MercadoLivreAffiliatesException):
    pass
