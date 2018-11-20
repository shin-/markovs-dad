from requests import Session

# Note: this client currently assumes all requests go through properly and
# doesn't do any error checking or HTTP status checking. A production-ready
# solution would handle retries and raise gracefully when appropriate.


class Client(Session):
    base = 'https://icanhazdadjoke.com'
    _headers = {
        'Accept': 'application/json'
    }

    def get_random_joke(self):
        return self.get(self.base, headers=self._headers).json()

    def get_joke_by_id(self, jid):
        url = '{}/j/{}'.format(self.base, jid)
        return self.get(url, headers=self._headers).json()

    def search(self, term=None, limit=20, page=1):
        url = '{}/search'.format(self.base)
        qs = {
            'page': page,
            'limit': limit,
        }

        if term is not None:
            qs['term'] = term

        return self.get(url, headers=self._headers, params=qs).json()

    def next_page(self, results):
        if results['next_page'] == results['current_page']:
            # this is the last page
            return None
        return self.search(
            term=results['search_term'],
            limit=results['limit'],
            page=results['next_page'],
        )

    def iterate_jokes(self, term=None):
        data = self.search(term, limit=30)
        while data is not None:
            for joke in data['results']:
                yield joke
            data = self.next_page(data)
