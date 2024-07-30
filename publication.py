from dataclasses import dataclass

@dataclass
class Publication:
    title: str
    authors: list[tuple[str,str]]
    venue: str
    venue_short: str | None = None
    pdf: str | None = None
    doi: str | None = None
    venue_table: str | None = None
    venue_url: str | None = None

    def _authors_to_html(self):
        return ", ".join(
            f"{first} {last}" for (first, last) in self.authors
        )
    
    def _venue_to_html(self, long_venue):
        if long_venue:
            return f"<em>{self.venue}</em>"
        else:
            return self.venue_short or self.venue

    def to_html_simple(self, one_line, long_venue):
        res = "<p>"
        if self.pdf is None:
            res += self.title
        else:
            res += f"<a href='{self.pdf}'>{self.title}</a>"
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
            res += f"<a href='{self.venue_url}'>"
        res += self.venue_table or self.venue_short or self.venue
        if self.venue_url is not None:
            res += "</a>"
        res += "</td><td>"
        if self.pdf is None:
            res += self.title
        else:
            res += f"<a href='{self.pdf}'>{self.title}</a>"
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
            res += f" <a href='{self.pdf}'>pdf</a>"
        if self.doi is not None:
            res += f" <a href='{self.doi}'>doi</a>"
        res += "</p>"
        return res

