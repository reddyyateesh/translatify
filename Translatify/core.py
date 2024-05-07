import re
import html
import aiohttp
import requests
from typing import Union

def translate(to_translate, from_language="auto", to_language="auto") -> str:
    """
    Returns the translation using Google Translate.
    You must shortcut the language you define
    (French = fr, English = en, Spanish = es, etc...).
    If not defined, it will detect or use English by default.
    """

    base_link: str = r"http://translate.google.com/m?tl=%s&sl=%s&q=%s"

    to_translate: Union[str, bytes] = aiohttp.helpers.quote(to_translate)
    link: str = base_link % (to_language, from_language, to_translate)
    response: requests.Response = requests.get(link)

    data: str = response.text
    pattern: str = r'(?s)class="(?:t0|result-container)">(.*?)<'
    re_result: list[str] = re.findall(pattern, data)

    if len(re_result) == 0:
        result: str = "No Translation Found."
    else:
        result: str = html.unescape(re_result[0])

    return result

async def async_translate(to_translate, from_language="auto", to_language="auto") -> str:
    """
    Returns the translation using Google Translate asynchronously.
    You must shortcut the language you define
    (French = fr, English = en, Spanish = es, etc...).
    If not defined, it will detect or use English by default.
    """

    base_link: str = r"http://translate.google.com/m?tl=%s&sl=%s&q=%s"

    to_translate: str = aiohttp.helpers.quote(to_translate)
    link: str = base_link % (to_language, from_language, to_translate)

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            data: str = await response.text()

    pattern: str = r'(?s)class="(?:t0|result-container)">(.*?)<'
    re_result: list[str] = re.findall(pattern, data)

    if len(re_result) == 0:
        result: str = "No Translation Found."
    else:
        result: str = html.unescape(re_result[0])

    return result
