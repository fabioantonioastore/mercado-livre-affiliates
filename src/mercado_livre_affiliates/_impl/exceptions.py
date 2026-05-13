class MercadoLivreAffiliateException(Exception):
    pass


class LoginError(MercadoLivreAffiliateException):
    pass


class CreateContextError(MercadoLivreAffiliateException):
    pass


class GenerateAffiliateLinkError(MercadoLivreAffiliateException):
    pass


class ManualLoginError(MercadoLivreAffiliateException):
    pass


class AddCookiesError(MercadoLivreAffiliateException):
    pass


class VerifyLoginError(MercadoLivreAffiliateException):
    pass


class MeliProductUrlError(MercadoLivreAffiliateException):
    pass
