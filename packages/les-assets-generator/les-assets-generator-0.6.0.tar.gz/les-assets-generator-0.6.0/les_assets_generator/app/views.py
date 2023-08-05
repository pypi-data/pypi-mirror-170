from io import BytesIO
from urllib.error import HTTPError
from urllib.request import urlopen

from django.core.exceptions import PermissionDenied, ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page
from PIL import Image, ImageDraw, ImageFont

from les_assets_generator.app.models import Asset, Parameter


def index(request):
    return redirect("https://github.com/lyon-esport/assets-generator")


@cache_page(60 * 15)
def generate(request, title: str):
    asset = get_object_or_404(Asset.objects.select_related(), pk=title)
    if asset.authentication and not request.user.is_authenticated:
        raise PermissionDenied()
    else:
        params = Parameter.objects.select_related().filter(asset=asset)

        img = Image.open(asset.picture)
        draw = ImageDraw.Draw(img)

        for param in params:
            param_value = request.GET.get(param.name)
            # If param is mandatory
            if param.mandatory and param_value is None:
                return HttpResponse(_("Missing GET parameter %s" % param), status=422)
            elif param_value is not None:
                validator = URLValidator()
                # check if param is an image url
                try:
                    validator(param_value)
                except ValidationError:
                    try:
                        param_font_size = int(
                            request.GET.get(f"{param.name}_font_size", param.font_size)
                        )
                        if param.font.font_url:
                            font_file = urlopen(param.font.font_url)
                        else:
                            font_file = param.font.font.path
                        font = ImageFont.truetype(font_file, param_font_size)
                    except ValueError:
                        return HttpResponse(
                            _("%s_font_size must be a number" % param.name),
                            status=422,
                        )
                    except OSError:
                        return HttpResponse(
                            _("Font %s not supported" % param.font),
                            status=422,
                        )
                    draw.text(
                        (param.x, param.y),
                        param_value,
                        font=font,
                        anchor="ms",
                        fill=param.color,
                    )
                else:
                    try:
                        image_to_paste = Image.open(
                            BytesIO(urlopen(param_value).read())
                        )
                        img.paste(image_to_paste, (param.x, param.y))
                    except HTTPError:
                        return HttpResponse(
                            _("Error when loading logo %s" % param_value),
                            status=422,
                        )

        byte_io = BytesIO()
        img.save(byte_io, "png")
        byte_io.seek(0)

        return HttpResponse(byte_io, content_type="image/png")
