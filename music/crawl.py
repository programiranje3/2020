"""Web crawling and scraping.
BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

import requests
from bs4 import BeautifulSoup

from util import utility

BASE_URL = 'https://www.imdb.com/'


def get_soup(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Creates Response object from HTTP GET request, using requests.get(<url string>, allow_redirects=False),
    and then uses the text field of the Response object and the 'html.parser' to create the BeautifulSoup object.
    """

    # Create Response object from HTTP GET request; assume that no redirection is allowed (allow_redirects=False)
    response = requests.get(url, allow_redirects=False)
    # Get text from the Response object, using <response>.text
    response_text = response.text
    # Create and return the corresponding BeautifulSoup object from the response text; use 'html.parser'
    return BeautifulSoup(response_text, 'html.parser')


def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """

    if '&page=' in start_url:
        url_chunks = start_url.split('&page=')
        return url_chunks[0] + '&page=' + str(page) + '&' + url_chunks[1].split('&', maxsplit=1)[1]
    else:
        return start_url


def get_next_soup(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    """

    return get_soup(get_specific_page(start_url, page))


def crawl(url: str, max_pages=1):
    """Web crawler that collects info about movies from IMDb,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup()) from multi-page movie lists.
    Parameters: the url of the starting IMDb page and the max number of pages to crawl in case of multi-page lists.
    """

    for p in range(max_pages):
        yield get_next_soup(url, p + 1)
        p += 1


def get_4_digit_substring(a_string):
    """Returns the first 4-digit substring from a_string.
    It assumes that a_string contains a 4-digit substring representing a year.
    Useful when the year of a movie release on IMDb is represented like '(1988, part 2)', or '(video, 2002)'."""

    if len(a_string) >=4:
        # all_4_digit_substrings = [a_string[i:j]
        #                           for i in range(0, len(a_string) - 3)
        #                           for j in range(i + 1, len(a_string) + 1)
        #                           if len(a_string[i:j]) == 4]
        all_4_digit_substrings = [a_string[i:(i+4)] for i in range(0, len(a_string) - 3)]
        first_4_digit_substring = next((x for x in all_4_digit_substrings if x.isdigit()), None)
        return first_4_digit_substring
    else:
        return None


def get_m_info(start_url: str, max_pages=1):
    """
    Returns structured information about movies from a multi-page IMDb movie list.
    :param start_url: the url of the starting page of a multi-page IMDb movie list
    :param max_pages: the max number of pages to crawl
    :return: a list of tuples of info-items about the movies from a multi-page IMDb movie list
    Creates and uses the following data:
    - h3_list - a list of all 'h3' tags from multiple IMDb pages
                (each 'h3' tag contains: movie title, year of release, and (relative) link to the movie's IMDb page)
    - poster_list - a list of all relevant 'div' tags from multiple IMDb pages
                    (each such a 'div' tag contains the link to the poster of the corresponding movie)
    - info_list - a list of 3-tuples of information about each movie from h3_list
    - poster_link_list - a list of links to the posters of the movies from poster_list
    - complete_list - a list of 4-tuples of information about each movie from h3_list and poster_list
    """

    h3_list = []
    poster_list = []
    next__soup = crawl(start_url, max_pages)
    while True:
        try:
            soup = next(next__soup)
            h3_list.extend(soup.find_all('h3')[:-1])
            poster_list.extend(soup.find_all('div', {'class': 'lister-item-image ribbonize'}))
        except StopIteration:
            break

    info_list = []
    for h3 in h3_list:
        title = h3.a.text.strip()                   # some titles contain leading/trailing whitespace
        # year = h3.a.find_next_sibling('span').text[-5:-1]
        # year = h3.a.find_next_sibling('span').text.split()[-1].lstrip('(').rstrip(')')
        year = h3.find('span', {'class': "lister-item-year text-muted unbold"}).text
        year = get_4_digit_substring(year)
        year = 'unknown' if not year else year      # covers the case when get_4_digit_substring(year) returns None
        link = BASE_URL + h3.a['href'][1:]
        info_list.append((title, year, link))

    poster_link_list = []
    for p in poster_list:
        poster_link_list.append(p.a.img['loadlate'])

    complete_list = []
    for info, p in zip(info_list, poster_link_list):
        title, year, link = info
        complete_list.append((title, year, link, p))

    return complete_list


