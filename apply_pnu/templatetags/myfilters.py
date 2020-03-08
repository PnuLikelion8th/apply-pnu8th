from django import template


register = template.Library()


@register.filter
def delete_portfolio(text):
    print(text)

    print(str(text).replace("portfolio/",""))
    return str(text).replace("portfolio/", "")
