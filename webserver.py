'''
Design of the Web Server Code
    ||
    ||
    ||  handler
    ||  
    ||
    =============
    ||
    ||  main()
    ||  
    ||
'''
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

############## Adding CRUD Operations ###############
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Restaurant, MenuItem # importing classes
############## handler code ###################
'''
Indicates what code to execute based on the type of HTTP request that is sent to the server.
'''
engine = create_engine('sqlite:///restaurantmenu.db') 
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class WebServerHandler(BaseHTTPRequestHandler):
    '''Request Handler Class.'''
    def do_GET(self):
        ''' Function to handle all the GET requests received by the server.'''
        # In order to figure out which resource we are trying to access, we will
        # use a simple pattern matching plan that only looks for the ending of
        # our URL path.
        try:
            # `path` contains the URL sent by the client to the server
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"# sending message back to the client
                self.wfile.write(output)
                print(output)
                return

            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                # sending message back to the client
                self.wfile.write(output)
                print(output)
                return

            if self.path.endswith('/restaurants'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                all_restaurants = session.query(Restaurant).all()
                output = ""
                output += "<html><body>"
                output += "<h1>List of all the restaurants</h1>"
                
                for restaurant in all_restaurants:
                    output += restaurant.name
                    output += '<br>'
                    output += '<a href="#">Edit</a> '
                    output += '<a href="#">Delete</a>'
                    output += '<br>'

                output += "</body></html>"# sending message back to the client
                self.wfile.write(output)
                print(output)
                return

        except IOError:
            self.send_error(404, 'File not found %s' % self.path)

    def do_POST(self):
        ''' Function to handle all the POST requests sent by the client.'''
        ## XXX: Unclear what is happening !
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass

########## main() Portion ##############
def main():
    '''Instantiate our server and specify the port it will listen on.'''
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print('Web server is running on port %s' %port)
        # for listening constantly for requests or a ctrl+C interrupt
        server.serve_forever()

    except KeyboardInterrupt:
        print('^C entered, stoppng web server...')
        # shutting down server
        server.socket.close()

if __name__ == '__main__':
    main()