if __name__ == "__main__":

    # # Getting started
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
    #             'mode=detail&page=1&sort=moviemeter,asc'
    #
    # # Create Response object from GET request, using requests.get(<url>, allow_redirects=False)
    # response = requests.get(start_url, allow_redirects=False)
    # # print(response)
    # # print(type(response))
    # # print()
    #
    # # Get response text from Response object, using <response>.text
    # response_text = response.text
    # # print(response_text)
    # # print()
    #
    # # Get BeautifulSoup object from response text, using BeautifulSoup(<response text>, 'html.parser')
    # soup = BeautifulSoup(response_text, 'html.parser')
    # # print(type(soup))
    # # print()
    # # print(soup)
    # print()
    #
    # # # Save BeautifulSoup object to an HTML file,
    # # # using <Path-file-object>.write_text(<BeautifulSoup object>, encoding='utf-8', errors='replace')
    # # f = utility.get_data_dir() / 'imdb.html'
    # # f.write_text(str(soup), encoding='utf-8', errors='replace')
    # # print()
    #
    # # Demonstrate <BeautifulSoup object>.find('<tag>'), <BeautifulSoup object>.find_all(<tag>),
    # # <BeautifulSoup object>.find_all(<tag>, {'<tag_attr_name>': "<tag_attr_value>"});
    # # use, e.g., 'h3' or 'div' as the tags in the examples
    # # print(soup.find('h3'))
    # # print()
    # # print(soup.find_all('h3'))
    # h3_list = soup.find_all('h3')
    # print()
    # print(type(h3_list))
    # print(h3_list[23])
    # print()
    # print(len(h3_list))
    # print()
    #
    # # Demonstrate getting a 'subtag' for a tag (a bs4.element.Tag object), e.g. h3.find('<subtag>')
    # print(type(h3_list[23]))
    # print()
    # item_24 = h3_list[23]
    # print(item_24.find('span'))
    # print(item_24.find('span', {'class': "lister-item-year text-muted unbold"}))
    # print()
    #
    # # Demonstrate getting an attribute value for a tag (a bs4.element.Tag object),
    # # e.g. h3.find('<subtag>'), filtered with <{'class': "<class name>"}>;
    # # alternatively: h3.find('<tag>')['<attr>'],
    # # h3.find('<subtag>').get('<attribute>'),
    # # h3.find('<subtag>').<attribute>,... (<attribute>: e.g. text (or string))
    # print(item_24.find('span').get('class'))
    # print()
    #
    # # Demonstrate shorthand notation (e.g., h3.find('<tag>').text is equivalent to h3.<tag>.text (or .string)
    # print(item_24.a)
    # print(item_24.a['href'])
    # print(item_24.a.text)
    # print()
    #
    # # Get/Return all text from a bs4.element.Tag object, using <bs4.element.Tag object>.text
    # print(item_24.text)
    # print()
    #
    # # Demonstrate <tag>.find_next_siblings() (returns all <tag>'s siblings) and
    # # <tag>.find_next_sibling() (returns just the first one)
    # print(item_24.a.find_next_sibling('span'))
    # print(item_24.find('span').find_next_siblings())
    # print()
    #
    # # Get/Return and remove a specific item from a bs4.element.ResultSet using <result set>.pop(<index>) (default: last)
    # h3_list.pop(50)
    # print(h3_list)
    # item_23 = h3_list.pop(22)
    # print(item_23)
    # print(len(h3_list))
    # print()
    #
    # # Each bs4.element.ResultSet, bs4.element.Tag,... can be used to create another BeautifulSoup object,
    # # using BeautifulSoup(str(<bs4.element object>), 'html.parser')
    # soup_23 = BeautifulSoup(str(item_23), 'html.parser')
    # print(soup_23)
    # print()

    # # Example: get all movie titles from an IMDb page
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
    #             'mode=detail&page=1&sort=moviemeter,asc'
    # response = requests.get(start_url, allow_redirects=False)
    # response_text = response.text
    # soup = BeautifulSoup(response_text, 'html.parser')
    # h3_set = soup.find_all('h3')[:-1]
    # # print(soup)
    # for h3 in h3_set:
    #     # print(h3)
    #     print(h3.a.text)
    # print()

    # # Test get_soup()
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
    #             'mode=detail&page=1&sort=moviemeter,asc'
    # soup = get_soup(start_url)
    # print(soup)
    print()

    # # Test get_specific_page()
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
    #             'mode=detail&page=1&sort=moviemeter,asc'
    # print(get_specific_page(start_url, 2))
    # print()

    # # Test get_next_soup()
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
    #             'mode=detail&page=1&sort=moviemeter,asc'
    # print(get_next_soup(start_url, 3))
    # print()

    # # Test crawl()
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
    #             'mode=detail&page=1&sort=moviemeter,asc'
    # next_soup = crawl(start_url, 3)
    # while True:
    #     try:
    #         s = next(next_soup)
    #         print(s)
    #         print()
    #         print()
    #         print()
    #     except StopIteration:
    #         break
    # print()

    # Test get_m_info()
    start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
                'mode=detail&page=1&sort=moviemeter,asc'
    movies = get_m_info(start_url, 3)
    for m in movies:
        print(m)
    print()

    # # Test writing the output of get_m_info() to a csv file
    # # A test list of movie info tuples, try with this list first; illustrates handling Unicode chars and whitespace
    # movies = [('шђ', '2000', 'https://www.imdb.com/title/tt0238784/',
    #            'https://m.media-amazon.com/images/M/MV5BNDk5NjI2NzMzMl5BMl5BanBnXkFtZTgwMjkyOTM0MjE@._V1_UY209_CR69,0,140,209_AL_.jpg'),
    #           ('šđ', '1989', 'https://www.imdb.com/title/tt0096684/',
    #            'https://m.media-amazon.com/images/M/MV5BMzA4MGEzZTMtNGQ3Ny00YjdiLWI2MTgtMzA4YmJlMDY5OGFkXkEyXkFqcGdeQXVyMDgyNjA5MA@@._V1_UY209_CR64,0,140,209_AL_.jpg'),
    #           (' Rockpalast', '1974', 'https://www.imdb.com/title/tt0479780/',
    #            'https://m.media-amazon.com/images/M/MV5BOWM2ZDAyOWUtYWQ0Ni00OTYyLWEwMjktZDJmNjdmNDZlYTdjXkEyXkFqcGdeQXVyMTQ0MzMwNQ@@._V1_UY209_CR1,0,140,209_AL_.jpg'),
    #           (' Ten Days That Unexpectedly Changed America', '2006', 'https://www.imdb.com/title/tt0953255/',
    #            'https://m.media-amazon.com/images/M/MV5BMjA2NDE3NDk1Nl5BMl5BanBnXkFtZTcwNjQ2NDMzMQ@@._V1_UY209_CR4,0,140,209_AL_.jpg')
    #           ]
    import csv
    from util.utility import get_data_dir
    csv_file = get_data_dir() / 'movies.csv'
    header_row = ['Title', 'Year', 'Link', 'Poster']
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:    # newline: avoid blank rows; encoding: enable ш,š...
        out = csv.writer(f)
        out.writerow(header_row)
        out.writerows(movies)


