def getLinkTitle(st =""):
    st1 = st.split('/')

    title = st1[-3]
    title = ' '.join([x.capitalize() for x in title.split('-')])
    category = st1[3]

    print(title)
    print(category)

getLinkTitle("https://timesofindia.indiatimes.com/elections/lok-sabha-elections-2019/west-bengal/news/arrest-me-for-chanting-jai-shri-ram-amit-shah-dares-mamata-banerje/articleshow/69306304.cms")
