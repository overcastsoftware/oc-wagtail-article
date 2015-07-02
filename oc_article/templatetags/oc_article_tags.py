from django import template

register = template.Library()


@register.simple_tag()
def parse_csv_as_table(table_data, table_caption, table_header_row,
                       table_header_column, separator='|'):

    rows = table_data.split('\n')

    html = '<table>'

    if table_caption:
        html += '<caption>%s</caption>' % table_caption

    for row_num, row in enumerate(rows):

        if row_num == 0:
            if table_header_row:
                html += ' <thead>'
            else:
                html += ' <tbody>'

        html += '  <tr>'

        row = row.replace(' %s' % separator, '%s' % separator)
        row = row.replace('%s ' % separator, '%s' % separator)
        cells = row.split('%s' % separator)

        for cell_num, cell in enumerate(cells):

            if row_num == 0 and table_header_row:
                html += '   <th>%s</th>' % cell
            else:
                if cell_num == 0 and table_header_column:
                    html += '   <th>%s</th>' % cell
                else:
                    html += '   <td>%s</td>' % cell

        html += '  </tr>'

        if row_num == 0 and table_header_row:
            html += ' </thead>'
            html += ' <tbody>'

    html += ' </tbody>'
    html += '</table>'

    return html
