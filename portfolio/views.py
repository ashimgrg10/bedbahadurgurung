"""
Views for the Bed Bahadur Gurung portfolio site.

All content below is placeholder data living in plain Python dictionaries/
lists. To update a movie, song, timeline entry, or contact detail, edit the
values here — no template changes required. No forms are processed and no
database is used at this stage, per the current project brief.
"""

from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home'
        # Countdown target dates are read directly in the template/JS as
        # Bikram Sambat dates converted to an approximate Gregorian ISO
        # date so JavaScript's Date object can parse them.
        context['term_start_bs'] = '2079/08/04 B.S.'
        context['term_end_bs'] = '2084/08/04 B.S.'
        # Approximate Gregorian equivalent of 2084/08/04 B.S. — update once
        # the exact conversion is confirmed.
        context['term_end_iso'] = '2027-11-20'
        return context


class JourneyView(TemplateView):
    template_name = 'portfolio/journey.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Journey'
        context['timeline'] = [
            {
                'year': 'Early Years',
                'title': 'Businessman',
                'description': 'मेरो जीवनको यात्रा संघर्ष, परिश्रम र आत्मविश्वासबाट सुरु भएको हो। सफलता कुनै एकै दिनमा प्राप्त भएको होइन; प्रत्येक उपलब्धिको पछाडि अनगिन्ती चुनौती, मेहनत र धैर्य लुकेको छ। व्यवसायिक जीवनको सुरुवात मैले दूधपोखरी राइस मिल (Dudhpokhari Rice Mill) स्थापना गरेर गरेँ। त्यो समय व्यवसाय सानो थियो, स्रोत–साधन सीमित थिए, तर सपना ठूलो थियो। ग्राहकको विश्वास जित्न म आफैं धान कुट्ने कामदेखि चामल प्याक गर्ने र ठेलामा चामल बोकेर ग्राहकको घर–घरमा पुर्‍याउने काम गर्थें। मेरो विश्वास थियो कि कुनै पनि काम सानो हुँदैन; इमानदारी र मेहनतले गरेको काम नै सफलताको पहिलो पाइला हो। '
                'राइस मिलसँगै मैले बंगुर पालन र कुखुरा पालन व्यवसाय पनि सञ्चालन गरेँ। यी व्यवसायहरू केवल आम्दानीका माध्यम मात्र थिएनन्, बरु जोखिम लिन, अवसर चिन्न र निरन्तर मेहनत गर्न सिकाउने विद्यालय बने। कहिले बजारको उतारचढाव, कहिले आर्थिक अभाव र कहिले अन्य चुनौतीहरू आए, तर मैले कहिल्यै हार मानिनँ। प्रत्येक कठिनाइलाई नयाँ अवसरका रूपमा स्वीकार गर्दै अगाडि बढिरहेँ।यी प्रारम्भिक संघर्षहरूले मलाई एउटा महत्वपूर्ण पाठ सिकाए—सफलता भाग्यले होइन, निरन्तर परिश्रम, अनुशासन र दृढ संकल्पले प्राप्त हुन्छ। ग्राहकको विश्वास, कामप्रतिको इमानदारी र समाजसँगको सम्बन्ध नै मेरो व्यवसायको सबैभन्दा ठूलो पूँजी बन्यो।आज मैले जीवनमा जे जति सफलता हासिल गरेको छु, त्यसको जग त्यही संघर्षका दिनहरूले निर्माण गरेका हुन्। ठेलामा चामल पुर्‍याउँदै सुरु भएको मेरो यात्रा केवल व्यवसाय गर्ने यात्रा थिएन; त्यो आत्मनिर्भर बन्ने, सम्मानपूर्वक जीवन जिउने र भविष्यमा समाजको अझ ठूलो सेवा गर्ने सपना बोकेको यात्रा थियो।',
                'icon': 'bi-film',
            },
            {
                'year': 'Early Years',
                'title': 'Theatre Actor',
                'description': 'व्यवसाय सम्हाल्दै गर्दा मेरो मनभित्र कला र अभिनयप्रतिको लगाव पनि उत्तिकै बलियो थियो। दिनभरि दूधपोखरी राइस मिल, बंगुर पालन र कुखुरा पालनको जिम्मेवारी पूरा गरेपछि बाँकी समय म रंगमञ्चमा बिताउँथेँ। जीवन निर्वाहका लागि व्यवसाय आवश्यक थियो, तर आत्मसन्तुष्टि र समाजसँग भावनात्मक रूपमा जोडिने माध्यम भने अभिनय थियो।मेरो अभिनय यात्रा रंगमञ्च (थिएटर) बाट सुरु भएको हो। रंगमञ्चले मलाई अभिनय मात्र सिकाएन, अनुशासन, धैर्य, टोलीमा काम गर्ने क्षमता र मानिसका भावना तथा जीवनका विविध पक्ष बुझ्ने अवसर पनि दियो। प्रत्येक पात्रले समाजका फरक–फरक कथा र यथार्थसँग परिचित गरायो, जसले मेरो सोचलाई अझ परिपक्व बनायो।व्यवसाय र रंगमञ्चलाई सँगसँगै अघि बढाउनु सहज थिएन। दिनभरि व्यवसायको जिम्मेवारी र साँझ अभ्यास तथा मञ्चनका लागि समय निकाल्न ठूलो मेहनत गर्नुपर्थ्यो। तर चुनौतीहरूका बीच पनि मैले आफ्नो सपना कहिल्यै छोडिनँ। मलाई विश्वास थियो कि निरन्तर अभ्यास, लगन र मेहनतले एक दिन ठूलो अवसरको ढोका अवश्य खोल्नेछ।रंगमञ्चका ती दिनहरू नै मेरो कलाकारिताको आधार बने। त्यही अनुभव, आत्मविश्वास र मेहनतले पछि चलचित्र क्षेत्रमा प्रवेश गर्ने बाटो खोल्यो। आज पनि म विश्वास गर्छु कि कलाकारको वास्तविक विद्यालय रंगमञ्च नै हो, जहाँ प्रतिभा मात्र होइन, व्यक्तित्व पनि निर्माण हुन्छ।',
                'icon': 'bi-film',
            },
            {
                'year': 'Building Years',
                'title': 'Film Actor',
                'description': 'रंगमञ्चमा प्राप्त अनुभव, निरन्तर अभ्यास र कलाप्रतिको समर्पणले मलाई चलचित्र क्षेत्रमा प्रवेश गर्ने अवसर प्रदान गर्‍यो। अभिनयप्रतिको मेरो लगावले गुरुङ भाषाका चलचित्रहरूमा काम गर्ने अवसर ल्यायो, जहाँ मैले कलाकार मात्र नभई लेखक र निर्देशकका रूपमा पनि आफ्नो योगदान दिने अवसर पाएँ।मेरो चलचित्र यात्रा छ वटा गुरुङ चलचित्रसँग जोडिएको छ। सुरुवाती दुई चलचित्रमा विशेष भूमिकामा (Special Guest Appearance) अभिनय गरेँ। ती अनुभवहरूले चलचित्र निर्माण प्रक्रिया, क्यामेराको भाषा र दर्शकको अपेक्षालाई अझ नजिकबाट बुझ्ने अवसर दिए।त्यसपछि चार वटा गुरुङ चलचित्रमा मुख्य कलाकार (Lead Actor) का रूपमा अभिनय गर्ने अवसर प्राप्त भयो। ती चलचित्रहरूमा मैले अभिनय मात्र गरेन, आफ्ना सहयात्री तथा अग्रज स्वर्गीय लोकबहादुर गुरुङसँग मिलेर कथा लेखन र निर्देशनको जिम्मेवारी पनि निर्वाह गरेँ। हाम्रो उद्देश्य मनोरञ्जन मात्र प्रदान गर्नु थिएन; गुरुङ समुदायको भाषा, संस्कृति, परम्परा, जीवनशैली र सामाजिक यथार्थलाई चलचित्रमार्फत जगेर्ना गर्दै नयाँ पुस्तासम्म पुर्‍याउनु पनि थियो।चलचित्र मेरो लागि केवल पर्दामा देखिने कला होइन, समाजसँग संवाद गर्ने सशक्त माध्यम हो। त्यसैले प्रत्येक कथामा सामाजिक सन्देश, सांस्कृतिक पहिचान र मानवीय मूल्यलाई समेट्ने प्रयास गरियो। कलाकार, लेखक र निर्देशकका रूपमा एउटै परियोजनामा काम गर्दा सिर्जनशीलता, नेतृत्व र जिम्मेवारीबीच सन्तुलन कायम गर्नु पर्ने चुनौती थियो, तर यही यात्राले मलाई अझ परिपक्व सर्जक बनायो।स्वर्गीय लोक बहादुर गुरुङसँगको सहकार्य मेरो चलचित्र जीवनको सबैभन्दा महत्वपूर्ण अध्यायमध्ये एक हो। उहाँको अनुभव र मार्गदर्शन तथा हाम्रो साझा दृष्टिकोणले गुरुङ चलचित्र क्षेत्रमा उल्लेखनीय योगदान पुर्‍याउने अवसर मिल्यो। ती सिर्जनाहरू आज पनि हाम्रो भाषा, संस्कृति र पहिचानप्रतिको समर्पणका साक्षी बनेर रहेका छन्।',
                'icon': 'bi-film',
            },
            {
                'year': 'Building Years',
                'title': 'Film Director',
                'description': 'अभिनेताका रूपमा पहिचान स्थापित गरेपछि मेरो यात्रा चलचित्र निर्देशन र लेखनतर्फ अझ सशक्त रूपमा अघि बढ्यो। मेरो विश्वास सधैं यही रह्यो कि एउटा राम्रो चलचित्र केवल मनोरञ्जनको माध्यम मात्र होइन, समाज, संस्कृति र मानवीय भावनालाई पुस्तौँसम्म जीवित राख्ने माध्यम पनि हो।मैले सात वटा गुरुङ चलचित्रको कथा लेखन तथा निर्देशन गर्ने अवसर पाएँ। प्रत्येक चलचित्रमा गुरुङ समुदायको भाषा, संस्कृति, परम्परा, जीवनशैली, प्रेम, संघर्ष र सामाजिक यथार्थलाई जीवन्त रूपमा प्रस्तुत गर्ने प्रयास गरियो। दर्शकले ती चलचित्रहरूलाई आत्मीयताका साथ स्वीकार गरे, र सबै चलचित्र व्यावसायिक तथा लोकप्रिय दुवै हिसाबले सफल भए।मेरा निर्देशनमा बनेका चलचित्रका धेरै गीतहरू अत्यन्त लोकप्रिय भए। ती गीतहरूले मनोरञ्जन मात्र दिएनन्, गुरुङ भाषा र संस्कृतिको मौलिकतालाई व्यापक रूपमा चिनाए। आज पनि ती गीतहरू विभिन्न सांस्कृतिक कार्यक्रम, उत्सव र पारिवारिक समारोहहरूमा उत्तिकै रुचिका साथ गाइन्छन् र सुनिन्छन्। यही लोकप्रियताले चलचित्रहरूलाई दर्शकको मनमा दीर्घकालसम्म जीवित राख्न महत्वपूर्ण भूमिका खेलेको छ।निर्देशकका रूपमा मेरो प्रयास सधैं मौलिक कथा, यथार्थपरक प्रस्तुति र सांस्कृतिक पहिचानलाई सम्मान गर्ने रह्यो। सीमित स्रोत–साधनका बीच पनि गुणस्तरीय चलचित्र निर्माण गर्न सकिन्छ भन्ने विश्वासका साथ मैले प्रत्येक परियोजनामा पूर्ण समर्पणका साथ काम गरेँ।मेरो चलचित्र निर्देशनको उद्देश्य सफलता वा लोकप्रियतामा मात्र सीमित थिएन। गुरुङ भाषा, कला र संस्कृतिलाई संरक्षण गर्दै नयाँ पुस्तासम्म पुर्‍याउने, स्थानीय प्रतिभालाई अवसर दिने र नेपाली चलचित्र उद्योगमा गुरुङ चलचित्रको छुट्टै पहिचान स्थापित गर्ने मेरो मुख्य लक्ष्य थियो। यही दृष्टिकोणका साथ गरिएको निरन्तर प्रयासले मलाई निर्देशक र लेखकका रूपमा दर्शकको विश्वास र सम्मान दिलाएको छ।',
                'icon': 'bi-film',
            },
            {
                'year': 'GFAN Presidency',
                'title': 'President, GFAN (Gurung Film Association of Nepal)',
                'description': 'चलचित्र क्षेत्रमा लामो समयसम्म कलाकार, लेखक र निर्देशकका रूपमा सक्रिय रहँदै गुरुङ भाषा, कला र संस्कृतिको प्रवर्द्धनमा पुर्‍याएको योगदानका कारण मलाई गुरुङ फिल्म एसोसिएसन अफ नेपाल (GFAN) को अध्यक्षको जिम्मेवारी सम्हाल्ने अवसर प्राप्त भयो।अध्यक्षका रूपमा मेरो प्राथमिकता गुरुङ चलचित्र क्षेत्रलाई संगठित, व्यावसायिक र थप सशक्त बनाउनु थियो। नयाँ कलाकार, लेखक, निर्देशक र प्राविधिकहरूलाई अवसर सिर्जना गर्ने, गुरुङ चलचित्रको गुणस्तर अभिवृद्धि गर्ने तथा राष्ट्रिय स्तरमा यसको पहिचान स्थापित गर्ने दिशामा विभिन्न पहलहरू गरिए। साथै, गुरुङ भाषा र संस्कृतिलाई चलचित्रमार्फत संरक्षण र प्रवर्द्धन गर्ने अभियानलाई अझ प्रभावकारी बनाउने प्रयास पनि निरन्तर जारी राखियो।मेरो विश्वास थियो कि चलचित्र मनोरञ्जनको माध्यम मात्र होइन, समुदायको इतिहास, संस्कृति र पहिचानलाई जोगाउने शक्तिशाली साधन पनि हो। यही सोचका साथ चलचित्रकर्मीहरूबीच सहकार्य, एकता र सिर्जनात्मक वातावरण निर्माण गर्न विशेष जोड दिइयो।चलचित्र क्षेत्रको नेतृत्व गर्दै समाज र समुदायका लागि काम गर्ने मेरो यात्राले अन्ततः राजनीतिक जीवनतर्फ नयाँ अध्यायको सुरुवात गर्‍यो। GFAN को अध्यक्षको जिम्मेवारी सफलतापूर्वक निर्वाह गरेपछि जनताको विश्वासका आधारमा मादी गाउँपालिकाको अध्यक्ष पदमा निर्वाचित हुँदै प्रत्यक्ष जनसेवाको यात्रामा प्रवेश गरेँ।',
                'icon': 'bi-camera-reels-fill',
            },
            {
                'year': '2074 – 2079 B.S.',
                'title': 'Chairman, Madi Rural Municipality',
                'description': 'चलचित्र, संस्कृति र सामाजिक नेतृत्वमार्फत समाजसँग जोडिएको मेरो यात्राले अन्ततः प्रत्यक्ष जनसेवाको जिम्मेवारीतर्फ डोर्‍यायो। कला र समाजसेवाबाट प्राप्त अनुभव, जनतासँगको निरन्तर सम्बन्ध तथा विकासप्रतिको प्रतिबद्धताका आधारमा वि.सं. २०७४ को स्थानीय तह निर्वाचनमा मादी गाउँपालिकाको अध्यक्ष पदमा निर्वाचित हुने अवसर प्राप्त भयो।जनताले व्यक्त गरेको विश्वासलाई मैले सम्मान मात्र होइन, ठूलो जिम्मेवारीका रूपमा ग्रहण गरेँ। अध्यक्षका रूपमा मेरो पहिलो प्राथमिकता सुशासन, पारदर्शिता, उत्तरदायित्व र जनसहभागितामा आधारित स्थानीय सरकार निर्माण गर्नु थियो। स्थानीय सरकार नागरिकको सबैभन्दा नजिकको सरकार भएकाले विकासका हरेक योजना जनताको आवश्यकता र अपेक्षाअनुसार अघि बढ्नुपर्छ भन्ने मान्यताका साथ काम गरेँ।मेरो कार्यकालमा सडक, खानेपानी, शिक्षा, स्वास्थ्य, कृषि, पर्यटन, सिँचाइ, वातावरण संरक्षण तथा आधारभूत पूर्वाधार विकासलाई विशेष प्राथमिकता दिइयो। गाउँपालिकाको समग्र विकासका लागि दीर्घकालीन सोचका साथ योजनाहरू तर्जुमा गरिए र उपलब्ध स्रोत–साधनको प्रभावकारी परिचालनमा जोड दिइयो।मादी गाउँपालिकाको अध्यक्षका रूपमा निर्वाचित हुनु मेरो व्यक्तिगत उपलब्धि मात्र थिएन; त्यो जनताले विकास, सुशासन र परिवर्तनप्रति व्यक्त गरेको विश्वासको सम्मान थियो। यही विश्वासलाई मार्गदर्शक बनाएर इमानदारी, सेवाभाव, सिर्जनशीलता र जवाफदेहिताका साथ जनताको जीवनस्तर उकास्ने लक्ष्य लिएर मैले आफ्नो जिम्मेवारी निर्वाह गरेँ।',
                'icon': 'bi-building-fill',
            },
            {
                'year': '2079 B.S. – Present',
                'title': 'Member, Gandaki Province Assembly',
                'description': 'मादी गाउँपालिकाको अध्यक्षका रूपमा पाँच वर्षे कार्यकाल सफलतापूर्वक सम्पन्न गरेपछि, जनताले फेरि एकपटक मप्रति विश्वास व्यक्त गरे। वि.सं. २०७९ को प्रदेश सभा निर्वाचनमा म गण्डकी प्रदेश सभा सदस्यमा निर्वाचित भएँ, र हालसम्म पनि उक्त जिम्मेवारी निर्वाह गरिरहेको छु। आगामी वि.सं. २०८४ को निर्वाचनसम्म जनताको प्रतिनिधिका रूपमा सेवा गर्ने अवसर प्राप्त भएको छ।प्रदेश सभा सदस्यका रूपमा मेरो भूमिका स्थानीय तहको अनुभवलाई प्रदेशस्तरीय नीति निर्माणसँग जोड्ने रहेको छ। गाउँपालिका अध्यक्षका रूपमा हासिल गरेको अनुभवले जनताका वास्तविक आवश्यकता, स्थानीय सरकारका चुनौती र विकासका प्राथमिकताहरूलाई नजिकबाट बुझ्ने अवसर दिएको थियो। यही अनुभवलाई आधार बनाएर प्रदेश सभामा जनताको आवाज प्रभावकारी रूपमा उठाउने, जनमुखी नीति निर्माणमा योगदान दिने र प्रदेशको समग्र विकासका लागि सक्रिय भूमिका निर्वाह गर्दै आएको छु।मेरो विश्वास छ कि जनप्रतिनिधिको सफलता पदमा होइन, जनताका जीवनमा ल्याएको सकारात्मक परिवर्तनमा मापन हुन्छ। त्यसैले प्रदेश सभा सदस्यका रूपमा पनि इमानदारी, पारदर्शिता, जवाफदेहिता र सेवाभावलाई आफ्नो नेतृत्वको मूल आधार बनाएर जनताको विश्वासलाई निरन्तर सम्मान गर्दै आएको छु।गाउँपालिकादेखि प्रदेश सभासम्मको यो यात्रा मेरो व्यक्तिगत उन्नतिको कथा मात्र होइन, जनताको विश्वास, निरन्तर सेवा र समृद्ध समाज निर्माणप्रतिको अटल प्रतिबद्धताको यात्रा हो। यही प्रतिबद्धताका साथ म गण्डकी प्रदेश र समग्र नेपालको समृद्धिका लागि निरन्तर कार्यरत रहनेछु।',
                'icon': 'bi-bank2',
            },
            {
                'year': 'Ministerial Service',
                'title': 'Two-Time Minister',
                'description': 'वि.सं. २०७९ मा गण्डकी प्रदेश सभा सदस्यमा निर्वाचित भएपछि, प्रदेशको विकास र समृद्धिप्रति मेरो अनुभव, कार्यक्षमता र प्रतिबद्धतालाई मूल्याङ्कन गर्दै मुख्यमन्त्री खगराज अधिकारीको नेतृत्वमा गठित गण्डकी प्रदेश सरकारमा दुई पटक कृषि, ऊर्जा, जलस्रोत तथा सिंचाइ मन्त्रीको जिम्मेवारी सम्हाल्ने अवसर प्राप्त भयो।मन्त्रीका रूपमा मेरो मुख्य लक्ष्य गण्डकी प्रदेशको कृषि क्षेत्रलाई आधुनिक, व्यावसायिक र आत्मनिर्भर बनाउनु, ऊर्जा उत्पादन र उपयोगलाई विस्तार गर्नु, जलस्रोतको दिगो व्यवस्थापन गर्नु तथा सिंचाइ पूर्वाधारको विकासमार्फत कृषकको उत्पादन र आम्दानी वृद्धि गर्नु थियो।मन्त्रीका रूपमा मैले नीति निर्माणमा मात्र सीमित नभई, सम्बन्धित निकाय, स्थानीय तह, कृषक, प्राविधिक तथा सरोकारवालासँग निरन्तर संवाद र समन्वय गर्दै प्रभावकारी सेवा प्रवाहमा जोड दिएँ। मेरो विश्वास थियो कि विकासका योजना कागजमा मात्र सीमित नभई प्रत्यक्ष रूपमा जनताको जीवनमा परिवर्तन ल्याउन सक्षम हुनुपर्छ।गण्डकी प्रदेश सरकारमा दुई पटक मन्त्रीका रूपमा सेवा गर्ने अवसर मेरो सार्वजनिक जीवनको महत्वपूर्ण उपलब्धिमध्ये एक हो। यो जिम्मेवारीले नेतृत्व, निर्णय क्षमता, सुशासन र जनसेवाप्रतिको मेरो प्रतिबद्धतालाई अझ सुदृढ बनायो। भविष्यमा पनि जनताको विश्वासलाई सर्वोपरि राख्दै इमानदारी, पारदर्शिता, जवाफदेहिता र सेवाभावका साथ राष्ट्र र समाजको हितमा निरन्तर योगदान पुर्‍याउने मेरो अटल संकल्प रहनेछ।',
                'icon': 'bi-award-fill',
            },
        ]
        context['slider_images'] = [
            {'src': 'images/profile/profile.jpg', 'alt': 'Portrait of Bed Bahadur Gurung in formal attire'},
            {'src': 'images/profile/prof2.jpg', 'alt': 'Portrait of Bed Bahadur Gurung during public events'},
            {'src': 'images/profile/old.jpg', 'alt': 'Historic portrait of Bed Bahadur Gurung'},
            {'src': 'images/profile/adachye.jpg', 'alt': 'Bed Bahadur Gurung in a cultural or public setting'},
        ]
        return context


