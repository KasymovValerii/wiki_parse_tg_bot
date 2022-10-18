import wikipedia
wikipedia.set_lang('en')


def request_to_wiki(request: str) -> tuple:
    flag = 'One'
    try:
        page = wikipedia.page(request)
        request_summary = page.summary
        request_summary = request_summary[:4093] + '...' if len(request_summary) > 4096 else request_summary
        request_result = {'summary': request_summary, 'link': page.url}
    except wikipedia.exceptions.DisambiguationError as e:
        flag = 'More than one'
        request_result = '\n'.join(e.options)
    return request_result, flag

