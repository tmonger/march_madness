import requests, pprint, urllib
import BeautifulSoup as bs

def makeRequest(url_list):
    #User-Agent is a string that verifies whether the person requesting the webpage is bot or not
    user_agent = {'User Agent': 'python-requests/4.8.2 (Compatible; Average Joe; mailto: average.joe.123@gmail.com)'}

    response_dict = {}
    
    for item in range(len(url_list)):
        
        status = requests.get('https://{}/robots.txt'.format(url_list[item]),headers = user_agent)
        status_num = status.status_code

        #By default, set item in response dictionary to True, change if anything other than successful connection returned
        response_dict.setdefault(url_list[item],True)
        
        #If request to robot.txt file was unresponsive, display information
        if status_num != 200:
            response_dict[url_list[item]] = False
            if status_num == 404:
                pprint.pprint('{} does not have a robots.txt file'.format(url_list[item]))
            else:
                pprint.pprint('{} was unresponsive and returned the following error: {}'.format(url_list[item],status_num))
            
    return response_dict
        
def main():
    url_list = ['www.reddit.com',
                'www.mangareader.net']
    makeRequest(url_list)
    

if __name__ == '__main__':
    main()
