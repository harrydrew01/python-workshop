import flickrapi

api_key = '37637f77593e94f56f3f14b52f92301d'
api_secret = 'abcd4f3d4427edda'

flickr = flickrapi.FlickrAPI(api_key, api_secret)

(token, frob) = flickr.get_token_part_one(perms='write')
if not token: 
    raw_input("Press ENTER after you authorized this program")

flickr.get_token_part_two((token, frob))

#make the call, get XML back
xml_result = flickr.upload(filename='test.jpg', title='test from windows', description='test')

#parse the XML with ElementTree
photo_id = xml_result.find('photoid').text
print "uploaded to: http://www.flickr.com/photos/pythonworkshop/" + photo_id
