import requests
def main():
    webcast_dic = {}
    for year in range(1992, 2020):
        url = 'https://www.thebluealliance.com/api/v3/events/{}'.format(year)
        headers = {'X-TBA-Auth-Key':'p8MD1dJfS2xOHD6cX7MIIW1mcFw1GWHuBKlUq9foxjt1Fp4f17B9PoYVreTBLC7a'}
        response = requests.get(url, headers=headers)
        for event in response.json():
            for webcast in event['webcasts']:
                if webcast['type'] in webcast_dic:
                    webcast_dic[webcast['type']] += 1
                else:
                    webcast_dic[webcast['type']] = 1

    print(webcast_dic)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
