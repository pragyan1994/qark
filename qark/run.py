import os
x = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/workspace/qark/sampleApps/goatdroid/goatdroid.apk'
print x
os.system("python qark/qarkMain.py --source 1 --pathtoapk "+x+" --exploit 1 --install 0 --reportdir /Users/suruchi.srivastava/.jenkins/jobs/qark/workspace");

print "Done"
