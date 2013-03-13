# -*- coding: utf-8 -*-

from gluon.tools import prettydate
from datetime import datetime


def tagfy(tags, extension='html'):
    links = [A(" %s " % tag.strip(), _href=CURL('article', 'list', vars=dict(tag=tag), extension=extension)) for tag in tags]
    return CAT(*links)


DATEFORMAT = T("%Y-%m-%d")
TIMEFORMAT = T("%H:%M:%S")
current.TIMEFORMAT = TIMEFORMAT
current.DATEFORMAT = DATEFORMAT


def ftime(value):
    return value.strftime(str(DATEFORMAT))


def pdate(value):
    if isinstance(value, str):
        value = datetime.strptime(value, "%s %s" % (DATEFORMAT, TIMEFORMAT))
    return prettydate(value, T=T)

current.pdate = pdate
current.ftime = ftime


def ICONBUTTON(icon, text, action):
    bt = BUTTON(_class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-icon-primary",
                _role="button",
                _onclick=action)
    bt.append(SPAN(_class="ui-button-icon-primary ui-icon ui-icon-%s" % icon))
    bt.append(SPAN(text, _class="ui-button-text"))

    return bt


def ICONLINK(icon, text, action=None):
    bt = A(_class="icon-link",
              _onclick=action,
              _style="cursor:pointer;")
    bt.append(CAT(
        IMG(_src=URL('static', 'basic/images/icons', args="%s.png" % icon), _width=16),
        SPAN(text, _style="line-height:16px;")
    ))

    return bt


def get_image(image, placeholder="image", themename='basic', user=None, host=False, scheme=False):
    if user:
        if user.photo_source == 1:
            if user.thumbnail:
                return URL('default', 'download', args=user.thumbnail, extension=False, host=host, scheme=scheme)
            # pass and let go to return default placeholder
        # elif user.photo_source == 6:
        #     return user.googlepicture
        elif user.photo_source == 5:
            pass  # pass and let go to return default placeholder
        else:
            # try to get the image from the source
            from helpers.images import GetImages
            return GetImages.getphoto(user=user)

    if image and image.startswith("http://"):
        return image
    if image:
        return URL('default', 'download', args=image, extension=False, host=host, scheme=scheme)
    else:
        return URL('static', '%s/images' % themename, args='%s.png' % placeholder, extension=False, host=host, scheme=scheme)

current.get_image = get_image


def has_permission_to_edit(record):
    userid = session.auth.user.id if session.auth else 0
    return record.author == userid


def user_is(group="admin"):
    try:
        return group in session.auth.user_groups.values()
    except:
        return False

current.user_is = user_is

c = 1


def getclass(columns=2):
    global c
    if c % columns == 0:
        c += 1
        return 'omega'
    else:
        c += 1
        return 'alpha'


current.getclass = getclass


def get_name_of(user):
    return "%(first_name)s %(last_name)s (%(nickname)s)" % user

search_form = FORM(
    DIV(
        SELECT(*[OPTION(option, _value=value) for value, option in [("article", T("Articles")), ("user", T("Users"))]], _name="kind", _id="kind"),
       _class="two columns alpha search-select"),
    DIV(
        INPUT(_type="search", _placeholder=T("Type word or name to find"), _name="q", _id="q"),
        BUTTON(IMG(_src=URL('static', 'images', args='search_button.png'))),
        _class="four columns omega search-input"
    ),
    _class="search-form",
    _method="GET",
    _action=CURL("home", "search")
)


def iicon(iconname):
    return TAG['i'](_class="icon-%s" % iconname, _style="margin-right:5px;")


def get_menu(menus, visibility=1, parent=None, place="top"):
    ret = []
    if not parent:
        ret = menus.find(lambda row: (row.parent == 0 or row.parent == None) and row.visibility == visibility and row.place == place)
    else:
        ret = menus.find(lambda row: row.parent == parent and row.visibility == visibility and row.place == place)
    return ret


def get_menu_link(menu):
    if menu.href.startswith("http") or menu.href.startswith("mailto") or menu.href.startswith("#"):
        return menu.href
    if menu.href.startswith("{"):
        try:
            from gluon.contrib import simplejson as json
            params = json.loads(menu.href, encoding="utf-8")
            for key in params:
                params[key] = str(params[key])
            return CURL(**params)
        except Exception:
            return CURL()


from HTMLParser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def remove_tags(s):
    try:
        # import lxml.html
        # return lxml.html.fromstring(s).text_content()
        import re
        p = re.compile(r'<.*?>')
        return p.sub('', s)
    except Exception:
        try:
            return strip_tags(s)
        except Exception:
            # is there a better way?
            s = s.replace("<p>", "")
            s = s.replace("</p>", "")
            s = s.replace("<div>", "")
            s = s.replace("</div>", "")
            s = s.replace("<strong>", "")
            s = s.replace("</strong>", "")
            s = s.replace("<b>", "")
            s = s.replace("</b>", "")
            s = s.replace("<pre>", "")
            s = s.replace("</pre>", "")
            return s


def helpmodallink(href,
                  content=iicon('question-sign'),
                  title="help",
                  cls="help-popup",
                  style=""):
    return A(content, _class=cls, _style=style, _href=href, **{"_data-toggle": "modal"})


def helpmodal(mid, content, header=None, style=""):
    ret = DIV(_class="modal hide", _id=mid)
    if style:
        ret.append(XML("<style>#%s { %s }</style>" % (mid, style)))
    if header:
        ret.append(TAG.BUTTON("×", _class="close", _type="button", **{'_data-dismiss': 'modal'}))
        ret.append(DIV(header, _class="modal-header"))
    ret.append(DIV(content, _class="modal-body"))
    ret.append(DIV(A(T('Close'), _href="#", _class="btn", **{'_data-dismiss': 'modal'}), _class="modal-footer"))
    return ret

htmlcolors = ["FF0000", "00FFFF", "0000FF", "0000A0", "ADD8E6", "800080", "FFFF00", "00FF00", "FF00FF", "FFA500", "800000", "808000", "008000"]


# temporary
def get_random_colors(n):
    import random
    return random.sample(htmlcolors, n)


# temporary
def get_google_chart_img(items):
    items = [item for item in items if not item.startswith('#')]
    url = "http://chart.apis.google.com/chart?chf=a,s,000000|bg,s,00000000&chxs=0,00000000,11.5&chxt=x&chs=451x451&cht=p&chco=%(colors)s&chd=t:%(data)s&chdl=%(label)s&chdlp=r"
    colors = "|".join(get_random_colors(len(items)))
    porcentagem = 100 / len(items)
    data = ','.join([str(porcentagem) for item in items])
    label = "|".join(items)

    d = dict(label=label, data=data, colors=colors)
    return url % d
