class MercadoLivreAffiliateException(Exception):
    pass


class LoginError(MercadoLivreAffiliateException):
    pass


class ChromiumLaunchError(MercadoLivreAffiliateException):
    pass


class GenerateAffiliateLinkError(MercadoLivreAffiliateException):
    pass