class FilmView(TemplateView):
    template_name = 'portfolio/film.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Film'

        context['upcoming_movie'] = {
            'title': 'Buki Fuul',
            'description': 'An upcoming feature film directed by Om Prakash Gurung, Story and Produced by Bed Bahadur Gurung, headlined by two of Nepali cinema\u2019s most celebrated performers.',
            'starring': ['Dayahang Rai', 'Sanskriti Gurung'],
            'poster': 'images/movies/buki.jpg',
            'trailer_url': '#',
        }

        # 10+ placeholder movies — swap "poster", "title", "description",
        # and "trailer_url" for each real title.
        context['movies'] = [
            {'title': 'Nhamsyo Nhori', 'description': 'Nhyamso Nhori (often simply called Nhori) holds a major place in indigenous cinema as the second Gurung language movie ever made.', 'poster': 'images/movies/nhori.png', 'trailer_url': 'https://www.youtube.com/watch?v=M1KW61OL0SI'},
            {'title': 'ङ्योए नांस टहो full movie ft. Bed bahadur Gurung, Kalpana Gurung', 'description': '▶Story : Late Lok Bahadur Gurung \n ▶Script : Bed Bahadur Gurung (Shyam) \n ▶Camera/Edit/Director: Om Prakash Gurung \n ▶Ass.Camera/Director : Bhoj Bahadur Gurung', 'poster': 'images/movies/nasa.png', 'trailer_url': 'https://www.youtube.com/watch?v=m0zngf9KktA&t=41s'},
            {'title': 'Cho चों - Gurung Movie', 'description': 'Directed by Late Lok Bhadur Gurung \n Bed Bahadur Gurung', 'poster': 'images/movies/cho.jpg', 'trailer_url': 'https://www.youtube.com/watch?v=jYwXP7dBVec&list=RDjYwXP7dBVec&start_radio=1'},
            {'title': ' Herbai ta/हेर्बै ट ', 'description': 'Story/Concept: Bed Bahadur Gurung (Shyam) \n Script/Dialogue: Late.Lok Bahadur Gurung, Bed Bahadur Gurung \n Director: Late Lok Bahadur Gurung \n Asst.Dir: Bed Bahadur Gurung (Shyam) \n Camera/Edit: Bhoj Bahadur Gurung', 'poster': 'images/movies/herbeta.jpg', 'trailer_url': 'https://www.youtube.com/watch?v=fGBq4nPyq3k&t=2s'},
            {'title': 'Kramu Gurung Movie क्रमु Ft.Bed Bahadur Gurung (Shyam),Nabina Gurung,Balbahadur Gurung', 'description': 'Story/Direction: Bed Bahadur Gurung (Shyam), Late Lok Bahadur Gurung ', 'poster': 'images/movies/kramu.jpg', 'trailer_url': 'https://www.youtube.com/watch?v=TCdSKft1XTQ&t=7214s'},
            {'title': 'Presyo Gurung Movie Full / दुलही ft. Om Prakash Gurung, Mira Gurung, Nabina Gurung', 'description': 'Writer/Director:  Bed Bahadur Gurung(Shyam),\n Late Lok Bahadur Gurung \n Cast: Om Prakash Gurung, Mira Gurung, Nabina Gurung, Bal Bahadur Gurung', 'poster': 'images/movies/preshyo.jpg', 'trailer_url': 'https://www.youtube.com/watch?v=sgGh3qR5WkQ&t=603s'},
            {'title': ' Gurung movie Dhee |धि /घर Ft.Rajani Gurung,Om Prakash Gurung', 'description': 'Director: Late Lok Bahadur Gurung \n Bed Bahadur Gurung(Shyam) ', 'poster': 'images/movies/dhee.jpg', 'trailer_url': 'https://www.youtube.com/watch?v=jMkMiB9iBO4&t=1491s'},
            {'title': 'Yumpo Deurali ft Sajan Gurung, Dhanmaya Gurung, Laxmi Gurung, Rupa Devi Gurung, Anand Gurung, Tikaram Ghale, Bal Bahadur Gurung', 'description': 'Writer: Late Lok Bahadur Gurung \n Writer/Director: Bed Bahadur Gurung (Shyam)', 'poster': 'images/movies/yumpo.jpg', 'trailer_url': 'https://www.youtube.com/watch?v=v_gnjCOsid0&t=196s'},
          
        ]

        context['songs_written'] = [
            {
                'title': 'hyale Nholsyo | ह्यले ङोल्स्यो ङ्योए नांस ट्हो',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Music/vocal- Dhan Bahadur Gurung',
                'thumbnail': 'images/songs-written/hyale.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=tk80Zoq41Xs&list=RDtk80Zoq41Xs&start_radio=1',
            },
            {
                'title': 'chhuikho Reemai | छुई खो रीमै | ङ्योए नांस ट्हो',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Music- Dhan Bahadur Gurung \nVocal-Kesh Bahadur Gurung,Chandra Gurung,Tara Gurung and Bishnu Gurung',
                'thumbnail': 'images/songs-written/chuikho.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=5F3k07n4hpc&list=RD5F3k07n4hpc&start_radio=1',
            },
            {
                'title': 'Tali ngi chu sai | तली ङि चु सैं |',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Music- Dhan Bahadur Gurung \n Vocal- Jyoti Gurung',
                'thumbnail': 'images/songs-written/talina.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=Wd2O06R4JvU&list=RDWd2O06R4JvU&start_radio=1',
            },
            {
                'title': 'kho remai syokai chale | खो रिमै स्योकै चले |',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Music- Dhan Bahadur Gurung \n Vocal- Gobin Gurung, Shankar Birahi Gurung, Basmati Gurung,TauSubba Gurung ',
                'thumbnail': 'images/songs-written/khorimei.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=yqq1cHv8XyA&list=RDyqq1cHv8XyA&start_radio=1',
            },
            {
                'title': '| तु जमाना खाजे हो  "हर्बै ट" |',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Music- Dhan Bahadur Gurung \n Vocal- Debu Gurung ',
                'thumbnail': 'images/songs-written/jamana.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=6ZZMFsGLf08&list=RD6ZZMFsGLf08&start_radio=1',
            },
            {
                'title': 'Namsyo yaje नामस्यो खाजे Gurung Movie Kramu | क्रमु |',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Music- Dhan Bahadur Gurung \n Vocal- Gobin Gurung, Dhan Bahadur Gurung',
                'thumbnail': 'images/songs-written/nyamso.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=JqtImW-tugU&list=RDJqtImW-tugU&start_radio=1',
            },
             {
                'title': 'Saili Yorbai Paa |Gurung movie Phresyo',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Vocal : Manoj Gurung,Gobin Gurung',
                'thumbnail': 'images/songs-written/saili.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=u6Jp_gr6jdI&list=RDu6Jp_gr6jdI&start_radio=1',
            },
             {
                'title': 'Kyo khanar hyale |Gurung movie Phresyo',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Music- Dhan Bahadur Gurung \n Vocal-  Kusum Gurung, Dhan Bahadur Gurung',
                'thumbnail': 'images/songs-written/kyu.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=xrN7iCpdjNA&list=RDxrN7iCpdjNA&start_radio=1',
            },
             {
                'title': 'Ngai Min Prasad |Gurung movie Dhee |',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Vocal- Rubi Gauli',
                'thumbnail': 'images/songs-written/dhee.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=TVHMHS3ofBI&list=RDTVHMHS3ofBI&start_radio=1',
            },
            {
                'title': 'kyai ngyole | Yumpo Deurali Movie |',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Music-Tejendra Gurung \n Vocal- Gobin Gurung,Malati Gurung',
                'thumbnail': 'images/songs-written/yumpo.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=_r8tkxY1riY&list=RD_r8tkxY1riY&start_radio=1',
            },
            {
                'title': 'मादी गाउपलिका चिनारी गीत',
                'description': 'Lyrics- Bed Bahadur Gurung (Shyam) \n Vocal- Melina Rai, Prabin Bedwal',
                'thumbnail': 'images/songs-written/madi.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=inO9noT47BE&list=RDinO9noT47BE&start_radio=1',
            },
        ]

        context['songs_performed'] = [
            {
                'title': 'Aasa Mara Churot | आशा मारा चुरोट |',
                'description': 'a song form Gurung Movie Porchhe,\n singer: Late Yukta Gurung, Maya Gurung',
                'thumbnail': 'images/songs-performed/asamara.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=Gwf68USd9ZQ&list=RDGwf68USd9ZQ&start_radio=1',
            },
            {
                'title': 'Chhyabarani Ngolsyone | Herbe ta Gurung Movie |',
                'description': 'Lyrics and Music- Late Lok Bahadur Gurung \n Vocal- Dhan Bahadur Gurung & Jyoti Gurung',
                'thumbnail': 'images/songs-performed/chyabarani.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=3PqgbwL4izo&list=RD3PqgbwL4izo&start_radio=1',
            },
            {
                'title': 'Chau chhyabai butte kramu kuba | क्रमु Gurung Movie |',
                'description': 'Lyrics: Late Lok Bahadur Gurung \n Music: Dhan Bahadur Gurung\nVocal: Dhan Bahadur Gurung, Jyoti Gurung \n Choreography: Bed Bahadur Gurung (Shyam) \nCamera/Edit: Birkha Raj Gurung',
                'thumbnail': 'images/songs-performed/kramu.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=tUxMf4is8kc&list=RDtUxMf4is8kc&start_radio=1',
            },
            {
                'title': 'Nyamsyo Nori Song',
                'description': 'Artist: Bed Bahadur Gurung, Roshan Gurung, Shukla Gurung.',
                'thumbnail': 'images/songs-performed/nori.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=Hs8hDovcCtc&list=RDHs8hDovcCtc&start_radio=1',
            },
             {
                'title': 'Murabai musara मुर्बै मुसारा  ft bed bahadur gurung, nabina gurung',
                'description': 'Lyrics: Late Lok Bahadur Gurung \n Music: Dhan Bahadur Gurung \n Vocal: Sabina Gurung, Dhan Bahadur Gurung, Sarbagayman Shakya',
                'thumbnail': 'images/songs-performed/murabei.jpg',
                'watch_url': 'https://www.youtube.com/watch?v=8LfS8kRSvAU&list=RD8LfS8kRSvAU&start_radio=1',
            },
           
        ]
        return context


