from scrapy import Request, Spider
import numpy as np

class SpiderSites(Spider):
    name = "crawls"
    
    start_urls= ['https://www.dmr.gov.za/news-room/post/1928/meeting-of-the-presidential-climate-commission-on-just-energy-transition-virtual-platform',
                  'https://www.eskom.co.za/about-eskom/just-energy-transition-jet/',
         'https://www.eskom.co.za/world-bank-approves-r9-billion-concessional-loan-facility-for-komati-power-station-repurposing-and-just-energy-transition/',
           'https://www.eskom.co.za/exxaro-and-seriti-resources-join-forces-with-eskom-in-realising-a-just-energy-transition-to-a-low-carbon-future-in-south-africa/',
             'https://green-cape.co.za/sector/energy/utility-scale-renewable-energy/', 
             'https://sawea.org.za/initial-just-energy-transition-work-points-to-need-to-cushion-coal-regions/',
               'https://sawea.org.za/wind-industry-stands-together-in-support-of-the-just-energy-transition-training-facility-in-mpumalanga/', 
               'https://sawea.org.za/sawea-announces-chair-to-lead-wind-energy-transition/', 
               'https://sawea.org.za/biztrends2021-just-energy-transition-will-continue-to-accelerate/', 
               'https://sawea.org.za/just-energy-transition-kicks-off-with-support-from-mpumalanga-schools-and-stakeholders/', 
               'https://sawea.org.za/board-appointment-to-support-the-drive-of-sustainable-energy-transition/', 
               'https://www.sapvia.org.za/technical-advisor-power-sector-reform-and-just-energy-transition-under-the-south-african-german-energy-programme-sagen/',
                 'https://www.csir.co.za/energy-industry-0', 
                 'https://www.csir.co.za/energy-industry-0#:~:text=The%20CSIR%20aims%20to%20lead,in%20regions%20most%20adversely%20affected.', 
                 'https://www.csir.co.za/csir-and-afd-partner-generate-local-knowledge-advance-south-africa%E2%80%99s-just-energy-transition',
                   'https://www.csir.co.za/res4africa-foundation-welcomes-csir-and-nedbank-among-its-partners', 
                   'https://www.csir.co.za/renewable-energy-development-zones', 
                   'https://saesa.org.za/wptest/wp-content/uploads/2019/11/2019-09-17-IDC_The-energy-transition-and-opportunities-for-South-Africa-in-cleaner-fuels_SAESA-1.pdf', 
                   'https://www.climatecommission.org.za/south-africas-jet-ip', 'https://www.climatecommission.org.za/just-energy-transition',
                   'https://sawea.org.za/category/sarec-campaign/', 'https://www.nersa.org.za/', 
                   'https://www.gov.za/about-government/government-programmes/renewable-independent-power-producer-programme', 
                   'https://www.sasol.com/', 'https://www.enelgreenpower.com/', 'https://www.mainstreamrp.com/', 
                   'https://bterenewables.com/', 'https://scatec.com/', 'https://www.globeleq.com/', 'https://www.engie.com/', 
                   'https://www.edf-renouvelables.com/', 'https://sr.energy/', 'https://www.h1holdings.co.za/', 'https://www.juwi.com/',
                     'https://www.edpr.com/en', 'https://www.pelegreenenergy.com/', 'https://www.windlab.com/']
    

    #start_urls=['https://www.edpr.com/en']



    def start_requests(self):
        for url in self.start_urls:
            self.source = url
            yield Request(url=url, callback=self.parse)
    
    def parse(self,response):
        links = response.css('a')
        
        for link in links:
           
            
            try:
                site =  link.css('a::attr(href)').get().strip().strip('\t').strip('\r').strip('\n')
                #hyperlink = link.css('a::text').get()
                source_url = response.url
                source = response.url.split('/')
                nom_site = source[2]
                if not site.startswith('http') or site.startswith("/".join(source[:3])): #or hyperlink==None :
                #if site.startswith('https://')==False or site.startswith('http://')==False or site.startswith("/".join(source[:3])):
                    continue
                
                #if site.startswith('https://')==False :
                 #   continue
                if nom_site.split('.')[1] in site.split('/')[2].split('.'):
                    continue

                yield {
                    "source": nom_site,
                    "source_url": source_url,
                    "target": site.split('/')[2],
                    "target_url" : site       
                }
            except:
                yield {
                    "source": np.nan,
                    "source_url": np.nan,
                    "target": np.nan,
                    "target_url": np.nan
                           
                } 
  
        
        """
        for link in links: 
            try:
                site =  link.css('a::attr(href)').get().strip().strip('\t').strip('\r').strip('\n')
                hyperlink = link.css('a::text').get()
                source = response.url
                #nom_site = source[2]
                yield {
                    "source": source, #nom_site,
                    #"target": site.split('/')[2],
                    "site" : site,
                    "hyperlink" : hyperlink          
                }
            except:
                yield {
                    "source": np.nan,
                    #"target": np.nan,
                    "site" : np.nan,
                    "hyperlink" : np.nan         
                }       
    
        """
