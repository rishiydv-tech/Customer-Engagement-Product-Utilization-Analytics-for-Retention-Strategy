
def center_table(df, hide_index=False):
    styler = df.style
    if hide_index:
        styler = styler.hide(axis='index')
    return (styler
            .set_properties(**{'text-align': 'center'})
            .set_table_styles([{'selector': 'th',
                                'props': [('text-align', 'center')]}]))