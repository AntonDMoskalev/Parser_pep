import logging

from requests import RequestException

from constants import EXPECTED_STATUS
from exceptions import ParserFindTagException


def get_response(session, url):
    """Interception of the Request Exception error."""
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None, string=None):
    """Intercepting a tag search error."""
    searched_tag = soup.find(tag, attrs=(attrs or {}), string=string)
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def difference_status(url_card, preview_status, card_status):
    """Error logging status discrepancy."""
    if card_status not in EXPECTED_STATUS.get(card_status[0]) and (
            card_status != 'Draft'):
        card_status = 'Some unknown status'
    if card_status not in preview_status:
        error_msg = (f'Несовпадающие статусы: '
                     f'{url_card} '
                     f'Статус в карточке: {card_status} '
                     f'Ожидаемые статусы: {preview_status}')
        logging.error(error_msg)
