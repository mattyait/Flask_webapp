from flask import Flask,render_template,request
import logging
import os
import subprocess
import crypt

# Create a flask app object using a unique name. In this case we are
# using the name of the current file
app = Flask(__name__)

@app.route("/")
def main():
  return render_template('index.html')

#Function to check the user already exist or not 
def check_user_exist(user_name):
    user_exist_res=None
    cmd='getent passwd '+user_name
    app.logger.info(user_exist_res)
    #Runnign the command and checking the output
    for line in runProcess(cmd.split()):
        line.strip()
        user_exist_res = line.split()
        app.logger.info(user_exist_res[0])
        #If provided user already exist
        return "true"
    #If provided user not exist then create else give the message        
    return "false"      

#Running shell command and returing the output
def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

@app.route('/usercreate',  methods=['GET','POST'])
def usercreate():
    error=None
    # If the request is GET, render the form template
    if request.method == "GET":      
      return render_template("index.html", errors=errors)
    else:
      app.logger.info('Post request')  
      user_name = request.form['username'].strip()
      shell_type = request.form['shell_list'].strip()
      # shell_type = request.form['shelltype'].strip()
      home_folder = request.form['folder'].strip()
      passwd = request.form['password'].strip()
      #Create encrypted password with salt value 22
      encPass = crypt.crypt(passwd,"22")
      action = request.form['action_list']
      privileges = request.form.get('checkbox')
      
      
      #Check all the field are non empty otherwise raise an error message
      if not user_name or not shell_type or not home_folder or not passwd or action=="none":
            app.logger.info("Please enter the fields values.")            
            errors = "Please enter the fields values."
            # return errors
            return render_template("index.html", errors=errors)  
      #Performing the action based on Type of Event(Create,Modify,Delete)      
      if action == "create":
          app.logger.info("Create")
          #If create user with sudo preivelge
          if privileges == "on":
            # #Checking user name already exist or not
            if check_user_exist(user_name) == "false":
              os.system("sudo useradd "+ user_name +" -d /home/"+home_folder +" -s "+ shell_type +" -p "+encPass+" -G sudouser")
              message="User"+user_name+" Created successfully with sudo privileges"
              return render_template("index.html", message=message)  
            else:
              app.logger.info("User "+user_name+" already exist for creating")
              errors = "User "+user_name+" already exist."
              return render_template("index.html", errors=errors)  
          #If create user without sudo preivelge    
          else:
            os.system("sudo useradd "+ user_name +" -d /home/"+home_folder +" -s "+ shell_type +" -p "+encPass)
            message="User"+user_name+" Created successfully without sudo privileges"
            return render_template("index.html", message=message)  
      elif action == "modify":
          #If user already present then only modify else raise the message
          if check_user_exist(user_name) == "true":
            app.logger.info("Modify")
            os.system("sudo usermod "+ user_name +" -d /home/"+home_folder +" -s "+ shell_type +" -p "+encPass)
            message="User"+user_name+" modified successfully"
            return render_template("index.html", message=message)  
          else:
            app.logger.info("User "+user_name+" not exist for modifying")   
            errors = "User "+user_name+" not exist."
            return render_template("index.html", errors=errors)         
      elif action == "delete":
          if check_user_exist(user_name) == "true":
            app.logger.info("Delete")
            os.system("sudo userdel "+ user_name)
            message="User"+user_name+" deleted successfully"
            return render_template("index.html", message=message)  
          else:
            app.logger.info("User "+user_name+" not exist for deleting")
            errors = "User "+user_name+" not exist."
            return render_template("index.html", errors=errors)


      return render_template('index.html')

if __name__ == "__main__":
  app.debug = True
  app.run(host= '0.0.0.0')
