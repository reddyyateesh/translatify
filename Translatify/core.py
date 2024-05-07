"""
MIT License

Copyright (c) 2024 Yateesh Reddy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import re
import html
from typing import Union
import aiohttp
import requests

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
