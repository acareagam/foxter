# -*- coding: utf-8 -*-

from gluon.dal import Field
from gluon import current
from gluon.validators import IS_IN_SET


class Setup(object):

    def __init__(self):
        T = current.T
        self.db_options = [
            Field("uri", "string", notnull=True, default="sqlite://movuca.sqlite"),
            Field("migrate", "boolean", notnull=True, default=True),
            Field("migrate_enabled", "boolean", notnull=True, default=True),
            Field("pool_size", "integer", notnull=True, default=10),
            Field("gaeuri", "string", notnull=True, default="google:datastore"),
            Field("setuptime", "datetime", notnull=True),
        ]

        self.mail_options = [
            Field("server", "string", notnull=True, default="logging"),
            Field("sender", "string", notnull=True, default="mail@domain.com"),
            Field("login", "string", notnull=False, default="teste:1234"),
            Field("setuptime", "datetime", notnull=True),
        ]

        self.auth_options = [
            Field("formstyle", "string", notnull=True, default="divs"),
            Field("photo_source", "list:string", notnull=True, default=["1:upload", "2:gravatar", "3:facebook", "4:twitter", "5:no photo", "6:Google"]),
            Field("gender", "list:string", notnull=True, default=["Male:Male", "Female:Female", "Not specified:Not specified"]),
            Field("privacy", "list:string", notnull=True, default=["1:Public", "2:Visible only for contacts"]),
            Field("use_facebook", "boolean", notnull=True, default=True),
            Field("facebook", "list:string", notnull=True, default=["id:133622423420992",
                                                                     "secret:6b0880726a21a89dfcb07c19c7807817",
                                                                     "admins:1766038844"]),
            Field("use_google", "boolean", notnull=True, default=True),
            Field("google", "list:string", notnull=True, default=["id:908928538602.apps.googleusercontent.com",
                                                                  "secret:HH6ITKRWOkhS-prHliD21weA",
                                                                  "xoauth_displayname:Movuca Social CMS",
                                                                  "redirect_scheme:http", "redirect_uri:movu.ca/demo/person/google/login",
                                                                  "approval_prompt:force"]),
            Field("use_recaptcha", "boolean", notnull=True, default=True),
            Field("recaptcha", "list:string", notnull=True, default=["public:6Ld9QswSAAAAAN1DlVBEOxFkMGsFytzSZ54v1nur",
                                                                     "private:6Ld9QswSAAAAAIzXZXJQmxKKaDS5AMrCA1Cnq5ut",
                                                                     "theme:clean",
                                                                     "lang:en"]),
            Field("use_mailhide", "boolean", notnull=True, default=True),
            Field("mailhide", "list:string", notnull=True, default=["public:01_qmBPgGX5nvV1rYv_bxK4A==",
                                                                    "private:37565e87d8f80bd680afbc31e0d4e3df"]),
            Field("registration_requires_verification", "boolean", notnull=True, default=False),
            Field("registration_requires_approval", "boolean", notnull=True, default=False),
            Field("registration_requires_invitation", "boolean", notnull=True, default=False),
            Field("server", "string", notnull=True, default="default"),
            Field("sender", "string", notnull=True, default="mail@domain.com"),
            Field("login", "string", notnull=False, default="teste:1234"),
            Field("setuptime", "datetime", notnull=True),
        ]

        self.crud_options = [
            Field("formstyle", "string", notnull=True, default="divs"),
            Field("setuptime", "datetime", notnull=True),
        ]

        self.theme_options = [
            Field("name", "string", notnull=True, default="bootstrap"),  # basic
            Field("setuptime", "datetime", notnull=True),
        ]

        self.article_options = [
            Field("license", "list:string", notnull=True, default=["1:All rights reserved", "2:Public domain", "3:Creative Commons"]),
            Field("setuptime", "datetime", notnull=True),
        ]

        self.meta_options = [
            Field("title", "string", notnull=True, default="Foxter"),
            Field("subtitle", "string", notnull=True, default="Foxter news"),
            Field("author", "string", notnull=True, default="Samuel Bonilla R."),
            Field("keywords", "string", notnull=True, default="web2py, python, cms, social network, CMS"),
            Field("description", "string", notnull=True, default="Free Social CMS Engine built with web2py and Python by blouweb.com"),
            Field("generator", "string", notnull=True, default="web2py, Python, Foxter"),
            Field("copyright", "string", notnull=True, default="Free"),
            Field("setuptime", "datetime", notnull=True),
        ]

        comment_systems = [
            ('internal', T("Internal comments")),
            ('disqus', T("Disqus")),
            ('intense', T("Intense Debate")),
            ('facebook', T("Facebook comments")),
            ('disabled', T("Comments disabled")),
        ]

        self.comment_options = [
           Field("system", "string", requires=IS_IN_SET(comment_systems), notnull=True, default="internal"),
           Field("anonymous", "boolean", notnull=True, default=False),
           Field("disqus_shortname", "string", notnull=True, default="foxter"),
           Field("disqus_developer", "integer", notnull=True, default=1),
           Field("intense_acct", "string", notnull=True, default="fe83a2e2af975dd1095a8e4e9ebe1902"),
           Field("facebook_appid", "string", notnull=True, default="257838757587678"),
           Field("facebook_numposts", "integer", notnull=True, default=10),
           Field("setuptime", "datetime", notnull=True),
        ]

        notification_events = [
                "nuevo_contacto:%s te sigue %s",
                "esribio_en_tu_muro:%s escribio en tu muro %s",
                "le_gusta:%s le gusta tu publicacion %s",
                "compartido:%s compartio tu publicacion %s",
                "favorito:%s favorito tu publicacion %s",
                "no_le_gusta:%s no le gusta tu publicacion %s",
                "nuevo_articulo_comentado:%s comento tu publicacion %s",
                "repondio_comentario:%s respondio tu comentario %s",
                "board_respondio:%s respopndio tu publicacion en board %s",
                "nuevo_articulo_comentado_subscribir:%s comentario en publicacion donde tu estas subcrito %s",
                "cargo_articulos_subscritores:%s cargo publicaciones donde tu estas subcrito %s",
                "mencionar:%s mensiono tu nombre %s",
                "mensagee:%s tienes un nuevo mensage %s",
        ]

        notification_ways = ["site:site notifications", "email:e-mail"]

        self.notification_options = [
          Field("event", "list:string", default=notification_events, notnull=True),
          Field("way", "list:string", default=notification_ways, notnull=True),
          Field("worker", "string", default="site", comment="site or scheduler"),
          Field("setuptime", "datetime", notnull=True),
        ]
