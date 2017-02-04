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

############## handler code ###################
'''
Indicates what code to execute based on the type of HTTP request that is sent to the server.
'''
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

                output = '<html><body>Hello, World!</body></html>'
                # sending message back to the client
                self.wfile.write(output)
                print(output)
                return

            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = '<html><body>&#161Hola <a href="/hello">Back to Hello!</a></body></html>'
                # sending message back to the client
                self.wfile.write(output)
                print(output)
                return

        except IOError:
            self.send_error(404, 'File not found %s' % self.path)

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
