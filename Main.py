
#from Clustering import MyClass
import ftplib
import os
from socket import *
from flask import *
from werkzeug import *
from test.test_xml_etree import methods


#import Example
#from Example import MyClass1
#import kfold
app=Flask(__name__);
sess=Session()
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload', methods=['GET','POST'])
def upload():
    print "this is upload function:"
    #print request.files['file']
    #if request.method=='POST':
    if 'filename' not in request.files:
        flash('No file part')
        print "No File found..."
        return redirect(request.url)
    file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    #else:
    #print "this is not a POST request"
    # Get the name of the uploaded file
    file = request.files['file']
    print "this is file name tobe uploaded::"
    print file
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        #filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print "llllllllllllllll"
        return redirect(url_for('uploaded_file',
                                filename=file.filename))
    else:
        return '<h3>Invalid File, PDF or image only.</h3>'
    print "kkkkkkkkkkkkk"
    

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print filename
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)
    #return send_from_directory(app.config['UPLOAD_FOLDER'],
     #                          filename)


@app.route('/getNoteText',methods=['GET','POST'])
def GetNoteText():
    if request.method == 'POST':
        global int_message
        int_message=1
        print "Data uploading"
        print request.headers
        logdata = request.stream.readline()
        for v in request.values:
          print v
        #logdata = request.stream.readline()
        #while(logdata):
        #    print "uploading"
        #    print logdata
        #    logdata = request.stream.readline()
        print "Uploading done"
        while(logdata):
            print "Data received is :"
            print logdata
            logdata = request.stream.readline()
        return Response(str(int_message), mimetype='text/plain')
    return Response(str(int_message), mimetype='text/plain')

#this is different code////
@app.route('/input1')
def render():
    if 'filename' in request.args:
        myfilename = request.args.get('filename')
        return render_template(myfilename)
    else:
        return "No input file specified"
    

APP_ROOT=os.path.dirname(os.path.abspath(__file__))
@app.route("/")
def index():
    return render_template("uploaded.html")

@app.route("/uploaded",methods=['POST'])
def uploaded():
    target=os.path.join(APP_ROOT,"files/")
    print target
    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        print file
        filename=file.filename
        destination="/".join([target,filename])
        print destination
        file.save(destination)
    
    js = json.dumps("Server Got it....")

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp
    

if __name__ == '__main__':
    
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)
    
    app.run(host='192.168.43.125', debug=True,port=8080)
    
    #Open ftp connection
    
    target=os.path.join(APP_ROOT,"files/")
    print target
    if not os.path.isdir(target):
        os.mkdir(target)
     
    os.chdir(target)
     
     
    ftp = ftplib.FTP('ftp.combinaryclix.com')
    ftp.login('rizwan@combinaryclix.com', '8sVI]_Ku+M{f/')
 
    #List the files in the current directory
    print "File List:"
    files = ftp.dir()
    print "file is;::"
     
 
    #Get the file
    ftp.cwd("/uploads")
    gFile = open("AccelerometerValue.csv", "wb")
    print gFile.name
     
     
    for file in ftp.nlst(gFile.name): # Loop - looking for matching files
        fhandle = open(file, 'wb')
        print 'Getting ' + file #for confort sake, shows the file that's being retrieved
        ftp.retrbinary('RETR ' + file, fhandle.write)
 
        #fhandle.save(destination)
        fhandle.close()
     
     
    #ftp.retrbinary('RETR AccelerometerValue.csv', gFile.write)
     
    #Saving file...
     
    gFile.close()
    ftp.quit()

    
    #cp=MyClass()
    #cp.graphss()
    
    print "this is it"
    HOST = "192.168.43.125" #local host
    PORT = 5000 #open port 7000 for connection
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.setsockopt(IPPROTO_TCP,TCP_NODELAY,1)
    s.bind((HOST, PORT))
    s.listen(1) #how many connections can it receive at one time
    conn, addr = s.accept() #accept the connection
    print "Connected by: " , addr #print the address of the person connected
    while True:
        data = conn.recv(1024) #how many bytes of data will the server receive
        print "Received: ", repr(data)
        reply = raw_input("Reply: ") #server's reply to the client
        conn.sendall(reply)
    conn.close()

    
    

    
    #cd=MyClass1()
    #cd.training()
    
    
    
    
    pass