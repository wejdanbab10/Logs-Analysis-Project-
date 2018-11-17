

# logs analysis project

This project contains executing three SQL queries from the newsdata database in order to report 
1. The most popular three articles of all time.
2. The most popular article authors of all time.
3. The days I which did more than 1% of requests lead to errors.
<br/> by using a reporting tool which is a Python program using the psycopg2 module to connect to the database.
 
# Getting Started
In order to start running the python file in this project you need to have [project1.py](https://github.com/wejdanbab10/Logs-Analysis-Project-/blob/master/project1.py) file downloaded to vagrant folder inside the VM machine.

# Prerequisites
•	Install Linux-based virtual machine (VM)<br/>
•	Download [Vagrant](https://www.vagrantup.com)<br/>
•	Download [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)<br/>
•	Download [newsdata.sql](https://classroom.udacity.com/nanodegrees/nd004-connect/parts/4237300b-ed78-4462-a353-a0bd14af33bc/modules/b632715b-7aae-4670-9137-bcd880561475/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91) Database <br/>
•	Download [Python 3.6.6](https://www.python.org/downloads/release/python-366/)<br/>
•	Download [project1.py](https://github.com/wejdanbab10/Logs-Analysis-Project-/blob/master/project1.py) file


# Installing and Running the program
 1. Put the [newsdata.sql](https://classroom.udacity.com/nanodegrees/nd004-connect/parts/4237300b-ed78-4462-a353-a0bd14af33bc/modules/b632715b-7aae-4670-9137-bcd880561475/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91) file inside the <b>vagrant</b> folder
 2. Open up your Terminal and change the directory to the vagrant directory by using <b>cd</b>
 3. Run the command <b>vagrant up</b> to start installing Linux
 4. Run the commaed <b>vagrant ssh</b> to log in to the VM
 5. Change the directory to the vagrant directory by using <b>cd/vagrant</b>
 6. Type <b>python project1.py </b> to run to python file that contains the project
 
 # Output
 <b>The most popular three articles of all time:<br/></b> 
   • Candidate is jerk, alleges rival -- 338647 views<br/>
   • Bears love berries, alleges bear -- 253801 views<br/>
   • Bad things gone, say good people -- 170098 views<br/><br/>

<b>The most popular article authors of all time:<br/></b>
   • Ursula La Multa -- 507594 views<br/>
   • Rudolf von Treppenwitz -- 423457 views<br/>
   • Anonymous Contributor -- 170098 views<br/>
   • Markoff Chaney -- 84557 views<br/><br/>

<b>Days where more than 1% of requests lead to errors:<br/></b>
   • 2016-07-17 -- 2.2600 % errors<br/>
