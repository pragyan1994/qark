import os
x = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/workspace/qark/sampleApps/goatdroid/goatdroid.apk' 
y = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/workspace'
print x
print y
os.system("python qark/qarkMain.py --source 1 --pathtoapk "+x+" --exploit 1 --install 0 --reportdir" +y );

print "Done"