class PoliticsView(TemplateView):
    template_name = 'portfolio/politics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Politics'
        context['positions'] = [
            {
                'role': 'Chairman',
                'body': 'Madi Rural Municipality',
                'term': '2074 \u2013 2079 B.S.',
                'icon': 'bi-building-fill',
            },
            {
                'role': 'Member',
                'body': 'Gandaki Province Assembly',
                'term': '2079 B.S. \u2013 Present',
                'icon': 'bi-bank2',
            },
        ]
        context['ministries'] = ['Agriculture', 'Energy', 'Water Resources', 'Irrigation']
        context['political_timeline'] = [
            {'year': '2074 B.S.', 'text': 'Elected Chairman of Madi Rural Municipality.'},
           
            {'year': '2079 B.S.', 'text': 'Elected Member of the Gandaki Province Assembly.'},
            {'year': '2079 B.S. \u2013 Present', 'text': 'Continues to serve constituents in the Province Assembly.'},
             { 'text': 'Served two terms as Minister of Agriculture, Energy, Water Resources and Irrigation of Gandaki Province.'},
        ]
        return context


class AboutView(TemplateView):
    template_name = 'portfolio/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'About'
        context['roles'] = [
            'Politician', 'Province Assembly Member', 'Former Chairman', 'Former Minister',
            'Film Director', 'Film Actor', 'Writer', 'Theatre Artist',
            'Head of Abhiyan Film Production',
        ]
        context['core_values'] = [
            {'title': 'Integrity (इमानदारी)', 'description': 'मेरो लागि इमानदारी कुनै नारा होइन, जीवन जिउने आधार हो। सार्वजनिक जीवनमा बोलेको कुरा र व्यक्तिगत जीवनमा गरेको व्यवहार एउटै हुनुपर्छ भन्ने मेरो विश्वास छ। पद, शक्ति वा स्वार्थभन्दा माथि सत्य, न्याय र नैतिकतालाई राख्नु नै मेरो प्रतिबद्धता हो।'},
            {'title': 'Service (सेवा)', 'description': 'राजनीति मेरो लागि अधिकार प्राप्त गर्ने माध्यम होइन, जनताको सेवा गर्ने जिम्मेवारी हो। जनताको विश्वास नै मेरो सबैभन्दा ठूलो शक्ति हो। विकासका अवसर सबै नागरिकसम्म समान रूपमा पुगून्, कसैलाई पनि विभेदको अनुभूति नहोस् भन्ने उद्देश्यका साथ काम गर्नेछु।'},
            {'title': 'Creativity (सिर्जनशीलता)', 'description': 'चलचित्र, अभिनय र लेखनले मलाई समाजलाई नयाँ दृष्टिकोणबाट हेर्न सिकाएको छ। सिर्जनशील सोचले समस्याको नयाँ समाधान खोज्न प्रेरित गर्छ। कला र संस्कृतिको संरक्षण गर्दै शिक्षा, स्वास्थ्य, रोजगारी र सुशासनमा नवीन सोच र व्यवहारिक योजनाहरू लागू गर्नु मेरो विश्वास हो।'},
            {'title': 'Accountability (जवाफदेहिता)', 'description': 'नेतृत्व भनेको सफलताको श्रेय मात्र लिने होइन, गल्तीको जिम्मेवारी पनि स्वीकार गर्ने क्षमता हो। जनताप्रति पारदर्शी रहनु, निर्णयहरूको स्पष्ट जवाफ दिनु र आवश्यक परे आफ्ना कमजोरीहरू स्वीकार गरेर सुधार गर्नु नै साँचो नेतृत्वको पहिचान हो।'},
        ]
        context['education'] = [
            {'degree': 'Degree / Qualification Placeholder', 'institution': 'Institution Name Placeholder', 'year': 'Year'},
            {'degree': 'Degree / Qualification Placeholder', 'institution': 'Institution Name Placeholder', 'year': 'Year'},
        ]
        context['achievements'] = [
            'Placeholder achievement or award one.',
            'Placeholder achievement or award two.',
            'Placeholder achievement or award three.',
        ]
        return context


class ContactView(TemplateView):
    template_name = 'portfolio/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Contact'
        context['contact_details'] = {
            'address': 'Madi Rural Municipality,Tangting, Gandaki Province, Nepal',
            'phone': '+977-9856020663',
            'email': 'bedbdrgrg@gmail.com',
            'facebook': 'https://www.facebook.com/bedbahadur.gurung.7',
            'Instagram': 'https://www.instagram.com/bedgrg61/',
        }
        return context
