import logging

from requests import ConnectionError

from .utils import SESSION, VQD_DICT, _do_output, _get_vqd

logger = logging.getLogger(__name__)


def ddg_translate(
    keywords,
    from_=None,
    to="en",
    output=None,
):
    """DuckDuckGo translate

    Args:
        keywords: string or a list of strings to translate
        from_: what language to translate from (defaults automatically). Defaults to None.
        to: what language to translate. Defaults to "en".
        output: print, csv, json. Defaults to None.

    Returns:
        DuckDuckGo translate results.
    """

    if not keywords:
        return None

    # get vqd
    vqd = _get_vqd("translate")
    if not vqd:
        return None

    # translate
    params = {
        "vqd": vqd,
        "query": "translate",
        "from": from_,
        "to": to,
    }

    if isinstance(keywords, str):
        keywords = [keywords]

    results = []
    for data in keywords:
        try:
            resp = SESSION.post(
                "https://duckduckgo.com/translation.js",
                params=params,
                data=data.encode("utf-8"),
            )
            logger.info(
                "%s %s %s", resp.status_code, resp.url, resp.elapsed.total_seconds()
            )
            result = resp.json()
            result["original"] = data
            results.append(result)
        except ConnectionError:
            logger.error("Connection Error.")
        except Exception:
            VQD_DICT.pop("translate", None)
            logger.exception("Exception.", exc_info=True)

    if output:
        keywords = keywords[0]
        _do_output(__name__, keywords, output, results)
    return results
