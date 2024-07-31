from dataclasses import dataclass


@dataclass
class Author:
    first: str
    last: str
    url: str | None = None
    is_me: bool = False


@dataclass
class Publication:
    title: str
    authors: list[Author]
    venue: str
    venue_short: str | None = None
    pdf: str | None = None
    doi: str | None = None
    venue_table: str | None = None
    venue_url: str | None = None
    asterisk: list[int] | None = None

    def _author_i_to_html(self, i):
        author = self.authors[i]
        s = f"{author.first} {author.last}"
        if author.is_me:
            s = "<span class='author'>" + s + "</span>"
        if author.url is not None:
            s = f"<a href='{author.url}' class='a light'>{s}</a>"
        if self.asterisk and i in self.asterisk:
            s += "*"
        return s

    def _authors_to_html(self):
        return ", ".join(self._author_i_to_html(i) for i in range(len(self.authors)))

    def _venue_to_html(self, long_venue):
        s = f"<em>{self.venue}</em>" if long_venue else self.venue_short or self.venue
        if self.venue_url is not None:
            s = f"<a href='{self.venue_url}' class='a light'>{s}</a>"
        return s

    def _title_to_html(self):
        s = self.title
        if self.pdf is not None:
            s = f"<a class='a' href='{self.pdf}'>{s}</a>"
        return f"<span class='pub-title'>{s}</span>"

    def to_html_simple(self, one_line, long_venue):
        res = "<p>"
        res += self._title_to_html()
        res += ". " if one_line else "<br>"
        res += self._authors_to_html()
        res += ". " if one_line else "<br>"
        res += self._venue_to_html(long_venue)
        res += "." if one_line else ""
        res += "</p>"
        return res

    def to_html_table(self):
        res = "<tr>"
        res += f"<td class='venue'>"
        if self.venue_url is not None:
            res += f"<a class='a' href='{self.venue_url}'>"
        res += self.venue_table or self.venue_short or self.venue
        if self.venue_url is not None:
            res += "</a>"
        res += "</td><td>"
        if self.pdf is None:
            res += self.title
        else:
            res += f"<a class='a' href='{self.pdf}'>{self.title}</a>"
        res += "<br>"
        res += self._authors_to_html()
        res += "</td></tr>"

        return res

    def to_html_with_links(self, one_line, long_venue):
        res = "<p>"
        res += f"<strong>{self.title}</strong>"
        res += ". " if one_line else "<br>"
        res += self._authors_to_html()
        res += self._venue_to_html(long_venue)
        if one_line:
            res += "."
        if self.pdf is not None:
            res += f" <a class='a' href='{self.pdf}'>pdf</a>"
        if self.doi is not None:
            res += f" <a class='a' href='{self.doi}'>doi</a>"
        res += "</p>"
        return res
