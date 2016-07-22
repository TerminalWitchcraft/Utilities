from urllib import parse, request
import json

url = r"https://developers.zomato.com/api/v2.1"

class Zomato:
    """
    ####
    """
    def __init__(self, key,accept_method='application/json', base_url=url ):
        """
        :param key:Zomato user-key
        :param accept_method:application/json | application/xml
        :param base_url:Zomato developers api
        """
        self.api_key = key
        self.accept_method = accept_method
        self.base_url = base_url



    def request(self, call, params={}):
        """
        :param call: Zomato Get Request
        :param params:Request Parameters
        :return: Response of type accept_method
        """
        url = self.base_url+r'/'+call
        GET_url = url + "?" + parse.urlencode(params) if params else url
        print(GET_url)
        z_request= request.Request(GET_url)
        z_request.add_header('Accept',self.accept_method)
        z_request.add_header('user-key',self.api_key)

        z_reponse = request.urlopen(z_request)
        self._z_data = z_reponse.read()

        return self.__z_parse(self._z_data.decode('utf-8'))

    def __z_parse(self, data):
        """
        :param data:
        :return:
        """
        if self.accept_method == "application/json":
            response = json.loads(data)
        else:
            response = data
        return response


