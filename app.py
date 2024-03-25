import streamlit as st
from streamlit_option_menu import option_menu

from df import df


from graphs import *

st.set_page_config(
        page_title="BCA Result Analysis",
)
st.title('BCA Result Analysis')



with st.sidebar:
    option=option_menu(
        menu_title=None,
        options=['Overall Analysis','Individual Analysis','Competitive Analysis'],
        icons=['house','file-person','file-person']
    )

if option=='Overall Analysis':
    st.plotly_chart(plotter(mean_line()+median_line(),title='Class Statistics'))
    st.markdown("""---""")
    st.header('Statistical Analysis')
    st.dataframe(df.describe().iloc[1:,1:6])
    st.markdown("""---""")
    st.plotly_chart(plotter(max_line()+mean_line(),title='Topper VS Average'))
    st.markdown("""---""")
    st.write('No. of Students in 1st Sem VS SGPA')
    st.pyplot(bar_plot('first_sem','1st'))
    st.markdown("""---""")
    st.write('No. of Students in 2nd Sem VS SGPA')
    st.pyplot(bar_plot('second_sem','2nd'))
    st.markdown("""---""")
    st.write('No. of Students in 3rd Sem VS SGPA')
    st.pyplot(bar_plot('third_sem','3rd'))
    st.markdown("""---""")
    st.write('No. of Students in 4th Sem VS SGPA')
    st.pyplot(bar_plot('fourth_sem','4th'))
    st.markdown("""---""")
    st.write('No. of Students in 5th Sem VS SGPA')
    st.pyplot(bar_plot('fifth_sem','5th'))


if option=='Individual Analysis':
    credentials=st.selectbox(label='Select Your Credentials to view your Statistics',options=['Select']+list(df['credentials'].values))
    if credentials!='Select':
        name=df[df['credentials']==credentials][['name']].values[0][0]
        st.write('Hii 👋 ',name)
        st.markdown("""---""")
        st.plotly_chart(plotter(line_graph([credentials])+mean_line()+max_line(),title='You VS Topper VS Average'))
        st.markdown("""---""")
        st.header('Your rank semester wise')
        st.dataframe(df[df['credentials']==credentials].iloc[:,9:14])
        st.write('Students with equal SGPA are given same ranking.')
        st.markdown("""---""")
        st.header('OverAll Ranking')
        st.write(f'Hey {name}, your overall ranking is ',df[df['credentials']==credentials]['total_avg_rank'].values[0],'out of ',75,' students.')



if option=='Competitive Analysis':
        st.header('Select students for competitive analysis')
        others=st.multiselect(label='You can select multiple students',options=df['credentials'])
        if others:
            st.plotly_chart(plotter(line_graph(others),title='SGPA Line Graph'))
            st.plotly_chart(plotter(bar_graph(others),title='SGPA Bar Graph'))
            st.markdown("""---""")
            st.header('Rank Comparision')
            st.plotly_chart(rank_plotter(rank_line_graph(others),title='Rank Line Graph'))
            st.write('Students with equal SGPA are given same ranking.')


